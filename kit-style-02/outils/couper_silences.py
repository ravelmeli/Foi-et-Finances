"""Raccourcit les silences de la voix off et recale transcript.json en conséquence.

Chaque pause entre deux mots plus longue que --max (0,32 s par défaut) est ramenée à --garde (0,22 s).
Les originaux sont conservés : assets/voix-originale.wav et transcript-original.json.

    python3 -I couper_silences.py <dossier du projet> [--max 0.32] [--garde 0.22]
"""
import argparse
import json
import os
import shutil
import wave

import numpy as np


def main(proj, max_gap, keep):
    wav = os.path.join(proj, "assets/voix.wav")
    tr = os.path.join(proj, "transcript.json")
    orig_wav = os.path.join(proj, "assets/voix-originale.wav")
    orig_tr = os.path.join(proj, "transcript-original.json")
    if not os.path.exists(orig_wav):
        shutil.copy(wav, orig_wav)
        shutil.copy(tr, orig_tr)
    with wave.open(orig_wav, "rb") as w:
        sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        pcm = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").reshape(-1, ch)
    words = json.load(open(orig_tr))
    fade = int(0.012 * sr)
    cuts = []                                              # (début, fin) des morceaux de silence retirés, en secondes
    for a, b in zip(words, words[1:]):
        gap = b["start"] - a["end"]
        if gap > max_gap:
            mid = a["end"] + keep / 2
            cuts.append((mid, b["start"] - keep / 2))
    pieces, pos = [], 0
    for s, e in cuts:
        i, j = int(s * sr), int(e * sr)
        seg = pcm[pos:i].astype(np.float32)
        if len(seg) > 2 * fade:
            seg[-fade:] *= np.linspace(1, 0, fade)[:, None]
        pieces.append(seg)
        pos = j
        nxt = pcm[pos:pos + fade].astype(np.float32)
        if len(nxt) == fade:
            pcm_next = pcm[pos:].astype(np.float32)
            pcm_next[:fade] *= np.linspace(0, 1, fade)[:, None]
            pcm = np.concatenate([pcm[:pos], pcm_next.astype("<i2")])
    pieces.append(pcm[pos:].astype(np.float32))
    out = np.concatenate(pieces).clip(-32768, 32767).astype("<i2")
    with wave.open(wav, "wb") as w:
        w.setnchannels(ch)
        w.setsampwidth(sw)
        w.setframerate(sr)
        w.writeframes(out.tobytes())

    def shift(t):
        removed = sum(min(e, t) - s for s, e in cuts if t > s)
        return round(t - removed, 3)

    new = [dict(w, start=shift(w["start"]), end=shift(w["end"])) for w in words]
    json.dump(new, open(tr, "w"), ensure_ascii=False, indent=1)
    gained = sum(e - s for s, e in cuts)
    print(f"{len(cuts)} pauses raccourcies, {gained:.1f} s gagnées : {len(pcm) / sr:.1f} s → {len(out) / sr:.1f} s")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("projet")
    ap.add_argument("--max", type=float, default=0.32)
    ap.add_argument("--garde", type=float, default=0.22)
    a = ap.parse_args()
    main(a.projet, a.max, a.garde)

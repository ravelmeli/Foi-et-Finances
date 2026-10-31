"""Musique de fond générée par synthèse, sans modèle ni échantillon : 100 % libre de droits (composition originale du projet).

Style « louange moderne / explainer » : nappe chaude, arpège pincé, basse douce, pulsation légère (kick doux + shaker).
Progression I – V – vi – IV, tempo modéré, montée d'énergie au milieu, fins en fondu.

    python3 -I gen_musique_libre.py sortie.wav 75            # 75 secondes, tonalité et graine par défaut
    python3 -I gen_musique_libre.py sortie.wav 75 --tonalite D --bpm 92 --graine 3

Mixage conseillé : volume 0.15 sous la voix (build(music_volume=0.15)), comme le prévoit le moteur.
"""
import argparse
import wave

import numpy as np

SR = 44100
NOTES = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
# Accords en degrés de la gamme majeure (fondamentale, tierce, quinte), progression I – V – vi – IV
PROG = [(0, 4, 7), (7, 11, 14), (9, 12, 16), (5, 9, 12)]


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def env_adsr(n, a, d, s, r):
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    e = np.full(n, s, dtype=np.float32)
    a = min(a, n)
    e[:a] = np.linspace(0, 1, a, endpoint=False)
    d = min(d, n - a)
    e[a:a + d] = np.linspace(1, s, d, endpoint=False)
    if r and n > r:
        e[-r:] *= np.linspace(1, 0, r)
    return e


def lowpass(x, cutoff):
    """Filtre passe-bas à un pôle, appliqué deux fois (pente douce)."""
    k = np.exp(-2 * np.pi * cutoff / SR)
    for _ in range(2):
        y = np.empty_like(x)
        acc = 0.0
        for i in range(0, len(x), 4096):
            seg = x[i:i + 4096]
            out = np.empty_like(seg)
            for j, v in enumerate(seg):
                acc = (1 - k) * v + k * acc
                out[j] = acc
            y[i:i + 4096] = out
        x = y
    return x


def onepole_fast(x, cutoff):
    """Passe-bas vectorisé approché (moyenne glissante exponentielle par FFT)."""
    n = len(x)
    k = np.exp(-2 * np.pi * cutoff / SR)
    h = (1 - k) * k ** np.arange(min(n, int(SR * 0.05)))
    m = 1 << int(np.ceil(np.log2(n + len(h))))
    y = np.fft.irfft(np.fft.rfft(x, m) * np.fft.rfft(h, m), m)[:n]
    return y.astype(np.float32)


def reverb(x, seconds=2.2, mix=0.28, seed=0):
    rnd = np.random.default_rng(seed)
    n = int(SR * seconds)
    ir = rnd.standard_normal(n).astype(np.float32) * np.exp(-np.linspace(0, 6, n)).astype(np.float32)
    ir = onepole_fast(ir, 4500)
    ir /= np.sqrt((ir ** 2).sum())
    m = 1 << int(np.ceil(np.log2(len(x) + n)))
    wet = np.fft.irfft(np.fft.rfft(x, m) * np.fft.rfft(ir, m), m)[:len(x)].astype(np.float32)
    return (1 - mix) * x + mix * wet


def pad_note(f, dur, rnd):
    t = np.arange(int(dur * SR)) / SR
    sig = np.zeros_like(t, dtype=np.float32)
    for det in (-0.12, 0.0, 0.11):                     # trois voix légèrement désaccordées
        ff = f * 2 ** (det / 12)
        ph = rnd.uniform(0, 2 * np.pi)
        saw = 2 * ((ff * t + ph / (2 * np.pi)) % 1) - 1
        sig += (0.55 * np.sin(2 * np.pi * ff * t + ph) + 0.18 * saw).astype(np.float32)
    sig = onepole_fast(sig, 1400)
    return sig * env_adsr(len(sig), 0.9, 0.6, 0.75, 1.0)


def pluck(f, dur):
    t = np.arange(int(dur * SR)) / SR
    sig = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sin(2 * np.pi * 3 * f * t)).astype(np.float32)
    return sig * np.exp(-t * 6.5).astype(np.float32) * env_adsr(len(t), 0.004, 0.0, 1.0, 0.05)


def bass(f, dur):
    t = np.arange(int(dur * SR)) / SR
    sig = (np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t)).astype(np.float32)
    return sig * env_adsr(len(t), 0.02, 0.3, 0.6, 0.2)


def kick(dur=0.35):
    t = np.arange(int(dur * SR)) / SR
    f = 50 + 70 * np.exp(-t * 28)
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)).astype(np.float32)


def shaker(rnd, dur=0.08):
    n = int(dur * SR)
    x = rnd.standard_normal(n).astype(np.float32)
    x = x - onepole_fast(x, 5000)                      # passe-haut : souffle aigu
    return x * np.exp(-np.linspace(0, 8, n)).astype(np.float32)


def add(buf, sig, start, gain=1.0):
    i = int(start * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += gain * sig[:j - i]


def main(out, seconds, tonalite="D", bpm=90, graine=1):
    rnd = np.random.default_rng(graine)
    root = 60 + NOTES[tonalite]                         # do4 + décalage
    beat = 60 / bpm
    bar = 4 * beat
    n = int((seconds + 3) * SR)
    pad, arp, low, drums = (np.zeros(n, dtype=np.float32) for _ in range(4))
    bars = int(np.ceil((seconds + 3) / bar))
    pattern = [0, 1, 2, 1, 2, 1, 0, 1]                   # arpège en croches sur la triade
    for b in range(bars):
        chord = PROG[b % 4]
        t0 = b * bar
        for deg in chord:
            add(pad, pad_note(hz(root - 12 + deg), bar + 0.4, rnd), t0, 0.16)
        energie = 0.55 if b < 2 else (1.0 if b % 8 in (2, 3, 4, 5) else 0.8)  # entrée douce, respiration toutes les 8 mesures
        for k, p in enumerate(pattern):
            deg = chord[p] + (12 if k in (3, 5) else 0)
            add(arp, pluck(hz(root + deg), beat * 0.9), t0 + k * beat / 2, 0.11 * energie * (1.0 if k % 2 == 0 else 0.75))
        add(low, bass(hz(root - 24 + chord[0]), bar * 0.95), t0, 0.22)
        if b >= 2:                                      # pulsation après l'intro
            for k in range(4):
                add(drums, kick(), t0 + k * beat, 0.32 if k % 2 == 0 else 0.18)
                add(drums, shaker(rnd), t0 + k * beat + beat / 2, 0.06)
    mix = pad + arp + low + 0.85 * drums
    mix = reverb(mix, 2.4, 0.3, graine)
    mix = mix[:int(seconds * SR)]
    fade_in, fade_out = int(1.5 * SR), int(2.5 * SR)
    mix[:fade_in] *= np.linspace(0, 1, fade_in)
    mix[-fade_out:] *= np.linspace(1, 0, fade_out)
    mix /= max(1e-6, np.abs(mix).max()) / 0.8
    st = np.stack([mix, np.roll(mix, int(0.012 * SR)) * 0.96], axis=1)   # léger élargissement stéréo
    pcm = (np.clip(st, -1, 1) * 32767).astype("<i2")
    with wave.open(out, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print(f"{out} : {seconds:.1f} s, {tonalite} majeur, {bpm} bpm, graine {graine}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("sortie")
    ap.add_argument("secondes", type=float)
    ap.add_argument("--tonalite", default="D", choices=list(NOTES))
    ap.add_argument("--bpm", type=float, default=90)
    ap.add_argument("--graine", type=int, default=1)
    a = ap.parse_args()
    main(a.sortie, a.secondes, a.tonalite, a.bpm, a.graine)

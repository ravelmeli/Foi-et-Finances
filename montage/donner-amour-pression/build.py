"""Short « Donner par amour ou par pression religieuse ? » (2 Corinthiens 9.7) — style 02, 9:16, ~72.4 s.
Lot de 4 Shorts. Acquis : mots géants, compteurs, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte refermée, fin qui revient sur la première image. Temps lus dans transcript.json (voix fournie).

Lancer : python3 build.py   (puis hyperframes check et hyperframes render -q draft)
"""
import difflib
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Donner par amour ou par pression religieuse ?", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=72.4, cols=COLS, rows=ROWS, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
S = ST
_TR = json.load(open(os.path.join(HERE, "transcript.json"), encoding="utf-8"))


def _norm(x):
    return re.sub(r"[^\w]+", "", unicodedata.normalize("NFC", x.lower()))


def W(prefix, after=0.0, nth=0):
    """Début (en secondes) du n-ième mot contenant `prefix`, après l'instant `after` (repli approximatif signalé)."""
    pn = _norm(prefix).rstrip("s")
    k = 0
    for w in _TR:
        if w["start"] >= after and pn in _norm(w["text"]):
            if k == nth:
                return round(w["start"], 2)
            k += 1
    cand = [w for w in _TR if after <= w["start"] <= after + 12]
    best = difflib.get_close_matches(_norm(prefix), [_norm(w["text"]) for w in cand], n=1, cutoff=0.55)
    for w in cand:
        if best and _norm(w["text"]) == best[0]:
            print("  ~ repli", prefix, "->", w["text"], w["start"])
            return round(w["start"], 2)
    raise KeyError((prefix, after))


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


CTA = '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire'


def verse_block(stn, ref_txt, t_ref, verse_html, t_text, marks, size=54, ref_y=1420, ref_label=None):
    verse_html = verse_html.replace(" »", "&nbsp;»").replace("« ", "«&nbsp;").replace(" ;", "&nbsp;;").replace(" :", "&nbsp;:")
    tag(stn, 70, 600, ref_txt, t_ref, "acc", 52)
    sfx("spark", t_ref, 1.6)
    v = put(stn, 70, 710, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.22">{verse_html}</div>', "headline", f"width:{W_PX}px")
    blur_in(v, t_text - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', mt)
    ref(stn, 70, ref_y, (ref_label or ref_txt.upper()) + " · LSG 1910", t_text + 0.3)


W_PX = 1080 - 2 * 70 - 60

S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15 = S[:15]


# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-donne-pression", 20, 650, 600, 0.0, rot=-2, instant=True)
sticker(S1, "baton-donne-joie", 560, 900, 400, 68.0, rot=3)
headline(S1, 300, ["Par [amour]", "ou par pression ?"], 0.0, kicker="Tu donnes à l'église", hl_t=1.0, size=92)
bigword("Un test simple", 4.1, 1.0, y=1260, size=96)
hit(4.6, 0.9)

# --- S2 · un poids sur le cœur
cam(7.1, S2)
headline(S2, 280, ["Un poids sur", "le [cœur]"], 7.2, kicker="Beaucoup de chrétiens", hl_t=W("poids", 7.1), size=104)
sticker(S2, "baton-donne-pression", 40, 650, 480, 7.5, rot=-2)
tag(S2, 70, 1160, "Un poids sur le cœur", W("poids", 7.1) + 0.4, "", 38)
tag(S2, 70, 1250, "« Mauvais croyant »", W("mauvais", 7.1), "acc", 38)
hit(W("mauvais", 7.1), 0.8)

# --- S3 · le verset (2 Corinthiens 9.7) : séquence « Parole »
cam(12.9, S3)
headline(S3, 280, ["Donner", "[librement]"], 13.0, kicker="Deuxième lettre aux Corinthiens", hl_t=W("joie", 17.2), size=104)
verse = "«&nbsp;Que chacun donne comme il l'a résolu en son cœur, " + m(0, "sans tristesse ni contrainte") + " ; car Dieu aime celui qui donne " + m(1, "avec joie") + "&#8288;.&nbsp;»"
verse_block(S3, "2 Corinthiens 9.7", 15.4, verse, 17.2, [W("sans", 17.2), W("joie", 17.2)], size=50, ref_label="2 CORINTHIENS 9.7")
sticker(S3, "livre-croix-ouvert", 60, 1090, 320, 13.4, rot=-3)
sticker(S3, "croix-verte", 600, 1100, 190, 22.5, rot=4)
hit(24.0, 1.0)

# --- S4 · trois mots
cam(24.3, S4)
headline(S4, 280, ["Trois", "[mots]"], 24.4, kicker="Remarque", hl_t=25.0, size=120)
sticker(S4, "baton-donne-joie", 40, 650, 480, 24.8, rot=-2)
tag(S4, 70, 1160, "En son cœur", W("cœur", 24.3), "", 40)
tag(S4, 70, 1250, "Sans contrainte", W("contrainte", 24.3), "", 40)
tag(S4, 70, 1340, "Avec joie", W("joie", 24.3), "acc", 40)
hit(W("joie", 24.3), 0.8)

# --- S5 · le test
cam(32.5, S5)
headline(S5, 280, ["Le [test]", "en 3 questions"], 32.6, kicker="Voici", hl_t=33.0, size=96)
counter(S5, 70, 640, 0, 3, 33.3, 0.8, " questions", 140)
sticker(S5, "liste-trois-cases", 600, 820, 300, 33.0, rot=3)
hit(34.4, 0.7)

# --- S6 · question 1
cam(35.2, S6)
headline(S6, 280, ["Si personne", "ne le [savait] ?"], 35.3, kicker="Question 1", hl_t=W("savait", 35.2), size=92)
sticker(S6, "baton-donne-cache", 40, 650, 470, 35.6, rot=-2)
bigword("Question 1", 35.4, 0.9, y=1180, size=110)

# --- S7 · question 2
cam(38.8, S7)
headline(S7, 280, ["Libre de", "dire [non] ?"], 38.9, kicker="Question 2", hl_t=W("non", 38.8), size=104)
sticker(S7, "baton-libre-calme", 40, 650, 440, 39.2, rot=-2)
bigword("Question 2", 39.0, 0.9, y=1180, size=110)
tag(S7, 70, 1300, "Sans culpabilité", W("culpabilit", 38.8), "acc", 38)

# --- S8 · question 3
cam(43.7, S8)
headline(S8, 280, ["Acheter une", "[bénédiction] ?"], 43.8, kicker="Question 3", hl_t=W("bénédiction", 43.7), size=84)
sticker(S8, "balance-coeur-chaine", 40, 650, 520, 44.1, rot=-2)
bigword("Question 3", 43.9, 0.9, y=1180, size=110)
tag(S8, 70, 1300, "Ou parce que j'ai reçu", W("reçu", 43.7), "acc", 38)

# --- S9 · tu donnes par amour
cam(47.5, S9)
headline(S9, 280, ["Tu donnes", "par [amour]"], 47.6, kicker="Si tu réponds oui", hl_t=W("amour", 47.5), size=104)
sticker(S9, "baton-donne-joie", 40, 650, 500, 47.9, rot=-2)
hit(W("amour", 47.5), 0.9)

# --- S10 · peur, comparaison, marchandage
cam(52.0, S10)
headline(S10, 280, ["Peur, [comparaison],", "marchandage"], 52.1, kicker="Si c'est ça qui te fait donner", hl_t=W("comparaison", 52.0), size=80)
sticker(S10, "baton-tiraille", 60, 650, 320, 52.4, rot=-2)
tag(S10, 70, 1160, "Ralentis", W("ralentis", 52.0), "acc", 46)
tag(S10, 70, 1250, "Parles-en à un responsable de confiance", W("responsable", 52.0), "", 30)
hit(W("ralentis", 52.0), 0.8)

# --- S11 · besoins essentiels
cam(58.6, S11)
headline(S11, 280, ["Tes besoins", "[essentiels] d'abord"], 58.7, kicker="Rappelle-toi", hl_t=W("essentiels", 58.6), size=84)
sticker(S11, "enveloppes-budget", 40, 650, 440, 59.0, rot=-2)
tag(S11, 70, 1160, "Donner sans te mettre en difficulté", W("difficult", 58.6), "acc", 32)
hit(W("essentiels", 58.6), 0.7)

# --- S12 · question aux spectateurs
cam(63.8, S12)
headline(S12, 300, ["De quel côté", "es-[tu] ?"], 63.9, kicker="À ton tour", hl_t=W("côté", 63.8), size=104)
sticker(S12, "baton-pense", 700, 880, 210, 64.2, rot=3)
cta = put(S12, 70, 760, CTA, "cta")
blur_in(cta, W("commentaire", 63.8) - 0.4, 14)
sfx("click", W("commentaire", 63.8) - 0.4, 0.8)
tag(S12, 70, 900, "Abonne-toi", W("abonne", 63.8), "acc", 48)

# --- fin en boucle
cam(67.7, S1)
bigword("Sans pression", W("pression", 67.7), 1.0, y=1260, size=100)
hit(W("joyeusement", 67.7), 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 12.9), ("02", "Verset", 12.9, 32.5), ("03", "Test", 32.5, 63.8), ("04", "Action", 63.8, DUR)],
    suppress=[(17.1, 24.2)],
)

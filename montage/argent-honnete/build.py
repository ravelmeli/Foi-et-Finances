"""Short « Le principe biblique de l'argent honnêtement gagné » (Éphésiens 4.28) — style 02, 9:16, ~85.8 s.
Lot de 4 Shorts. Acquis : mots géants, compteurs, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte refermée, fin qui revient sur la première image. Temps lus dans transcript.json (voix fournie).

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Le principe biblique de l'argent honnêtement gagné", "lang": "fr"}
COLS, ROWS = 3, 13
s.setup(here=HERE, duration=85.8, cols=COLS, rows=ROWS, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
S = ST
_TR = json.load(open(os.path.join(HERE, "transcript.json"), encoding="utf-8"))


def _norm(x):
    return re.sub(r"[^\w]+", "", unicodedata.normalize("NFC", x.lower()))


def W(prefix, after=0.0, nth=0):
    """Début (en secondes) du n-ième mot contenant `prefix`, après l'instant `after`."""
    k = 0
    for w in _TR:
        if w["start"] >= after and _norm(prefix) in _norm(w["text"]):
            if k == nth:
                return round(w["start"], 2)
            k += 1
    raise KeyError(prefix)


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



S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13 = S[:13]

# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "balance-juste", 30, 660, 560, 0.0, rot=-2, instant=True)
headline(S1, 300, ["De l'argent,", "à [quel] prix ?"], 0.0, kicker="Gagner honnêtement", hl_t=2.2, size=100)
bigword("À tout prix ?", 2.4, 0.8, y=1260, size=110)
hit(2.6, 0.9)

# --- S2 · boucle ouverte : la deuxième raison
cam(3.0, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 3.1, kicker="La raison n°2", hl_t=4.2, size=104)
q = put(S2, 230, 640, "<small>Raison</small>2 ?", "box out", "width:620px;font-size:120px")
blur_in(q, 6.2, 12)
sticker(S2, "baton-pense", 680, 860, 230, 3.8, rot=3)
tag(S2, 70, 1000, "Elle ne se voit pas sur ton compte", 7.2, "acc", 30)
hit(6.4, 0.8)

# --- S3 · le verset (Éphésiens 4.28) : séquence « Parole »
cam(9.5, S3)
headline(S3, 280, ["Arrête de prendre,", "[travaille]"], 9.6, kicker="Lettre aux Éphésiens", hl_t=14.0, size=84)
verse = ("«&nbsp;Que celui qui dérobait ne dérobe plus ; mais plutôt qu'il " + m(0, "travaille") + ", faisant de ses mains ce qui est bien, afin "
         + m(1, "d'avoir de quoi donner") + " à celui qui est dans le besoin.&nbsp;»")
verse_block(S3, "Éphésiens 4.28", 11.0, verse, 12.7, [W("travaille", 12.7), W("donner", 12.7)], size=48, ref_label="ÉPHÉSIENS 4.28")
sticker(S3, "livre-croix-ouvert", 60, 1130, 320, 10.0, rot=-3)
sticker(S3, "mains-outil-piece", 560, 1110, 340, 16.5, rot=3)
hit(21.0, 1.0)

# --- S4 · un principe en trois temps
cam(21.1, S4)
headline(S4, 280, ["Trois", "[temps]"], 21.2, kicker="Un principe", hl_t=21.9, size=110)
counter(S4, 70, 640, 0, 3, 22.4, 0.8, " temps", 140)
tag(S4, 70, 860, "Arrête de prendre", 23.4, "", 38)
tag(S4, 70, 950, "Travaille honnêtement", 24.8, "", 38)
tag(S4, 70, 1040, "Donne", 26.2, "acc", 42)
sticker(S4, "baton-rend-bourse", 620, 700, 300, 23.0, rot=3)
hit(26.8, 0.7)

# --- S5 · ce que cela change pour ton argent
cam(27.2, S5)
headline(S5, 280, ["Pour ton", "[argent]"], 27.3, kicker="Ce que cela change", hl_t=28.3, size=110)
sticker(S5, "baton-rend-bourse", 40, 650, 440, 27.8, rot=-2)
hit(29.4, 0.7)

# --- S6 · 1 : sans tromperie
cam(29.7, S6)
headline(S6, 280, ["Sans", "[tromperie]"], 29.8, kicker="Honnête 1", hl_t=30.8, size=110)
sticker(S6, "facture-propre", 40, 660, 380, 30.2, rot=-2)
tag(S6, 70, 1100, "Pas de mensonge sur un prix", 32.0, "", 34)
tag(S6, 70, 1190, "Pas de revenus cachés", 34.0, "", 36)
tag(S6, 70, 1280, "Pas de promesse exagérée", 35.4, "acc", 34)
hit(36.8, 0.7)

# --- S7 · 2 : une paix qui ne se voit pas
cam(37.3, S7)
headline(S7, 280, ["Une [paix]", "qui ne se voit pas"], 37.4, kicker="Honnête 2", hl_t=38.6, size=84)
sticker(S7, "bocal-transparent", 60, 650, 330, 38.0, rot=-2)
sticker(S7, "baton-banc-calme", 580, 720, 330, 43.0, rot=3)
tag(S7, 70, 1090, "Pas peur d'un contrôle", 39.8, "", 36)
tag(S7, 70, 1180, "Ni d'une conversation", 41.2, "", 36)
tag(S7, 70, 1270, "Ni de ton regard", 42.4, "acc", 38)
hit(45.0, 0.9)

# --- S8 · 3 : pouvoir donner (referme la boucle)
cam(46.7, S8)
headline(S8, 280, ["Pouvoir", "[donner]"], 46.8, kicker="Honnête 3", hl_t=47.8, size=110)
sticker(S8, "mains-outil-piece", 40, 660, 420, 47.2, rot=-2)
tag(S8, 70, 1100, "Avec un cœur libre", 49.2, "acc", 42)
hit(50.0, 0.7)

# --- S9 · honnête, pas facile
cam(51.6, S9)
headline(S9, 280, ["Honnête,", "pas [facile]"], 51.7, kicker="Attention", hl_t=52.8, size=110)
sticker(S9, "baton-pense", 600, 700, 240, 52.0, rot=3)
tag(S9, 70, 700, "Modeste", 54.0, "", 40)
tag(S9, 70, 790, "Long", 55.0, "", 40)
tag(S9, 70, 880, "Mal payé", 56.0, "acc", 40)
hit(56.8, 0.7)

# --- S10 · honnête, pas parfait : on peut réparer
cam(57.4, S10)
headline(S10, 280, ["Honnête,", "pas [parfait]"], 57.5, kicker="Tu peux réparer", hl_t=58.5, size=110)
sticker(S10, "baton-rend-bourse", 600, 640, 340, 58.0, rot=3)
tag(S10, 70, 640, "Rembourser", 60.6, "", 38)
tag(S10, 70, 730, "Corriger", 61.6, "", 38)
tag(S10, 70, 820, "Demander pardon", 62.4, "", 38)
tag(S10, 70, 910, "Recommencer", 63.8, "acc", 40)
hit(64.8, 0.7)

# --- S11 · pas de promesse de salaire : il protège ton cœur
cam(65.4, S11)
headline(S11, 280, ["Il protège", "ton [cœur]"], 65.5, kicker="Ce principe", hl_t=68.6, size=110)
sticker(S11, "coeur-receptacle", 60, 650, 400, 66.0, rot=-3)
sticker(S11, "croix-verte", 620, 700, 230, 68.6, rot=4)
tag(S11, 70, 1100, "Pas une promesse de salaire", 66.4, "", 34)
hit(69.2, 0.8)

# --- S12 · cette semaine : passe en revue tes revenus
cam(69.6, S12)
headline(S12, 280, ["Passe en revue", "tes [revenus]"], 69.7, kicker="Cette semaine", hl_t=70.5, size=92)
sticker(S12, "facture-propre", 60, 650, 360, 70.0, rot=-2)
sticker(S12, "baton-ecrit-liste", 600, 700, 300, 72.0, rot=3)
tag(S12, 70, 1130, "Une source te gêne ?", 73.0, "", 36)
tag(S12, 70, 1220, "Corrige-la", 74.9, "acc", 44)

# --- S13 · question aux spectateurs
cam(76.3, S13)
headline(S13, 300, ["Quelle habitude", "[renforcer] ?"], 76.4, kicker="À ton tour", hl_t=77.0, size=96)
sticker(S13, "baton-serein", 700, 880, 210, 76.8, rot=3)
cta = put(S13, 70, 760, CTA, "cta")
blur_in(cta, 78.6, 14)
sfx("click", 78.6, 0.8)
tag(S13, 70, 900, "Abonne-toi", 80.0, "acc", 48)

# --- fin en boucle
cam(81.2, S1)
bigword("Rien à cacher", 83.4, 1.0, y=1260, size=110)
hit(83.6, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 9.5), ("02", "Verset", 9.5, 21.1), ("03", "Principe", 21.1, 69.6), ("04", "Action", 69.6, DUR)],
    suppress=[(12.65, 21.15)],
)

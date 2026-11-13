"""Short « Pourquoi Dieu s'intéresse à ta façon de dépenser » (1 Corinthiens 10.31) — style 02, 9:16, ~76.0 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Pourquoi Dieu s'intéresse à ta façon de dépenser", "lang": "fr"}
COLS, ROWS = 3, 16
s.setup(here=HERE, duration=76.0, cols=COLS, rows=ROWS, theme=THEME)
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



S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16 = S[:16]

# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-allee-pause", 30, 650, 540, 0.0, rot=-2, instant=True)
sticker(S1, "portefeuille-croix", 620, 760, 310, 3.0, rot=3)
headline(S1, 300, ["Mon argent,", "mon [affaire] ?"], 0.0, kicker="Tu penses peut-être", hl_t=2.2, size=100)
bigword("Et Dieu ?", 3.9, 0.8, y=1260, size=120)
hit(4.0, 0.9)

# --- S2 · pourquoi la Bible parle-t-elle de dépenser ?
cam(4.4, S2)
headline(S2, 280, ["La Bible parle", "de [dépenser]"], 4.5, kicker="Alors pourquoi ?", hl_t=6.0, size=88)
sticker(S2, "ticket-caisse-icones", 60, 650, 330, 4.9, rot=-3)
sticker(S2, "loupe-budget", 560, 720, 340, 6.4, rot=3)
hit(7.0, 0.7)

# --- S3 · boucle ouverte : la raison est une bonne nouvelle
cam(7.7, S3)
headline(S3, 280, ["Reste jusqu'au", "[bout]"], 7.8, kicker="Une bonne nouvelle", hl_t=8.6, size=104)
q = put(S3, 190, 640, "<small>Une menace ?</small>Non", "box out", "width:700px;font-size:120px")
blur_in(q, 10.3, 12)
sticker(S3, "baton-pense", 680, 860, 230, 8.2, rot=3)
hit(10.5, 0.8)

# --- S4 · le verset (1 Corinthiens 10.31) : séquence « Parole » ; sous-titres coupés
cam(12.0, S4)
headline(S4, 280, ["Tout pour", "la [gloire]"], 12.1, kicker="1 Corinthiens 10", hl_t=20.2, size=104)
verse = ("«&nbsp;Soit donc que vous mangiez, soit que vous buviez, soit que vous fassiez quelque autre chose, " + m(0, "faites tout pour la gloire de Dieu") + ".&nbsp;»")
verse_block(S4, "1 Corinthiens 10.31", 13.3, verse, 15.2, [W("faites", 15.0)], size=54, ref_label="1 CORINTHIENS 10.31")
sticker(S4, "livre-croix-ouvert", 60, 1100, 380, 12.8, rot=-3)
sticker(S4, "croix-verte", 580, 1090, 190, 18.5, rot=4)
hit(21.0, 1.0)

# --- S5 · « quelque autre chose » : acheter, payer, donner, se faire plaisir
cam(21.6, S5)
headline(S5, 280, ["« Quelque autre", "[chose] »"], 21.7, kicker="Remarque", hl_t=22.8, size=88)
sticker(S5, "ticket-caisse-icones", 600, 640, 380, 22.4, rot=3)
tag(S5, 70, 640, "Acheter", 23.4, "", 40)
tag(S5, 70, 730, "Payer", 24.3, "", 40)
tag(S5, 70, 820, "Donner", 25.0, "", 40)
tag(S5, 70, 910, "Se faire plaisir", 25.8, "acc", 40)
hit(26.4, 0.7)

# --- S6 · rien n'est neutre
cam(26.7, S6)
headline(S6, 280, ["Rien n'est", "[neutre]"], 26.8, kicker="Chaque dépense", hl_t=27.6, size=110)
sticker(S6, "loupe-budget", 60, 650, 420, 27.2, rot=-3)
sticker(S6, "baton-pense", 620, 700, 240, 28.4, rot=3)
tag(S6, 70, 1100, "Dit ce qu'on valorise", 29.0, "acc", 38)
hit(29.6, 0.7)

# --- S7 · pas « ne dépense rien », mais « pour sa gloire »
cam(30.2, S7)
headline(S7, 280, ["Dépenser", "[pour lui]"], 30.3, kicker="Ce que Dieu dit", hl_t=32.4, size=110)
sticker(S7, "portefeuille-croix", 60, 660, 420, 31.0, rot=-3)
sticker(S7, "croix-verte", 620, 700, 230, 33.0, rot=4)
hit(33.4, 0.8)

# --- S8 · il s'intéresse à toi tout entier
cam(34.6, S8)
headline(S8, 280, ["Il s'intéresse", "à toi [tout entier]"], 34.7, kicker="La vraie raison", hl_t=36.4, size=78)
sticker(S8, "coeur-receptacle", 60, 650, 400, 35.5, rot=-3)
sticker(S8, "baton-priere", 620, 700, 250, 38.0, rot=3)
hit(38.8, 0.8)

# --- S9 · il ne te surveille pas pour te piéger
cam(40.0, S9)
headline(S9, 280, ["Pas pour", "te [piéger]"], 40.1, kicker="Un père qui te conduit", hl_t=41.3, size=110)
sticker(S9, "baton-serein", 60, 650, 300, 40.5, rot=-2)
sticker(S9, "soleil-nuage", 600, 700, 330, 42.4, rot=3)
tag(S9, 70, 1130, "Il veut ton bien", 42.9, "acc", 42)
hit(43.8, 0.7)

# --- S10 · trois questions
cam(44.5, S10)
headline(S10, 280, ["Trois", "[questions]"], 44.6, kicker="Avant une dépense", hl_t=45.2, size=110)
counter(S10, 70, 640, 0, 3, 45.4, 0.8, " questions", 140)
sticker(S10, "baton-pense", 560, 880, 220, 46.0, rot=3)
hit(46.2, 0.7)

# --- S11 · question 1 : mes priorités
cam(47.2, S11)
headline(S11, 280, ["Mes", "[priorités] ?"], 47.3, kicker="Question 1", hl_t=48.2, size=110)
sticker(S11, "baton-budget", 60, 650, 330, 47.7, rot=-2)
tag(S11, 70, 1190, "Me rapproche ou m'éloigne ?", 49.2, "acc", 36)

# --- S12 · question 2 : avec reconnaissance
cam(51.2, S12)
headline(S12, 280, ["Avec", "[reconnaissance] ?"], 51.3, kicker="Question 2", hl_t=52.4, size=84)
sticker(S12, "baton-repas-merci", 40, 650, 540, 51.7, rot=-2)
hit(52.8, 0.7)

# --- S13 · question 3 : au service des autres
cam(53.9, S13)
headline(S13, 280, ["Au service", "des [autres] ?"], 54.0, kicker="Question 3", hl_t=55.0, size=100)
sticker(S13, "baton-cadeau-ami", 40, 650, 560, 54.3, rot=-2)
hit(55.8, 0.7)

# --- S14 · bonté et gratitude
cam(56.7, S14)
headline(S14, 280, ["Dépenser,", "un acte de [bonté]"], 56.8, kicker="Et se faire plaisir ?", hl_t=58.2, size=84)
sticker(S14, "baton-cadeau-ami", 40, 650, 500, 57.2, rot=-2)
tag(S14, 70, 1050, "Pas un péché", 59.8, "", 42)
tag(S14, 70, 1140, "Avec gratitude", 61.0, "acc", 42)
hit(61.6, 0.8)

# --- S15 · cette semaine : dix secondes
cam(62.5, S15)
headline(S15, 280, ["Dix", "[secondes]"], 62.6, kicker="Avant chaque dépense", hl_t=65.0, size=110)
counter(S15, 70, 660, 0, 10, 65.2, 1.0, " s", 140)
sticker(S15, "ticket-caisse-icones", 600, 700, 330, 63.2, rot=3)
tag(S15, 70, 1000, "Pose-toi la question 2", 67.0, "acc", 36)
hit(66.4, 0.7)

# --- S16 · question aux spectateurs
cam(67.9, S16)
headline(S16, 300, ["Quelle dépense", "offrir à [Dieu] ?"], 68.0, kicker="À ton tour", hl_t=69.2, size=90)
sticker(S16, "baton-serein", 700, 880, 210, 68.6, rot=3)
cta = put(S16, 70, 760, CTA, "cta")
blur_in(cta, 70.1, 14)
sfx("click", 70.1, 0.8)
tag(S16, 70, 900, "Abonne-toi", 70.8, "acc", 48)

# --- fin en boucle
cam(71.2, S1)
bigword("Un témoignage", 73.3, 1.0, y=1260, size=100)
hit(73.5, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 12.0), ("02", "Verset", 12.0, 21.6), ("03", "Pourquoi", 21.6, 44.5), ("04", "Questions", 44.5, DUR)],
    suppress=[(15.15, 21.65)],
)

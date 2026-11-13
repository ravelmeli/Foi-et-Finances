"""Short « La règle biblique des 24 heures avant un achat » (Proverbes 14.15) — style 02, 9:16, ~79.8 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - La règle biblique des 24 heures avant un achat", "lang": "fr"}
COLS, ROWS = 3, 18
s.setup(here=HERE, duration=79.8, cols=COLS, rows=ROWS, theme=THEME)
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


S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17 = S[:17]

# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-tente-achat", 30, 660, 540, 0.0, rot=-2, instant=True)
sticker(S1, "panier-pause", 640, 760, 300, 1.2, rot=3)
headline(S1, 300, ["Une [promo]…", "ta main veut payer ?"], 0.0, kicker="Attends !", hl_t=0.4, size=92)
bigword("Attends !", 0.3, 0.8, y=1260, size=120)
hit(0.5, 0.9)

# --- S2 · boucle ouverte : la question n°2
cam(3.0, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 3.1, kicker="La question n°2", hl_t=3.9, size=104)
q = put(S2, 230, 640, "<small>Question</small>2 ?", "box out", "width:620px;font-size:120px")
blur_in(q, 5.2, 12)
sticker(S2, "baton-pense", 680, 860, 230, 3.6, rot=3)
tag(S2, 70, 1000, "Elle évite les regrets", 6.4, "acc", 38)
hit(5.4, 0.8)

# --- S3 · précision : pas de règle de 24 h dans la Bible
cam(7.7, S3)
headline(S3, 280, ["Pas de règle", "de [24 h]"], 7.8, kicker="Petite précision honnête", hl_t=9.4, size=104)
sticker(S3, "livre-croix-ouvert", 60, 660, 360, 8.3, rot=-3)
sticker(S3, "horloge-jour-nuit", 560, 700, 340, 9.6, rot=3)
tag(S3, 70, 1100, "Mais un principe très clair", 11.4, "acc", 38)
hit(12.2, 0.7)

# --- S4 · le verset (Proverbes 14.15) : séquence « Parole » ; sous-titres coupés
cam(13.6, S4)
headline(S4, 280, ["L'homme", "[prudent]"], 13.7, kicker="Livre des Proverbes", hl_t=19.2, size=110)
verse = ("«&nbsp;L'homme simple " + m(0, "croit tout ce qu'on dit") + ", mais " + m(1, "l'homme prudent est attentif à ses pas") + ".&nbsp;»")
verse_block(S4, "Proverbes 14.15", 15.4, verse, 16.9, [W("croit", 16.0), W("prudent", 16.0)], size=50, ref_label="PROVERBES 14.15")
sticker(S4, "livre-croix-ouvert", 60, 1110, 380, 14.0, rot=-3)
sticker(S4, "croix-verte", 580, 1090, 190, 18.0, rot=4)
hit(21.0, 1.0)

# --- S5 · être prudent
cam(21.4, S5)
headline(S5, 280, ["Regarder où", "on met les [pieds]"], 21.5, kicker="Être prudent", hl_t=22.6, size=88)
sticker(S5, "baton-attend", 40, 650, 460, 21.8, rot=-2)
tag(S5, 70, 1170, "Avant d'avancer", 23.0, "acc", 44)
hit(23.8, 0.7)

# --- S6 · la règle des 24 heures
cam(24.7, S6)
headline(S6, 280, ["La règle des", "[24 heures]"], 24.8, kicker="Une application pratique", hl_t=26.0, size=104)
sticker(S6, "horloge-jour-nuit", 60, 660, 420, 25.2, rot=-3)
sticker(S6, "panier-pause", 600, 720, 320, 27.0, rot=3)
counter(S6, 70, 1230, 0, 24, 25.6, 1.0, " h", 110)
hit(26.2, 0.8)

# --- S7 · étape 1 : note l'envie, ne l'achète pas
cam(28.5, S7)
headline(S7, 280, ["Note-la,", "ne l'[achète] pas"], 28.6, kicker="Étape 1", hl_t=29.6, size=96)
sticker(S7, "baton-tente-achat", 40, 660, 360, 28.9, rot=-2)
sticker(S7, "liste-envies", 560, 680, 380, 29.9, rot=3)
tag(S7, 70, 1130, "Écris l'envie", 31.0, "acc", 44)
hit(31.8, 0.7)

# --- S8 · étape 2 : attends 24 heures
cam(32.3, S8)
headline(S8, 280, ["Attends", "[24 heures]"], 32.4, kicker="Étape 2", hl_t=33.5, size=110)
sticker(S8, "baton-attend", 40, 650, 440, 32.8, rot=-2)
sticker(S8, "calendrier-mois", 600, 720, 320, 35.0, rot=3)
tag(S8, 70, 1150, "Gros achat : une semaine", 35.2, "acc", 38)
hit(36.0, 0.7)

# --- S9 · trois questions
cam(36.5, S9)
headline(S9, 280, ["Trois", "[questions]"], 36.6, kicker="Après ce délai", hl_t=37.2, size=110)
counter(S9, 70, 640, 0, 3, 37.0, 0.8, " questions", 140)
sticker(S9, "baton-pense", 580, 860, 230, 37.8, rot=3)
hit(37.9, 0.7)

# --- S10 · question 1 : besoin
cam(38.5, S10)
headline(S10, 280, ["Un [besoin] ?"], 38.6, kicker="Question 1", hl_t=39.0, size=120)
sticker(S10, "panier-besoins", 60, 650, 330, 39.0, rot=-3)
sticker(S10, "maison-simple", 560, 690, 300, 40.0, rot=3)
tag(S10, 70, 1050, "En ai-je vraiment besoin ?", 39.8, "", 38)

# --- S11 · question 2 : sans crédit ni découvert (referme la boucle ouverte)
cam(41.3, S11)
headline(S11, 280, ["Sans [crédit]", "ni découvert"], 41.4, kicker="Question 2", hl_t=42.8, size=100)
sticker(S11, "carte-cadenas", 40, 650, 520, 41.8, rot=-2)
bigword("Question 2", 41.6, 0.9, y=1130, size=110)
tag(S11, 70, 1300, "La plus utile", 44.6, "acc", 42)
hit(44.8, 0.9)

# --- S12 · question 3 : encore envie demain ?
cam(46.6, S12)
headline(S12, 280, ["Encore [envie]", "demain ?"], 46.7, kicker="Question 3", hl_t=48.2, size=104)
sticker(S12, "baton-pense", 60, 650, 240, 47.0, rot=-2)
sticker(S12, "horloge-jour-nuit", 560, 720, 300, 48.4, rot=3)

# --- S13 · l'envie baisse
cam(49.8, S13)
headline(S13, 280, ["L'envie", "[baisse]"], 49.9, kicker="Souvent", hl_t=51.0, size=110)
sticker(S13, "baton-serein", 60, 650, 300, 50.3, rot=-2)
sticker(S13, "soleil-nuage", 600, 720, 320, 52.4, rot=3)
tag(S13, 70, 1130, "Une promo crée de l'urgence", 52.8, "", 36)
tag(S13, 70, 1220, "pas du besoin", 54.0, "acc", 44)
hit(54.4, 0.8)

# --- S14 · trois fois oui : achète en paix
cam(54.9, S14)
headline(S14, 280, ["Achète", "en [paix]"], 55.0, kicker="Si trois fois oui", hl_t=56.2, size=110)
sticker(S14, "baton-content", 60, 650, 300, 55.4, rot=-2)
sticker(S14, "colombe", 600, 720, 300, 57.0, rot=3)
tag(S14, 70, 1190, "Un filtre, pas une punition", 58.6, "acc", 36)
hit(59.0, 0.8)

# --- S15 · cette semaine : mets en attente
cam(60.7, S15)
headline(S15, 280, ["Mets en", "[attente]"], 60.8, kicker="Cette semaine", hl_t=61.8, size=110)
sticker(S15, "panier-pause", 60, 650, 360, 61.2, rot=-2)
sticker(S15, "liste-envies", 560, 700, 380, 64.4, rot=3)
tag(S15, 70, 1200, "Écris-la sur ton téléphone", 64.6, "", 34)
tag(S15, 70, 1290, "Date et heure", 66.2, "acc", 42)

# --- S16 · prudent ne veut pas dire radin
cam(67.0, S16)
headline(S16, 280, ["Prudent,", "pas [radin]"], 67.1, kicker="Rappelle-toi", hl_t=68.2, size=110)
sticker(S16, "baton-attend", 60, 650, 420, 67.5, rot=-2)
sticker(S16, "croix-verte", 620, 700, 220, 69.0, rot=4)
tag(S16, 70, 1130, "Cela veut dire : libre", 68.8, "acc", 44)
hit(69.2, 0.8)

# --- S17 · question aux spectateurs
cam(69.9, S17)
headline(S17, 300, ["Quel achat", "mettre en [pause] ?"], 70.0, kicker="À ton tour", hl_t=71.2, size=92)
sticker(S17, "baton-serein", 700, 880, 210, 70.6, rot=3)
cta = put(S17, 70, 760, CTA, "cta")
blur_in(cta, 72.2, 14)
sfx("click", 72.2, 0.8)
tag(S17, 70, 900, "Abonne-toi", 73.0, "acc", 48)

# --- fin en boucle
cam(73.7, S1)
bigword("Son argent", 75.6, 0.8, y=1260, size=110)
bigword("Sa paix", 77.4, 0.9, y=1260, size=120)
hit(77.5, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 13.6), ("02", "Principe", 13.6, 24.7), ("03", "Règle", 24.7, 49.9), ("04", "Action", 49.9, DUR)],
    suppress=[(16.85, 21.35)],
)

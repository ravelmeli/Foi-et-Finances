"""Short « Comment prier avant de prendre une décision financière » (Jacques 1.5) — style 02, 9:16, ~86.5 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Comment prier avant de prendre une décision financière", "lang": "fr"}
COLS, ROWS = 3, 14
s.setup(here=HERE, duration=86.5, cols=COLS, rows=ROWS, theme=THEME)
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



S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14 = S[:14]

# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-stop-offre", 30, 650, 540, 0.0, rot=-2, instant=True)
headline(S1, 300, ["Une grosse", "décision [d'argent]"], 0.0, kicker="Tu hésites ?", hl_t=1.4, size=96)
bigword("Que faire ?", 2.9, 0.9, y=1260, size=120)
hit(3.0, 0.9)

# --- S2 · boucle ouverte : la quatrième étape
cam(4.4, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 4.5, kicker="L'étape n°4", hl_t=5.0, size=104)
q = put(S2, 230, 640, "<small>Étape</small>4 ?", "box out", "width:620px;font-size:120px")
blur_in(q, 6.4, 12)
sticker(S2, "baton-pense", 680, 860, 230, 5.0, rot=3)
tag(S2, 70, 1000, "Presque tout le monde l'oublie", 7.4, "acc", 34)
hit(6.4, 0.8)

# --- S3 · le verset (Jacques 1.5) : séquence « Parole » ; sous-titres coupés
cam(9.2, S3)
headline(S3, 280, ["Demander la", "[sagesse]"], 9.3, kicker="Épître de Jacques", hl_t=13.6, size=110)
verse = ("«&nbsp;Si quelqu'un d'entre vous " + m(0, "manque de sagesse") + ", qu'il la " + m(1, "demande à Dieu") + ", qui donne à tous simplement et sans reproche, et elle lui sera donnée.&nbsp;»")
verse_block(S3, "Jacques 1.5", 10.4, verse, 11.7, [W("sagesse", 11.5), W("demande", 11.5)], size=50, ref_label="JACQUES 1.5")
sticker(S3, "livre-croix-ouvert", 60, 1130, 300, 9.8, rot=-3)
sticker(S3, "croix-verte", 700, 1120, 170, 16.0, rot=4)
hit(19.3, 1.0)

# --- S4 · Dieu n'est pas agacé
cam(19.6, S4)
headline(S4, 280, ["Il t'invite à", "[demander]"], 19.7, kicker="Il n'est pas agacé", hl_t=22.4, size=104)
sticker(S4, "baton-prie-bureau", 40, 650, 480, 20.0, rot=-2)
sticker(S4, "coeur-receptacle", 620, 740, 300, 22.5, rot=3)
hit(23.6, 0.7)

# --- S5 · prier ne remplace pas réfléchir
cam(24.6, S5)
headline(S5, 280, ["Prier ne remplace", "pas [réfléchir]"], 24.7, kicker="Cinq étapes", hl_t=26.6, size=84)
counter(S5, 70, 640, 0, 5, 27.8, 0.9, " étapes", 140)
sticker(S5, "faits-dossier", 580, 880, 330, 26.4, rot=3)
hit(28.8, 0.7)

# --- S6 · étape 1 : arrête-toi
cam(29.8, S6)
headline(S6, 280, ["Arrête-[toi]"], 29.9, kicker="Étape 1", hl_t=30.5, size=120)
sticker(S6, "baton-stop-offre", 40, 650, 460, 30.2, rot=-2)
tag(S6, 70, 1150, "Pas sous pression", 32.0, "acc", 40)
tag(S6, 70, 1240, "Une offre qui expire", 33.4, "", 36)
hit(33.8, 0.7)

# --- S7 · étape 2 : prie simplement
cam(34.9, S7)
headline(S7, 280, ["Prie", "[simplement]"], 35.0, kicker="Étape 2", hl_t=36.0, size=110)
sticker(S7, "baton-prie-bureau", 40, 650, 500, 35.4, rot=-2)
tag(S7, 70, 1190, "« Donne-moi la sagesse »", 37.4, "acc", 34)
tag(S7, 70, 1280, "Garde mon cœur de la peur", 40.2, "", 32)
hit(38.0, 0.7)

# --- S8 · étape 3 : regarde les faits
cam(43.8, S8)
headline(S8, 280, ["Regarde les", "[faits]"], 43.9, kicker="Étape 3", hl_t=44.8, size=110)
sticker(S8, "faits-dossier", 40, 650, 480, 44.3, rot=-2)
tag(S8, 70, 1090, "Les chiffres", 45.6, "", 38)
tag(S8, 70, 1180, "Le contrat", 46.6, "", 38)
tag(S8, 70, 1270, "Les risques", 47.6, "", 38)
tag(S8, 70, 1360, "Le vrai coût", 48.8, "acc", 36)
hit(49.4, 0.7)

# --- S9 · étape 4 : demande conseil (referme la boucle ouverte)
cam(49.9, S9)
headline(S9, 280, ["Demande", "[conseil]"], 50.0, kicker="Étape 4", hl_t=50.9, size=110)
sticker(S9, "baton-conseil-cafe", 40, 650, 520, 50.3, rot=-2)
tag(S9, 70, 1140, "Une personne sage", 52.0, "", 38)
tag(S9, 70, 1230, "pas seulement qui t'approuve", 53.0, "acc", 34)
hit(54.0, 0.9)

# --- S10 · étape 5 : décide, puis confie
cam(55.3, S10)
headline(S10, 280, ["Décide,", "puis [confie]"], 55.4, kicker="Étape 5", hl_t=56.6, size=110)
sticker(S10, "baton-marche-confiant", 40, 650, 460, 55.8, rot=-2)
sticker(S10, "soleil-nuage", 620, 720, 300, 58.5, rot=3)
tag(S10, 70, 1150, "Avance sans te torturer", 60.0, "acc", 36)
hit(61.0, 0.7)

# --- S11 · attention : la paix ne remplace pas les chiffres
cam(62.6, S11)
headline(S11, 280, ["La paix ne remplace", "pas les [chiffres]"], 62.7, kicker="Attention", hl_t=64.4, size=78)
sticker(S11, "faits-dossier", 40, 650, 420, 63.0, rot=-2)
sticker(S11, "baton-serein", 580, 720, 280, 64.5, rot=3)
tag(S11, 70, 1130, "Tranquille ≠ bon choix", 65.5, "acc", 36)
hit(66.5, 0.7)

# --- S12 · attendre quelques jours
cam(67.8, S12)
headline(S12, 280, ["Attendre", "[quelques jours]"], 67.9, kicker="Si tu hésites encore", hl_t=69.2, size=88)
sticker(S12, "sablier-feuille", 60, 650, 380, 68.2, rot=-2)
sticker(S12, "calendrier-mois", 600, 720, 300, 70.0, rot=3)
hit(71.5, 0.7)

# --- S13 · cette semaine : les cinq étapes dans l'ordre
cam(72.3, S13)
headline(S13, 280, ["Cinq étapes,", "dans [l'ordre]"], 72.4, kicker="Cette semaine", hl_t=73.6, size=100)
sticker(S13, "baton-ecrit-liste", 60, 650, 360, 73.0, rot=-2)
hit(75.0, 0.7)

# --- S14 · question aux spectateurs
cam(76.9, S14)
headline(S14, 300, ["Quelle décision", "te [pèse] ?"], 77.0, kicker="À ton tour", hl_t=77.6, size=96)
sticker(S14, "baton-serein", 700, 880, 210, 77.4, rot=3)
cta = put(S14, 70, 760, CTA, "cta")
blur_in(cta, 79.5, 14)
sfx("click", 79.5, 0.8)
tag(S14, 70, 900, "Abonne-toi", 80.3, "acc", 48)

# --- fin en boucle
cam(81.2, S1)
bigword("Décide mieux", 83.9, 0.9, y=1260, size=110)
hit(84.0, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 9.2), ("02", "Verset", 9.2, 24.6), ("03", "Étapes", 24.6, 62.6), ("04", "Action", 62.6, DUR)],
    suppress=[(11.65, 19.65)],
)

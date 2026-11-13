"""Short « Comment devenir fidèle dans les petites finances » (Luc 16.10) — style 02, 9:16, ~84.8 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Comment devenir fidèle dans les petites finances", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=84.8, cols=COLS, rows=ROWS, theme=THEME)
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


S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15 = S[:15]

# --- S1 · accroche (aussi l'image de fin)
cam(0, S1)
sticker(S1, "main-piece", 30, 660, 500, 0.0, rot=-2, instant=True)
sticker(S1, "marches-pieces", 560, 740, 400, 2.4, rot=3)
headline(S1, 300, ["Grandes finances,", "[petits] gestes"], 0.0, kicker="On rêve de grandes finances", hl_t=3.0, size=92)
bigword("Fidèle ?", 4.0, 0.9, y=1250, size=120)
hit(4.2, 0.9)

# --- S2 · boucle ouverte : la quatrième habitude
cam(5.1, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 5.2, kicker="L'habitude n°4", hl_t=6.0, size=104)
q = put(S2, 230, 640, "<small>Habitude</small>4 ?", "box out", "width:620px;font-size:120px")
blur_in(q, 7.0, 12)
sticker(S2, "baton-pense", 680, 860, 230, 5.8, rot=3)
tag(S2, 70, 1000, "L'argent des autres", 8.0, "acc", 38)
hit(7.4, 0.8)

# --- S3 · le verset (Luc 16.10) : séquence « Parole »
cam(9.1, S3)
headline(S3, 280, ["Fidèle dans", "le [peu]"], 9.2, kicker="Évangile de Luc", hl_t=14.6, size=104)
verse = ("«&nbsp;Celui qui est fidèle dans " + m(0, "les moindres choses") + " l'est aussi dans les grandes, et celui qui est " + m(1, "injuste") + " dans les moindres choses l'est aussi dans les grandes.&nbsp;»")
verse_block(S3, "Luc 16.10", 12.2, verse, 14.2, [W("moindres", 14.0), W("injuste", 14.0)], size=50, ref_label="LUC 16.10")
sticker(S3, "livre-croix-ouvert", 60, 1150, 300, 9.8, rot=-3)
sticker(S3, "marches-pieces", 520, 1130, 360, 12.4, rot=3)
hit(21.0, 1.0)

# --- S4 · les grandes finances se construisent dans les petits gestes
cam(21.6, S4)
headline(S4, 280, ["Les petits", "[gestes]"], 21.7, kicker="Se construisent", hl_t=24.0, size=110)
sticker(S4, "marches-pieces", 40, 660, 520, 22.4, rot=-2)
sticker(S4, "baton-epargne", 620, 700, 280, 24.4, rot=3)
tag(S4, 70, 1100, "Pas d'un seul coup", 23.8, "acc", 40)
hit(24.6, 0.7)

# --- S5 · quatre habitudes
cam(26.3, S5)
headline(S5, 280, ["Quatre", "[habitudes]"], 26.4, kicker="Petites finances", hl_t=27.2, size=110)
counter(S5, 70, 640, 0, 4, 27.6, 0.8, " habitudes", 140)
sticker(S5, "baton-budget", 560, 880, 300, 28.4, rot=2)
hit(28.8, 0.7)

# --- S6 · habitude 1 : note chaque dépense
cam(30.3, S6)
headline(S6, 280, ["Note chaque", "[dépense]"], 30.4, kicker="Habitude 1", hl_t=31.8, size=104)
sticker(S6, "baton-note-depense", 40, 650, 420, 31.0, rot=-2)
sticker(S6, "carnet-depenses", 580, 720, 320, 32.6, rot=3)
tag(S6, 70, 1170, "Même 2 euros", 33.4, "acc", 44)
hit(34.6, 0.7)

# --- S7 · habitude 2 : paie à temps
cam(35.9, S7)
headline(S7, 280, ["Paie à", "[temps]"], 36.0, kicker="Habitude 2", hl_t=37.2, size=110)
sticker(S7, "facture-coche", 40, 660, 420, 36.5, rot=-2)
tag(S7, 70, 1060, "Même les petites factures", 38.4, "", 36)
tag(S7, 70, 1150, "Un retard répété devient une habitude", 40.6, "acc", 30)
hit(41.0, 0.7)

# --- S8 · habitude 3 : tiens tes promesses
cam(42.7, S8)
headline(S8, 280, ["Tiens tes", "[promesses]"], 42.8, kicker="Habitude 3", hl_t=43.8, size=104)
sticker(S8, "poignee-main-sac", 40, 650, 440, 43.3, rot=-2)
tag(S8, 70, 1100, "Rembourser un ami", 44.8, "", 38)
tag(S8, 70, 1190, "Le don décidé", 46.4, "", 38)
tag(S8, 70, 1280, "L'abonnement à résilier", 47.8, "acc", 36)
hit(49.0, 0.7)

# --- S9 : habitude 4 : rends ce qui n'est pas à toi (referme la boucle ouverte)
cam(49.5, S9)
headline(S9, 280, ["Rends ce qui", "n'est pas [à toi]"], 49.6, kicker="Habitude 4", hl_t=50.8, size=88)
sticker(S9, "monnaie-rendue", 40, 650, 520, 50.5, rot=-2)
tag(S9, 70, 1120, "La monnaie en trop", 51.6, "", 38)
tag(S9, 70, 1210, "Un objet emprunté", 53.0, "", 38)
tag(S9, 70, 1300, "Une somme avancée", 54.0, "acc", 38)
hit(54.6, 0.8)

# --- S10 · la plus oubliée
cam(54.9, S10)
headline(S10, 280, ["La plus", "[oubliée]"], 55.0, kicker="Personne ne regarde", hl_t=56.4, size=110)
sticker(S10, "baton-pense", 60, 650, 260, 55.5, rot=-2)
tag(S10, 70, 1290, "Personne ne nous regarde", 57.3, "", 36)

# --- S11 · ce que dit ton cœur
cam(59.6, S11)
headline(S11, 280, ["Ce que dit", "ton [cœur]"], 59.7, kicker="C'est là qu'on voit", hl_t=61.0, size=104)
sticker(S11, "coeur-receptacle", 60, 650, 400, 60.0, rot=-3)
sticker(S11, "croix-verte", 620, 700, 230, 61.0, rot=4)
hit(61.8, 0.7)

# --- S12 · fidèle, pas parfait
cam(62.1, S12)
headline(S12, 280, ["Fidèle,", "pas [parfait]"], 62.2, kicker="Attention", hl_t=63.2, size=110)
sticker(S12, "baton-serein", 60, 650, 300, 62.7, rot=-2)
tag(S12, 70, 1130, "Si tu as failli : corrige", 64.8, "", 36)
tag(S12, 70, 1220, "Et recommence", 66.2, "acc", 44)
hit(67.0, 0.7)

# --- S13 · cette semaine : une seule habitude
cam(67.4, S13)
headline(S13, 280, ["Une seule", "[habitude]"], 67.5, kicker="Cette semaine", hl_t=69.0, size=110)
counter(S13, 70, 700, 0, 7, 70.2, 1.0, " jours", 140)
sticker(S13, "calendrier-mois", 600, 650, 330, 68.5, rot=3)
tag(S13, 70, 1000, "La plus facile", 69.8, "acc", 40)
hit(71.8, 0.7)

# --- S14 · ce qui compte : la fidélité
cam(72.6, S14)
headline(S14, 280, ["Pas la taille,", "la [fidélité]"], 72.7, kicker="Ce qui compte", hl_t=74.0, size=96)
sticker(S14, "marches-pieces", 40, 660, 500, 73.2, rot=-2)
sticker(S14, "baton-content", 620, 700, 300, 75.0, rot=3)
hit(75.6, 0.7)

# --- S15 · question aux spectateurs
cam(76.4, S15)
headline(S15, 300, ["Quelle [habitude]", "en premier ?"], 76.5, kicker="À ton tour", hl_t=76.9, size=96)
sticker(S15, "baton-serein", 700, 880, 210, 77.2, rot=3)
cta = put(S15, 70, 760, CTA, "cta")
blur_in(cta, 78.3, 14)
sfx("click", 78.3, 0.8)
tag(S15, 70, 900, "Abonne-toi", 79.0, "acc", 48)

# --- fin en boucle
cam(79.8, S1)
bigword("Le petit", 80.6, 0.8, y=1250, size=120)
bigword("Du grand", 82.4, 0.9, y=1250, size=120)
hit(82.6, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 9.1), ("02", "Verset", 9.1, 21.6), ("03", "Habitudes", 21.6, 54.9), ("04", "Action", 54.9, DUR)],
    suppress=[(14.05, 21.65)],
)

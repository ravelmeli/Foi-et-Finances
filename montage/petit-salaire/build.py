"""Short « Comment gérer un petit salaire avec une grande sagesse » (Proverbes 15.16) — style 02, 9:16, ~87 s.
Acquis des Shorts et longues : mots géants, compteurs, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte (« la quatrième habitude ne coûte pas un euro ») refermée, fin qui revient sur la première image.
Temps lus dans transcript.json.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Petit salaire, grande sagesse", "lang": "fr"}
COLS, ROWS = 3, 5
s.setup(here=HERE, duration=87.2, cols=COLS, rows=ROWS, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13 = ST[:13]


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-fin-de-mois", 30, 640, 420, 0.0, rot=-2, instant=True)
sticker(S1, "petit-salaire-pousse", 540, 760, 400, 3.7, rot=3)
headline(S1, 300, ["Petit salaire,", "[grande] sagesse"], 0.0, kicker="Ton salaire est petit", hl_t=5.0, size=96)
bigword("Sagesse", 5.0, 0.9, y=1290, size=100)
hit(5.2, 0.9)

# --- S2 · boucle ouverte : l'habitude n°4
cam(7.1, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 7.2, kicker="L'habitude n°4", hl_t=8.0, size=104)
q = put(S2, 190, 640, "<small>Coût</small>0 €", "box out", "width:700px;font-size:130px")
blur_in(q, 10.2, 12)
sticker(S2, "baton-pense", 680, 840, 230, 8.5, rot=3)
tag(S2, 70, 1000, "Elle change tout", 11.3, "acc", 40)
hit(11.5, 0.8)

# --- S3 · le verset (Proverbes 15.16) : séquence « Parole » ; sous-titres coupés pendant la citation
cam(12.6, S3)
headline(S3, 280, ["Mieux vaut", "[peu]"], 12.7, kicker="Livre des Proverbes", hl_t=17.2, size=104)
tag(S3, 70, 600, "Proverbes 15.16", 15.6, "acc", 52)
sfx("spark", 15.6, 1.6)
verse = ("«&nbsp;Mieux vaut " + m(0, "peu, avec la crainte de l'Éternel") + ", qu'un grand trésor, " + m(1, "avec le trouble") + ".&nbsp;»")
v = put(S3, 70, 710, f'<div class="h" style="font-size:56px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, 16.7, 20)
tween(f"#{v} .m0 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 18.0)
tween(f"#{v} .m1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 20.7)
sticker(S3, "balance-peu-paix", 60, 1030, 420, 13.2, rot=-2)
sticker(S3, "livre-croix-ouvert", 580, 1140, 320, 16.9, rot=3)
ref(S3, 70, 1420, "PROVERBES 15.16 · LSG 1910", 15.8)
hit(21.4, 1.0)

# --- S4 · la pauvreté n'est pas une vertu ; la paix vaut plus
cam(22.2, S4)
headline(S4, 280, ["Pas une", "[vertu]"], 22.3, kicker="La pauvreté", hl_t=24.2, size=110)
sticker(S4, "baton-serein", 60, 640, 300, 22.8, rot=-2)
sticker(S4, "colombe", 620, 720, 300, 26.0, rot=3)
tag(S4, 70, 1120, "La paix vaut plus", 25.5, "acc", 40)
tag(S4, 70, 1210, "qu'une abondance sans paix", 26.8, "", 34)
hit(27.8, 0.8)

# --- S5 · quatre habitudes
cam(28.2, S5)
headline(S5, 280, ["Quatre", "[habitudes]"], 28.3, kicker="Pour un petit salaire", hl_t=29.0, size=104)
counter(S5, 70, 640, 0, 4, 28.7, 0.8, " habitudes", 130)
sticker(S5, "baton-budget", 560, 880, 300, 29.8, rot=2)
hit(29.9, 0.7)

# --- S6 · habitude 1 : connais tes chiffres
cam(30.4, S6)
headline(S6, 280, ["Connais tes", "[chiffres]"], 30.5, kicker="Habitude 1", hl_t=31.8, size=104)
sticker(S6, "carnet-depenses", 40, 640, 480, 32.0, rot=-2)
sticker(S6, "baton-ecrit-liste", 620, 720, 300, 33.6, rot=3)
tag(S6, 70, 1150, "Ce qui entre, ce qui sort", 33.0, "", 38)
tag(S6, 70, 1240, "On gère ce qu'on regarde", 35.0, "acc", 34)
hit(36.0, 0.8)

# --- S7 · habitude 2 : l'essentiel d'abord
cam(36.5, S7)
headline(S7, 280, ["L'[essentiel]", "d'abord"], 36.6, kicker="Habitude 2", hl_t=37.7, size=104)
sticker(S7, "tuiles-essentiel", 600, 640, 320, 38.0, rot=3)
tag(S7, 70, 660, "Logement", 39.7, "", 40)
tag(S7, 70, 750, "Nourriture", 40.1, "", 40)
tag(S7, 70, 840, "Transport", 40.5, "", 40)
tag(S7, 70, 930, "Factures", 41.4, "", 40)
tag(S7, 70, 1100, "Les envies viennent après", 42.8, "acc", 36)
hit(43.4, 0.7)

# --- S8 · habitude 3 : mets de côté, même un tout petit montant
cam(44.2, S8)
headline(S8, 280, ["Mets de", "[côté]"], 44.3, kicker="Habitude 3", hl_t=45.7, size=110)
sticker(S8, "tirelire-semaine", 40, 640, 520, 46.0, rot=-2)
tag(S8, 70, 1010, "5 € par semaine", 47.6, "acc", 40)
counter(S8, 70, 1100, 0, 260, 49.2, 1.0, " € / an", 110)
tag(S8, 70, 1290, "L'important : l'habitude", 51.5, "", 36)
hit(50.6, 0.8)

# --- S9 · habitude 4 : un cœur content (referme la boucle ouverte)
cam(53.0, S9)
headline(S9, 280, ["Un cœur", "[content]"], 53.1, kicker="Habitude 4", hl_t=54.7, size=110)
sticker(S9, "baton-content", 60, 640, 300, 54.2, rot=-2)
sticker(S9, "soleil-nuage", 620, 720, 300, 55.7, rot=3)
tag(S9, 70, 1180, "Ça ne coûte rien", 56.5, "acc", 40)
tag(S9, 70, 1270, "Plus besoin d'imiter", 58.4, "", 34)
hit(56.8, 0.9)

# --- S10 · la gestion ne suffit pas toujours : demande de l'aide
cam(59.4, S10)
headline(S10, 280, ["La gestion", "ne suffit [pas]"], 59.5, kicker="Attention", hl_t=61.6, size=100)
sticker(S10, "baton-soucieux", 60, 640, 250, 60.0, rot=-2)
sticker(S10, "enveloppe-salaire", 600, 720, 320, 62.0, rot=3)
tag(S10, 70, 1120, "Demande de l'aide", 64.0, "acc", 40)
tag(S10, 70, 1205, "Cherche à gagner plus", 65.8, "", 36)
tag(S10, 70, 1290, "Pas une honte", 66.9, "acc", 42)
hit(67.5, 0.8)

# --- S11 · une seule chose cette semaine
cam(68.1, S11)
headline(S11, 280, ["Une seule", "[chose]"], 68.2, kicker="Cette semaine", hl_t=70.2, size=110)
sticker(S11, "carnet-depenses", 60, 700, 520, 68.8, rot=-2)
tag(S11, 70, 1130, "Note chaque dépense", 70.9, "acc", 40)
counter(S11, 70, 1210, 0, 7, 72.6, 0.9, " jours", 120)
hit(73.0, 0.8)

# --- S12 · petit salaire ne veut pas dire petite sagesse
cam(73.2, S12)
headline(S12, 280, ["Petit salaire,", "[pas] petite sagesse"], 73.3, kicker="Rappelle-toi", hl_t=75.3, size=88)
sticker(S12, "petit-salaire-pousse", 60, 680, 480, 73.6, rot=-2)
sticker(S12, "baton-serein", 620, 660, 260, 74.5, rot=3)
tag(S12, 70, 1080, "Une grande sagesse", 75.5, "acc", 44)
hit(75.4, 0.8)

# --- S13 · question aux spectateurs
cam(75.9, S13)
headline(S13, 300, ["Quelle [habitude]", "en premier ?"], 76.0, kicker="À ton tour", hl_t=76.2, size=100)
sticker(S13, "baton-budget", 700, 880, 210, 77.0, rot=3)
cta = put(S13, 70, 760, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 78.9, 14)
sfx("click", 78.9, 0.8)
tag(S13, 70, 900, "Abonne-toi", 79.3, "acc", 48)

# --- fin en boucle : retour sur l'image d'ouverture
cam(79.9, S1)
bigword("Ta paix", 83.3, 0.8, y=1290, size=100)
bigword("La sagesse", 84.5, 1.0, y=1290, size=110)
hit(84.6, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 12.6), ("02", "Verset", 12.6, 28.2), ("03", "Habitudes", 28.2, 59.4), ("04", "Action", 59.4, DUR)],
    suppress=[(16.75, 21.5)],
)

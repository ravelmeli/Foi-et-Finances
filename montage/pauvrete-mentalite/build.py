"""Short « La différence entre pauvreté et mentalité de pauvreté selon la Bible » (2 Corinthiens 8.2) — style 02, 9:16, ~92 s.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Pauvrete et mentalite de pauvrete", "lang": "fr"}
s.setup(here=HERE, duration=92.5, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8, S9 = (0, 2), (1, 2), (2, 2)
S10, S11 = (2, 3), (1, 3)

# --- S1 · 0 – 4.7 · accroche : deux choses différentes
cam(0, S1)
sticker(S1, "poches-vides", 60, 640, 300, 0.0, rot=-3, instant=True)
sticker(S1, "perso-honte-portrait", 540, 660, 330, T("mentalité") - 0.1, rot=3)
headline(S1, 300, ["Pauvreté", "et [mentalité]"], 0.0, kicker="Pas la même chose", hl_t=T("mentalité"), size=104)
hit(T("chose"), 0.8)

# --- S2 · 4.7 – 15.8 · la pauvreté est une situation, ni péché ni malédiction
cam(4.7, S2)
headline(S2, 280, ["Une [situation],", "pas un verdict"], T("pauvreté", 2) - 0.3, kicker="La pauvreté", hl_t=T("situation"), size=100)
sticker(S2, "perso-poches-pied", 60, 620, 280, T("manque") - 0.2, rot=-2)
tag(S2, 400, 700, "Ni péché", T("péché") - 0.4, "", 40)
tag(S2, 400, 790, "Ni malédiction", T("malédiction") - 0.5, "", 40)
tag(S2, 70, 1250, "Dieu protège les pauvres", T("protège") - 0.3, "acc", 38)
hit(T("protège"), 0.8)

# --- S3 · 15.8 – 31.0 · la mentalité de pauvreté est une façon de penser
cam(15.8, S3)
headline(S3, 280, ["Une façon", "de [penser]"], T("mentalité", 1) - 0.3, kicker="La mentalité de pauvreté", hl_t=T("penser"), size=104)
sticker(S3, "coffre-cadenas", 60, 640, 380, T("jamais") - 0.3, rot=-3)
sticker(S3, "perso-honte-portrait", 600, 640, 300, T("honte") - 0.2, rot=3)
tag(S3, 70, 1000, "Peur", T("peur") - 0.1, "", 40)
tag(S3, 70, 1085, "Honte", T("honte") - 0.1, "", 40)
tag(S3, 70, 1170, "Jalousie", T("jalousie") - 0.1, "", 40)
tag(S3, 70, 1290, "Avec peu ou beaucoup d'argent", T("peu") - 0.2, "acc", 38)
hit(T("jamais"), 0.8)

# --- S4 · 31.0 – 35.1 · pas un reproche
cam(30.9, S4)
headline(S4, 280, ["Pas un [reproche]"], T("attention") - 0.7, kicker="Attention", hl_t=T("reproche"), size=104)
sticker(S4, "perso-serein-portrait", 290, 640, 500, T("reproche") - 0.1, rot=-2)
tag(S4, 70, 1260, "Ceux qui manquent : du respect", T("manquent") - 0.4, "acc", 36)
hit(T("reproche"), 0.8)

# --- S5 · 35.1 – 47.0 · les Églises de Macédoine ; verset (2 Co 8.2), sous-titres coupés
cam(35.1, S5)
headline(S5, 280, ["Les Églises", "de [Macédoine]"], T("regarde") - 0.2, kicker="Paul aux Corinthiens", hl_t=T("macédoine"), size=100)
tag(S5, 70, 600, "2 Corinthiens 8.2", T("corinthiens", 1) - 0.2, "acc", 52)
verse = ('« L\'abondance de leur joie et leur <em class="hl h1"><span>pauvreté</span><i></i></em> profonde ont produit avec abondance '
         'de riches <em class="hl h2"><span>libéralités</span><i></i></em>. »')
v = put(S5, 70, 710, f'<div class="h" style="font-size:52px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("labondance") - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("pauvreté", 3))
tween(f"#{v} .h2 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("libéralité"))
sticker(S5, "page-bible-enluminee", 70, 1050, 220, T("verset", 0) + 0.3, rot=-3)
sticker(S5, "piece-humble", 400, 1100, 200, T("libéralité") - 0.2, rot=4)
ref(S5, 640, 1130, "LSG 1910", T("verset") + 0.4)
hit(T("libéralité"), 1.0)

# --- S6 · 47.0 – 53.0 · vraie pauvreté, mais confiance et générosité
cam(47.0, S6)
headline(S6, 280, ["Pauvres,", "mais [généreux]"], T("ils") - 0.3, kicker="Les Macédoniens", hl_t=T("générosité"), size=104)
sticker(S6, "perso-don-pied", 60, 620, 280, T("pourtant") - 0.2, rot=-2)
sticker(S6, "piece-humble", 440, 700, 220, T("générosité") - 0.4, rot=4)
sticker(S6, "plante-pot", 700, 640, 200, T("confiance") - 0.1, rot=3)
tag(S6, 70, 1230, "Confiance et générosité", T("confiance") - 0.1, "acc", 40)
hit(T("générosité"), 0.8)

# --- S7 · 53.0 – 56.9 · comment reconnaître cette mentalité ?
cam(53.0, S7)
headline(S7, 280, ["Comment", "[reconnaître] ?"], T("alors") - 0.2, kicker="Cette mentalité", hl_t=T("reconnaître"), size=104)
sticker(S7, "perso-livre-pied", 400, 640, 280, T("comment") + 0.2, rot=2)
tag(S7, 70, 1000, "3 signes", T("trois") - 0.1, "acc", 52)
hit(T("trois"), 0.7)

# --- S8 · 56.9 – 69.3 · les trois signes
cam(56.8, S8)
headline(S8, 280, ["Trois [signes]"], T("voici") - 0.2, kicker="Cette mentalité", hl_t=T("signes"), size=110)
sticker(S8, "poches-vides", 50, 640, 240, T("1") - 0.1, rot=-3)
label_box(S8, 50, 960, "1 · Jamais", "ta situation figée", T("1") + 0.2)
sticker(S8, "coffre-cadenas", 380, 650, 250, T("2", 1) - 0.1, rot=3)
label_box(S8, 380, 960, "2 · Peur", "dépenser ou tout garder", T("2", 1) + 0.2)
sticker(S8, "perso-honte-portrait", 710, 640, 220, T("3") - 0.1, rot=-3)
label_box(S8, 710, 960, "3 · Honte", "éviter d'apprendre", T("3") + 0.2)

# --- S9 · 69.3 – 74.2 · ne te condamne pas : ta situation n'est pas ta valeur
cam(69.3, S9)
headline(S9, 280, ["Ta situation", "n'est pas ta [valeur]"], T("si") - 0.3, kicker="Ne te condamne pas", hl_t=T("valeur"), size=84)
sticker(S9, "perso-serein-portrait", 330, 700, 420, T("condamne") - 0.2, rot=-2)
hit(T("valeur"), 0.9)

# --- S10 · 74.2 – 81.5 · un petit pas
cam(74.2, S10)
headline(S10, 280, ["Un petit [pas]"], T("commence") - 0.2, kicker="Ce que tu peux faire", hl_t=75.1, size=110)
sticker(S10, "escalier-trois-marches", 60, 640, 420, T("commence") + 0.2, rot=-2)
tag(S10, 500, 700, "Apprendre", T("apprendre", 1) - 0.1, "", 40)
tag(S10, 500, 790, "Planifier", T("planifier") - 0.1, "", 40)
tag(S10, 500, 880, "Donner un peu", T("donner") - 0.1, "", 40)
sticker(S10, "plante-pot", 700, 1000, 200, T("confiance", 1) - 0.2, rot=3)
tag(S10, 70, 1120, "Un jour à la fois", T("jour") - 0.3, "acc", 44)
hit(T("jour"), 0.8)

# --- S11 · 81.5 – 88.7 · mode sombre : la question aux spectateurs
cam(81.6, S11)
dark_mode(81.55)
headline(S11, 430, ["Quel [changement]", "de pensée", "en premier ?"], T("quel") - 0.2, kicker="À ton tour", hl_t=T("changement"), size=96, dark=True)
sticker(S11, "plante-pot", 680, 1040, 220, T("premier") - 0.3, rot=3)
cta = put(S11, 70, 900, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(88.7, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Constat", 0, 15.8), ("02", "Mentalité", 15.8, 35.1), ("03", "Exemple", 35.1, 53.0), ("04", "Gestes", 53.0, DUR)],
    suppress=[(40.8, 47.0), (89.2, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("piece-humble", 40, 1200, 260, -6), ("plante-pot", 800, 1050, 200, 5)]},
    endcard_t=89.3,
)

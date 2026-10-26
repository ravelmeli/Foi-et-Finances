"""Short « Pourquoi prier pour l'argent ne suffit pas » (Proverbes 21.5) — style 02, 9:16, ~67 s.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Prier pour l'argent ne suffit pas", "lang": "fr"}
s.setup(here=HERE, duration=67.5, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8, S9 = (0, 2), (1, 2), (2, 2)
S10 = (2, 3)

# --- S1 · 0 – 5.0 · accroche : rien ne change ? (personnage frustré dès la 1re image)
cam(0, S1)
sticker(S1, "perso-frustre-pied", 60, 600, 300, 0.0, rot=-2, instant=True)
headline(S1, 300, ["Rien ne [change] ?"], 0.0, kicker="Tu as prié pour ton argent", hl_t=T("change"), size=110)
tag(S1, 400, 1100, "Prier est essentiel", T("essentiel") - 0.5, "acc", 40)
hit(T("rien"), 0.8)

# --- S2 · 5.0 – 11.0 · notre pain quotidien ; la prière ne remplace pas la sagesse
cam(5.0, S2)
headline(S2, 280, ["Notre pain", "[quotidien]"], T("jésus") - 0.2, kicker="Jésus nous l'a appris", hl_t=T("quotidien"), size=110)
sticker(S2, "pain", 60, 640, 420, T("pain") - 0.1, rot=-4)
sticker(S2, "perso-paisible-portrait", 540, 600, 330, T("prière") - 0.1, rot=3)
tag(S2, 70, 1100, "La prière ne remplace pas la sagesse", T("remplace") - 0.3, "acc", 34)
hit(T("sagesse"), 0.9)

# --- S3 · 11.0 – 15.3 · Dieu répond aussi par des actions concrètes
cam(11.0, S3)
headline(S3, 280, ["Dieu répond", "par des [actions]"], T("dieu") - 0.2, kicker="Souvent", hl_t=T("actions"), size=100)
sticker(S3, "calendrier-coche", 60, 640, 420, T("actions") - 0.2, rot=-3)
sticker(S3, "carnet-budget", 560, 640, 300, T("concrètes") - 0.2, rot=3)
hit(T("concrètes"), 0.7)

# --- S4 · 15.3 – 23.6 · le verset (Pr 21.5) ; sous-titres coupés pendant la citation
cam(15.3, S4)
headline(S4, 280, ["Le [plan]", "de l'homme diligent"], T("proverbe") - 0.3, kicker="La Parole", hl_t=T("projets"), size=82)
tag(S4, 70, 600, "Proverbes 21.5", T("proverbe") + 0.1, "acc", 52)
verse = ('« Les <em class="hl h1"><span>projets</span><i></i></em> de l\'homme <em class="hl h2"><span>diligent</span><i></i></em> '
         'ne mènent qu\'à l\'abondance, mais celui qui agit avec précipitation n\'arrive qu\'à la disette. »')
v = put(S4, 70, 710, f'<div class="h" style="font-size:52px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("les") - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("projets"))
tween(f"#{v} .h2 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("diligent"))
sticker(S4, "bible-ouverte", 60, 1060, 420, T("proverbe") + 0.4, rot=-3)
ref(S4, 500, 1060, "PROVERBES 21.5 · LSG 1910", T("verset") + 0.4)
sticker(S4, "plante-pot", 640, 1130, 170, T("labondance") - 0.1, rot=3)
hit(T("disette"), 1.0)

# --- S5 · 23.6 – 29.9 · prier sans budget
cam(23.6, S5)
headline(S5, 280, ["Prier", "sans [budget] ?"], T("projet") - 0.2, kicker="Un projet, c'est un plan", hl_t=T("budget"), size=104)
sticker(S5, "carnet-budget", 60, 650, 330, T("plan") - 0.1, rot=-3)
sticker(S5, "perso-notes-pied", 600, 600, 260, T("budget") - 0.2, rot=3)
tag(S5, 70, 1130, "Changer ses habitudes", T("habitudes") - 0.4, "", 38)
hit(T("budget"), 0.9)

# --- S6 · 29.9 – 34.7 · la baignoire au robinet ouvert
cam(29.9, S6)
headline(S6, 280, ["Vider la baignoire", "robinet [ouvert]"], T("sortir") - 0.3, kicker="Les dettes", hl_t=T("ouvert") - 0.2, size=88)
sticker(S6, "baignoire-robinet", 190, 650, 700, T("baignoire") - 0.3, rot=-2)
tag(S6, 70, 1250, "Sortir des dettes", T("dettes") - 0.1, "acc", 40)
hit(T("ouvert"), 0.9)

# --- S7 · 34.7 – 41.2 · la prière change le cœur, puis on agit
cam(34.7, S7)
headline(S7, 280, ["La prière change", "ton [cœur]"], T("prière", 1) - 0.2, kicker="Prie, puis agis", hl_t=T("cœur"), size=96)
sticker(S7, "perso-paisible-portrait", 250, 660, 480, T("cœur") - 0.1, rot=-2)
tag(S7, 70, 1250, "Prie, puis agis", T("alors") - 0.1, "acc", 56)
hit(T("agis"), 0.9)

# --- S8 · 41.2 – 50.0 · trois gestes simples
cam(41.2, S8)
headline(S8, 280, ["Trois gestes", "pour [cette semaine]"], T("voici") - 0.2, kicker="À faire", hl_t=T("semaine"), size=80)
sticker(S8, "carnet-budget", 60, 640, 200, T("note") - 0.1, rot=-3)
label_box(S8, 60, 920, "1 · Note", "tes dépenses", T("note") + 0.1)
sticker(S8, "tirelire", 350, 650, 250, T("mets") - 0.1, rot=3)
label_box(S8, 350, 920, "2 · Épargne", "un petit montant", T("mets") + 0.1)
sticker(S8, "perso-conseil-pied", 700, 610, 230, T("conseil") - 0.2, rot=-2)
label_box(S8, 700, 1130, "3 · Conseil", "d'une personne sage", T("conseil") + 0.1)
hit(T("sage"), 0.7)

# --- S9 · 50.0 – 57.4 · pas un manque de foi : Dieu t'accompagne
cam(50.0, S9)
headline(S9, 280, ["Pas un", "manque de [foi]"], T("pries") - 0.7, kicker="Si c'est difficile", hl_t=T("foi"), size=110)
sticker(S9, "perso-serein-pied", 60, 620, 250, T("juge") - 0.3, rot=-2)
tag(S9, 360, 1000, "Dieu t'accompagne", T("taccompagne") - 0.1, "acc", 44)
tag(S9, 360, 1090, "pas à pas", T("taccompagne") + 0.9, "", 44)
hit(T("foi"), 0.9)

# --- S10 · 57.4 – 63.7 · mode sombre : la question aux spectateurs
cam(57.4, S10)
dark_mode(57.35)
headline(S10, 430, ["Quelle [action]", "vas-tu ajouter", "à ta prière ?"], T("quelle") - 0.2, kicker="À ton tour", hl_t=T("action"), size=96, dark=True)
sticker(S10, "plante-pot", 660, 1000, 220, T("ajouter") - 0.1, rot=3)
cta = put(S10, 70, 900, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(63.7, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Constat", 0, 15.3), ("02", "Verset", 15.3, 23.6), ("03", "Habitudes", 23.6, 41.2), ("04", "Gestes", 41.2, DUR)],
    suppress=[(17.2, 23.6), (64.1, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("bible-ouverte", 40, 1190, 400, -5), ("plante-pot", 780, 1050, 200, 5)]},
    endcard_t=64.3,
)

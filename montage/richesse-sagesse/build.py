"""Short « La richesse sans sagesse peut devenir une malédiction » (Proverbes 11.28) — style 02, 9:16, ~91 s.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Richesse sans sagesse", "lang": "fr"}
s.setup(here=HERE, duration=91.5, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8, S9 = (0, 2), (1, 2), (2, 2)
S10, S11, S12 = (2, 3), (1, 3), (0, 3)
S13, S14, S15 = (0, 4), (1, 4), (2, 4)

# --- S1 · 0 – 4.6 · accroche : sommes-nous prêts à recevoir la richesse ?
cam(0, S1)
sticker(S1, "perso-reve-pied", 60, 620, 300, 0.0, rot=-2, instant=True)
sticker(S1, "sac-argent", 500, 700, 330, T("richesse") - 0.2, rot=3)
headline(S1, 300, ["Riche, mais", "[prêt] ?"], 0.0, kicker="Beaucoup rêvent de richesse", hl_t=T("prêts"), size=104)
hit(T("prêts"), 0.8)

# --- S2 · 4.6 – 13.9 · la Bible ne condamne pas la richesse, mais avertit
cam(4.6, S2)
headline(S2, 280, ["La richesse :", "pas [condamnée]"], T("bible") - 0.6, kicker="La Bible", hl_t=T("condamne"), size=100)
sticker(S2, "perso-serein-pied", 60, 620, 260, T("condamne") - 0.2, rot=-2)
sticker(S2, "tour-pieces-bascule", 480, 640, 300, T("piège") - 0.2, rot=3)
tag(S2, 70, 1250, "Sans sagesse : un piège", T("sans") - 0.1, "acc", 38)
hit(T("piège"), 0.9)

# --- S3 · 13.9 – 19.1 · pas une punition de Dieu, mais des conséquences
cam(13.9, S3)
headline(S3, 280, ["Pas une [punition]"], T("ce") - 0.3, kicker="Les conséquences", hl_t=T("punit"), size=96)
sticker(S3, "perso-sac-pied", 60, 620, 240, T("conséquences") - 0.2, rot=-2)
tag(S3, 360, 1000, "Un cœur sans sagesse", T("cœur") - 0.2, "acc", 40)
hit(T("conséquences"), 0.7)

# --- S4 · 19.1 – 27.6 · le verset (Pr 11.28) ; sous-titres coupés pendant la citation
cam(19.0, S4)
headline(S4, 280, ["Tombera ou", "[verdira]"], T("proverbe") - 0.3, kicker="La Parole", hl_t=T("verdiront"), size=110)
tag(S4, 70, 600, "Proverbes 11.28", T("proverbe") + 0.1, "acc", 52)
verse = ('« Celui qui se <em class="hl h1"><span>confie</span><i></i></em> dans ses richesses '
         '<em class="hl h2"><span>tombera</span><i></i></em>, mais les justes '
         '<em class="hl h3"><span>verdiront</span><i></i></em> comme le feuillage. »')
v = put(S4, 70, 710, f'<div class="h" style="font-size:52px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("celui", 1) - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("confie"))
tween(f"#{v} .h2 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("tombera"))
tween(f"#{v} .h3 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("verdiront"))
sticker(S4, "tour-pieces-bascule", 60, 1020, 260, T("tombera") - 0.1, rot=-3)
sticker(S4, "arbre-vert", 440, 1040, 300, T("verdiront") - 0.1, rot=3)
sticker(S4, "page-bible-enluminee", 770, 1030, 150, T("proverbe") + 0.4, rot=-3)
ref(S4, 70, 1420, "PROVERBES 11.28 · LSG 1910", T("verset") + 0.4)
hit(T("tombera"), 1.0)

# --- S5 · 27.6 – 32.4 · le problème : s'y confier
cam(27.6, S5)
headline(S5, 280, ["Pas d'avoir,", "mais [s'y confier]"], T("remarque") - 0.2, kicker="Remarque bien", hl_t=T("confier"), size=96)
sticker(S5, "sac-argent", 60, 640, 360, T("largent") - 0.2, rot=-3)
sticker(S5, "perso-sac-pied", 600, 620, 260, T("confier") - 0.3, rot=3)
hit(T("confier"), 0.8)

# --- S6 · 32.4 – 35.6 · trois dangers
cam(32.4, S6)
headline(S6, 280, ["Trois [dangers]"], T("sans", 2) - 0.2, kicker="Sans sagesse", hl_t=T("dangers"), size=110)
boxes(S6, 50, 640, ["1", "2", "3"], T("trois") - 0.2, step=300, small="Danger", cls="day wide")
hit(T("dangers"), 0.8)

# --- S7 · 35.6 – 40.0 · danger n°1 : l'orgueil
cam(35.6, S7)
headline(S7, 280, ["Danger n°1 :", "l'[orgueil]"], T("premier") - 0.2, kicker="On croit que tout nous est dû", hl_t=T("lorgueil"), size=104)
sticker(S7, "couronne-doree", 60, 650, 400, T("lorgueil") - 0.2, rot=-4)
sticker(S7, "perso-satisfait-portrait", 540, 640, 360, T("croit") - 0.1, rot=3)
hit(T("lorgueil"), 0.8)

# --- S8 · 40.0 – 45.0 · danger n°2 : l'insécurité
cam(40.0, S8)
headline(S8, 280, ["Danger n°2 :", "l'[insécurité]"], T("deuxième") - 0.2, kicker="La peur de perdre", hl_t=T("linsécurité"), size=100)
sticker(S8, "perso-sac-pied", 60, 600, 280, T("linsécurité") - 0.2, rot=-2)
tag(S8, 70, 1330, "Plus on a, plus on craint de perdre", T("plus") - 0.2, "acc", 34)
hit(T("peur"), 0.8)

# --- S9 · 45.0 – 49.3 · danger n°3 : l'égoïsme
cam(45.0, S9)
headline(S9, 280, ["Danger n°3 :", "l'[égoïsme]"], T("troisième") - 0.2, kicker="On oublie ceux qui manquent", hl_t=T("légoïsme"), size=104)
sticker(S9, "perso-fier-pied", 60, 620, 260, T("oublie") - 0.2, rot=-2)
sticker(S9, "mur-briques", 440, 700, 400, T("oublie") - 0.1, rot=3)
hit(T("légoïsme"), 0.8)

# --- S10 · 49.3 – 53.5 · Salomon choisit la sagesse
cam(49.3, S10)
headline(S10, 280, ["Salomon choisit", "la [sagesse]"], T("quand") - 0.2, kicker="1 Rois 3", hl_t=T("sagesse", 3), size=100)
sticker(S10, "boussole", 60, 640, 360, T("choisi") - 0.1, rot=-3)
tag(S10, 70, 1200, "Il a demandé la sagesse", T("demander") - 0.2, "acc", 40)
hit(T("choisi"), 0.8)

# --- S11 · 53.5 – 60.0 · savoir gagner ne suffit pas : gérer, donner, rester humble
cam(53.5, S11)
headline(S11, 280, ["Savoir [gagner]", "ne suffit pas"], T("sagesse", 4) - 0.5, kicker="La sagesse", hl_t=T("gagner"), size=100)
tag(S11, 70, 640, "Savoir gérer", T("gérer") - 0.1, "", 44)
tag(S11, 70, 730, "Donner", T("donner") - 0.1, "", 44)
tag(S11, 70, 820, "Rester humble", T("humble") - 0.3, "acc", 44)
sticker(S11, "perso-serein-pied", 640, 620, 260, T("humble") - 0.2, rot=3)
hit(T("humble"), 0.8)

# --- S12 · 60.0 – 68.2 · qui dirige mon argent ?
cam(60.0, S12)
headline(S12, 280, ["Qui dirige", "[mon argent] ?"], T("alors") - 0.2, kicker="Demande-toi", hl_t=T("dirige"), size=104)
b1 = put(S12, 30, 700, "Moi", "box out", "width:280px;font-size:44px")
b2 = put(S12, 350, 700, "La peur", "box out", "width:280px;font-size:44px")
b3 = put(S12, 670, 700, "La sagesse", "box out", "width:280px;font-size:44px")
blur_in(b1, T("moi") - 0.2, 12)
blur_in(b2, T("peur", 1) - 0.2, 12)
blur_in(b3, T("sagesse", 5) - 0.2, 12)
sfx("click", T("moi") - 0.2, 0.6)
sticker(S12, "boussole", 330, 900, 300, T("sagesse", 5), rot=-2)
hit(T("sagesse", 5), 0.9)

# --- S13 · 68.2 – 74.7 · une règle simple : trois éléments
cam(68.2, S13)
headline(S13, 280, ["Une règle", "[simple]"], T("cette") - 0.2, kicker="Cette semaine", hl_t=T("simple"), size=110)
boxes(S13, 50, 640, ["1", "2", "3"], T("budget") - 0.3, step=300, small="Règle", cls="day wide")
label_box(S13, 60, 820, "Un budget", None, T("budget") + 0.1)
label_box(S13, 360, 820, "Un montant<br>à donner", None, T("montant") + 0.1)
label_box(S13, 660, 820, "Un conseiller<br>sage", None, T("conseiller") + 0.1)
hit(T("conseiller"), 0.8)

# --- S14 · 74.7 – 79.9 · la richesse sert la sagesse
cam(74.6, S14)
headline(S14, 280, ["La richesse", "sert la [sagesse]"], T("richesse", 4) - 0.3, kicker="Une bénédiction", hl_t=T("sagesse", 6), size=96)
sticker(S14, "arbre-vert", 60, 640, 400, T("bénédiction") - 0.1, rot=-3)
sticker(S14, "boussole", 560, 700, 260, T("sert") - 0.2, rot=3)
hit(T("remplace"), 0.9)

# --- S15 · 79.9 – 87.7 · mode sombre : la question aux spectateurs
cam(79.9, S15)
dark_mode(79.85)
headline(S15, 430, ["Quelle [règle]", "vas-tu te fixer ?"], T("quelle") - 0.2, kicker="À ton tour", hl_t=T("règle", 1), size=92, dark=True)
sticker(S15, "boussole", 680, 950, 240, T("sagesse", 7) - 0.3, rot=3)
cta = put(S15, 70, 780, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(87.7, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Avertissement", 0, 19.0), ("02", "Verset", 19.0, 32.4), ("03", "Dangers", 32.4, 60.0), ("04", "Sagesse", 60.0, DUR)],
    suppress=[(21.0, 27.5), (88.2, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("arbre-vert", 40, 1180, 360, -4), ("boussole", 780, 1050, 220, 5)]},
    endcard_t=88.3,
)

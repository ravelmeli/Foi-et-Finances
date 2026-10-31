"""Short « Comment savoir si un achat est un besoin ou une envie selon la Bible » (1 Timothée 6.8) — style 02, 9:16, ~72 s.
Première vidéo de la nouvelle identité : bonhommes bâtons, Bible à la croix, croix flottantes (moteur), euros.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Besoin ou envie", "lang": "fr"}
s.setup(here=HERE, duration=72.0, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8, S9 = (0, 2), (1, 2), (2, 2)
S10, S11 = (2, 3), (1, 3)

# --- S1 · 0 – 7.0 · accroche : « j'en ai besoin » ?
cam(0, S1)
sticker(S1, "baton-vitrine", 50, 600, 360, 0.0, rot=-2, instant=True)
sticker(S1, "sac-shopping", 560, 640, 300, T("dacheter") - 0.1, rot=4)
sticker(S1, "boite-smartphone", 520, 1000, 330, T("besoin") - 0.2, rot=-3)
headline(S1, 300, ["Besoin ou", "[envie] ?"], 0.0, kicker="Avant d'acheter", hl_t=T("envie", 1), size=110)
tag(S1, 70, 1300, "« J'en ai besoin »", T("jen") - 0.1, "", 40)
hit(T("envie", 1), 0.9)

# --- S2 · 7.0 – 9.4 · la Bible nous aide à faire la différence
cam(7.0, S2)
headline(S2, 280, ["La Bible aide", "à faire la [différence]"], T("bible") - 0.3, kicker="La Parole", hl_t=T("différence"), size=88)
sticker(S2, "baton-lit-livre", 70, 620, 330, T("bible") - 0.1, rot=-2)
sticker(S2, "pupitre-parole", 520, 640, 380, T("aide") - 0.1, rot=3)
hit(T("différence"), 0.8)

# --- S3 · 9.4 – 17.3 · le verset (1 Tm 6.8) ; sous-titres coupés pendant la citation
cam(9.4, S3)
headline(S3, 280, ["Cela nous", "[suffira]"], T("paul") - 0.3, kicker="Paul à Timothée", hl_t=T("suffira"), size=110)
tag(S3, 70, 600, "1 Timothée 6.8", T("1") - 0.1, "acc", 52)
verse = ('« Si donc nous avons la <em class="hl h1"><span>nourriture</span><i></i></em> et le '
         '<em class="hl h2"><span>vêtement</span><i></i></em>, cela nous suffira. »')
v = put(S3, 70, 710, f'<div class="h" style="font-size:58px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("si") - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("nourriture"))
tween(f"#{v} .h2 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("vêtement"))
sticker(S3, "livre-croix-ouvert", 60, 1020, 380, T("1") + 0.3, rot=-3)
sticker(S3, "panier-besoins", 480, 1010, 260, T("nourriture") - 0.1, rot=3)
sticker(S3, "vetements-plies", 760, 1060, 220, T("vêtement") - 0.1, rot=-3)
ref(S3, 70, 1420, "1 TIMOTHÉE 6.8 · LSG 1910", T("verset") + 0.4)
hit(T("suffira"), 1.0)

# --- S4 · 17.3 – 24.8 · un besoin : vivre et prendre soin des siens
cam(17.3, S4)
headline(S4, 280, ["Un [besoin]"], T("besoin", 2) - 0.2, kicker="Ce qui te fait vivre", hl_t=T("besoin", 2), size=120)
sticker(S4, "panier-besoins", 50, 600, 300, T("nourrir") - 0.2, rot=-3)
sticker(S4, "maison-simple", 380, 610, 300, T("loger") - 0.2, rot=3)
sticker(S4, "vetements-plies", 710, 620, 270, T("vêtir") - 0.2, rot=-2)
tag(S4, 70, 960, "Se nourrir", T("nourrir") - 0.1, "", 38)
tag(S4, 70, 1045, "Se loger · se vêtir", T("loger") - 0.1, "", 38)
tag(S4, 70, 1130, "Se soigner · travailler", T("soigner") - 0.1, "", 38)
tag(S4, 70, 1250, "Prendre soin des tiens", T("tiens") - 0.3, "acc", 40)
hit(T("travailler"), 0.8)

# --- S5 · 24.8 – 29.1 · une envie : agréable, mais on peut s'en passer
cam(24.8, S5)
headline(S5, 280, ["Une [envie]"], T("envie", 2) - 0.3, kicker="Ce qui rend la vie agréable", hl_t=T("envie", 2), size=120)
sticker(S5, "montre-luxe", 60, 620, 240, T("agréable") - 0.4, rot=-4)
sticker(S5, "boite-smartphone", 340, 650, 320, T("agréable") - 0.1, rot=3)
sticker(S5, "sac-shopping", 720, 620, 230, T("mais") - 0.2, rot=-3)
tag(S5, 70, 1100, "Tu peux t'en passer", T("passer") - 0.4, "acc", 42)
hit(T("passer"), 0.8)

# --- S6 · 29.1 – 35.3 · pas un péché ; le problème : quand elle passe avant les besoins
cam(29.1, S6)
headline(S6, 280, ["Pas un [péché]"], T("attention") - 0.5, kicker="Attention", hl_t=T("péché"), size=110)
sticker(S6, "baton-deux-mains", 60, 600, 380, T("attention") - 0.2, rot=-2)
sticker(S6, "panier-besoins", 520, 640, 220, T("problème") - 0.1, rot=3)
sticker(S6, "sac-shopping", 770, 660, 190, T("passe") - 0.1, rot=-3)
tag(S6, 470, 950, "Le problème :", T("problème") - 0.1, "", 36)
tag(S6, 470, 1035, "l'envie avant le besoin", T("avant") - 0.3, "acc", 36)
hit(T("besoins"), 0.8)

# --- S7 · 35.3 – 38.0 · trois questions avant d'acheter
cam(35.3, S7)
headline(S7, 280, ["Trois [questions]"], T("voici") - 0.2, kicker="Avant d'acheter", hl_t=T("questions"), size=110)
boxes(S7, 50, 640, ["1", "2", "3"], T("trois") - 0.1, step=300, small="Question", cls="day wide")
sticker(S7, "baton-pense", 380, 860, 300, T("simples") - 0.2, rot=2)
hit(T("questions"), 0.8)

# --- S8 · 38.0 – 48.4 · les trois questions
cam(38.0, S8)
headline(S8, 280, ["Le [test]", "en trois questions"], T("1", 1) - 0.3, kicker="Avant d'acheter", hl_t=T("1", 1), size=96)
q1 = put(S8, 60, 620, "<small>1</small>Puis-je vivre sans,<br>ce mois-ci ?", "box q", "width:600px;font-size:40px")
q2 = put(S8, 60, 860, "<small>2</small>Pour moi, ou pour<br>l'image que je donne ?", "box q", "width:600px;font-size:40px")
q3 = put(S8, 60, 1100, "<small>3</small>Dans une semaine,<br>en aurai-je encore envie ?", "box q", "width:600px;font-size:40px")
blur_in(q1, T("1", 1) - 0.1, 12)
blur_in(q2, T("2") - 0.1, 12)
blur_in(q3, T("3") - 0.1, 12)
sfx("click", T("2") - 0.1, 0.6)
sfx("click", T("3") - 0.1, 0.6)
sticker(S8, "boite-smartphone", 700, 640, 260, T("vivre", 1) - 0.2, rot=4)
sticker(S8, "sac-shopping", 720, 880, 220, T("limage") - 0.3, rot=-3)
sticker(S8, "baton-sablier", 720, 1090, 180, T("jattends") - 0.3, rot=2)
hit(T("envie", 4), 0.8)

# --- S9 · 48.4 – 57.9 · d'abord les besoins, puis les envies, sans culpabilité
cam(48.4, S9)
headline(S9, 280, ["D'abord tes", "[besoins]"], T("si", 2) - 0.2, kicker="Dans le bon ordre", hl_t=T("besoins", 1), size=110)
b1 = put(S9, 60, 640, "<small>D'abord</small>Besoins", "box out", "width:420px;font-size:52px")
b2 = put(S9, 560, 640, "<small>Ensuite</small>Envies", "box out", "width:420px;font-size:52px")
blur_in(b1, T("couvre") - 0.2, 12)
blur_in(b2, T("puis") - 0.2, 12)
sfx("click", T("couvre") - 0.2, 0.6)
sticker(S9, "baton-panier", 80, 850, 300, T("couvre") + 0.2, rot=-2)
sticker(S9, "montre-luxe", 640, 900, 220, T("envies") - 0.2, rot=4)
tag(S9, 70, 1300, "Sans culpabilité", T("culpabilité") - 0.4, "acc", 44)
hit(T("culpabilité"), 0.8)

# --- S10 · 57.9 – 62.7 · le contentement : la paix de savoir que tu as assez
cam(57.9, S10)
headline(S10, 280, ["Le [contentement]"], T("contentement") - 0.4, kicker="Pas la privation", hl_t=T("contentement"), size=96)
sticker(S10, "baton-priere", 90, 600, 320, T("contentement") - 0.2, rot=-2)
sticker(S10, "livre-croix-ferme", 560, 700, 340, T("privation") - 0.2, rot=4)
tag(S10, 70, 1250, "La paix de savoir que tu as assez", T("paix") - 0.3, "acc", 36)
hit(T("assez"), 0.9)

# --- S11 · 62.7 – 68.7 · mode sombre : la question aux spectateurs
cam(62.7, S11)
dark_mode(62.65)
headline(S11, 430, ["Quel [achat]", "vas-tu tester", "cette semaine ?"], T("quel") - 0.2, kicker="À ton tour", hl_t=T("achat"), size=96, dark=True)
sticker(S11, "baton-serein", 680, 980, 260, T("test") - 0.2, rot=3)
cta = put(S11, 70, 900, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(68.7, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 9.4), ("02", "Verset", 9.4, 24.8), ("03", "Différence", 24.8, 35.3), ("04", "Test", 35.3, DUR)],
    suppress=[(12.8, 17.2), (69.2, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 40, 1180, 330, -6), ("baton-priere", 800, 1020, 200, 4)]},
    endcard_t=69.3,
)

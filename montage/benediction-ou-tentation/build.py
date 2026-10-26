"""Short « L'argent est-il une bénédiction ou une tentation ? » (1 Timothée 6.10) — style 02, 9:16, ~77 s.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Benediction ou tentation", "lang": "fr"}
s.setup(here=HERE, duration=77.0, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8, S9 = (0, 2), (1, 2), (2, 2)
S10 = (2, 3)

# --- S1 · 0 – 9.8 · la question : bénédiction ou tentation ? (personnage hésitant et carrefour dès la 1re image)
cam(0, S1)
sticker(S1, "perso-hesite-pied", 50, 590, 270, 0.0, rot=-2, instant=True)
sticker(S1, "panneau-carrefour", 520, 620, 380, T("ni") - 0.2, rot=3)
headline(S1, 300, ["Bénédiction ou", "[tentation] ?"], 0.0, kicker="Argent · Foi", hl_t=T("tentation"), size=100)
tag(S1, 380, 1130, "Ni l'un, ni l'autre en soi", T("ni") + 0.2, "acc", 34)
hit(T("ni"), 0.8)

# --- S2 · 9.8 – 18.7 · le verset (1 Tm 6.10) ; sous-titres coupés pendant la citation
cam(9.8, S2)
headline(S2, 280, ["Paul écrit", "à [Timothée]"], T("l'apôtre") - 0.2, kicker="La Parole", hl_t=T("timothée"), size=100)
tag(S2, 70, 600, "1 Timothée 6.10", T("1") - 0.1, "acc", 52)
verse = '« Car l\'<em class="hl h1"><span>amour</span><i></i></em> de l\'argent est la racine de tous les maux. »'
v = put(S2, 70, 710, f'<div class="h" style="font-size:60px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("car") - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("l'amour"))
sticker(S2, "page-bible-enluminee", 70, 985, 260, T("timothée") + 0.4, rot=-3)
sticker(S2, "statere-or", 420, 1040, 300, T("l'amour") + 0.2, rot=4)
ref(S2, 70, 1420, "1 TIMOTHÉE 6.10 · LSG 1910", T("verset") + 0.4)
hit(T("maux"), 1.0)

# --- S3 · 18.7 – 23.2 · pas l'argent, l'amour de l'argent
cam(18.7, S3)
headline(S3, 280, ["Pas l'argent :", "l'[amour] de l'argent"], T("remarque") - 0.2, kicker="Remarque bien", hl_t=T("l'amour", 1), size=80)
sticker(S3, "tas-pieces", 60, 640, 320, T("l'argent", 2) - 0.1, rot=-3)
label_box(S3, 60, 990, "L'argent", "pas condamné", T("l'argent", 2) + 0.2)
sticker(S3, "perso-pensif-portrait", 600, 640, 300, T("l'amour", 1) - 0.1, rot=3)
label_box(S3, 600, 1050, "L'amour<br>de l'argent", "c'est lui, le problème", T("l'amour", 1) + 0.3)
hit(T("l'amour", 1), 0.9)

# --- S4 · 23.2 – 30.3 · l'argent est un outil (le marteau)
cam(23.2, S4)
headline(S4, 280, ["Un marteau :", "ni bon, ni mauvais"], T("marteau") - 0.5, kicker="Une image", size=88)
sticker(S4, "marteau", 60, 640, 420, T("marteau") - 0.1, rot=-4)
sticker(S4, "maison-simple", 560, 650, 340, T("construire") - 0.1, rot=3)
tag(S4, 560, 1000, "ou blesser", T("blesser") - 0.2, "", 40)
tag(S4, 70, 1150, "L'argent est un outil", T("outil") - 0.3, "acc", 46)
hit(T("outil"), 1.0)

# --- S5 · 30.3 – 36.9 · quand il sert : une bénédiction
cam(30.3, S5)
headline(S5, 280, ["Une [bénédiction]"], T("quand") - 0.2, kicker="Quand il sert", hl_t=T("bénédiction", 1) - 0.8, size=96)
sticker(S5, "maison-simple", 60, 640, 260, T("tiens") - 0.2, rot=-3)
label_box(S5, 60, 920, "Prendre soin<br>des tiens", None, T("tiens") + 0.1)
sticker(S5, "bourse", 380, 640, 230, T("aider") - 0.1, rot=3)
label_box(S5, 380, 920, "Aider<br>les autres", None, T("aider") + 0.1)
sticker(S5, "statere-or", 700, 650, 220, T("honnête") - 0.1, rot=-4)
label_box(S5, 700, 920, "Rester<br>honnête", None, T("honnête") + 0.1)
hit(T("bénédiction", 1), 0.9)

# --- S6 · 36.9 – 42.5 · quand il règne : une tentation
cam(36.9, S6)
headline(S6, 280, ["Une [tentation]"], T("quand", 1) - 0.2, kicker="Quand il règne", hl_t=T("tentation", 1) - 1.2, size=96)
sticker(S6, "bourse", 60, 650, 230, T("sécurité") - 0.1, rot=-3)
label_box(S6, 60, 920, "Ta<br>sécurité", None, T("sécurité") + 0.1)
sticker(S6, "tas-pieces", 360, 650, 280, T("fierté") - 0.1, rot=3)
label_box(S6, 380, 920, "Ta<br>fierté", None, T("fierté") + 0.1)
sticker(S6, "piece-hamecon", 760, 640, 160, T("idole") - 0.1, rot=2)
label_box(S6, 700, 1030, "Ton<br>idole", None, T("idole") + 0.1)
hit(T("tentation", 1), 0.9)

# --- S7 · 42.5 – 52.0 · avoir peu ou beaucoup : ce n'est pas le sujet, c'est le cœur
cam(42.5, S7)
headline(S7, 280, ["Avoir peu,", "avoir beaucoup"], T("attention") - 0.2, kicker="Attention", size=96)
tag(S7, 70, 640, "Peu : pas une malédiction", T("malédiction") - 0.5, "", 38)
tag(S7, 70, 730, "Beaucoup : pas un péché", T("péché") - 0.6, "", 38)
sticker(S7, "bourse", 60, 860, 230, T("peu") + 0.1, rot=-3)
sticker(S7, "tas-pieces", 400, 850, 300, T("beaucoup") + 0.1, rot=3)
tag(S7, 70, 1170, "Ce qui compte : ton cœur", T("compte") - 0.1, "acc", 40)
hit(T("cœur", 1), 0.9)

# --- S8 · 52.0 – 62.0 · le test de la paix (schéma de décision)
cam(52.0, S8)
headline(S8, 280, ["Le test de [la paix]"], T("voici") - 0.2, kicker="Un test simple", hl_t=T("paix"), size=92)
f1 = put(S8, 230, 640, "Si tu perdais<br>cet argent demain ?", "box q")
blur_in(f1, T("perdais") - 0.3, 14)
sx8, sy8 = st(*S8)
arrows = uid()
html.append(f'<svg class="node lead arrows" id="{arrows}" style="left:{sx8}px;top:{sy8}px" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<path class="a1" d="M380 794 L240 952" stroke-dasharray="220"/>'
            f'<path class="a2" d="M700 794 L840 952" stroke-dasharray="220"/></svg>')
tween(f"#{arrows} .a1, #{arrows} .a2", "strokeDashoffset: 220", 'strokeDashoffset: 0, duration: 0.4, stagger: 0.15', T("paix") - 0.2)
ok = put(S8, 90, 960, "<small>Paix</small>intacte", "box out", "font-size:42px")
bad = put(S8, 690, 960, "<small>Paix</small>en danger", "box out", "font-size:36px")
blur_in(ok, T("paix") + 0.3, 12)
blur_in(bad, T("dépendait") - 0.1, 12)
sfx("click", T("dépendait") - 0.1, 0.6)
tag(S8, 70, 1250, "Il a pris trop de place", T("trop") - 0.3, "acc", 40)
hit(T("trop"), 0.8)

# --- S9 · 62.0 – 66.3 · un serviteur, pas un maître
cam(62.0, S9)
headline(S9, 280, ["Un [serviteur],", "pas un maître"], T("redonne-lui") - 0.2, kicker="Sa vraie place", hl_t=T("serviteur"), size=104)
sticker(S9, "perso-serein-portrait", 280, 700, 520, T("serviteur") - 0.1, rot=-2)
hit(T("maître"), 1.0)

# --- S10 · 66.3 – 73.4 · mode sombre : la question aux spectateurs
cam(66.3, S10)
dark_mode(66.25)
headline(S10, 430, ["Dans quel [domaine]", "l'argent te met-il", "à l'épreuve ?"], T("toi") - 0.5, kicker="À ton tour", hl_t=T("domaine"), size=88, dark=True)
sticker(S10, "panneau-carrefour", 640, 1080, 280, T("lépreuve") - 0.1, rot=3)
cta = put(S10, 70, 900, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(73.4, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 9.8), ("02", "Verset", 9.8, 23.2), ("03", "Outil", 23.2, 42.5), ("04", "Cœur", 42.5, DUR)],
    suppress=[(15.0, 18.9), (73.8, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("statere-or", 40, 1180, 330, -6), ("perso-serein-portrait", 740, 1040, 300, 4)]},
    endcard_t=74.0,
)

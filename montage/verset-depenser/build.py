"""Short « Ce verset biblique peut changer ta façon de dépenser » (Proverbes 21.20) — style 02, 9:16, ~59 s.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Proverbes 21.20", "lang": "fr"}
s.setup(here=HERE, duration=59.0, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8, S9 = (0, 2), (1, 2), (2, 2)
S10 = (2, 3)

# --- S1 · 0 – 5.3 · accroche : le personnage et le portefeuille sont à l'écran dès la 1re image
cam(0, S1)
sticker(S1, "perso-stresse-pied", 50, 570, 360, 0.0, rot=-3, instant=True)
sticker(S1, "portefeuille", 500, 610, 440, 0.0, rot=3, instant=True)
headline(S1, 300, ["Le 20 du mois,", "il reste [presque rien]"], 0.0, kicker="Budget · Le constat", hl_t=T("presque") + 0.1, size=84)
counter(S1, 500, 1040, 100, 3, T("mois") + 0.1, 1.5, " %", 150, "small")
label_box(S1, 500, 1210, "Solde du mois", "illustration, sans chiffres réels", T("mois") + 0.3)
tag(S1, 440, 1300, "Où est passé l'argent ?", T("passé") - 0.15, "acc", 34)
hit(T("rien"), 1.0)

# --- S2 · 5.3 – 11.4 · ce n'est pas (toujours) le revenu, c'est la réflexion avant de dépenser
cam(5.3, S2)
headline(S2, 290, ["Pas toujours un", "manque de [revenu]"], T("ce") - 0.3, kicker="Le vrai problème", hl_t=T("revenu"), size=92)
bar_to_scale(S2, 170, 1230, 540, T("revenu") - 0.2, width=210, acc=False)
bar_to_scale(S2, 560, 1230, 140, T("réflexion") - 0.2, width=210, acc=True)
label_box(S2, 150, 1250, "Revenu", None, T("revenu") + 0.1)
label_box(S2, 540, 1250, "Réflexion", "avant de dépenser", T("réflexion") + 0.1)
ref(S2, 150, 1355, "SCHÉMA ILLUSTRATIF", T("réflexion") + 0.4)
hit(T("réflexion"), 0.7)

# --- S3 · 11.4 – 21.8 · le verset (Pr 21.20) ; sous-titres coupés pendant la citation
cam(11.4, S3)
headline(S3, 280, ["La Bible le dit", "très [clairement]"], T("bible") - 0.3, kicker="La Parole", hl_t=T("clairement"), size=96)
tag(S3, 70, 590, "Proverbes 21.20", T("proverbes") - 0.1, "acc", 52)
verse = ('« De précieux <em class="hl h1"><span>trésors</span><i></i></em> et de l\'huile sont dans la demeure du '
         '<em class="hl h2"><span>sage</span><i></i></em>, mais l\'homme '
         '<em class="hl h3"><span>insensé</span><i></i></em> les engloutit. »')
v = put(S3, 70, 700, f'<div class="h" style="font-size:58px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("précieux") - 0.2, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("trésors"))
tween(f"#{v} .h2 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("sage"))
tween(f"#{v} .h3 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("insensé"))
sticker(S3, "statere-or", 60, 1010, 280, T("précieux") + 0.1, rot=-5)
sticker(S3, "tetradrachme", 360, 1030, 260, T("trésors") + 0.15, rot=4)
sticker(S3, "lekythos", 700, 960, 170, T("l'huile") - 0.1, rot=3)
ref(S3, 70, 1400, "TRADUCTION : LOUIS SEGOND 1910", T("verset") + 0.3)
hit(T("engloutit"), 1.0)

# --- S4 · 21.8 – 26.0 · le sage garde, l'insensé engloutit
cam(21.8, S4)
headline(S4, 280, ["Le [sage] garde,", "l'[insensé] engloutit"], T("le", 2) - 0.2, kicker="Le contraste", hl_t=T("linsensé") - 0.1, size=88)
sticker(S4, "sage-pied", 60, 600, 300, T("sage", 1) - 0.1, rot=-3)
sticker(S4, "bourse-pleine", 50, 1215, 190, T("réserves") - 0.2, rot=-4)
sticker(S4, "insense-pied", 520, 600, 440, T("linsensé") - 0.1, rot=3)
sticker(S4, "bourse-vide", 560, 1215, 300, T("linsensé") + 0.3, rot=2)
hit(T("engloutit", 1), 0.9)

# --- S5 · 26.0 – 32.7 · exemple : café, abonnement oublié, livraison
cam(26.0, S5)
headline(S5, 280, ["Un exemple [simple]"], T("prends") - 0.2, kicker="Au quotidien", hl_t=T("simple"), size=90)
sticker(S5, "cafe", 60, 580, 260, T("café") - 0.1, rot=-4)
label_box(S5, 60, 1140, "Un café", None, T("café") + 0.2)
sticker(S5, "telephone-abonnements", 400, 600, 240, T("abonnement") - 0.1, rot=3)
label_box(S5, 340, 1140, "Un abonnement", "oublié", T("abonnement") + 0.2)
sticker(S5, "colis-livraison", 700, 640, 270, T("livraison") - 0.1, rot=-3)
label_box(S5, 690, 1140, "Une livraison", "« juste cette fois »", T("livraison") + 0.2)
hit(T("fois"), 0.6)

# --- S6 · 32.7 – 36.1 · ensemble, ça avale le trésor
cam(32.7, S6)
headline(S6, 280, ["Ça avale le [trésor]"], T("ensemble") - 0.2, kicker="Petit à petit", hl_t=T("trésor"), size=92)
sticker(S6, "bocal-plein", 80, 600, 360, T("ensemble") + 0.1, rot=-3)
label_box(S6, 80, 1215, "La réserve", "au départ", T("ensemble") + 0.4)
sticker(S6, "bocal-presque-vide", 560, 600, 360, T("avale") + 0.1, rot=3)
label_box(S6, 560, 1215, "Après les", "petites dépenses", T("avale") + 0.4)
hit(T("avale"), 0.9)

# --- S7 · 36.1 – 43.0 · la question à se poser (schéma de décision)
cam(36.1, S7)
headline(S7, 280, ["Une seule [question]"], T("alors") - 0.2, kicker="Avant d'acheter", hl_t=T("question"), size=88)
f1 = put(S7, 290, 640, "Ma prochaine<br>dépense", "box")
blur_in(f1, T("prochaine") - 0.1, 14)
f2 = put(S7, 230, 860, "Cet achat construit-il<br>ma réserve ?", "box q")
blur_in(f2, T("cet") - 0.1, 14)
sx7, sy7 = st(*S7)
arrows = uid()
html.append(f'<svg class="node lead arrows" id="{arrows}" style="left:{sx7}px;top:{sy7}px" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<path class="a0" d="M540 748 L540 852" stroke-dasharray="110"/>'
            f'<path class="a1" d="M380 1014 L240 1172" stroke-dasharray="220"/>'
            f'<path class="a2" d="M700 1014 L840 1172" stroke-dasharray="220"/></svg>')
tween(f"#{arrows} .a0", "strokeDashoffset: 110", 'strokeDashoffset: 0, duration: 0.3', T("prochaine") + 0.2)
tween(f"#{arrows} .a1, #{arrows} .a2", "strokeDashoffset: 220", 'strokeDashoffset: 0, duration: 0.4, stagger: 0.15', T("réserve") - 0.2)
ok = put(S7, 90, 1180, "<small>Il</small>construit", "box out", "font-size:46px")
bad = put(S7, 690, 1180, "<small>Il</small>engloutit", "box out", "font-size:46px")
blur_in(ok, T("réserve") + 0.1, 12)
blur_in(bad, T("l'engloutit-il") - 0.1, 12)
sfx("click", T("réserve") + 0.1, 0.6)
hit(T("l'engloutit-il"), 0.9)

# --- S8 · 43.0 – 46.2 · si tu hésites, 24 heures
cam(43.0, S8)
headline(S8, 280, ["Si tu hésites,", "attends [24 h]"], T("si") - 0.2, kicker="La règle", hl_t=T("attends"), size=92)
counter(S8, 70, 700, 0, 24, T("vingt-quatre") - 0.3, 1.2, " heures", 220, "small")
sticker(S8, "sablier", 700, 1000, 230, T("hésites") + 0.1, rot=4)
tag(S8, 70, 1010, "Une pause, pas une interdiction", T("heures") - 0.1, "", 36)
hit(T("vingt-quatre"), 0.8)

# --- S9 · 46.2 – 49.3 · pas de la privation, de la sagesse
cam(46.2, S9)
headline(S9, 280, ["Pas de privation,", "mais de [sagesse]"], T("ce", 1) - 0.2, kicker="Le principe", hl_t=T("sagesse"), size=90)
sticker(S9, "perso-calme-portrait", 240, 640, 560, T("privation") - 0.1, rot=-2)
hit(T("sagesse"), 1.0)

# --- S10 · 49.3 – 55.7 · mode sombre : la question aux spectateurs
cam(49.3, S10)
dark_mode(49.25)
headline(S10, 430, ["Quelle [dépense]", "vas-tu", "repenser ?"], T("quelle") - 0.2, kicker="À ton tour", hl_t=T("dépense", 1), size=110, dark=True)
sticker(S10, "perso-calme-portrait", 640, 1000, 300, T("repenser") - 0.1, rot=3)
cta = put(S10, 70, 890, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(55.7, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Constat", 0, 13.4), ("02", "Verset", 13.4, 21.8), ("03", "Piège", 21.8, 36.1), ("04", "Action", 36.1, DUR)],
    suppress=[(13.6, 21.6), (56.2, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("statere-or", 40, 1180, 380, -6), ("perso-calme-portrait", 790, 1060, 240, 5)]},
    endcard_t=56.3,
)

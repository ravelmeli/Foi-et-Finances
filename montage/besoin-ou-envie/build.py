"""Short « Comment savoir si un achat est un besoin ou une envie selon la Bible » (1 Timothée 6.8) — style 02, 9:16, ~65 s.
Version 2 « rétention » : accroche + boucle ouverte (question n°3), silences raccourcis, mouvement permanent, mots géants,
zooms-impacts, pièces qui tombent, musique libre de droits, et fin qui revient sur la première image (la vidéo boucle).

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Besoin ou envie", "lang": "fr"}
s.setup(here=HERE, duration=65.3, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8, S9 = (0, 2), (1, 2), (2, 2)
S10, S11, S12 = (2, 3), (1, 3), (0, 3)

# --- S1 · accroche : ce que tu veux acheter, maintenant… besoin ou envie ? (c'est aussi l'image de fin : boucle)
cam(0, S1)
sticker(S1, "baton-vitrine", 50, 600, 360, 0.0, rot=-2, instant=True)
sticker(S1, "boite-smartphone", 520, 980, 330, T("acheter") - 0.1, rot=-3)
sticker(S1, "sac-shopping", 580, 600, 280, T("maintenant") - 0.1, rot=4)
headline(S1, 300, ["Besoin ou", "[envie] ?"], 0.0, kicker="Avant d'acheter", hl_t=T("envie"), size=110)
bigword("Besoin", T("besoin"), 0.7)
bigword("Envie ?", T("envie"), 0.6)
hit(T("envie"), 0.9)

# --- S2 · boucle ouverte : la question n°3
cam(T("reste") - 0.15, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], T("reste") - 0.1, kicker="La question n°3", hl_t=T("bout"), size=104)
q = put(S2, 230, 640, "<small>Question</small>3 ?", "box out", "width:620px;font-size:120px")
blur_in(q, T("troisième") - 0.1, 12)
sticker(S2, "baton-pense", 380, 960, 300, T("question") - 0.1, rot=2)
tag(S2, 70, 1300, "Presque personne ne se la pose", T("personne") - 0.3, "acc", 36)
hit(T("troisième"), 0.8)

# --- S3 · la Bible nous aide à faire la différence
cam(T("bible") - 0.5, S3)
headline(S3, 280, ["La Bible aide", "à faire la [différence]"], T("bible") - 0.3, kicker="La Parole", hl_t=T("différence"), size=88)
sticker(S3, "baton-lit-livre", 70, 620, 330, T("bible") - 0.2, rot=-2)
sticker(S3, "pupitre-parole", 520, 640, 380, T("aide") - 0.1, rot=3)
hit(T("différence"), 0.7)

# --- S4 · le verset (1 Tm 6.8) : séquence « Parole » ; sous-titres coupés pendant la citation
cam(T("paul") - 0.25, S4)
headline(S4, 280, ["Cela nous", "[suffira]"], T("paul") - 0.2, kicker="Paul à Timothée", hl_t=T("suffira"), size=110)
tag(S4, 70, 600, "1 Timothée 6.8", T("1") - 0.1, "acc", 52)
sfx("spark", T("1") - 0.1, 1.6)
verse = ('« Si donc nous avons la <em class="hl h1"><span>nourriture</span><i></i></em> et le '
         '<em class="hl h2"><span>vêtement</span><i></i></em>, cela nous suffira. »')
v = put(S4, 70, 710, f'<div class="h" style="font-size:58px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("si") - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("nourriture"))
tween(f"#{v} .h2 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("vêtement"))
sticker(S4, "livre-croix-ouvert", 60, 1020, 380, T("1") + 0.2, rot=-3)
pan, _ = sticker(S4, "panier-besoins", 480, 1010, 260, T("nourriture") - 0.1, rot=3)
vet, _ = sticker(S4, "vetements-plies", 760, 1060, 220, T("vêtement") - 0.1, rot=-3)
ref(S4, 70, 1420, "1 TIMOTHÉE 6.8 · LSG 1910", T("verset") + 0.3)
hit(T("suffira"), 1.0)

# --- S5 · un besoin : chaque mot fait apparaître ou battre une image
cam(T("un", 1) - 0.2, S5)
headline(S5, 280, ["Un [besoin]"], T("un", 1) - 0.1, kicker="Ce qui te fait vivre", hl_t=T("besoin", 1), size=120)
p5, _ = sticker(S5, "panier-besoins", 50, 600, 300, T("nourrir") - 0.2, rot=-3)
m5, _ = sticker(S5, "maison-simple", 380, 610, 300, T("loger") - 0.2, rot=3)
v5, _ = sticker(S5, "vetements-plies", 710, 620, 270, T("vêtir") - 0.2, rot=-2)
tag(S5, 70, 960, "Se nourrir", T("nourrir") - 0.1, "", 38)
tag(S5, 70, 1045, "Se loger · se vêtir", T("loger") - 0.1, "", 38)
tag(S5, 70, 1130, "Se soigner · travailler", T("soigner") - 0.1, "", 38)
tag(S5, 70, 1250, "Prendre soin des tiens", T("vivre") - 0.1, "acc", 40)
bump(p5, T("soigner"))
bump(m5, T("travailler"))
hit(T("travailler"), 0.7)

# --- S6 · une envie
cam(T("envie", 1) - 0.6, S6)
headline(S6, 280, ["Une [envie]"], T("envie", 1) - 0.4, kicker="Ce qui rend la vie agréable", hl_t=T("envie", 1), size=120)
w6, _ = sticker(S6, "montre-luxe", 60, 620, 240, T("rend") - 0.1, rot=-4)
b6, _ = sticker(S6, "boite-smartphone", 340, 650, 320, T("agréable") - 0.2, rot=3)
sticker(S6, "sac-shopping", 720, 620, 230, T("mais") - 0.2, rot=-3)
tag(S6, 70, 1100, "Tu peux t'en passer", T("passer") - 0.4, "acc", 42)
bigword("Envie", T("envie", 1), 0.7)
hit(T("passer"), 0.7)

# --- S7 · pas un péché ; le problème : l'envie avant le besoin
cam(T("attention") - 0.4, S7)
headline(S7, 280, ["Pas un [péché]"], T("attention") - 0.3, kicker="Attention", hl_t=T("péché"), size=110)
d7, _ = sticker(S7, "baton-deux-mains", 60, 600, 380, T("attention") - 0.2, rot=-2)
sticker(S7, "panier-besoins", 520, 640, 220, T("problème") - 0.1, rot=3)
sticker(S7, "sac-shopping", 770, 660, 190, T("passe") - 0.1, rot=-3)
tag(S7, 470, 950, "Le problème :", T("problème") - 0.1, "", 36)
tag(S7, 470, 1035, "l'envie avant le besoin", T("avant") - 0.3, "acc", 36)
shake(d7, T("problème"))
hit(T("besoins"), 0.8)

# --- S8 · trois questions avant d'acheter
cam(T("alors") - 0.2, S8)
headline(S8, 280, ["Trois [questions]"], T("alors") - 0.1, kicker="Avant d'acheter", hl_t=T("questions"), size=110)
boxes(S8, 50, 640, ["1", "2", "3"], T("trois") - 0.2, step=300, small="Question", cls="day wide", gap=0.22)
sticker(S8, "baton-pense", 380, 860, 300, T("pose-toi") - 0.1, rot=2)
hit(T("questions"), 0.8)

# --- S9 · les trois questions (la n°3 referme la boucle ouverte de l'accroche)
cam(T("1", 1) - 0.25, S9)
headline(S9, 280, ["Le [test]", "en trois questions"], T("1", 1) - 0.2, kicker="Avant d'acheter", hl_t=T("1", 1), size=96)
q1 = put(S9, 60, 620, "<small>1</small>Puis-je vivre sans,<br>ce mois-ci ?", "box q", "width:600px;font-size:40px")
q2 = put(S9, 60, 860, "<small>2</small>Pour moi, ou pour<br>l'image que je donne ?", "box q", "width:600px;font-size:40px")
q3 = put(S9, 60, 1100, "<small>3</small>Dans une semaine,<br>en aurai-je encore envie ?", "box q", "width:600px;font-size:40px")
blur_in(q1, T("1", 1) - 0.1, 12)
blur_in(q2, T("2") - 0.1, 12)
blur_in(q3, T("3") - 0.1, 12)
sfx("click", T("2") - 0.1, 0.6)
sfx("click", T("3") - 0.1, 0.6)
sticker(S9, "boite-smartphone", 700, 640, 260, T("vivre", 1) - 0.2, rot=4)
sticker(S9, "sac-shopping", 720, 880, 220, T("limage") - 0.3, rot=-3)
sticker(S9, "baton-sablier", 720, 1090, 180, T("jattends") - 0.3, rot=2)
bump(q1, T("sans"))
bump(q2, T("limage"))
bigword("Question 3", T("3"), 0.8, y=1250, size=120)
bump(q3, T("semaine"))
hit(T("envie", 3), 0.8)

# --- S10 · une hésitation = une envie ; d'abord les besoins (les pièces vont d'abord au panier)
cam(T("si", 2) - 0.2, S10)
headline(S10, 280, ["D'abord tes", "[besoins]"], T("si", 2) - 0.1, kicker="Une hésitation ? Une envie", hl_t=T("besoins", 1), size=110)
b1 = put(S10, 60, 640, "<small>D'abord</small>Besoins", "box out", "width:420px;font-size:52px")
b2 = put(S10, 560, 640, "<small>Ensuite</small>Envies", "box out", "width:420px;font-size:52px")
blur_in(b1, T("couvre") - 0.2, 12)
blur_in(b2, T("puis") - 0.2, 12)
sfx("click", T("couvre") - 0.2, 0.6)
sticker(S10, "baton-panier", 80, 850, 300, T("hésiter") - 0.1, rot=-2)
coins(S10, 140, 1180, T("couvre") + 0.1, n=5, spread=200, size=70)
sticker(S10, "montre-luxe", 640, 900, 220, T("envies") - 0.2, rot=4)
tag(S10, 70, 1330, "Sans culpabilité", T("culpabilité") - 0.4, "acc", 44)
hit(T("culpabilité"), 0.8)

# --- S11 · le contentement : la paix de savoir que tu as assez
cam(T("contentement") - 0.6, S11)
headline(S11, 280, ["Le [contentement]"], T("contentement") - 0.4, kicker="Pas la privation", hl_t=T("contentement"), size=96)
sticker(S11, "baton-priere", 90, 600, 320, T("contentement") - 0.3, rot=-2)
sticker(S11, "livre-croix-ferme", 560, 700, 340, T("privation") - 0.2, rot=4)
tag(S11, 70, 1250, "La paix de savoir que tu as assez", T("paix") - 0.3, "acc", 36)
bigword("Assez", T("assez"), 0.7)
hit(T("assez"), 0.9)

# --- S12 · la question aux spectateurs (pas de mode sombre : la fin revient à l'image d'ouverture)
cam(T("quel") - 0.2, S12)
headline(S12, 300, ["Quel [achat]", "vas-tu tester ?"], T("quel") - 0.1, kicker="À ton tour", hl_t=T("achat"), size=104)
sticker(S12, "baton-serein", 680, 820, 260, T("test") - 0.2, rot=3)
cta = put(S12, 70, 760, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)
tag(S12, 70, 900, "Abonne-toi", T("abonne-toi") - 0.2, "acc", 48)

# --- fin en boucle · retour sur l'image d'ouverture, même question
cam(T("prochaine") - 0.5, S1)
bigword("Besoin", T("besoin", 2), 0.6)
bigword("ou envie ?", T("envie", 5) - 0.2, 0.8, size=140)
hit(T("envie", 5), 0.8)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 9.8), ("02", "Verset", 9.8, 23.6), ("03", "Différence", 23.6, 35.0), ("04", "Test", 35.0, DUR)],
    suppress=[(13.2, 16.7)],     # verset affiché en grand : pas de sous-titres
)

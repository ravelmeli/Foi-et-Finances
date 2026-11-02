"""Short « Comment sortir progressivement du cycle des dettes » (Galates 6.9) — style 02, 9:16, ~75 s.
Acquis des vidéos longues : mots géants, compteur, pièces, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte (étape 4) refermée à l'étape 4, fin qui revient sur la première image. Temps lus dans transcript.json.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Sortir du cycle des dettes", "lang": "fr"}
s.setup(here=HERE, duration=75.4, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

S = [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (1, 3), (0, 3), (0, 4), (1, 4)]
S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14 = S


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-tapis-roulant", 40, 620, 480, 0.0, rot=-2, instant=True)
sticker(S1, "pile-factures", 600, 660, 340, 1.0, rot=3)
sticker(S1, "tapis-roulant-pieces", 650, 980, 260, 2.0, rot=-3)
headline(S1, 300, ["Tes dettes", "[baissent] ?"], 0.0, kicker="Chaque mois", hl_t=3.1, size=110)
bigword("Jamais ?", 3.5, 0.8, y=1260, size=130)
hit(3.6, 0.9)

# --- S2 · boucle ouverte : l'étape 4
cam(4.7, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 4.8, kicker="L'étape n°4", hl_t=5.7, size=104)
q = put(S2, 230, 640, "<small>Étape</small>4 ?", "box out", "width:620px;font-size:120px")
blur_in(q, 6.4, 12)
sticker(S2, "baton-pense", 380, 960, 300, 6.8, rot=2)
tag(S2, 70, 1330, "Presque tout le monde la saute", 7.2, "acc", 36)
hit(6.5, 0.8)

# --- S3 · un verset pour tenir debout
cam(9.2, S3)
headline(S3, 280, ["Un [verset]", "pour tenir"], 9.3, kicker="Courage", hl_t=10.2, size=104)
sticker(S3, "baton-lit-livre", 70, 640, 360, 9.6, rot=-2)
sticker(S3, "pupitre-parole", 520, 700, 400, 10.6, rot=3)
tag(S3, 70, 1330, "Pour te tenir debout", 10.9, "acc", 40)

# --- S4 · le verset (Galates 6.9) : séquence « Parole » ; sous-titres coupés pendant la citation
cam(11.6, S4)
headline(S4, 280, ["Ne nous", "[lassons] pas"], 11.7, kicker="Paul aux Galates", hl_t=15.9, size=104)
tag(S4, 70, 600, "Galates 6.9", 14.0, "acc", 52)
sfx("spark", 14.0, 1.6)
verse = ("«&nbsp;Ne nous lassons pas de " + m(0, "faire le bien") + " ; car nous moissonnerons au temps convenable, "
         "si nous " + m(1, "ne nous relâchons pas") + ".&nbsp;»")
v = put(S4, 70, 710, f'<div class="h" style="font-size:56px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, 15.0, 20)
tween(f"#{v} .m0 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 16.6)
tween(f"#{v} .m1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 19.8)
sticker(S4, "livre-croix-ouvert", 60, 1080, 380, 14.2, rot=-3)
sticker(S4, "croix-verte", 560, 1060, 190, 17.4, rot=4)
sticker(S4, "piles-croissantes", 780, 1130, 230, 18.7, rot=-3)
ref(S4, 70, 1420, "GALATES 6.9 · LSG 1910", 14.6)
hit(20.4, 1.0)

# --- S5 · le principe : la constance, pas le coup d'éclat
cam(21.2, S5)
headline(S5, 280, ["La [constance]"], 21.3, kicker="Le principe vaut ici aussi", hl_t=25.9, size=104)
sticker(S5, "baton-serein", 60, 620, 330, 21.8, rot=-2)
sticker(S5, "graphique-hausse", 520, 700, 330, 23.5, rot=3)
tag(S5, 70, 1160, "Pas un coup d'éclat", 26.7, "acc", 46)
hit(25.9, 0.7)

# --- S6 · cinq étapes
cam(28.0, S6)
headline(S6, 280, ["Une étape", "à la [fois]"], 28.1, kicker="Cinq étapes", hl_t=30.2, size=104)
counter(S6, 70, 760, 0, 5, 28.5, 0.9, " étapes", 150)
sticker(S6, "baton-budget", 560, 900, 320, 29.4, rot=2)
hit(29.1, 0.7)

# --- S7 · étape 1 : arrête d'ajouter
cam(30.5, S7)
headline(S7, 280, ["Arrête", "d'[ajouter]"], 30.6, kicker="Étape 1", hl_t=31.6, size=110)
sticker(S7, "carte-bancaire", 60, 640, 380, 31.3, rot=-4)
sticker(S7, "seau-perce", 700, 640, 250, 33.7, rot=3)
tag(S7, 70, 1010, "Plus de nouveau crédit", 32.1, "", 40)
tag(S7, 70, 1105, "Plus de découvert volontaire", 33.5, "acc", 36)
bigword("Stop", 31.1, 0.8, y=1210, size=140)
hit(31.8, 0.7)

# --- S8 · étape 2 : fais la liste
cam(35.1, S8)
headline(S8, 280, ["Fais la", "[liste]"], 35.2, kicker="Étape 2", hl_t=36.4, size=110)
sticker(S8, "baton-ecrit-liste", 560, 640, 400, 35.8, rot=2)
sticker(S8, "feuille-liste", 60, 700, 330, 36.6, rot=-3)
tag(S8, 70, 1130, "Tout ce que tu dois", 37.2, "", 40)
tag(S8, 70, 1220, "Les montants et les taux", 38.2, "acc", 40)
hit(38.9, 0.7)

# --- S9 : étape 3 : minimum partout, petit montant sur une seule dette
cam(39.4, S9)
headline(S9, 280, ["La plus [petite]", "d'abord"], 39.5, kicker="Étape 3", hl_t=44.2, size=96)
sticker(S9, "enveloppes-budget", 60, 640, 320, 39.8, rot=-3)
sticker(S9, "piles-croissantes", 560, 700, 330, 44.0, rot=3)
tag(S9, 70, 970, "Le minimum partout", 40.7, "", 40)
tag(S9, 70, 1070, "Un petit montant, une seule dette", 42.2, "", 34)
coins(S9, 640, 1120, 42.3, n=4, spread=180, size=60)
counter(S9, 70, 1190, 0, 20, 45.0, 0.9, " €", 120)
hit(45.5, 0.8)

# --- S10 · étape 4 : la mensualité passe à la suivante (referme la boucle ouverte)
cam(46.3, S10)
headline(S10, 280, ["Verse-la sur", "la [suivante]"], 46.4, kicker="Étape 4", hl_t=50.8, size=104)
sticker(S10, "chaine-cassee", 60, 640, 360, 47.7, rot=-3)
sticker(S10, "enveloppe-salaire", 560, 660, 320, 49.3, rot=3)
tag(S10, 70, 1010, "Dette soldée", 47.7, "", 42)
tag(S10, 70, 1105, "Ne dépense pas la mensualité", 48.6, "", 36)
tag(S10, 70, 1200, "Verse-la sur la suivante", 50.0, "acc", 40)
hit(50.8, 0.9)

# --- S11 · l'étape qu'on saute : elle accélère tout
cam(51.3, S11)
headline(S11, 280, ["L'étape qu'on", "[saute]"], 51.4, kicker="Elle accélère tout", hl_t=53.2, size=104)
sticker(S11, "calendrier-mois", 60, 640, 330, 51.9, rot=-3)
sticker(S11, "graphique-hausse", 540, 680, 380, 54.2, rot=3)
bigword("Accélère", 54.2, 0.9, y=1190, size=130)
hit(54.6, 0.9)

# --- S12 · étape 5 : ne reste pas seul
cam(55.5, S12)
headline(S12, 280, ["Ne reste pas", "[seul]"], 55.6, kicker="Étape 5", hl_t=57.1, size=104)
sticker(S12, "baton-ami", 60, 640, 360, 56.4, rot=-2)
sticker(S12, "baton-priere", 650, 700, 230, 58.0, rot=3)
tag(S12, 70, 1170, "Un conseiller en budget", 57.8, "", 36)
tag(S12, 70, 1255, "ou une association", 58.9, "", 36)
tag(S12, 70, 1340, "Ce n'est pas une honte", 60.4, "acc", 36)
hit(60.7, 0.7)

# --- S13 · un pas après l'autre
cam(61.2, S13)
headline(S13, 280, ["Un pas après", "l'[autre]"], 61.3, kicker="Tu avances", hl_t=64.1, size=104)
sticker(S13, "baton-pose-fardeau", 60, 640, 400, 62.0, rot=-2)
sticker(S13, "soleil-nuage", 600, 700, 330, 64.6, rot=3)
hit(64.7, 0.8)

# --- S14 · question aux spectateurs
cam(65.7, S14)
headline(S14, 300, ["Quelle [dette]", "en premier ?"], 65.8, kicker="À ton tour", hl_t=66.3, size=104)
sticker(S14, "baton-serein", 680, 820, 260, 66.8, rot=3)
cta = put(S14, 70, 760, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 67.7, 14)
sfx("click", 67.7, 0.8)
tag(S14, 70, 900, "Abonne-toi", 68.7, "acc", 48)

# --- fin en boucle : retour sur l'image d'ouverture
cam(69.4, S1)
bigword("Elles baissent", 72.4, 0.9, y=1270, size=110)
bigword("Enfin !", 73.7, 0.9, y=1250, size=150)
hit(73.8, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 9.2), ("02", "Verset", 9.2, 21.2), ("03", "Étapes", 21.2, 55.5), ("04", "Action", 55.5, DUR)],
    suppress=[(14.95, 20.9)],
)

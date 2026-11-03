"""Short « Pourquoi comparer ta vie aux autres détruit tes finances » (Proverbes 14.30) — style 02, 9:16, ~70 s.
Acquis des vidéos longues : mots géants, compteur, pièces, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte (trois façons de l'arrêter) refermée, fin qui revient sur la première image. Temps lus dans transcript.json.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Comparer sa vie aux autres", "lang": "fr"}
s.setup(here=HERE, duration=70.5, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

S = [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (1, 3), (0, 3), (0, 4), (1, 4)]
S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14 = S


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-pelouse", 40, 640, 540, 0.0, rot=-2, instant=True)
sticker(S1, "telephone-parfait", 700, 620, 250, 1.0, rot=3)
headline(S1, 300, ["Ta vie te semble", "[trop petite] ?"], 0.0, kicker="Tu regardes les autres", hl_t=3.3, size=100)
bigword("Trop petite ?", 3.4, 0.8, y=1250, size=110)
hit(3.6, 0.9)

# --- S2 · boucle ouverte : trois façons de l'arrêter
cam(4.3, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 4.4, kicker="Ça te coûte cher", hl_t=5.1, size=104)
counter(S2, 70, 640, 0, 3, 8.5, 0.7, " façons", 150)
tag(S2, 70, 850, "Cette comparaison coûte cher", 6.3, "acc", 34)
sticker(S2, "baton-soucieux", 660, 800, 230, 4.9, rot=3)
hit(8.6, 0.8)

# --- S3 · le verset (Proverbes 14.30) : séquence « Parole » ; sous-titres coupés pendant la citation
cam(10.8, S3)
headline(S3, 280, ["Un cœur", "[calme]"], 10.9, kicker="Livre des Proverbes", hl_t=15.9, size=104)
tag(S3, 70, 600, "Proverbes 14.30", 13.9, "acc", 52)
sfx("spark", 13.9, 1.6)
verse = ("«&nbsp;Un " + m(0, "cœur calme") + " est la vie du corps, mais " + m(1, "l'envie est la carie des os") + ".&nbsp;»")
v = put(S3, 70, 710, f'<div class="h" style="font-size:58px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, 14.9, 20)
tween(f"#{v} .m0 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 15.9)
tween(f"#{v} .m1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 18.0)
sticker(S3, "livre-croix-ouvert", 60, 1090, 380, 11.4, rot=-3)
sticker(S3, "baton-coeur-calme", 560, 1050, 330, 16.0, rot=3)
ref(S3, 70, 1420, "PROVERBES 14.30 · LSG 1910", 14.4)
hit(18.9, 1.0)

# --- S4 · la carie
cam(19.2, S4)
headline(S4, 280, ["Elle ronge", "sans [bruit]"], 19.3, kicker="Comme une carie", hl_t=21.3, size=104)
sticker(S4, "baton-soucieux", 690, 640, 240, 19.8, rot=3)
tag(S4, 70, 700, "Ton cœur", 23.4, "", 46)
tag(S4, 70, 800, "Ton budget", 24.5, "acc", 46)
sticker(S4, "seau-perce", 80, 960, 250, 22.0, rot=-3)
hit(24.6, 0.8)

# --- S5 · comment elle détruit tes finances
cam(24.9, S5)
headline(S5, 280, ["Elle détruit", "tes [finances]"], 25.0, kicker="De trois façons", hl_t=26.3, size=104)
sticker(S5, "pile-factures", 60, 650, 380, 25.6, rot=-3)
sticker(S5, "carte-bancaire", 560, 720, 340, 26.6, rot=4)
bigword("Détruit", 25.9, 0.9, y=1100, size=140)
hit(26.4, 0.8)

# --- S6 · façon 1 : dépenser pour paraître
cam(27.0, S6)
headline(S6, 280, ["Dépenser pour", "[paraître]"], 27.1, kicker="Façon 1", hl_t=28.3, size=104)
sticker(S6, "baton-sacs-masque", 50, 640, 400, 28.3, rot=-2)
sticker(S6, "baton-voiture-hesite", 560, 700, 400, 30.3, rot=3)
tag(S6, 70, 1160, "Voiture, téléphone, vacances", 30.4, "", 34)
tag(S6, 70, 1250, "Pour ne pas être en reste", 32.6, "acc", 36)
hit(28.4, 0.7)

# --- S7 · façon 2 : s'endetter pour une vie qu'on voit de loin
cam(33.9, S7)
headline(S7, 280, ["T'endetter pour", "une vie de [loin]"], 34.0, kicker="Façon 2", hl_t=37.2, size=92)
sticker(S7, "facade-maison", 50, 660, 520, 34.6, rot=-2)
sticker(S7, "telephone-parfait", 650, 660, 250, 37.8, rot=3)
tag(S7, 70, 1130, "On montre le sourire", 39.2, "", 40)
tag(S7, 70, 1220, "Jamais les factures", 40.4, "acc", 42)
hit(40.6, 0.8)

# --- S8 · façon 3 : jamais content
cam(41.0, S8)
headline(S8, 280, ["Jamais", "[content]"], 41.1, kicker="Façon 3", hl_t=42.6, size=110)
sticker(S8, "baton-jaloux", 50, 650, 440, 42.0, rot=-2)
sticker(S8, "piedestal-pieces", 600, 700, 330, 43.9, rot=3)
sticker(S8, "montre-luxe", 780, 1010, 140, 44.3, rot=-4)
tag(S8, 70, 1180, "Toujours quelqu'un", 43.8, "", 40)
tag(S8, 70, 1270, "qui a plus", 44.8, "acc", 44)
hit(45.0, 0.8)

# --- S9 · alors, comment arrêter ?
cam(45.7, S9)
headline(S9, 280, ["Comment", "[arrêter] ?"], 45.8, kicker="Trois remèdes", hl_t=46.8, size=110)
sticker(S9, "baton-pense", 60, 660, 280, 46.2, rot=-2)
sticker(S9, "colombe", 600, 720, 300, 47.0, rot=3)

# --- S10 · remède 1 : ton budget
cam(47.3, S10)
headline(S10, 280, ["Ton [budget],", "pas les autres"], 47.4, kicker="Remède 1", hl_t=49.4, size=104)
sticker(S10, "baton-budget", 60, 660, 340, 48.5, rot=-2)
sticker(S10, "calendrier-mois", 600, 720, 300, 49.4, rot=3)
tag(S10, 70, 1190, "Compare-toi à ton budget", 49.3, "acc", 38)
hit(50.4, 0.7)

# --- S11 · remède 2 : arrête de suivre
cam(50.7, S11)
headline(S11, 280, ["Arrête de", "[suivre]"], 50.8, kicker="Remède 2", hl_t=52.3, size=110)
sticker(S11, "baton-reseaux", 60, 650, 320, 51.8, rot=-2)
sticker(S11, "boite-smartphone", 560, 720, 300, 53.3, rot=3)
tag(S11, 70, 1160, "Les comptes qui donnent", 53.1, "", 36)
tag(S11, 70, 1250, "envie d'acheter", 53.8, "acc", 40)
hit(54.0, 0.7)

# --- S12 · remède 3 : remercie
cam(54.3, S12)
headline(S12, 280, ["Remercie", "[chaque jour]"], 54.4, kicker="Remède 3", hl_t=56.1, size=100)
sticker(S12, "carnet-gratitude", 50, 660, 500, 54.7, rot=-2)
sticker(S12, "baton-priere", 650, 640, 250, 57.0, rot=3)
tag(S12, 70, 1130, "Ce que tu as déjà", 57.2, "acc", 42)
hit(57.4, 0.8)

# --- S13 · ta valeur
cam(57.9, S13)
headline(S13, 280, ["Ta [valeur]", "n'est pas là"], 58.0, kicker="Rappelle-toi", hl_t=58.5, size=104)
sticker(S13, "baton-serein", 60, 650, 300, 58.2, rot=-2)
sticker(S13, "croix-verte", 650, 700, 200, 60.0, rot=4)
tag(S13, 70, 1130, "Ni ce que tu possèdes", 59.6, "", 38)
tag(S13, 70, 1220, "ni ce que les autres montrent", 60.8, "acc", 34)
hit(61.2, 0.7)

# --- S14 · question aux spectateurs
cam(61.6, S14)
headline(S14, 300, ["Quel [compte]", "arrêter de suivre ?"], 61.7, kicker="À ton tour", hl_t=62.2, size=96)
sticker(S14, "baton-content", 700, 820, 230, 62.6, rot=3)
cta = put(S14, 70, 760, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 64.7, 14)
sfx("click", 64.7, 0.8)
tag(S14, 70, 900, "Abonne-toi", 65.5, "acc", 48)

# --- fin en boucle : retour sur l'image d'ouverture
cam(66.1, S1)
bigword("Pas ton budget", 68.8, 0.9, y=1250, size=110)
hit(69.0, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 10.8), ("02", "Verset", 10.8, 19.2), ("03", "Pourquoi", 19.2, 45.7), ("04", "Remèdes", 45.7, DUR)],
    suppress=[(14.85, 19.15)],
)

"""Short « La richesse peut-elle éloigner de Dieu ? » (Marc 10.25) — style 02, 9:16, ~77.5 s.
Lot de 4 Shorts. Acquis : mots géants, compteurs, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte refermée, fin qui revient sur la première image. Temps lus dans transcript.json (voix fournie).

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - La richesse peut-elle éloigner de Dieu ?", "lang": "fr"}
COLS, ROWS = 3, 21
s.setup(here=HERE, duration=77.5, cols=COLS, rows=ROWS, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
S = ST
_TR = json.load(open(os.path.join(HERE, "transcript.json"), encoding="utf-8"))


def _norm(x):
    return re.sub(r"[^\w]+", "", unicodedata.normalize("NFC", x.lower()))


def W(prefix, after=0.0, nth=0):
    """Début (en secondes) du n-ième mot contenant `prefix`, après l'instant `after`."""
    k = 0
    for w in _TR:
        if w["start"] >= after and _norm(prefix) in _norm(w["text"]):
            if k == nth:
                return round(w["start"], 2)
            k += 1
    raise KeyError(prefix)


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


CTA = '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire'


def verse_block(stn, ref_txt, t_ref, verse_html, t_text, marks, size=54, ref_y=1420, ref_label=None):
    verse_html = verse_html.replace(" »", "&nbsp;»").replace("« ", "«&nbsp;").replace(" ;", "&nbsp;;").replace(" :", "&nbsp;:")
    tag(stn, 70, 600, ref_txt, t_ref, "acc", 52)
    sfx("spark", t_ref, 1.6)
    v = put(stn, 70, 710, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.22">{verse_html}</div>', "headline", f"width:{W_PX}px")
    blur_in(v, t_text - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', mt)
    ref(stn, 70, ref_y, (ref_label or ref_txt.upper()) + " · LSG 1910", t_ref + 0.3)


W_PX = 1080 - 2 * 70 - 60



S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19 = S[:19]

# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "riche-triste-sac", 40, 650, 380, 0.0, rot=-2, instant=True)
sticker(S1, "coeur-coffre-cadenas", 520, 760, 400, 3.2, rot=3)
headline(S1, 300, ["Riche… et", "[loin] de Dieu ?"], 0.0, kicker="Jésus regarde un homme riche", hl_t=2.6, size=92)
bigword("Éloigné ?", 4.0, 0.8, y=1260, size=120)
hit(4.2, 0.9)

# --- S2 · boucle ouverte : l'espoir des riches
cam(5.9, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 6.0, kicker="L'espoir des riches", hl_t=6.8, size=104)
q = put(S2, 190, 640, "<small>Une phrase</small>d'espoir", "box out", "width:700px;font-size:100px")
blur_in(q, 8.2, 12)
sticker(S2, "baton-leger-lumiere", 640, 860, 280, 7.0, rot=3)
hit(8.4, 0.8)

# --- S3 · Marc 10 : un homme riche
cam(10.2, S3)
headline(S3, 280, ["Un homme", "[riche]"], 10.3, kicker="Évangile de Marc 10", hl_t=12.4, size=110)
sticker(S3, "riche-triste-sac", 60, 650, 330, 11.0, rot=-3)
sticker(S3, "baton-pense", 620, 700, 240, 12.2, rot=3)
hit(13.4, 0.7)

# --- S4 · Jésus le regarde et l'aime
cam(15.0, S4)
headline(S4, 280, ["Jésus le regarde", "et l'[aime]"], 15.1, kicker="Marc 10.21", hl_t=16.6, size=88)
sticker(S4, "coeur-receptacle", 60, 650, 400, 16.0, rot=-3)
sticker(S4, "croix-verte", 620, 700, 220, 17.0, rot=4)
tag(S4, 70, 1100, "« Il te manque une chose »", 18.0, "acc", 36)
hit(19.2, 0.7)

# --- S5 · vends, donne, suis-moi
cam(19.9, S5)
headline(S5, 280, ["Vends, donne,", "[suis-moi]"], 20.0, kicker="Son invitation", hl_t=22.0, size=92)
sticker(S5, "baton-donne", 60, 650, 380, 20.5, rot=-2)
sticker(S5, "enveloppe-don", 620, 720, 300, 21.6, rot=3)
hit(22.4, 0.7)

# --- S6 · il s'en va tout triste
cam(23.4, S6)
headline(S6, 280, ["Il s'en va", "[triste]"], 23.5, kicker="Il avait de grands biens", hl_t=24.8, size=110)
sticker(S6, "riche-triste-sac", 60, 650, 420, 24.0, rot=-2)
hit(25.6, 0.7)

# --- S7 · le verset (Marc 10.25) : séquence « Parole » ; sous-titres coupés
cam(26.5, S7)
headline(S7, 280, ["Un chameau,", "une [aiguille]"], 26.6, kicker="Marc 10.25", hl_t=33.4, size=104)
verse = ("«&nbsp;Il est " + m(0, "plus facile à un chameau") + " de passer par le trou d'une aiguille " + m(1, "qu'à un riche") + " d'entrer dans le royaume de Dieu.&nbsp;»")
verse_block(S7, "Marc 10.25", 27.0, verse, 28.7, [W("chameau", 28.5), W("riche", 30.0)], size=54, ref_label="MARC 10.25")
sticker(S7, "chameau-aiguille", 60, 1050, 340, 27.4, rot=-2)
hit(35.0, 1.0)

# --- S8 · la richesse n'est pas un péché
cam(35.1, S8)
headline(S8, 280, ["La richesse,", "pas un [péché]"], 35.2, kicker="Jésus ne dit pas", hl_t=36.6, size=92)
sticker(S8, "piedestal-pieces", 60, 650, 360, 36.0, rot=-2)
sticker(S8, "coeur-coffre-cadenas", 580, 720, 340, 38.0, rot=3)
tag(S8, 70, 1120, "Elle avait pris la première place", 38.4, "acc", 32)
hit(40.2, 0.8)

# --- S9 · trois signes d'alerte
cam(40.5, S9)
headline(S9, 280, ["Trois [signes]", "d'alerte"], 40.6, kicker="Attention", hl_t=41.0, size=100)
counter(S9, 70, 640, 0, 3, 41.2, 0.8, " signes", 130)
sticker(S9, "baton-soucieux", 600, 820, 250, 41.2, rot=3)

# --- S10 · signe 1 : du mal à donner
cam(42.3, S10)
headline(S10, 280, ["Du mal", "à [donner]"], 42.4, kicker="Signe 1", hl_t=43.0, size=110)
sticker(S10, "baton-fardeau", 60, 650, 380, 42.7, rot=-2)

# --- S11 · signe 2 : plus d'argent que de proches
cam(44.0, S11)
headline(S11, 280, ["Plus d'argent", "que de [proches]"], 44.1, kicker="Signe 2", hl_t=45.0, size=88)
sticker(S11, "famille-sortie", 60, 650, 480, 44.4, rot=-2)
sticker(S11, "coeur-fil-tresor", 560, 780, 380, 45.5, rot=3)

# --- S12 · signe 3 : plus rien à lâcher
cam(46.7, S12)
headline(S12, 280, ["Plus rien", "à [lâcher]"], 46.8, kicker="Signe 3", hl_t=47.5, size=110)
sticker(S12, "porte-etroite-sac", 60, 650, 460, 47.0, rot=-2)

# --- S13 · et Jésus ajoute (verset 27)
cam(48.1, S13)
headline(S13, 280, ["Et alors ?", "[Jésus] ajoute"], 48.2, kicker="Marc 10.27", hl_t=49.0, size=100)
sticker(S13, "baton-pense", 60, 650, 260, 48.5, rot=-2)

# --- S14 · le verset 27 : tout est possible à Dieu
cam(50.9, S14)
headline(S14, 280, ["Tout est", "[possible]"], 51.0, kicker="Marc 10.27", hl_t=54.0, size=110)
verse27 = ("«&nbsp;Cela est impossible aux hommes, mais non à Dieu&nbsp;; car " + m(0, "tout est possible à Dieu") + ".&nbsp;»")
verse_block(S14, "Marc 10.27", 51.0, verse27, 51.1, [W("tout", 53.0)], size=56, ref_label="MARC 10.27")
sticker(S14, "baton-leger-lumiere", 60, 980, 360, 51.4, rot=-2)
hit(55.2, 1.0)

# --- S15 · voilà l'espoir
cam(56.0, S15)
headline(S15, 280, ["Un cœur attaché", "peut être [libéré]"], 56.1, kicker="Voilà l'espoir", hl_t=57.0, size=84)
sticker(S15, "coeur-coffre-cadenas", 60, 650, 380, 56.4, rot=-2)
sticker(S15, "baton-leger-lumiere", 580, 740, 330, 58.5, rot=3)
tag(S15, 70, 1150, "Par Dieu, pas par nos forces", 59.5, "acc", 34)
hit(60.0, 0.8)

# --- S16 · cette semaine : une seule question
cam(61.6, S16)
headline(S16, 280, ["Qu'ai-je du mal", "à [lâcher] ?"], 61.7, kicker="Une seule question", hl_t=63.0, size=92)
sticker(S16, "baton-pense", 60, 650, 260, 62.0, rot=-2)
sticker(S16, "baton-mains-ouvertes-pieces", 560, 700, 330, 64.5, rot=3)
hit(65.0, 0.7)

# --- S17 · un petit geste
cam(66.2, S17)
headline(S17, 280, ["Un petit", "[geste]"], 66.3, kicker="Donne · partage · remercie", hl_t=67.0, size=110)
sticker(S17, "baton-mains-ouvertes-pieces", 60, 650, 400, 66.8, rot=-2)
tag(S17, 70, 1170, "Donne", 67.5, "", 40)
tag(S17, 70, 1250, "Partage", 68.5, "", 40)
tag(S17, 70, 1330, "Remercie", 69.3, "acc", 40)
hit(69.8, 0.7)

# --- S18 · l'attachement, pas l'argent
cam(69.9, S18)
headline(S18, 280, ["Pas l'argent,", "l'[attachement]"], 70.0, kicker="Ce qui éloigne de Dieu", hl_t=71.8, size=88)
sticker(S18, "coeur-coffre-cadenas", 60, 650, 400, 70.4, rot=-2)
sticker(S18, "baton-leger-lumiere", 600, 700, 300, 72.0, rot=3)
hit(72.6, 0.8)

# --- S19 · question aux spectateurs
cam(73.1, S19)
headline(S19, 300, ["Quelle question", "te touche le [plus] ?"], 73.2, kicker="À ton tour", hl_t=74.0, size=88)
sticker(S19, "baton-serein", 700, 880, 210, 73.6, rot=3)
cta = put(S19, 70, 760, CTA, "cta")
blur_in(cta, 74.6, 14)
sfx("click", 74.6, 0.8)
tag(S19, 70, 900, "Abonne-toi", 75.4, "acc", 48)

# --- fin en boucle
cam(76.4, S1)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 10.2), ("02", "Le récit", 10.2, 35.1), ("03", "Les signes", 35.1, 48.1), ("04", "L'espoir", 48.1, DUR)],
    suppress=[(28.6, 35.15), (51.0, 56.0)],
)

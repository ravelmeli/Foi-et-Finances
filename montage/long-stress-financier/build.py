"""Vidéo longue « Comment gérer le stress financier selon la Bible » — style 02 en 16:9 (1920 × 1080), ~3 min 50.
Bonhommes bâtons, Bible à la croix, croix flottantes, 4 séquences « Parole » identiques, abonnement au milieu, carte de fin.

Mise en page 16:9 (fiche de style, section 11) : titre en haut à gauche, texte et bandeaux à gauche, illustration à droite,
sous-titres en bas (y = 880). Les temps sont ceux de transcript.json (voix déjà débarrassée de ses silences).

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Gerer le stress financier selon la Bible", "lang": "fr"}
COLS, ROWS = 6, 7
s.setup(here=HERE, duration=233.5, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# Stations en serpentin sur une toile de 6 × 7 écrans 16:9.
ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
_n = [0]


def nxt(t):
    """Station suivante, et la caméra y va à t."""
    stn = ST[_n[0]]
    _n[0] += 1
    cam(t, stn)
    return stn


def title(stn, lines, t, kicker, hl_t=None, size=80):
    return headline(stn, 172, lines, t, kicker=kicker, hl_t=hl_t, size=size, x=80)


def bw(text, t, dur=0.9, size=130):
    bigword(text, t, dur, y=640, size=min(size, 110))


def parole(stn, t_cam, ref_txt, ref_t, verse_html, t_text, marks, size=44):
    """Séquence « Parole », identique pour chaque verset : bandeau vert, verset en grand à gauche, Bible ouverte à droite."""
    cam(t_cam, stn)
    title(stn, ["La [Parole]"], t_cam + 0.1, "Ce que dit la Bible", hl_t=ref_t, size=84)
    tag(stn, 80, 350, ref_txt, ref_t, "acc", 46)
    sfx("spark", ref_t, 1.6)
    v = put(stn, 80, 450, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.25">{verse_html}</div>', "headline", "width:880px")
    blur_in(v, t_text - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', mt)
    sticker(stn, "pupitre-parole", 1080, 260, 420, ref_t + 0.2, rot=2)
    sticker(stn, "livre-croix-ouvert", 1500, 520, 330, t_text + 0.4, rot=-3)
    ref(stn, 80, 830, ref_txt.upper() + " · LSG 1910", ref_t + 0.4)
    return v


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


# ================================================================ STORY
# 01 · Constat ---------------------------------------------------------------------------------------------------------
S = nxt(0.0)
sticker(S, "baton-insomnie", 1060, 260, 560, 0.0, rot=-2, instant=True)
title(S, ["Trois heures", "du [matin]"], 0.0, "La nuit du stress", hl_t=1.2, size=96)
sticker(S, "reveil-nuit", 220, 520, 250, 0.6, rot=-5)
tag(S, 80, 800, "Les mêmes chiffres tournent en boucle", 3.6, "acc", 38)
bw("3 h", 0.6, 0.8, 170)
hit(1.0, 0.8)

S = nxt(6.0)
title(S, ["Le loyer, la facture,", "le [découvert]"], 6.0, "Dans ta tête", hl_t=8.6, size=80)
sticker(S, "pile-factures", 1150, 300, 520, 6.3, rot=3)
tag(S, 80, 420, "Le loyer", 6.4, "", 44)
tag(S, 80, 520, "La facture", 7.4, "", 44)
tag(S, 80, 620, "Le découvert", 8.5, "acc", 44)
sticker(S, "maison-simple", 620, 420, 260, 6.5, rot=-3)
hit(8.6, 0.8)

S = nxt(9.5)
title(S, ["Tu as prié…", "le nœud est [toujours là]"], 9.6, "Et pourtant", hl_t=12.4, size=80)
sticker(S, "baton-priere", 300, 380, 260, 9.8, rot=-2)
n3, _ = sticker(S, "baton-nuage", 1250, 220, 300, 11.6, rot=2)
shake(n3, 12.6)

S = nxt(13.3)
title(S, ["Tu n'es [pas seul]"], 13.4, "Si tu te reconnais", hl_t=14.8, size=96)
sticker(S, "baton-ami", 1150, 260, 520, 13.8, rot=-2)
tag(S, 80, 420, "Beaucoup de chrétiens sincères", 15.6, "acc", 40)
tag(S, 80, 520, "vivent le stress financier", 16.6, "", 40)
hit(15.6, 0.6)

S = nxt(18.5)
title(S, ["Aimer Dieu…", "et se sentir [écrasé]"], 18.6, "Les deux à la fois", hl_t=21.8, size=88)
sticker(S, "livre-croix-ferme", 300, 400, 330, 19.4, rot=-4)
f5, _ = sticker(S, "baton-fardeau", 1150, 260, 560, 21.2, rot=2)
shake(f5, 22.0)
hit(21.9, 0.8)

S = nxt(22.7)
title(S, ["Ce n'est pas un", "[manque de foi]"], 22.8, "Retiens bien", hl_t=23.6, size=92)
sticker(S, "baton-soucieux", 1350, 240, 300, 23.0, rot=-2)
tag(S, 80, 470, "C'est un poids", 24.6, "", 42)
tag(S, 80, 570, "qui n'est pas fait pour être porté seul", 26.4, "acc", 40)
bw("Pas un manque de foi", 23.2, 1.2, 96)

S = nxt(28.6)
title(S, ["Un chemin vers", "la [paix]"], 28.7, "Spirituel et concret", hl_t=31.6, size=96)
sticker(S, "baton-chemin", 1400, 300, 420, 29.0, rot=-2)
boxes(S, 80, 560, ["1", "2", "3", "4"], 32.7, step=310, small="Étape", gap=0.25)
hit(33.4, 0.8)

# 02 · Parole ----------------------------------------------------------------------------------------------------------
S = nxt(34.3)
title(S, ["Ce que dit", "la [Bible]"], 34.4, "Mais d'abord", hl_t=35.9, size=96)
sticker(S, "baton-lit-livre", 1250, 240, 330, 34.8, rot=-2)
hit(35.9, 0.6)

S = ST[_n[0]]
_n[0] += 1
verse1 = (f"« Ne vous {m(0, 'inquiétez')} de rien ; mais en toute chose faites connaître vos besoins à Dieu par des prières et des supplications, "
          f"avec des actions de grâces. Et la {m(1, 'paix de Dieu')}, qui surpasse toute intelligence, {m(2, 'gardera')} vos cœurs et vos pensées en Jésus-Christ. »")
parole(S, 36.2, "Philippiens 4.6-7", 36.4, verse1, 38.7, [T("inquiétez"), T("surpasse") - 0.6, T("gardera")], size=40)
hit(T("gardera"), 0.6)

S = nxt(52.4)
title(S, ["La paix [avant]", "la solution"], 52.5, "Remarque une chose étonnante", hl_t=58.6, size=92)
sticker(S, "nuage-orage", 1100, 260, 330, 54.0, rot=-3)
sticker(S, "colombe", 1460, 420, 330, 57.8, rot=4)
tag(S, 80, 440, "« Quand tout sera réglé » ?", 54.2, "", 40)
tag(S, 80, 540, "Non : pendant que les problèmes sont là", 57.8, "acc", 38)
bw("Pendant", T("pendant"), 0.8, 150)

S = nxt(61.7)
title(S, ["Cette vérité", "change [tout]"], 61.8, "Le stress financier", hl_t=63.2, size=96)
sticker(S, "soleil-nuage", 1150, 260, 420, 62.2, rot=-2)
sticker(S, "baton-serein", 1550, 320, 260, 63.0, rot=2)
hit(63.2, 0.8)

S = nxt(65.7)
title(S, ["Si cette vidéo", "t'[aide]…"], 65.8, "Un instant", hl_t=66.6, size=96)
tag(S, 80, 470, "Abonne-toi", 67.6, "acc", 72)
tag(S, 80, 600, "Chaque semaine, un principe biblique simple", 69.9, "", 38)
sticker(S, "croix-verte", 1200, 280, 260, 66.0, rot=-3)
sticker(S, "baton-lit-livre", 1520, 300, 300, 66.4, rot=2)
bw("Abonne-toi", 67.6, 1.0, 130)

# 03 · Étapes 1 et 2 ---------------------------------------------------------------------------------------------------
S = nxt(73.2)
title(S, ["Comment faire", "[concrètement] ?"], 73.3, "Alors", hl_t=74.4, size=96)
sticker(S, "baton-pense", 1450, 240, 300, 73.5, rot=-2)
boxes(S, 80, 560, ["1", "2", "3", "4"], 74.0, step=310, small="Étape", gap=0.2)

S = nxt(75.4)
title(S, ["Regarde la réalité", "en [face]"], 75.5, "Étape 1", hl_t=77.4, size=88)
sticker(S, "baton-factures", 1150, 260, 480, 75.8, rot=-2)
sticker(S, "nuage-orage", 300, 480, 280, 78.4, rot=3)
tag(S, 80, 800, "Le stress grandit dans le flou", 78.4, "acc", 38)

S = nxt(80.3)
title(S, ["Dans ta tête,", "tout paraît [immense]"], 80.4, "Le flou", hl_t=83.6, size=88)
p14, _ = sticker(S, "pile-factures", 1100, 300, 560, 80.8, rot=2)
sticker(S, "baton-telephone", 400, 420, 220, 81.5, rot=-3)
bump(p14, 83.6, 1.15)
hit(83.7, 0.7)

S = nxt(84.7)
title(S, ["Prends une feuille,", "écris [tout]"], 84.8, "Concrètement", hl_t=86.0, size=88)
sticker(S, "baton-ecrit-liste", 1150, 260, 480, 85.0, rot=-2)
tag(S, 80, 450, "Ce que tu dois", 86.5, "", 42)
tag(S, 80, 550, "À qui", 87.5, "", 42)
tag(S, 80, 650, "Pour quand", 88.4, "acc", 42)
sticker(S, "feuille-liste", 620, 430, 240, 86.6, rot=4)

S = nxt(89.6)
title(S, ["Un problème [nommé]", "fait moins peur"], 89.7, "Ce n'est pas facile", hl_t=92.0, size=84)
sticker(S, "feuille-liste", 1100, 300, 330, 90.0, rot=-3)
sticker(S, "soleil-nuage", 1480, 360, 330, 92.2, rot=3)
tag(S, 80, 520, "qu'un problème caché", 93.4, "acc", 42)
hit(92.1, 0.7)

S = nxt(94.5)
title(S, ["Remets ce poids", "à [Dieu]"], 94.6, "Étape 2", hl_t=96.2, size=96)
f17, _ = sticker(S, "baton-fardeau", 1050, 280, 440, 94.8, rot=-2)
sticker(S, "baton-pose-fardeau", 1500, 280, 330, 97.0, rot=2)
tag(S, 80, 600, "De façon concrète", 97.2, "acc", 44)
hit(96.3, 0.8)

S = ST[_n[0]]
_n[0] += 1
verse2 = f"« {m(0, 'Déchargez-vous')} sur lui de tous vos soucis, car lui-même {m(1, 'prend soin de vous')}. »"
parole(S, 98.5, "1 Pierre 5.7", 98.7, verse2, 101.3, [101.4, 103.6], size=56)
hit(104.5, 0.6)

S = nxt(105.4)
title(S, ["Prie avec ta [feuille]"], 105.5, "Concrètement", hl_t=106.4, size=92)
sticker(S, "baton-priere", 1250, 260, 320, 105.6, rot=-2)
sticker(S, "feuille-liste", 1600, 420, 230, 106.2, rot=4)
tag(S, 80, 440, "Nomme chaque dette", 108.4, "", 42)
tag(S, 80, 540, "chaque facture, devant Dieu", 109.6, "acc", 40)

S = nxt(112.1)
title(S, ["La prière change", "le [cœur]"], 112.2, "Pas le plan, mais le cœur", hl_t=114.6, size=92)
sticker(S, "croix-verte", 1150, 260, 260, 112.4, rot=-3)
sticker(S, "baton-serein", 1500, 300, 280, 113.4, rot=2)
tag(S, 80, 480, "Elle ne remplace pas le plan", 112.6, "", 40)
hit(114.7, 0.7)

# 04 · Étapes 3 et 4 ---------------------------------------------------------------------------------------------------
S = nxt(116.4)
title(S, ["Ne règle pas toute", "ta vie [ce soir]"], 116.5, "Étape 3", hl_t=119.2, size=84)
sticker(S, "reveil-nuit", 1150, 280, 300, 116.8, rot=-3)
sticker(S, "baton-soucieux", 1550, 280, 280, 118.0, rot=2)

S = ST[_n[0]]
_n[0] += 1
verse3 = (f"« Ne vous inquiétez donc pas du {m(0, 'lendemain')} ; car le lendemain aura soin de lui-même. "
          f"À {m(1, 'chaque jour')} suffit sa peine. »")
parole(S, 120.2, "Matthieu 6.34", 120.4, verse3, 122.7, [T("lendemain"), T("chaque", 1)], size=50)
hit(127.8, 0.6)

S = nxt(128.7)
title(S, ["L'erreur la plus", "[courante]"], 128.8, "Mais attention", hl_t=130.6, size=92)
t23, _ = sticker(S, "baton-tiraille", 1150, 300, 520, 129.0, rot=-2)
tag(S, 80, 470, "Tout résoudre d'un coup…", 132.0, "", 40)
tag(S, 80, 570, "… et abandonner", 134.0, "acc", 40)
shake(t23, 133.8)
hit(134.2, 0.8)

S = nxt(135.1)
title(S, ["Une seule action", "[aujourd'hui]"], 135.2, "Choisis", hl_t=137.0, size=92)
sticker(S, "baton-telephone-calme", 1450, 240, 260, 137.5, rot=-2)
tag(S, 80, 420, "Appeler un créancier", 137.6, "", 40)
tag(S, 80, 520, "Annuler un abonnement", 139.0, "", 40)
tag(S, 80, 620, "Mettre de côté quelques euros", 140.4, "acc", 40)
coins(S, 1000, 700, 141.0, n=5, spread=300, size=70)

S = nxt(142.0)
title(S, ["Une petite [action]", "aujourd'hui"], 142.1, "Vaut mieux", hl_t=143.2, size=92)
sticker(S, "baton-chemin", 1150, 280, 520, 142.4, rot=-2)
tag(S, 80, 520, "qu'un grand plan jamais commencé", 144.6, "acc", 40)
bw("Une petite action", 143.0, 1.1, 110)

S = nxt(147.1)
title(S, ["Ne porte pas", "ce poids [seul]"], 147.2, "Étape 4", hl_t=149.6, size=96)
sticker(S, "baton-fardeau", 1050, 300, 420, 147.4, rot=-2)
sticker(S, "baton-ami", 1460, 280, 420, 149.0, rot=2)
hit(149.7, 0.8)

S = ST[_n[0]]
_n[0] += 1
verse4 = f"« {m(0, 'Portez les fardeaux')} les uns des autres. »"
parole(S, 150.4, "Galates 6.2", 150.6, verse4, 152.4, [152.6], size=72)

S = nxt(154.5)
title(S, ["Le silence nourrit", "la [honte]"], 154.6, "Et la honte nourrit le stress", hl_t=156.0, size=88)
sticker(S, "nuage-orage", 1150, 260, 330, 154.8, rot=-3)
sticker(S, "baton-soucieux", 1550, 300, 260, 156.4, rot=2)

S = nxt(158.6)
title(S, ["[Parles-en]"], 158.7, "À quelqu'un de confiance", hl_t=158.9, size=110)
sticker(S, "baton-ami", 1150, 260, 500, 158.9, rot=-2)
tag(S, 80, 380, "Ton conjoint", 159.4, "", 40)
tag(S, 80, 470, "Un ami de confiance", 160.2, "", 40)
tag(S, 80, 560, "Ton pasteur", 161.4, "", 40)
tag(S, 80, 650, "Un conseiller en budget", 162.2, "acc", 40)

S = nxt(163.7)
title(S, ["Et ta [santé]"], 163.8, "Si l'angoisse dure", hl_t=168.8, size=110)
sticker(S, "baton-insomnie", 1150, 300, 480, 164.0, rot=-2)
tag(S, 80, 440, "Parles-en aussi à un médecin", 166.6, "acc", 40)
tag(S, 80, 540, "Prendre soin de toi, c'est aussi la sagesse", 168.2, "", 36)

# 05 · Exemple ---------------------------------------------------------------------------------------------------------
S = nxt(171.0)
title(S, ["Un exemple :", "[Marc]"], 171.1, "Prenons", hl_t=172.3, size=96)
sticker(S, "baton-insomnie", 1150, 300, 480, 172.2, rot=-2)
tag(S, 80, 480, "Trois crédits", 172.9, "", 42)
tag(S, 80, 580, "Un découvert chaque nuit", 173.8, "acc", 40)

S = nxt(175.4)
title(S, ["Il a [écrit],", "puis prié"], 175.5, "Un soir", hl_t=177.0, size=96)
sticker(S, "baton-ecrit-liste", 1050, 280, 420, 175.8, rot=-2)
sticker(S, "baton-priere", 1520, 300, 260, 177.6, rot=2)

S = nxt(179.6)
title(S, ["Il a appelé", "sa [banque]"], 179.7, "Le lendemain", hl_t=180.8, size=96)
sticker(S, "baton-telephone-calme", 1450, 260, 260, 179.9, rot=-2)
sticker(S, "pile-factures", 1000, 420, 330, 181.0, rot=3)
tag(S, 80, 480, "Étaler un remboursement", 181.4, "acc", 40)

S = nxt(182.9)
title(S, ["Il a [dormi]"], 183.0, "Les dettes n'ont pas disparu en un jour", hl_t=187.2, size=110)
sticker(S, "baton-dort", 1100, 280, 520, 185.2, rot=-2)
sticker(S, "colombe", 400, 460, 280, 186.8, rot=4)
bw("Il a dormi", 186.9, 1.0, 130)

# 06 · Action ----------------------------------------------------------------------------------------------------------
S = nxt(188.0)
title(S, ["La paix commence", "par le [premier pas]"], 188.1, "Tu vois", hl_t=194.6, size=88)
sticker(S, "baton-pose-fardeau", 1050, 280, 400, 190.8, rot=-2)
sticker(S, "colombe", 1500, 300, 300, 192.6, rot=4)
tag(S, 80, 520, "Confie à Dieu ce que tu portes seul", 191.6, "acc", 38)

S = nxt(196.0)
title(S, ["[Ce soir]"], 196.1, "À toi", hl_t=196.8, size=120)
tag(S, 80, 420, "1 · Écris", 197.4, "", 48)
tag(S, 80, 530, "2 · Prie", 198.4, "", 48)
tag(S, 80, 640, "3 · Une action pour demain", 199.4, "acc", 48)
sticker(S, "feuille-liste", 1150, 300, 300, 197.8, rot=-3)
sticker(S, "baton-priere", 1520, 280, 280, 198.6, rot=2)

S = nxt(202.1)
title(S, ["Un jour", "à la [fois]"], 202.2, "Dieu ne te demande pas de tout porter", hl_t=206.6, size=110)
sticker(S, "baton-chemin", 1100, 300, 500, 202.4, rot=-2)
sticker(S, "croix-verte", 600, 420, 200, 204.2, rot=3)
hit(206.7, 0.8)

S = nxt(207.3)
title(S, ["Ta [première étape]", "cette semaine ?"], 207.4, "Et toi", hl_t=209.2, size=92)
sticker(S, "baton-pense", 1450, 240, 300, 207.6, rot=-2)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 210.9, 14)
sfx("click", 210.9, 0.8)
tag(S, 80, 620, "Abonne-toi", 214.1, "acc", 56)

cam(217.6, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Constat", 0, 34.3), ("02", "Parole", 34.3, 73.2), ("03", "Étapes 1-2", 73.2, 116.4),
              ("04", "Étapes 3-4", 116.4, 171.0), ("05", "Exemple", 171.0, 196.0), ("06", "Action", 196.0, DUR)],
    suppress=[(38.6, 52.4), (101.2, 105.4), (122.6, 128.7), (151.2, 154.5), (218.4, DUR)],   # versets affichés, carte de fin
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=218.6,
)

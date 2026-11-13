"""Vidéo longue « Comment s'enrichir sans perdre la foi » — style 02 en 16:9, ~9 min 20.
5 passages (séquence « Parole » identique), 3 questions à retenir, appel à s'abonner au milieu, 5 garde-fous, exemple (Élise), récapitulatif.
Les temps sont lus dans transcript.json (voix fournie par l'utilisateur, passage inventé par la synthèse vocale retiré).

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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Comment s'enrichir sans perdre la foi", "lang": "fr"}
COLS, ROWS = 10, 9
VOICE_END = 545.7
s.setup(here=HERE, duration=561.0, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
_n = [0]
SUP = []
_TR = json.load(open(os.path.join(HERE, "transcript.json"), encoding="utf-8"))


def _norm(x):
    return re.sub(r"[^\w]+", "", unicodedata.normalize("NFC", x.lower()))


def W(prefix, after=0.0, nth=0):
    """Début (en secondes) du n-ième mot commençant par `prefix`, après l'instant `after`."""
    k = 0
    for w in _TR:
        if w["start"] >= after and _norm(prefix) in _norm(w["text"]):
            if k == nth:
                return round(w["start"], 2)
            k += 1
    raise KeyError(prefix)


def nxt(t):
    stn = ST[_n[0]]
    _n[0] += 1
    cam(t, stn)
    return stn


def title(stn, lines, t, kicker, hl=None, size=80):
    size = min(size, 78 if len(lines) > 1 else 96)
    return headline(stn, 172, lines, t, kicker=kicker, hl_t=hl, size=size, x=80)


def stk(stn, name, px, py, w, t, rot=-2):
    return sticker(stn, name, px, py, w, t, rot=rot)


def tg(stn, y, text, t, cls="", size=40):
    return tag(stn, 80, y, text, t, cls, size)


def bw(text, t, dur=0.9, size=110):
    bigword(text, t, dur, y=720, size=size)


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


def parole(t_cam, ref_txt, t_ref, verse_html, t_text, t_end, marks, size=44, ref_y=830, ref_label=None):
    """Séquence « Parole », identique pour chaque passage ; sous-titres coupés pendant la citation."""
    verse_html = verse_html.replace(" »", "&nbsp;»").replace("« ", "«&nbsp;").replace(" ;", "&nbsp;;").replace(" :", "&nbsp;:")
    stn = nxt(t_cam)
    title(stn, ["La [Parole]"], t_cam + 0.1, "Ce que dit la Bible", hl=t_ref, size=84)
    tag(stn, 80, 350, ref_txt, t_ref, "acc", 46)
    sfx("spark", t_ref, 1.6)
    v = put(stn, 80, 450, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.25">{verse_html}</div>', "headline", "width:880px")
    blur_in(v, t_text - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', mt)
    sticker(stn, "pupitre-parole", 1080, 260, 420, min(t_ref + 0.2, t_cam + 0.6), rot=2)
    sticker(stn, "livre-croix-ouvert", 1500, 520, 330, t_text + 0.4, rot=-3)
    ref(stn, 80, ref_y, (ref_label or ref_txt.upper()) + " · LSG 1910", t_ref + 0.4)
    SUP.append((t_text - 0.1, t_end))
    return stn


# ================================================================ 01 · Introduction
S = nxt(0.0)
stk(S, "baton-possede", 1040, 260, 440, 0.0, rot=-2)
title(S, ["Rester fidèle…", "en s'[enrichissant]"], 0.0, "Une peur courante", hl=4.6, size=84)
tg(S, 430, "En vouloir plus…", 2.4, "acc", 40)
bw("C'est mal ?", 3.4, 1.0, 110)

S = nxt(5.5)
title(S, ["Un [frein]", "dans la tête"], 5.6, "Beaucoup de chrétiens", hl=7.0)
stk(S, "baton-soucieux", 1180, 240, 280, 5.9)
tg(S, 450, "S'éloigner de Dieu ?", 9.0, "acc", 40)

S = nxt(11.0)
title(S, ["Rester [pauvre]", "pour rester fidèle ?"], 11.1, "Certains en concluent", hl=12.0, size=72)
stk(S, "baton-fardeau", 1150, 250, 320, 11.4)
tg(S, 450, "La fausse solution", 13.0, "acc", 38)

S = nxt(14.1)
title(S, ["Foncer, et", "[oublier]"], 14.2, "D'autres", hl=16.6)
stk(S, "baton-travaille", 1150, 250, 340, 14.5)
tg(S, 450, "Oublier pourquoi on a commencé", 15.6, "acc", 34)

S = nxt(17.8)
title(S, ["S'enrichir sans", "perdre la [foi] ?"], 17.9, "La question", hl=19.6)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 18.2, rot=-3)
stk(S, "croix-verte", 1560, 320, 220, 19.4, rot=4)
hit(19.7, 0.8)

S = nxt(20.9)
title(S, ["Au [programme]"], 21.0, "Dans cette vidéo", hl=21.6)
tg(S, 420, "5 passages de la Bible", 23.0, "", 40)
tg(S, 510, "5 garde-fous concrets", 25.0, "", 40)
tg(S, 600, "Un exemple pour tout appliquer", 27.0, "acc", 38)
stk(S, "pupitre-parole", 1100, 260, 380, 22.0, rot=-2)

S = nxt(29.0)
title(S, ["Un test en", "trois [questions]"], 29.1, "Reste jusqu'à la fin", hl=31.0)
counter(S, 80, 440, 0, 3, 30.4, 0.8, " questions", 120)
tg(S, 600, "À chaque hausse de revenu", 31.8, "acc", 38)
stk(S, "baton-test-trois", 1150, 240, 330, 29.6)

S = nxt(33.9)
title(S, ["Aucune [promesse]", "de richesse"], 34.0, "Une précision importante", hl=36.6)
tg(S, 450, "Pas de formule magique", 40.0, "", 40)
tg(S, 540, "Garder ton cœur", 42.0, "acc", 44)
stk(S, "coeur-receptacle", 1150, 300, 340, 40.5, rot=-3)
stk(S, "baton-priere", 1500, 280, 260, 34.6, rot=3)
hit(36.7, 0.8)

# ================================================================ 02 · Passage 1 : 1 Timothée 6.10
parole(45.8, "1 Timothée 6.10", 48.6,
       f"« Car {m(0, 'l’amour de l’argent')} est la racine de tous les maux ; et quelques-uns, en étant possédés, se sont "
       f"{m(1, 'égarés loin de la foi')}, et se sont jeté eux-mêmes dans bien des tourments. »",
       50.5, 59.6, [W("amour", 50.0), W("égarés", 50.0)], size=44)

S = nxt(59.6)
title(S, ["Pas l'argent,", "l'[amour] de l'argent"], 59.7, "Remarque bien", hl=64.0, size=72)
tg(S, 450, "Pas l'argent", 61.3, "", 40)
tg(S, 540, "L'amour de l'argent", 63.9, "acc", 40)
stk(S, "piedestal-pieces", 1050, 300, 360, 60.3, rot=-2)
stk(S, "coeur-fil-tresor", 1480, 420, 340, 64.0, rot=3)

S = nxt(65.8)
title(S, ["L'argent,", "un [outil]"], 65.9, "La différence", hl=67.1, size=90)
stk(S, "baton-budget", 1050, 250, 380, 66.0)
stk(S, "baton-possede", 1500, 330, 380, 69.6, rot=3)
tg(S, 450, "Le piège : être possédé", 70.0, "acc", 38)

S = nxt(72.1)
title(S, ["Égarés loin", "de la [foi]"], 72.2, "La conséquence", hl=73.0)
stk(S, "livre-croix-ferme", 1100, 300, 360, 72.8, rot=-3)
tg(S, 470, "Le danger : la place dans le cœur", 76.0, "acc", 34)
hit(78.0, 0.8)

S = nxt(80.2)
title(S, ["Riches…", "et [fidèles]"], 80.3, "Abraham, Job, Joseph", hl=85.5, size=96)
tg(S, 440, "Abraham", 80.8, "", 40)
tg(S, 520, "Job", 82.2, "", 40)
tg(S, 600, "Joseph", 83.4, "acc", 40)
stk(S, "baton-priere", 1100, 260, 280, 81.0)
stk(S, "colombe", 1480, 380, 300, 85.0, rot=4)

S = nxt(87.7)
title(S, ["Pas la richesse,", "la [possession]"], 87.8, "La Bible n'interdit pas", hl=89.6, size=78)
stk(S, "baton-possede", 1050, 280, 420, 88.8)
stk(S, "croix-verte", 1560, 340, 220, 90.0, rot=4)
hit(90.3, 0.8)

S = nxt(92.4)
title(S, ["Et si tu perdais", "la [moitié] ?"], 92.5, "Un petit test", hl=94.8)
stk(S, "baton-pense", 1150, 230, 260, 92.9)
stk(S, "piles-croissantes", 1520, 440, 330, 95.0, rot=-2)

S = nxt(98.2)
title(S, ["La [panique]", "totale ?"], 98.3, "Un signe d'alerte", hl=99.5)
stk(S, "baton-fardeau", 1150, 250, 320, 99.0)
tg(S, 470, "Ton argent te possède déjà ?", 100.5, "acc", 36)

S = nxt(102.8)
title(S, ["Possèdes-[tu]", "ton argent ?"], 102.9, "Question 1", hl=103.8)
tg(S, 450, "Possèdes-tu ton argent…", 103.4, "", 38)
tg(S, 540, "… ou te possède-t-il ?", 105.8, "acc", 38)
stk(S, "baton-test-trois", 1350, 230, 300, 104.2)
bw("Question 1", 103.1, 0.9, 100)

# ================================================================ 03 · Passage 2 : Deutéronome 8.17-18
parole(108.3, "Deutéronome 8.17-18", 111.8,
       f"« Garde-toi de dire en ton cœur : {m(0, 'Ma force et la puissance de ma main')} m'ont acquis ces richesses. "
       f"{m(1, 'Souviens-toi de l’Éternel')}, ton Dieu ; car c'est lui qui te donne de la force pour acquérir ces richesses. »",
       118.7, 128.9, [W("force", 118.5), W("souviens", 118.0)], size=42, ref_y=980, ref_label="DEUTÉRONOME 8.17-18")

S = nxt(129.0)
title(S, ["« Je me suis", "fait tout [seul] »"], 129.1, "L'orgueil", hl=131.0, size=78)
stk(S, "baton-fier", 1300, 230, 280, 129.5)
bw("Tout seul ?", 131.4, 0.9, 110)

S = nxt(132.7)
title(S, ["Le travail est", "[honoré]"], 132.8, "Bien sûr", hl=135.6)
stk(S, "baton-travaille", 1050, 250, 340, 133.0)
stk(S, "mallette-travail", 1500, 400, 260, 135.0, rot=3)
tg(S, 480, "Travailler, planifier, se sacrifier", 134.2, "", 34)

S = nxt(138.0)
title(S, ["Tout est [reçu]"], 138.1, "Moïse rappelle", hl=139.8)
tg(S, 420, "La santé", 139.0, "", 38)
tg(S, 510, "Les occasions", 140.4, "", 38)
tg(S, 600, "Les talents", 141.8, "", 38)
tg(S, 690, "La force de travailler", 143.0, "acc", 38)
stk(S, "baton-merci-argent", 1100, 250, 380, 139.0)

S = nxt(144.0)
title(S, ["Même le meilleur", "plan [dépend]"], 144.1, "Un entrepreneur honnête", hl=147.0, size=72)
stk(S, "baton-budget", 1100, 250, 380, 144.6)
stk(S, "soleil-nuage", 1520, 430, 300, 149.0, rot=3)
tg(S, 480, "Sans le bon moment…", 149.0, "acc", 38)

S = nxt(150.7)
title(S, ["La réussite", "devient un [piège]"], 150.8, "Quand on l'oublie", hl=153.0, size=78)
tg(S, 470, "On se croit supérieur", 153.6, "", 38)
tg(S, 560, "On compte sur soi seul", 155.6, "", 38)
tg(S, 650, "On ne prie plus", 157.0, "acc", 38)
stk(S, "tour-pieces-bascule", 1100, 270, 340, 152.0, rot=-2)

S = nxt(158.0)
title(S, ["Remercies-tu", "encore [Dieu] ?"], 158.1, "Question 2", hl=159.4)
stk(S, "baton-merci-argent", 1100, 250, 380, 158.4)
bw("Question 2", 158.3, 0.9, 100)

S = nxt(161.6)
title(S, ["Dis [merci]", "avant de dépenser"], 161.7, "Concrètement", hl=162.8, size=78)
tg(S, 450, "Une augmentation", 165.4, "", 38)
tg(S, 540, "Un contrat", 166.8, "", 38)
tg(S, 630, "Une prime", 168.0, "", 38)
tg(S, 720, "Dis merci d'abord", 169.2, "acc", 40)
stk(S, "baton-priere", 1100, 260, 300, 162.0)
stk(S, "carnet-gratitude", 1480, 440, 330, 164.0, rot=3)

# ================================================================ 04 · Passage 3 : Proverbes 30.8-9
parole(170.7, "Proverbes 30.8-9", 172.8,
       f"« Ne me donne {m(0, 'ni pauvreté, ni richesse')}, accorde-moi le pain qui m'est nécessaire, de peur que, dans l'abondance, "
       f"je ne te renie, et ne dise : Qui est l'Éternel ? ou que, dans la pauvreté, je ne dérobe, et ne profane le nom de mon Dieu. »",
       176.1, 189.3, [W("ni", 176.0), W("abondance", 176.0)], size=38, ref_y=980)

S = nxt(189.4)
title(S, ["Deux [dangers]"], 189.5, "Cet homme voit", hl=190.2)
tg(S, 420, "Abondance : renier Dieu", 191.2, "", 38)
tg(S, 510, "Manque : être tenté de tricher", 194.0, "acc", 36)
stk(S, "balance-peu-paix", 1100, 270, 430, 190.0, rot=-2)

S = nxt(196.8)
title(S, ["La pauvreté,", "un [risque] aussi"], 196.9, "Remarque", hl=198.1, size=78)
tg(S, 470, "La Bible ne glorifie pas le manque", 198.6, "acc", 32)
stk(S, "baton-soucieux", 1150, 240, 280, 197.0)

S = nxt(201.4)
title(S, ["Pas un chiffre,", "un [réflexe]"], 201.5, "Ce passage", hl=203.0, size=78)
stk(S, "boussole", 1100, 300, 330, 202.0, rot=-3)
tg(S, 470, "Apprendre à te surveiller", 204.0, "acc", 38)

S = nxt(206.6)
title(S, ["Quelle est ta", "[tentation] ?"], 206.7, "À chaque étape", hl=208.4)
stk(S, "baton-pense", 1150, 230, 260, 207.0)
stk(S, "calendrier-mois", 1520, 430, 300, 209.0, rot=3)

S = nxt(210.7)
title(S, ["Peu ou", "[beaucoup]"], 210.8, "Deux tentations", hl=211.8)
tg(S, 430, "Peu : l'inquiétude", 212.4, "", 38)
tg(S, 520, "ou la malhonnêteté", 214.0, "", 38)
tg(S, 610, "Beaucoup : se passer de Dieu", 216.0, "acc", 34)
stk(S, "seau-perce", 1100, 270, 260, 211.0, rot=-3)
stk(S, "piedestal-pieces", 1480, 360, 330, 216.0, rot=3)

S = nxt(217.7)
title(S, ["La [question]", "qui protège"], 217.8, "Régulièrement", hl=218.8)
stk(S, "baton-test-trois", 1150, 240, 330, 218.2)
tg(S, 470, "À chaque niveau de revenu", 220.0, "acc", 38)

S = nxt(222.3)
title(S, ["Si cette vidéo", "t'[aide]…"], 222.4, "Un instant", hl=223.4)
tg(S, 470, "Abonne-toi", 224.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", 227.0, "", 36)
stk(S, "croix-verte", 1200, 280, 260, 222.8, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 223.2, rot=2)
bw("Abonne-toi", 224.2, 1.0)

# ================================================================ 05 · Passage 4 : Matthieu 6.19-21
parole(232.1, "Matthieu 6.19-21", 236.8,
       f"« Ne vous amassez pas des trésors sur la terre, où la teigne et la rouille détruisent, et où les voleurs percent et dérobent ; "
       f"mais {m(0, 'amassez-vous des trésors dans le ciel')}, où la teigne et la rouille ne détruisent point, et où les voleurs ne percent ni ne dérobent ; "
       f"car {m(1, 'là où est ton trésor, là aussi sera ton cœur')}. »",
       239.2, 256.2, [W("amassez-vous", 240.0), W("car", 245.0)], size=36, ref_y=1000)

S = nxt(256.3)
title(S, ["Posséder,", "pas [amasser]"], 256.4, "Jésus ne dit pas", hl=258.0, size=84)
tg(S, 450, "Pas : ne rien posséder", 258.4, "", 38)
tg(S, 540, "Amasser comme but, comme sécurité", 262.4, "acc", 34)
stk(S, "tresor-terre", 1050, 260, 440, 256.8, rot=-2)

S = nxt(264.6)
title(S, ["Ton [cœur]", "suit ton trésor"], 264.7, "Le point clé", hl=265.5, size=84)
stk(S, "coeur-fil-tresor", 1040, 330, 540, 265.0)
bw("Pas l'inverse", 267.2, 1.0, 100)

S = nxt(268.9)
title(S, ["Tes [dépenses]", "des 3 derniers mois"], 269.0, "Regarde", hl=270.0, size=72)
stk(S, "baton-ecrit-liste", 1100, 250, 360, 269.5)
stk(S, "enveloppes-budget", 1520, 440, 320, 272.0, rot=3)
tg(S, 480, "Qu'est-ce qui revient le plus ?", 271.8, "acc", 34)

S = nxt(274.8)
title(S, ["Un exercice", "[simple]"], 274.9, "Écris deux listes", hl=276.0)
tg(S, 420, "3 dépenses faites volontiers", 277.4, "", 36)
tg(S, 510, "3 causes à soutenir", 280.0, "", 36)
tg(S, 600, "L'écart = ce qu'il faut ajuster", 282.8, "acc", 34)
stk(S, "carnet-gratitude", 1100, 300, 420, 276.5, rot=-2)

S = nxt(284.4)
title(S, ["Investir dans", "ce qui [dure]"], 284.5, "Amasser dans le ciel", hl=287.2)
tg(S, 450, "Des personnes", 287.6, "", 38)
tg(S, 540, "Des œuvres de bien", 288.8, "", 38)
tg(S, 630, "Ton église", 290.0, "", 38)
tg(S, 720, "L'éternité", 291.0, "acc", 40)
stk(S, "tresor-ciel", 1100, 260, 420, 285.0, rot=2)

S = nxt(292.4)
title(S, ["Patrimoine", "[et] ciel"], 292.5, "Les deux ensemble", hl=294.0)
stk(S, "piles-croissantes", 1050, 340, 330, 293.0, rot=-2)
stk(S, "tresor-ciel", 1450, 300, 340, 295.0, rot=3)
tg(S, 470, "Le second passe en premier", 296.0, "acc", 38)

# ================================================================ 06 · Passage 5 : 1 Timothée 6.17-18
parole(299.2, "1 Timothée 6.17-18", 301.0,
       f"« Recommande aux riches du présent siècle de ne pas être orgueilleux, et de ne pas mettre leur espérance dans des richesses incertaines, "
       f"mais de {m(0, 'la mettre en Dieu')}, qui nous donne avec abondance toutes choses pour que nous en jouissions ; de faire du bien, "
       f"d'être riches en bonnes œuvres, {m(1, 'd’avoir de la libéralité, de la générosité')}. »",
       306.8, 324.3, [W("mais", 309.0), W("libéralité", 315.0)], size=36, ref_y=1000, ref_label="1 TIMOTHÉE 6.17-18")

S = nxt(324.4)
title(S, ["Trois", "[consignes]"], 324.5, "Pour les riches", hl=325.2, size=90)
counter(S, 80, 420, 0, 3, 325.0, 0.8, " consignes", 110)
tg(S, 580, "Pas d'orgueil", 326.6, "", 36)
tg(S, 660, "Pas d'espérance dans l'incertain", 328.4, "", 34)
tg(S, 740, "Être généreux", 330.2, "acc", 38)
stk(S, "baton-priere", 1150, 260, 300, 325.2)

S = nxt(332.1)
title(S, ["Pas tout [vendre]"], 332.2, "Remarque", hl=334.0)
tg(S, 440, "Humbles", 335.6, "", 40)
tg(S, 520, "Espérer en Dieu", 337.0, "", 40)
tg(S, 600, "Donner", 338.2, "acc", 40)
stk(S, "baton-donne", 1100, 260, 340, 332.6)

S = nxt(339.0)
title(S, ["Jouir avec", "[reconnaissance]"], 339.1, "Dieu nous donne", hl=341.8, size=78)
stk(S, "famille-sortie", 1050, 280, 560, 340.0)
tg(S, 470, "Profiter n'est pas un péché", 343.0, "acc", 36)

S = nxt(346.1)
title(S, ["Des richesses", "[incertaines]"], 346.2, "La bourse monte et descend", hl=346.6, size=84)
stk(S, "tour-pieces-bascule", 1100, 270, 360, 346.8, rot=-2)
tg(S, 480, "Un emploi peut disparaître", 350.0, "acc", 36)
hit(346.8, 0.8)

S = nxt(353.5)
title(S, ["La [générosité],", "l'antidote"], 353.6, "Le meilleur remède", hl=353.9)
stk(S, "baton-donne", 1050, 250, 420, 354.3)
stk(S, "enveloppe-don", 1500, 430, 300, 357.5, rot=3)
tg(S, 480, "Un outil, pas un maître", 358.0, "acc", 38)

S = nxt(360.9)
title(S, ["Partages-tu", "ce que tu [reçois] ?"], 361.0, "Question 3", hl=363.4, size=78)
stk(S, "couple-don", 1250, 200, 420, 361.8)
bw("Question 3", 361.3, 0.9, 100)

# ================================================================ 07 · Cinq garde-fous
S = nxt(365.3)
title(S, ["Cinq", "[garde-fous]"], 365.4, "Passons à la pratique", hl=365.9)
counter(S, 80, 430, 0, 5, 366.4, 0.9, " garde-fous", 130)
stk(S, "garde-fou-route", 1050, 300, 520, 366.0, rot=-1)

S = nxt(369.5)
title(S, ["Donne en", "[premier]"], 369.6, "Garde-fou 1", hl=370.6)
tg(S, 450, "Avant de dépenser", 372.0, "", 40)
tg(S, 540, "Avant d'épargner", 373.6, "", 40)
tg(S, 630, "Décide ce que tu donnes", 375.2, "acc", 40)
stk(S, "enveloppe-don", 1100, 300, 340, 370.8, rot=-3)
stk(S, "baton-donne", 1500, 260, 330, 372.5, rot=2)

S = nxt(376.6)
title(S, ["Honore", "l'[Éternel]"], 376.7, "Proverbes 3.9", hl=379.0)
quote = put(S, 80, 430, '<div class="h" style="font-size:40px;font-weight:700;line-height:1.25">«&nbsp;Honore l\'Éternel avec tes biens, et avec les prémices de tout ton revenu.&nbsp;»</div>', "headline", "width:880px")
blur_in(quote, 377.4, 16)
ref(S, 80, 680, "PROVERBES 3.9 · LSG 1910", 377.4)
stk(S, "livre-croix-ouvert", 1100, 300, 380, 377.0, rot=-3)

S = nxt(382.6)
title(S, ["Ta conviction,", "ta [situation]"], 382.7, "Le montant dépend", hl=384.0, size=78)
stk(S, "baton-pense", 1150, 230, 260, 383.0)
tg(S, 470, "Mais commence par là", 385.5, "acc", 40)

S = nxt(388.0)
title(S, ["Donner ce qui", "[compte]"], 388.1, "Ton rapport à l'argent", hl=391.6)
tg(S, 450, "Pas ce qui reste", 390.6, "", 40)
tg(S, 540, "D'abord ce qui compte", 392.0, "acc", 40)
stk(S, "coeur-receptacle", 1100, 300, 330, 388.6, rot=-3)

S = nxt(393.4)
title(S, ["Gagne", "[honnêtement]"], 393.5, "Garde-fou 2", hl=394.6)
tg(S, 450, "Pas d'argent facile", 396.0, "", 38)
tg(S, 540, "Pas de raccourcis douteux", 398.5, "", 38)
tg(S, 630, "Pas de petites tromperies", 400.5, "", 38)
tg(S, 720, "La paix se perd", 402.0, "acc", 40)
stk(S, "chaine-cassee", 1100, 300, 380, 395.0, rot=-3)

S = nxt(403.9)
title(S, ["Pourrais-je", "l'[expliquer] ?"], 404.0, "Avant une opportunité", hl=406.4)
stk(S, "baton-pense", 1150, 230, 260, 404.5)
stk(S, "pupitre-parole", 1520, 300, 360, 408.5, rot=3)
tg(S, 470, "Devant mon église, sans gêne ?", 408.0, "acc", 34)

S = nxt(410.9)
title(S, ["Fixe ton", "[assez]"], 411.0, "Garde-fou 3", hl=411.9)
tg(S, 450, "Décide à l'avance", 414.9, "", 40)
tg(S, 540, "Quel niveau te suffit", 416.4, "", 40)
tg(S, 630, "Le surplus : épargner · donner · aider", 419.8, "acc", 32)
stk(S, "baton-ecrit-liste", 1100, 260, 330, 412.0)
stk(S, "baton-epargne", 1500, 330, 300, 419.8, rot=3)

S = nxt(423.1)
title(S, ["Jamais", "[assez] ?"], 423.2, "Le piège classique", hl=425.8)
stk(S, "baton-fardeau", 1150, 250, 320, 423.6)
tg(S, 470, "Gagner plus, sans jamais en avoir assez", 425.0, "acc", 30)

S = nxt(428.6)
title(S, ["Protège tes", "[priorités]"], 428.7, "Garde-fou 4", hl=429.8)
tg(S, 450, "Ta famille", 431.5, "", 40)
tg(S, 540, "Ton temps avec Dieu", 432.8, "", 40)
tg(S, 630, "Ton repos", 434.2, "acc", 40)
tg(S, 720, "Trop cher si ça t'éloigne", 436.5, "", 32)
stk(S, "famille-sortie", 1050, 280, 560, 430.0)

S = nxt(438.3)
title(S, ["Un jour", "de [repos]"], 438.4, "Ne se négocie pas", hl=440.0)
stk(S, "calendrier-repos", 1050, 290, 500, 438.8, rot=-2)
stk(S, "baton-repos", 1520, 330, 380, 440.8, rot=3)

S = nxt(442.1)
title(S, ["Entoure-[toi]"], 442.2, "Garde-fou 5", hl=443.0)
tg(S, 420, "Ton conjoint", 446.8, "", 36)
tg(S, 510, "Un frère ou une sœur mûrs", 448.0, "", 34)
tg(S, 600, "Qui te dit la vérité", 450.0, "acc", 36)
stk(S, "baton-conseillers", 1050, 300, 500, 443.5, rot=-2)

S = nxt(451.7)
title(S, ["Beaucoup de", "[conseillers]"], 451.8, "Proverbes 11.14", hl=453.8)
stk(S, "couple-lit-bible", 1100, 270, 440, 452.0)
tg(S, 480, "Le salut est dans le grand nombre des conseillers", 453.0, "acc", 30)

# ================================================================ 08 · Exemple : Élise
S = nxt(455.6)
title(S, ["Un exemple :", "[Élise]"], 455.7, "Prenons", hl=457.0)
stk(S, "baton-content", 1450, 250, 300, 457.4)
tg(S, 450, "Une petite pâtisserie", 459.0, "acc", 40)
bw("× 3", 461.0, 0.9, 130)

S = nxt(462.2)
title(S, ["Trois", "[tentations]"], 462.3, "Élise est tentée", hl=462.8)
tg(S, 420, "70 heures par semaine", 463.6, "", 38)
tg(S, 510, "Sauter les rencontres de l'église", 465.2, "", 34)
tg(S, 600, "Changer de voiture", 466.6, "acc", 38)
stk(S, "baton-soucieux", 1150, 240, 280, 462.8)

S = nxt(467.8)
title(S, ["Elle applique", "les 5 [garde-fous]"], 467.9, "Alors", hl=469.0, size=78)
stk(S, "garde-fou-route", 1050, 300, 500, 468.0)

S = nxt(470.0)
title(S, ["Donner,", "[refuser]"], 470.1, "Garde-fous 1 et 2", hl=472.4)
tg(S, 450, "Une part à donner", 471.0, "", 40)
tg(S, 540, "Une offre trop belle : refusée", 473.4, "acc", 36)
stk(S, "enveloppe-don", 1100, 300, 330, 470.8, rot=-3)

S = nxt(475.6)
title(S, ["Son [assez],", "son dimanche"], 475.7, "Garde-fous 3 et 4", hl=476.8)
stk(S, "calendrier-repos", 1050, 290, 460, 478.4, rot=-2)
stk(S, "baton-epargne", 1520, 340, 280, 476.0, rot=3)
tg(S, 470, "Le reste : épargner et aider", 477.0, "acc", 34)

S = nxt(481.8)
title(S, ["Une amie de", "[confiance]"], 481.9, "Garde-fou 5", hl=483.0)
stk(S, "baton-conseillers", 1050, 300, 470, 482.2, rot=-2)
tg(S, 470, "Chaque trimestre : ses comptes", 483.6, "acc", 36)

S = nxt(485.2)
title(S, ["Elle sait ce", "qu'elle [protège]"], 485.3, "Demain est incertain", hl=489.0, size=78)
stk(S, "coeur-receptacle", 1050, 300, 340, 485.9, rot=-3)
stk(S, "maison-roc", 1480, 380, 340, 490.5, rot=3)
tg(S, 470, "Son cœur", 490.5, "acc", 42)

S = nxt(491.9)
title(S, ["Un [exemple],", "pas une garantie"], 492.0, "À retenir", hl=493.0, size=78)
tg(S, 470, "Aucun résultat garanti", 493.6, "acc", 38)
tg(S, 560, "Valable pour chacun", 495.6, "", 38)
stk(S, "colombe", 1100, 300, 300, 494.0, rot=3)

# ================================================================ 09 · Récapitulatif et action
S = nxt(497.2)
title(S, ["L'[essentiel]"], 497.3, "Retenons", hl=497.9)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 497.6, rot=-3)

S = nxt(498.6)
title(S, ["Contre l'amour", "de l'[argent]"], 498.7, "La Bible met en garde", hl=501.9, size=78)
tg(S, 450, "L'amour de l'argent", 501.8, "", 38)
tg(S, 540, "L'orgueil", 503.4, "", 38)
tg(S, 630, "La fausse sécurité", 504.4, "", 38)
tg(S, 720, "L'oubli de Dieu", 505.6, "acc", 38)
stk(S, "baton-possede", 1100, 280, 380, 499.2)

S = nxt(506.6)
title(S, ["Trois", "[questions]"], 506.7, "À chaque niveau de revenu", hl=507.4, size=96)
stk(S, "baton-test-trois", 1150, 240, 330, 507.0)

S = nxt(510.7)
title(S, ["Le [test]"], 510.8, "Les trois questions", hl=511.4)
tg(S, 430, "1 · Je possède mon argent, ou il me possède ?", 511.3, "", 34)
tg(S, 520, "2 · Je remercie Dieu pour ce que je gagne ?", 515.5, "", 34)
tg(S, 610, "3 · Je partage ce que je reçois ?", 518.2, "acc", 34)
stk(S, "baton-pense", 1150, 230, 260, 511.0)

S = nxt(519.9)
title(S, ["Les cinq", "[garde-fous]"], 520.0, "Applique-les", hl=520.6)
tg(S, 400, "1 · Donner en premier", 522.0, "", 32)
tg(S, 480, "2 · Gagner honnêtement", 523.3, "", 32)
tg(S, 560, "3 · Fixer ton assez", 524.7, "", 32)
tg(S, 640, "4 · Protéger tes priorités", 526.4, "", 32)
tg(S, 720, "5 · T'entourer", 528.0, "acc", 32)
stk(S, "garde-fou-route", 1100, 300, 480, 520.3)

S = nxt(529.3)
title(S, ["Un seul", "[garde-fou]"], 529.4, "Cette semaine", hl=530.6)
stk(S, "baton-ecrit-liste", 1100, 250, 380, 529.8)
stk(S, "carnet-depenses", 1520, 440, 300, 531.0, rot=3)
tg(S, 470, "Écris-le sur une feuille", 531.2, "acc", 38)

S = nxt(532.9)
title(S, ["Ta foi n'est", "pas à [vendre]"], 533.0, "Rappelle-toi", hl=534.6)
stk(S, "baton-priere", 1100, 260, 300, 533.2)
stk(S, "croix-verte", 1480, 300, 240, 535.0, rot=4)
hit(534.8, 0.8)

S = nxt(536.5)
title(S, ["Quel garde-fou", "te [manque] ?"], 536.6, "Et toi", hl=537.9)
stk(S, "baton-pense", 1150, 230, 260, 537.0)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 540.6, 14)
sfx("click", 540.6, 0.8)
tg(S, 620, "Abonne-toi", 543.4, "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 45.8), ("02", "Passages 1-2", 45.8, 170.7), ("03", "Passages 3-4", 170.7, 299.2),
              ("04", "Passage 5", 299.2, 365.3), ("05", "Garde-fous", 365.3, 455.6), ("06", "Exemple et test", 455.6, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)

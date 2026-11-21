"""Vidéo longue « Comment arrêter de vivre au jour le jour » — style 02 en 16:9, ~10 min.
5 passages (séquence « Parole » identique), 3 questions à retenir, appel à s'abonner au milieu, 5 étapes, coussin en 3 paliers, 4 pièges, exemple (Julie), récapitulatif.
Les temps sont lus dans transcript.json (voix fournie par l'utilisateur ; mots mal transcrits corrigés).

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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Comment arrêter de vivre au jour le jour", "lang": "fr"}
COLS, ROWS = 10, 9
VOICE_END = 565.4
s.setup(here=HERE, duration=580.8, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
_n = [0]
SUP = []
_TR = json.load(open(os.path.join(HERE, "transcript.json"), encoding="utf-8"))


def _norm(x):
    return re.sub(r"[^\w]+", "", unicodedata.normalize("NFC", x.lower()))


def W(prefix, after=0.0, nth=0):
    """Début (en secondes) du n-ième mot commençant par `prefix`, après l'instant `after` (repli approximatif signalé)."""
    pn = _norm(prefix).rstrip("s")
    k = 0
    for w in _TR:
        if w["start"] >= after and pn in _norm(w["text"]):
            if k == nth:
                return round(w["start"], 2)
            k += 1
    import difflib
    cand = [w for w in _TR if after <= w["start"] <= after + 25]
    best = difflib.get_close_matches(_norm(prefix), [_norm(w["text"]) for w in cand], n=1, cutoff=0.55)
    if best:
        for w in cand:
            if _norm(w["text"]) == best[0]:
                print("  ~ repli", prefix, "->", w["text"], w["start"])
                return round(w["start"], 2)
    raise KeyError((prefix, after))


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
title(S, ["De chèque en chèque :", "comment [sortir] ?"], 0.1, "Une réalité courante", hl=W("sortir", 0.0), size=72)
tg(S, 450, "Le salaire tombe", W("tombe", 0.0), "", 36)
tg(S, 540, "Quelques jours plus tard : presque rien", W("presque", 0.0), "", 34)
tg(S, 630, "Tu n'es pas seul", W("seul", 0.0), "acc", 38)
stk(S, "baton-fin-mois", 1150, 220, 330, 0.6, rot=-2)

S = nxt(11.18)
title(S, ["Une situation", "[épuisante]"], 11.27, "Chaque mois", hl=W("épuisante", 11.18), size=84)
tg(S, 450, "Regarder le compte avant chaque achat", W("regarde", 11.18), "", 34)
tg(S, 530, "Espérer qu'aucune facture n'arrive", W("facture", 11.18), "", 34)
tg(S, 610, "Une petite angoisse permanente", W("angoisse", 11.18), "acc", 34)
stk(S, "calendrier-fin-mois", 1050, 260, 440, 11.83, rot=-2)

S = nxt(19.36)
title(S, ["Des causes", "[multiples]"], 19.46, "Chaque histoire est différente", hl=W("multiples", 19.36), size=78)
tg(S, 440, "Un loyer qui augmente", W("loyer", 19.36), "", 32)
tg(S, 515, "Des prix qui montent", W("prix", 19.36), "", 32)
tg(S, 590, "Un imprévu de santé", W("santé", 19.36), "", 32)
tg(S, 665, "Une dette ancienne", W("ancienne", 19.36), "", 32)
tg(S, 740, "Aucune ne définit ta valeur", W("valeur", 19.36), "acc", 32)
stk(S, "baton-soucieux", 1250, 260, 290, 20.03)

S = nxt(29.42)
title(S, ["Pas de [honte]"], 29.52, "Une chose importante", hl=W("honte", 29.42), size=96)
tg(S, 440, "Pas toujours un manque de discipline", W("discipline", 29.42), "", 34)
tg(S, 530, "Parfois, le revenu est simplement trop juste", W("trop", 29.42), "acc", 34)
stk(S, "baton-serein", 1150, 250, 300, 30.09)

S = nxt(39.2)
title(S, ["Reprendre un", "peu de [souffle]"], 39.3, "Il existe des étapes", hl=W("souffle", 39.2), size=84)
tg(S, 450, "Même avec un petit revenu", W("petit", 39.2), "acc", 38)
tg(S, 540, "Des principes très pratiques", W("pratiques", 39.2), "", 38)
stk(S, "baton-respire", 1100, 240, 330, 39.91)

S = nxt(46.48)
title(S, ["Un point de", "[départ]"], 46.57, "Pas besoin d'être parfait", hl=W("départ", 46.48), size=90)
tg(S, 450, "Pas besoin d'un gros revenu", W("gros", 46.48), "", 36)
tg(S, 540, "Ni d'une situation parfaite", W("parfaite", 46.48), "", 36)
tg(S, 630, "Un point de départ, de la constance", W("constance", 46.48), "acc", 34)
stk(S, "escalier-trois-paliers", 1100, 250, 380, 47.14)

S = nxt(52.86)
title(S, ["Au [programme]"], 52.96, "Dans cette vidéo", hl=53.57)
tg(S, 420, "5 passages", W("cinq", 52.86, 0), "", 40)
tg(S, 510, "5 étapes", W("cinq", 52.86, 1), "", 40)
tg(S, 600, "Les pièges à éviter", W("pièges", 52.86), "", 40)
tg(S, 690, "Un exemple", W("exemple", 52.86), "acc", 40)
stk(S, "pupitre-parole", 1100, 260, 380, 53.57, rot=-2)

S = nxt(60.62)
title(S, ["Trois [paliers]"], 60.72, "Reste jusqu'à la fin", hl=W("paliers", 60.62), size=96)
counter(S, 80, 430, 0, 3, 61.43, 0.8, " paliers", 110)
tg(S, 600, "Une méthode qui commence très petit", W("petit", 60.62), "", 34)
tg(S, 690, "Ne plus dépendre du prochain salaire", W("dépendre", 60.62), "acc", 34)
stk(S, "escalier-trois-paliers", 1150, 240, 400, 61.23)

S = nxt(67.96)
title(S, ["Pas un conseil", "[personnalisé]"], 68.06, "Une précision importante", hl=W("personnalisé", 67.96), size=78)
tg(S, 450, "Une réflexion biblique générale", W("réflexion", 67.96), "", 36)
tg(S, 540, "À adapter à ta situation", W("adaptes", 67.96), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 68.79)
hit(W("personnalisé", 67.96), 0.8)

# ================================================================ 02 · Passage 1 : Proverbes 21.20
parole(76.54, "Proverbes 21.20", 78.8,
       f"« Il y a dans la demeure du sage {m(0, 'des trésors précieux et de l’huile')}, mais l'homme insensé {m(1, 'les engloutit')}. »",
       80.86, 87.13, [W("trésors", 80.86), W("engloutit", 80.86)], size=48)

S = nxt(87.24)
title(S, ["Le sage a", "une [réserve]"], 87.34, "Dans ce verset", hl=W("réserve", 87.24), size=84)
tg(S, 450, "Pas forcément énorme", W("énorme", 87.24), "", 38)
tg(S, 540, "Quelque chose qui reste", W("reste", 87.24), "acc", 38)
stk(S, "bocal-reserve", 1100, 220, 330, 87.96)

S = nxt(94.6)
title(S, ["L'insensé", "[consomme] tout"], 94.7, "Pas une insulte", hl=W("consomme", 94.6), size=78)
tg(S, 450, "Tout ce qui rentre sort aussitôt", W("aussitôt", 94.6), "", 34)
tg(S, 540, "Le moindre imprévu devient une crise", W("crise", 94.6), "acc", 34)
stk(S, "decouvert-rouge", 1100, 260, 400, 95.31, rot=-2)

S = nxt(104.17)
title(S, ["Une [marge]", "de sécurité"], 104.28, "Entre imprévu et catastrophe", hl=W("marge", 104.17), size=84)
tg(S, 450, "Elle sépare un imprévu d'une catastrophe", W("sépare", 104.17), "", 32)
tg(S, 540, "Une forme de paix", W("paix", 104.17), "acc", 38)
stk(S, "maison-roc", 1100, 260, 360, 104.91, rot=-2)

S = nxt(110.83)
title(S, ["Mieux [dormir]"], 110.93, "Quand tu peux absorber", hl=W("dors", 110.83), size=96)
tg(S, 440, "Une petite panne", W("panne", 110.83), "", 36)
tg(S, 520, "Une petite facture", W("facture", 110.83), "", 36)
tg(S, 600, "Moins tenté d'emprunter dans l'urgence", W("emprunter", 110.83), "acc", 32)
stk(S, "baton-respire", 1100, 240, 330, 111.45)

S = nxt(118.56)
title(S, ["Étape 1 :", "une [réserve]"], 118.66, "Première étape", hl=W("réserve", 118.56), size=90)
tg(S, 450, "Même minuscule", W("minuscule", 118.56), "", 38)
tg(S, 540, "Le but : l'habitude", W("habitude", 118.56), "acc", 38)
stk(S, "bocal-reserve", 1150, 220, 330, 119.28)

S = nxt(125.3)
title(S, ["Un [muscle]", "à entraîner"], 125.41, "Une réserve se construit", hl=W("muscle", 125.3), size=84)
tg(S, 450, "Petites séances régulières", W("séances", 125.3), "", 36)
tg(S, 540, "Pas un effort héroïque", W("héroïque", 125.3), "acc", 36)
stk(S, "baton-travaille", 1100, 250, 340, 125.96)

# ================================================================ 03 · Passage 2 : Proverbes 6.6-8
parole(131.02, "Proverbes 6.6-8", 133.02,
       f"« Va vers la fourmi, paresseux ; {m(0, 'considère ses voies')}, et deviens sage. Elle n'a ni chef, ni inspecteur, ni maître ; "
       f"{m(1, 'elle prépare en été sa nourriture')}, elle amasse pendant la moisson de quoi manger. »",
       135.44, 146.23, [W("considère", 135.44), W("prépare", 135.44)], size=40, ref_y=860)

S = nxt(146.32)
title(S, ["La fourmi", "[prépare]"], 146.43, "Pas de jour le jour", hl=W("prépare", 146.32), size=90)
tg(S, 450, "À l'avance, pendant la récolte", W("récolte", 146.32), "", 34)
tg(S, 540, "Pour la période où il y aura moins", W("moins", 146.32), "acc", 34)
stk(S, "fourmi-graine", 1100, 250, 380, 147.07)

S = nxt(153.06)
title(S, ["Sans personne", "pour la [surveiller]"], 153.15, "Ce qui frappe", hl=W("surveille", 153.06), size=72)
tg(S, 450, "Un choix quotidien et discret", W("discret", 153.06), "acc", 38)
stk(S, "baton-travaille", 1100, 250, 340, 153.62)

S = nxt(159.02)
title(S, ["Même un [peu]"], 159.12, "Si tu ne peux pas beaucoup", hl=W("peu", 159.02), size=96)
tg(S, 440, "Prépare avec ce que tu as", W("prépare", 159.02), "", 38)
tg(S, 530, "Fais-le régulièrement", W("régulièrement", 159.02), "acc", 38)
stk(S, "bocal-reserve", 1100, 220, 330, 159.64)

S = nxt(167.14)
title(S, ["5 € par semaine,", "[260 €] par an"], 167.25, "La régularité compte", hl=W("260", 167.14), size=78)
bw("260 € en un an", W("260", 167.14) + 0.2, 1.1, 100)
stk(S, "calendrier-prelevement", 1100, 250, 440, 167.93, rot=-2)

S = nxt(173.46)
title(S, ["Si cette vidéo", "t'[aide]…"], 173.56, "Un instant", hl=W("aide", 173.46))
tg(S, 450, "Abonne-toi", W("abonne", 173.46) + 0.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", 177.67, "", 34)
stk(S, "croix-verte", 1200, 280, 260, 174.38, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 174.79, rot=2)
bw("Abonne-toi", W("abonne", 173.46) + 0.4, 1.0)

# ================================================================ 04 · Passage 3 : Proverbes 27.23-24
parole(182.04, "Proverbes 27.23-24", 184.38,
       f"« {m(0, 'Connais bien l’état de tes brebis')}, donne tes soins à tes troupeaux ; car {m(1, 'la richesse ne dure pas toujours')}. »",
       186.82, 192.51, [W("connais", 186.5), W("richesse", 186.82)], size=48, ref_label="PROVERBES 27.23-24")

S = nxt(192.62)
title(S, ["Un berger connaît", "son [troupeau]"], 192.72, "Dans ce verset", hl=W("troupeau", 192.62), size=72)
tg(S, 450, "Combien de brebis", W("combien", 192.62), "", 36)
tg(S, 530, "Lesquelles sont fragiles", W("fragiles", 192.62), "", 36)
tg(S, 610, "Lesquelles ont besoin de soin", W("soin", 192.62), "acc", 36)
stk(S, "baton-berger", 1050, 250, 500, 193.33)

S = nxt(198.64)
title(S, ["Connaître l'état", "de tes [finances]"], 198.72, "Pour toi", hl=W("finances", 198.64), size=72)
tg(S, 450, "Combien tu gagnes", W("gagnes", 198.64), "", 36)
tg(S, 530, "Combien tu dois", W("dois", 198.64), "", 36)
tg(S, 610, "Où va ton argent", W("argent", 198.64) - 0.2, "acc", 36)
stk(S, "loupe-depenses", 1100, 260, 400, 199.25, rot=-2)

S = nxt(205.77)
title(S, ["Une [impression],", "pas de chiffres"], 205.85, "Beaucoup ne savent pas", hl=W("impression", 205.77), size=78)
tg(S, 450, "Où part l'argent ?", W("part", 205.77), "acc", 40)
stk(S, "baton-tiraille", 1150, 250, 300, 206.36)

S = nxt(211.91)
title(S, ["Étape 2 :", "suis tes [dépenses]"], 212.0, "Deuxième étape", hl=W("dépenses", 211.91), size=84)
tg(S, 450, "Pendant 30 jours", W("30", 211.91), "", 38)
tg(S, 530, "Note tout, même les petits achats", W("note", 211.91), "", 34)
tg(S, 610, "Pour voir clair, pas pour te juger", W("juger", 211.91), "acc", 32)
stk(S, "baton-ecrit-liste", 1100, 260, 340, 212.61)
stk(S, "carnet-depenses", 1540, 460, 290, 214.73, rot=3)

S = nxt(220.18)
title(S, ["Dépenses [fixes]", "et variables"], 220.28, "Deux familles", hl=W("fixes", 220.18), size=78)
tg(S, 450, "Fixes : loyer, énergie, assurances", W("loyer", 220.18), "", 34)
tg(S, 540, "Variables : courses, sorties, plaisirs", W("variables", 220.18), "acc", 34)
stk(S, "enveloppes-budget", 1100, 270, 340, 220.76, rot=-2)

S = nxt(230.18)
title(S, ["Tu risques", "d'être [surpris]"], 230.27, "Souvent", hl=W("surpris", 230.18), size=84)
tg(S, 450, "Petites dépenses répétées", W("répétées", 230.18), "", 36)
tg(S, 540, "Abonnements oubliés", W("abonnements", 230.18), "", 36)
tg(S, 630, "Achats de confort", W("confort", 230.18), "acc", 36)
stk(S, "pile-factures", 1100, 270, 340, 230.82)

S = nxt(237.72)
title(S, ["Les dépenses [fixes]", "méritent un examen"], 237.81, "Plus dures à changer", hl=W("examen", 237.72), size=72)
tg(S, 450, "Un contrat plus cher que nécessaire", W("contrat", 237.72), "", 32)
tg(S, 540, "Un forfait pas entièrement utilisé", W("forfait", 237.72), "acc", 32)
stk(S, "ciseaux-abonnements", 1100, 260, 400, 238.35)

# ================================================================ 05 · Passage 4 : Proverbes 14.23
parole(245.1, "Proverbes 14.23", 247.03,
       f"« {m(0, 'Tout travail procure l’abondance')}, mais {m(1, 'les paroles en l’air')} ne mènent qu'à la disette. »",
       249.39, 253.97, [W("travail", 249.39), W("paroles", 249.39)], size=52)

S = nxt(254.06)
title(S, ["L'action", "[concrète]"], 254.16, "Ce verset valorise", hl=W("concrète", 254.06), size=90)
tg(S, 450, "Rêver ou se plaindre ne suffit pas", W("rêver", 254.06), "", 34)
tg(S, 540, "Des gestes simples, répétés", W("gestes", 254.06), "acc", 36)
stk(S, "baton-travaille", 1100, 250, 340, 254.67)

S = nxt(261.92)
title(S, ["Ajuster, ou", "[gagner] plus"], 262.01, "Cela peut vouloir dire", hl=W("revenu", 261.92), size=84)
tg(S, 450, "Ajuster ton budget", W("ajuster", 261.92), "", 36)
tg(S, 540, "Un revenu supplémentaire", W("supplémentaire", 261.92), "", 36)
tg(S, 630, "Des compétences pour gagner plus", W("compétences", 261.92), "acc", 34)
stk(S, "mallette-travail", 1100, 270, 320, 262.45, rot=3)

S = nxt(269.24)
title(S, ["Quelques [pistes]"], 269.33, "Concrètement", hl=269.86, size=96)
tg(S, 440, "Quelques heures en plus", W("heures", 269.24), "", 34)
tg(S, 520, "Vendre ce que tu n'utilises plus", W("vente", 269.24), "", 34)
tg(S, 600, "Un service rendu à des voisins", W("voisins", 269.24), "", 34)
tg(S, 680, "Une formation", W("formation", 269.24), "acc", 34)
stk(S, "baton-content", 1150, 260, 300, 269.77)

S = nxt(276.94)
title(S, ["Pas jusqu'à", "l'[épuisement]"], 277.04, "Attention", hl=W("épuisement", 276.94), size=84)
tg(S, 450, "Dieu a aussi prévu le repos", W("repos", 276.94), "acc", 38)
tg(S, 540, "Agir avec méthode", W("méthode", 276.94), "", 38)
stk(S, "calendrier-repos", 1100, 260, 440, 277.52, rot=-2)

S = nxt(285.34)
title(S, ["Une seule [piste]", "à la fois"], 285.43, "Méthode", hl=W("piste", 285.34), size=84)
tg(S, 450, "Teste quelques semaines", W("teste", 285.34), "", 38)
tg(S, 540, "Garde ce qui fonctionne", W("garde", 285.34), "acc", 38)
stk(S, "baton-pense", 1150, 240, 270, 285.88)

S = nxt(289.94)
title(S, ["Étape 3 :", "ton [écart]"], 290.03, "Troisième étape", hl=W("écart", 289.94), size=96)
tg(S, 440, "Regarde tes dépenses", W("regarde", 289.94), "", 36)
tg(S, 520, "Un abonnement", W("abonnement", 289.94), "", 36)
tg(S, 600, "Un forfait", W("forfait", 289.94), "", 36)
tg(S, 680, "Une dépense de confort", W("confort", 289.94), "acc", 36)
stk(S, "ciseaux-abonnements", 1100, 260, 400, 290.48)

# ================================================================ 06 · Passage 5 : Matthieu 6.34
parole(300.4, "Matthieu 6.34", 302.72,
       f"« {m(0, 'Ne vous inquiétez donc pas du lendemain')} ; car le lendemain aura soin de lui-même. {m(1, 'À chaque jour suffit sa peine')}. »",
       305.24, 311.78, [W("inquiétez", 305.24), W("suffit", 305.24)], size=50)

S = nxt(311.98)
title(S, ["Souvent [mal]", "compris"], 312.08, "Ce verset", hl=W("mal", 311.98), size=90)
tg(S, 450, "Jésus ne dit pas : ne planifie pas", W("planifier", 311.98), "", 34)
tg(S, 540, "La fourmi montre le contraire", W("fourmi", 311.98), "acc", 34)
stk(S, "fourmi-graine", 1100, 250, 380, 312.68)

S = nxt(317.88)
title(S, ["L'[inquiétude]", "qui paralyse"], 317.98, "De quoi il parle", hl=W("inquiétude", 317.88), size=84)
tg(S, 450, "Préparer sans angoisse", W("angoisse", 317.88), "acc", 38)
stk(S, "baton-soucieux", 1150, 250, 290, 318.57)

S = nxt(324.34)
title(S, ["Un plan", "calme l'[esprit]"], 324.44, "Même modeste", hl=W("calme", 324.34), size=84)
tg(S, 450, "L'inquiétude diminue quand l'action commence", W("diminue", 324.34), "", 32)
tg(S, 540, "Tu fais ta part, Dieu le reste", W("confies", 324.34), "acc", 34)
stk(S, "baton-priere", 1100, 260, 300, 325.02)
stk(S, "croix-verte", 1560, 340, 220, W("confies", 324.34), rot=4)

S = nxt(334.06)
title(S, ["Du sérieux,", "puis la [confiance]"], 334.16, "Pas indifférent", hl=W("reposer", 334.06), size=78)
tg(S, 450, "Travailler avec sérieux", W("sérieux", 334.06), "", 36)
tg(S, 540, "Te reposer sur lui pour le reste", W("reposer", 334.06), "acc", 34)
stk(S, "colombe", 1100, 260, 300, 334.77, rot=3)

# ================================================================ 07 · Cinq étapes
S = nxt(340.68)
title(S, ["Cinq [étapes]", "pour s'en sortir"], 340.78, "Passons à la pratique", hl=W("étapes", 340.68), size=78)
counter(S, 80, 430, 0, 5, 341.5, 0.9, " étapes", 100)
tg(S, 580, "1 · Une réserve", W("réserve", 340.68), "", 32)
tg(S, 650, "2 · Suivre tes dépenses", W("suivre", 340.68), "", 32)
tg(S, 720, "3 · Trouver ton écart", W("écart", 340.68), "acc", 32)
stk(S, "liste-cinq-etapes", 1100, 240, 380, 341.09, rot=-1)

S = nxt(349.44)
title(S, ["Étape 4 :", "trois [paliers]"], 349.54, "Étape 4", hl=W("paliers", 349.44), size=90)
tg(S, 450, "1 · Une semaine de dépenses essentielles", W("semaine", 349.44), "", 32)
tg(S, 540, "2 · Un mois", W("mois", 349.44), "", 34)
tg(S, 630, "3 · Trois mois, si possible", W("troisième", 349.44), "acc", 34)
stk(S, "escalier-trois-paliers", 1050, 250, 480, 350.11)

S = nxt(363.4)
title(S, ["Commence", "[petit]"], 363.5, "Dix ou vingt euros", hl=W("petit", 363.4), size=96)
tg(S, 450, "10 ou 20 € par semaine", W("10", 363.4), "", 38)
tg(S, 540, "Mieux qu'un grand projet jamais commencé", W("projet", 363.4), "acc", 32)
stk(S, "bocal-reserve", 1100, 220, 330, 364.07)

S = nxt(369.8)
title(S, ["Un compte", "[séparé]"], 369.9, "Pour le coussin", hl=W("séparé", 369.8), size=90)
tg(S, 450, "Pas trop facile à utiliser", W("facile", 369.8), "", 38)
tg(S, 540, "Pour ne pas dépenser par réflexe", W("réflexe", 369.8), "acc", 34)
stk(S, "baton-budget", 1100, 260, 380, 370.39)

S = nxt(375.02)
title(S, ["Un nom clair :", "« [imprévus] »"], 375.11, "Donne-lui", hl=W("imprévus", 375.02), size=84)
tg(S, 450, "Te rappeler à quoi il sert", W("rappeler", 375.02), "", 34)
tg(S, 540, "Uniquement pour une vraie urgence", W("urgence", 375.02), "acc", 34)
stk(S, "enveloppes-budget", 1100, 260, 340, 375.56, rot=-2)

S = nxt(381.66)
title(S, ["Étape 5 :", "[automatise]"], 381.76, "Étape 5", hl=W("automatise", 381.66), size=90)
tg(S, 450, "Un virement juste après le salaire", W("virement", 381.66), "", 34)
tg(S, 540, "Ce que tu ne vois pas, tu le dépenses moins", W("vois", 381.66), "acc", 32)
stk(S, "virement-automatique", 1050, 270, 520, 382.34)

S = nxt(388.8)
title(S, ["Salaire à dates", "[variables]"], 388.9, "Si c'est ton cas", hl=W("variables", 388.8), size=78)
tg(S, 450, "Un montant très simple", W("simple", 388.8), "", 38)
tg(S, 540, "L'augmenter quand tu reçois plus", W("augmente", 388.8), "acc", 34)
stk(S, "calendrier-prelevement", 1100, 260, 440, 389.44, rot=-2)

S = nxt(394.3)
title(S, ["L'astuce :", "le mois [précédent]"], 394.41, "Promise", hl=W("précédent", 394.3), size=78)
tg(S, 450, "Coussin = un mois de dépenses", W("coussin", 394.3), "", 34)
tg(S, 540, "Le salaire de ce mois paie le mois suivant", W("suivant", 394.3), "", 32)
tg(S, 630, "Plus de dépendance au prochain chèque", W("dépends", 394.3), "acc", 32)
stk(S, "calendriers-decalage", 1050, 280, 560, 395.05, rot=-1)

S = nxt(407.32)
title(S, ["Un peu de", "[patience]"], 407.42, "Pour y arriver", hl=W("patience", 407.32), size=90)
tg(S, 450, "Chaque palier franchi réduit le stress", W("stress", 407.32), "acc", 34)
stk(S, "escalier-trois-paliers", 1100, 250, 380, 408.05)

S = nxt(414.38)
title(S, ["Choisir plus", "[librement]"], 414.48, "Concrètement", hl=W("librement", 414.38), size=90)
tg(S, 450, "Plus besoin de surveiller ton compte chaque matin", W("surveiller", 414.38), "acc", 30)
stk(S, "baton-respire", 1100, 240, 330, 414.99)

S = nxt(419.78)
title(S, ["Quatre [pièges]", "à éviter"], 419.89, "Attention", hl=W("pièges", 419.78), size=84)
counter(S, 80, 450, 0, 4, 420.74, 0.8, " pièges", 110)
stk(S, "decouvert-rouge", 1150, 260, 400, 420.5, rot=-2)

tP = W("découvert", 419.78)
S = nxt(tP - 0.8)
title(S, ["Évite ces", "[pièges]"], tP - 0.7, "Les quatre", hl=tP + 0.1, size=84)
tg(S, 440, "1 · Découvert et crédit revolving", tP, "", 32)
tg(S, 520, "2 · Crédits rapides, très chers", W("offres", 419.78), "", 32)
tg(S, 600, "3 · Vider ton coussin sans urgence", W("vider", 419.78), "", 32)
tg(S, 680, "4 · Te décourager au premier faux pas", W("décourager", 419.78), "acc", 32)
stk(S, "baton-presse", 1250, 260, 420, tP, rot=-2)

S = nxt(436.82)
title(S, ["Un faux pas :", "[reprends]"], 436.93, "Pas de condamnation", hl=W("reprends", 436.82), size=84)
tg(S, 450, "Reprends le mois suivant", W("reprends", 436.82), "", 36)
tg(S, 530, "La grâce autant que la sagesse", W("grâce", 436.82), "", 34)
tg(S, 610, "Une information, pas une condamnation", W("condamnation", 436.82), "acc", 32)
stk(S, "colombe", 1100, 280, 300, 437.59, rot=3)
stk(S, "croix-verte", 1560, 340, 220, W("grâce", 436.82), rot=4)

S = nxt(446.52)
title(S, ["Demander de", "l'[aide]"], 446.61, "Si c'est trop lourd", hl=W("aide", 446.52), size=90)
tg(S, 440, "Un conseiller en budget", W("conseiller", 446.52), "", 36)
tg(S, 520, "Une association d'aide", W("association", 446.52), "", 36)
tg(S, 600, "Ton église", W("église", 446.52), "", 36)
tg(S, 680, "Pas une faiblesse", W("faiblesse", 446.52), "acc", 38)
stk(S, "baton-conseillers", 1050, 280, 470, 447.19, rot=-2)

# ================================================================ 08 · Exemple : Julie
S = nxt(457.46)
title(S, ["Un exemple :", "[Julie]"], 457.57, "Prenons", hl=W("Julie", 457.46), size=90)
tg(S, 450, "Un salaire modeste", W("modeste", 459.12), "", 36)
tg(S, 540, "Presque rien en fin de mois", W("presque", 459.12), "", 36)
tg(S, 630, "Un découvert qui revient", W("découvert", 459.12), "acc", 36)
stk(S, "baton-fin-mois", 1150, 220, 330, 458.23, rot=-2)

S = nxt(465.46)
title(S, ["Elle [note]", "ses dépenses"], 465.57, "Un soir", hl=W("note", 465.46), size=90)
tg(S, 450, "Trois abonnements oubliés", W("abonnements", 465.46), "", 36)
tg(S, 540, "Des achats de confort répétés", W("confort", 465.46), "acc", 36)
stk(S, "loupe-depenses", 1100, 260, 400, 466.2, rot=-2)

S = nxt(471.9)
title(S, ["Elle [réduit]", "et programme"], 472.01, "Puis", hl=W("réduit", 471.9), size=90)
tg(S, 450, "Un virement de 15 € après chaque salaire", W("virement", 471.9), "", 32)
tg(S, 540, "Ça paraît dérisoire", W("dérisoire", 471.9), "acc", 38)
stk(S, "virement-automatique", 1050, 270, 520, 472.64)

S = nxt(477.7)
title(S, ["Elle en [parle]", "à sa famille"], 477.8, "Elle prévient", hl=W("prévient", 477.7), size=84)
tg(S, 450, "Pour qu'ils comprennent", W("comprennent", 477.7), "acc", 38)
stk(S, "couple-budget", 1100, 260, 440, 478.32, rot=-2)

S = nxt(481.52)
title(S, ["Une semaine", "d'[avance]"], 481.62, "Après quelques mois", hl=W("avance", 481.52), size=90)
tg(S, 450, "Une petite facture imprévue", W("facture", 481.52), "", 36)
tg(S, 540, "Payée sans découvert", W("découvert", 481.52), "", 36)
tg(S, 630, "Pour la première fois, elle respire", W("respire", 481.52), "acc", 34)
stk(S, "baton-respire", 1100, 240, 330, 482.14)
stk(S, "bocal-reserve", 1520, 300, 300, W("respire", 481.52), rot=3)

S = nxt(490.76)
title(S, ["Un [exemple],", "pas un témoignage"], 490.86, "À retenir", hl=W("exemple", 490.76), size=78)
tg(S, 450, "Aucune méthode ne garantit un résultat", W("garantit", 490.76), "acc", 32)
stk(S, "colombe", 1100, 280, 300, 491.47, rot=3)

S = nxt(497.98)
title(S, ["Un petit pas", "[régulier]"], 498.08, "Le principe", hl=W("régulier", 497.98), size=90)
tg(S, 450, "Mieux que de grandes intentions", W("intentions", 497.98), "", 34)
tg(S, 540, "Pas de solution magique", W("magique", 497.98), "", 34)
tg(S, 630, "Commencer par ce qui est à portée", W("portée", 497.98), "acc", 32)
stk(S, "escalier-trois-paliers", 1100, 250, 380, 498.56)

# ================================================================ 09 · Récapitulatif et action
S = nxt(510.54)
title(S, ["L'[essentiel]"], 510.63, "Retenons", hl=511.01, size=96)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 510.82, rot=-3)

S = nxt(511.78)
title(S, ["La Bible nous", "[invite]"], 511.87, "Vivre au jour le jour n'est pas une fatalité", hl=W("invite", 511.78), size=84)
tg(S, 450, "Avoir une réserve", W("réserve", 511.78), "", 34)
tg(S, 530, "Te préparer, comme la fourmi", W("fourmi", 511.78), "", 34)
tg(S, 610, "Connaître l'état de tes finances", W("connaître", 511.78), "", 34)
tg(S, 690, "Agir avec méthode", W("méthode", 511.78), "", 34)
tg(S, 770, "Ne pas vivre dans l'angoisse", W("angoisse", 511.78), "acc", 34)
stk(S, "fourmi-graine", 1250, 260, 340, 512.43)

S = nxt(524.14)
title(S, ["Les cinq", "[étapes]"], 524.23, "Rappel", hl=524.75, size=90)
tg(S, 440, "1 · Décider d'avoir une réserve", W("1", 524.14), "", 32)
tg(S, 520, "2 · Suivre tes dépenses", W("2", 524.14), "", 32)
tg(S, 600, "3 · Trouver ton écart", W("3", 524.14), "", 32)
tg(S, 680, "4 · Un coussin en trois paliers", W("4", 524.14), "", 32)
tg(S, 760, "5 · Automatiser ton épargne", W("5", 524.14), "acc", 32)
stk(S, "liste-cinq-etapes", 1200, 260, 400, 524.58, rot=-1)

S = nxt(537.12)
title(S, ["Une seule chose", "cette [semaine]"], 537.22, "Ton action", hl=W("semaine", 537.12), size=78)
tg(S, 450, "Ouvre ton application bancaire", W("ouvre", 537.12), "", 36)
tg(S, 540, "Note tes dépenses des 7 derniers jours", W("note", 537.12), "acc", 34)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 537.73)
stk(S, "carnet-depenses", 1540, 460, 290, 538.74, rot=3)

S = nxt(543.58)
title(S, ["Le premier [pas],", "puis le suivant"], 543.67, "Pas tout changer d'un coup", hl=W("premier", 543.58) + 0.3, size=78)
tg(S, 450, "Un pas après l'autre", W("suivant", 543.58), "acc", 40)
stk(S, "escalier-trois-paliers", 1100, 250, 400, 544.11)

S = nxt(548.54)
title(S, ["Une petite", "[victoire]"], 548.63, "Remarque-la", hl=W("victoire", 548.54), size=90)
tg(S, 450, "Une semaine sans découvert", W("découvert", 548.54), "", 36)
tg(S, 540, "Le changement est possible", W("possible", 548.54), "acc", 36)
stk(S, "baton-content", 1150, 260, 300, 549.06)
stk(S, "croix-verte", 1560, 340, 220, W("possible", 548.54), rot=4)

S = nxt(554.82)
title(S, ["Ton plus grand", "[obstacle] ?"], 554.91, "Et toi", hl=W("obstacle", 554.82), size=84)
stk(S, "baton-pense", 1150, 230, 260, 555.36)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, W("commentaire", 558.86) - 0.6, 14)
sfx("click", W("commentaire", 558.86) - 0.6, 0.8)
tg(S, 620, "Abonne-toi", W("abonne", 562.36), "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 76.54), ("02", "Passages 1 et 2", 76.54, 182.04), ("03", "Passages 3 et 4", 182.04, 300.4),
              ("04", "Passage 5 et étapes", 300.4, 419.78), ("05", "Pièges et exemple", 419.78, 510.54), ("06", "À retenir", 510.54, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)

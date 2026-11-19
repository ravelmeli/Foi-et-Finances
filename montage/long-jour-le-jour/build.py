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
VOICE_END = 572.4
s.setup(here=HERE, duration=587.8, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
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

S = nxt(11.1)
title(S, ["Une situation", "[épuisante]"], 11.2, "Chaque mois", hl=W("épuisante", 11.1), size=84)
tg(S, 450, "Regarder le compte avant chaque achat", W("regarde", 11.1), "", 34)
tg(S, 530, "Espérer qu'aucune facture n'arrive", W("facture", 11.1), "", 34)
tg(S, 610, "Une petite angoisse permanente", W("angoisse", 11.1), "acc", 34)
stk(S, "calendrier-fin-mois", 1050, 260, 440, 11.8, rot=-2)

S = nxt(19.9)
title(S, ["Des causes", "[multiples]"], 20.0, "Chaque histoire est différente", hl=W("multiples", 19.9), size=78)
tg(S, 440, "Un loyer qui augmente", W("loyer", 19.9), "", 32)
tg(S, 515, "Des prix qui montent", W("prix", 19.9), "", 32)
tg(S, 590, "Un imprévu de santé", W("santé", 19.9), "", 32)
tg(S, 665, "Une dette ancienne", W("ancienne", 19.9), "", 32)
tg(S, 740, "Aucune ne définit ta valeur", W("valeur", 19.9), "acc", 32)
stk(S, "baton-soucieux", 1250, 260, 290, 20.6)

S = nxt(30.5)
title(S, ["Pas de [honte]"], 30.6, "Une chose importante", hl=W("honte", 30.5), size=96)
tg(S, 440, "Pas toujours un manque de discipline", W("discipline", 30.5), "", 34)
tg(S, 530, "Parfois, le revenu est simplement trop juste", W("trop", 30.5), "acc", 34)
stk(S, "baton-serein", 1150, 250, 300, 31.2)

S = nxt(40.7)
title(S, ["Reprendre un", "peu de [souffle]"], 40.8, "Il existe des étapes", hl=W("souffle", 40.7), size=84)
tg(S, 450, "Même avec un petit revenu", W("petit", 40.7), "acc", 38)
tg(S, 540, "Des principes très pratiques", W("pratiques", 40.7), "", 38)
stk(S, "baton-respire", 1100, 240, 330, 41.4)

S = nxt(47.9)
title(S, ["Un point de", "[départ]"], 48.0, "Pas besoin d'être parfait", hl=W("départ", 47.9), size=90)
tg(S, 450, "Pas besoin d'un gros revenu", W("gros", 47.9), "", 36)
tg(S, 540, "Ni d'une situation parfaite", W("parfaite", 47.9), "", 36)
tg(S, 630, "Un point de départ, de la constance", W("constance", 47.9), "acc", 34)
stk(S, "escalier-trois-paliers", 1100, 250, 380, 48.6)

S = nxt(54.7)
title(S, ["Au [programme]"], 54.8, "Dans cette vidéo", hl=55.4)
tg(S, 420, "5 passages", W("cinq", 54.7, 0), "", 40)
tg(S, 510, "5 étapes", W("cinq", 54.7, 1), "", 40)
tg(S, 600, "Les pièges à éviter", W("pièges", 54.7), "", 40)
tg(S, 690, "Un exemple", W("exemple", 54.7), "acc", 40)
stk(S, "pupitre-parole", 1100, 260, 380, 55.4, rot=-2)

S = nxt(62.4)
title(S, ["Trois [paliers]"], 62.5, "Reste jusqu'à la fin", hl=W("paliers", 62.4), size=96)
counter(S, 80, 430, 0, 3, 63.2, 0.8, " paliers", 110)
tg(S, 600, "Une méthode qui commence très petit", W("petit", 62.4), "", 34)
tg(S, 690, "Ne plus dépendre du prochain salaire", W("dépendre", 62.4), "acc", 34)
stk(S, "escalier-trois-paliers", 1150, 240, 400, 63.0)

S = nxt(69.6)
title(S, ["Pas un conseil", "[personnalisé]"], 69.7, "Une précision importante", hl=W("personnalisé", 69.6), size=78)
tg(S, 450, "Une réflexion biblique générale", W("réflexion", 69.6), "", 36)
tg(S, 540, "À adapter à ta situation", W("adaptes", 69.6), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 70.4)
hit(W("personnalisé", 69.6), 0.8)

# ================================================================ 02 · Passage 1 : Proverbes 21.20
parole(78.0, "Proverbes 21.20", 80.2,
       f"« Il y a dans la demeure du sage {m(0, 'des trésors précieux et de l’huile')}, mais l'homme insensé {m(1, 'les engloutit')}. »",
       82.2, 87.9, [W("trésors", 82.2), W("engloutit", 82.2)], size=48)

S = nxt(88.0)
title(S, ["Le sage a", "une [réserve]"], 88.1, "Dans ce verset", hl=W("réserve", 88.0), size=84)
tg(S, 450, "Pas forcément énorme", W("énorme", 88.0), "", 38)
tg(S, 540, "Quelque chose qui reste", W("reste", 88.0), "acc", 38)
stk(S, "bocal-reserve", 1100, 220, 330, 88.7)

S = nxt(95.2)
title(S, ["L'insensé", "[consomme] tout"], 95.3, "Pas une insulte", hl=W("consomme", 95.2), size=78)
tg(S, 450, "Tout ce qui rentre sort aussitôt", W("aussitôt", 95.2), "", 34)
tg(S, 540, "Le moindre imprévu devient une crise", W("crise", 95.2), "acc", 34)
stk(S, "decouvert-rouge", 1100, 260, 400, 95.9, rot=-2)

S = nxt(104.6)
title(S, ["Une [marge]", "de sécurité"], 104.7, "Entre imprévu et catastrophe", hl=W("marge", 104.6), size=84)
tg(S, 450, "Elle sépare un imprévu d'une catastrophe", W("sépare", 104.6), "", 32)
tg(S, 540, "Une forme de paix", W("paix", 104.6), "acc", 38)
stk(S, "maison-roc", 1100, 260, 360, 105.3, rot=-2)

S = nxt(110.9)
title(S, ["Mieux [dormir]"], 111.0, "Quand tu peux absorber", hl=W("dors", 110.9), size=96)
tg(S, 440, "Une petite panne", W("panne", 110.9), "", 36)
tg(S, 520, "Une petite facture", W("facture", 110.9), "", 36)
tg(S, 600, "Moins tenté d'emprunter dans l'urgence", W("emprunter", 110.9), "acc", 32)
stk(S, "baton-respire", 1100, 240, 330, 111.5)

S = nxt(118.3)
title(S, ["Étape 1 :", "une [réserve]"], 118.4, "Première étape", hl=W("réserve", 118.3), size=90)
tg(S, 450, "Même minuscule", W("minuscule", 118.3), "", 38)
tg(S, 540, "Le but : l'habitude", W("habitude", 118.3), "acc", 38)
stk(S, "bocal-reserve", 1150, 220, 330, 119.0)

S = nxt(124.8)
title(S, ["Un [muscle]", "à entraîner"], 124.9, "Une réserve se construit", hl=W("muscle", 124.8), size=84)
tg(S, 450, "Petites séances régulières", W("séances", 124.8), "", 36)
tg(S, 540, "Pas un effort héroïque", W("héroïque", 124.8), "acc", 36)
stk(S, "baton-travaille", 1100, 250, 340, 125.4)

# ================================================================ 03 · Passage 2 : Proverbes 6.6-8
parole(130.0, "Proverbes 6.6-8", 131.9,
       f"« Va vers la fourmi, paresseux ; {m(0, 'considère ses voies')}, et deviens sage. Elle n'a ni chef, ni inspecteur, ni maître ; "
       f"{m(1, 'elle prépare en été sa nourriture')}, elle amasse pendant la moisson de quoi manger. »",
       134.2, 145.7, [W("considère", 134.2), W("prépare", 134.2)], size=40, ref_y=860)

S = nxt(145.8)
title(S, ["La fourmi", "[prépare]"], 145.9, "Pas de jour le jour", hl=W("prépare", 145.8), size=90)
tg(S, 450, "À l'avance, pendant la récolte", W("récolte", 145.8), "", 34)
tg(S, 540, "Pour la période où il y aura moins", W("moins", 145.8), "acc", 34)
stk(S, "fourmi-graine", 1100, 250, 380, 146.5)

S = nxt(152.1)
title(S, ["Sans personne", "pour la [surveiller]"], 152.2, "Ce qui frappe", hl=W("surveille", 152.1), size=72)
tg(S, 450, "Un choix quotidien et discret", W("discret", 152.1), "acc", 38)
stk(S, "baton-travaille", 1100, 250, 340, 152.7)

S = nxt(158.5)
title(S, ["Même un [peu]"], 158.6, "Si tu ne peux pas beaucoup", hl=W("peu", 158.5), size=96)
tg(S, 440, "Prépare avec ce que tu as", W("prépare", 158.5), "", 38)
tg(S, 530, "Fais-le régulièrement", W("régulièrement", 158.5), "acc", 38)
stk(S, "bocal-reserve", 1100, 220, 330, 159.1)

S = nxt(166.3)
title(S, ["5 € par semaine,", "[260 €] par an"], 166.4, "La régularité compte", hl=W("260", 166.3), size=78)
bw("260 € en un an", W("260", 166.3) + 0.2, 1.1, 100)
stk(S, "calendrier-prelevement", 1100, 250, 440, 167.0, rot=-2)

S = nxt(171.9)
title(S, ["Si cette vidéo", "t'[aide]…"], 172.0, "Un instant", hl=W("aide", 171.9))
tg(S, 450, "Abonne-toi", W("abonne", 171.9) + 0.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", 176.0, "", 34)
stk(S, "croix-verte", 1200, 280, 260, 172.8, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 173.2, rot=2)
bw("Abonne-toi", W("abonne", 171.9) + 0.4, 1.0)

# ================================================================ 04 · Passage 3 : Proverbes 27.23-24
parole(180.2, "Proverbes 27.23-24", 182.4,
       f"« {m(0, 'Connais bien l’état de tes brebis')}, donne tes soins à tes troupeaux ; car {m(1, 'la richesse ne dure pas toujours')}. »",
       184.7, 189.8, [W("connais", 184.4), W("richesse", 184.7)], size=48, ref_label="PROVERBES 27.23-24")

S = nxt(189.9)
title(S, ["Un berger connaît", "son [troupeau]"], 190.0, "Dans ce verset", hl=W("troupeau", 189.9), size=72)
tg(S, 450, "Combien de brebis", W("combien", 189.9), "", 36)
tg(S, 530, "Lesquelles sont fragiles", W("fragiles", 189.9), "", 36)
tg(S, 610, "Lesquelles ont besoin de soin", W("soin", 189.9), "acc", 36)
stk(S, "baton-berger", 1050, 250, 500, 190.6)

S = nxt(195.8)
title(S, ["Connaître l'état", "de tes [finances]"], 195.9, "Pour toi", hl=W("finances", 195.8), size=72)
tg(S, 450, "Combien tu gagnes", W("gagnes", 195.8), "", 36)
tg(S, 530, "Combien tu dois", W("dois", 195.8), "", 36)
tg(S, 610, "Où va ton argent", W("argent", 195.8) - 0.2, "acc", 36)
stk(S, "loupe-depenses", 1100, 260, 400, 196.5, rot=-2)

S = nxt(203.9)
title(S, ["Une [impression],", "pas de chiffres"], 204.0, "Beaucoup ne savent pas", hl=W("impression", 203.9), size=78)
tg(S, 450, "Où part l'argent ?", W("part", 203.9), "acc", 40)
stk(S, "baton-tiraille", 1150, 250, 300, 204.6)

S = nxt(211.2)
title(S, ["Étape 2 :", "suis tes [dépenses]"], 211.3, "Deuxième étape", hl=W("dépenses", 211.2), size=84)
tg(S, 450, "Pendant 30 jours", W("30", 211.2), "", 38)
tg(S, 530, "Note tout, même les petits achats", W("note", 211.2), "", 34)
tg(S, 610, "Pour voir clair, pas pour te juger", W("juger", 211.2), "acc", 32)
stk(S, "baton-ecrit-liste", 1100, 260, 340, 211.9)
stk(S, "carnet-depenses", 1540, 460, 290, 214.0, rot=3)

S = nxt(219.4)
title(S, ["Dépenses [fixes]", "et variables"], 219.5, "Deux familles", hl=W("fixes", 219.4), size=78)
tg(S, 450, "Fixes : loyer, énergie, assurances", W("loyer", 219.4), "", 34)
tg(S, 540, "Variables : courses, sorties, plaisirs", W("variables", 219.4), "acc", 34)
stk(S, "enveloppes-budget", 1100, 270, 340, 220.0, rot=-2)

S = nxt(229.7)
title(S, ["Tu risques", "d'être [surpris]"], 229.8, "Souvent", hl=W("surpris", 229.7), size=84)
tg(S, 450, "Petites dépenses répétées", W("répétées", 229.7), "", 36)
tg(S, 540, "Abonnements oubliés", W("abonnements", 229.7), "", 36)
tg(S, 630, "Achats de confort", W("confort", 229.7), "acc", 36)
stk(S, "pile-factures", 1100, 270, 340, 230.4)

S = nxt(237.9)
title(S, ["Les dépenses [fixes]", "méritent un examen"], 238.0, "Plus dures à changer", hl=W("examen", 237.9), size=72)
tg(S, 450, "Un contrat plus cher que nécessaire", W("contrat", 237.9), "", 32)
tg(S, 540, "Un forfait pas entièrement utilisé", W("forfait", 237.9), "acc", 32)
stk(S, "ciseaux-abonnements", 1100, 260, 400, 238.6)

# ================================================================ 05 · Passage 4 : Proverbes 14.23
parole(246.1, "Proverbes 14.23", 248.4,
       f"« {m(0, 'Tout travail procure l’abondance')}, mais {m(1, 'les paroles en l’air')} ne mènent qu'à la disette. »",
       251.2, 256.8, [W("travail", 251.2), W("paroles", 251.2)], size=52)

S = nxt(256.9)
title(S, ["L'action", "[concrète]"], 257.0, "Ce verset valorise", hl=W("concrète", 256.9), size=90)
tg(S, 450, "Rêver ou se plaindre ne suffit pas", W("rêver", 256.9), "", 34)
tg(S, 540, "Des gestes simples, répétés", W("gestes", 256.9), "acc", 36)
stk(S, "baton-travaille", 1100, 250, 340, 257.5)

S = nxt(264.6)
title(S, ["Ajuster, ou", "[gagner] plus"], 264.7, "Cela peut vouloir dire", hl=W("revenu", 264.6), size=84)
tg(S, 450, "Ajuster ton budget", W("ajuster", 264.6), "", 36)
tg(S, 540, "Un revenu supplémentaire", W("supplémentaire", 264.6), "", 36)
tg(S, 630, "Des compétences pour gagner plus", W("compétences", 264.6), "acc", 34)
stk(S, "mallette-travail", 1100, 270, 320, 265.2, rot=3)

S = nxt(272.8)
title(S, ["Quelques [pistes]"], 272.9, "Concrètement", hl=273.5, size=96)
tg(S, 440, "Quelques heures en plus", W("heures", 272.8), "", 34)
tg(S, 520, "Vendre ce que tu n'utilises plus", W("vente", 272.8), "", 34)
tg(S, 600, "Un service rendu à des voisins", W("voisins", 272.8), "", 34)
tg(S, 680, "Une formation", W("formation", 272.8), "acc", 34)
stk(S, "baton-content", 1150, 260, 300, 273.4)

S = nxt(281.6)
title(S, ["Pas jusqu'à", "l'[épuisement]"], 281.7, "Attention", hl=W("épuisement", 281.6), size=84)
tg(S, 450, "Dieu a aussi prévu le repos", W("repos", 281.6), "acc", 38)
tg(S, 540, "Agir avec méthode", W("méthode", 281.6), "", 38)
stk(S, "calendrier-repos", 1100, 260, 440, 282.2, rot=-2)

S = nxt(290.3)
title(S, ["Une seule [piste]", "à la fois"], 290.4, "Méthode", hl=W("piste", 290.3), size=84)
tg(S, 450, "Teste quelques semaines", W("teste", 290.3), "", 38)
tg(S, 540, "Garde ce qui fonctionne", W("garde", 290.3), "acc", 38)
stk(S, "baton-pense", 1150, 240, 270, 290.9)

S = nxt(295.4)
title(S, ["Étape 3 :", "ton [écart]"], 295.5, "Troisième étape", hl=W("écart", 295.4), size=96)
tg(S, 440, "Regarde tes dépenses", W("regarde", 295.4), "", 36)
tg(S, 520, "Un abonnement", W("abonnement", 295.4), "", 36)
tg(S, 600, "Un forfait", W("forfait", 295.4), "", 36)
tg(S, 680, "Une dépense de confort", W("confort", 295.4), "acc", 36)
stk(S, "ciseaux-abonnements", 1100, 260, 400, 296.0)

# ================================================================ 06 · Passage 5 : Matthieu 6.34
parole(307.0, "Matthieu 6.34", 309.2,
       f"« {m(0, 'Ne vous inquiétez donc pas du lendemain')} ; car le lendemain aura soin de lui-même. {m(1, 'À chaque jour suffit sa peine')}. »",
       311.6, 318.0, [W("inquiétez", 311.6), W("suffit", 311.6)], size=50)

S = nxt(318.2)
title(S, ["Souvent [mal]", "compris"], 318.3, "Ce verset", hl=W("mal", 318.2), size=90)
tg(S, 450, "Jésus ne dit pas : ne planifie pas", W("planifier", 318.2), "", 34)
tg(S, 540, "La fourmi montre le contraire", W("fourmi", 318.2), "acc", 34)
stk(S, "fourmi-graine", 1100, 250, 380, 318.9)

S = nxt(324.1)
title(S, ["L'[inquiétude]", "qui paralyse"], 324.2, "De quoi il parle", hl=W("inquiétude", 324.1), size=84)
tg(S, 450, "Préparer sans angoisse", W("angoisse", 324.1), "acc", 38)
stk(S, "baton-soucieux", 1150, 250, 290, 324.8)

S = nxt(330.7)
title(S, ["Un plan", "calme l'[esprit]"], 330.8, "Même modeste", hl=W("calme", 330.7), size=84)
tg(S, 450, "L'inquiétude diminue quand l'action commence", W("diminue", 330.7), "", 32)
tg(S, 540, "Tu fais ta part, Dieu le reste", W("confies", 330.7), "acc", 34)
stk(S, "baton-priere", 1100, 260, 300, 331.4)
stk(S, "croix-verte", 1560, 340, 220, W("confies", 330.7), rot=4)

S = nxt(340.1)
title(S, ["Du sérieux,", "puis la [confiance]"], 340.2, "Pas indifférent", hl=W("reposer", 340.1), size=78)
tg(S, 450, "Travailler avec sérieux", W("sérieux", 340.1), "", 36)
tg(S, 540, "Te reposer sur lui pour le reste", W("reposer", 340.1), "acc", 34)
stk(S, "colombe", 1100, 260, 300, 340.8, rot=3)

# ================================================================ 07 · Cinq étapes
S = nxt(346.6)
title(S, ["Cinq [étapes]", "pour s'en sortir"], 346.7, "Passons à la pratique", hl=W("étapes", 346.6), size=78)
counter(S, 80, 430, 0, 5, 347.4, 0.9, " étapes", 100)
tg(S, 580, "1 · Une réserve", W("réserve", 346.6), "", 32)
tg(S, 650, "2 · Suivre tes dépenses", W("suivre", 346.6), "", 32)
tg(S, 720, "3 · Trouver ton écart", W("écart", 346.6), "acc", 32)
stk(S, "liste-cinq-etapes", 1100, 240, 380, 347.0, rot=-1)

S = nxt(355.2)
title(S, ["Étape 4 :", "trois [paliers]"], 355.3, "Étape 4", hl=W("paliers", 355.2), size=90)
tg(S, 450, "1 · Une semaine de dépenses essentielles", W("semaine", 355.2), "", 32)
tg(S, 540, "2 · Un mois", W("mois", 355.2), "", 34)
tg(S, 630, "3 · Trois mois, si possible", W("troisième", 355.2), "acc", 34)
stk(S, "escalier-trois-paliers", 1050, 250, 480, 355.9)

S = nxt(369.8)
title(S, ["Commence", "[petit]"], 369.9, "Dix ou vingt euros", hl=W("petit", 369.8), size=96)
tg(S, 450, "10 ou 20 € par semaine", W("10", 369.8), "", 38)
tg(S, 540, "Mieux qu'un grand projet jamais commencé", W("projet", 369.8), "acc", 32)
stk(S, "bocal-reserve", 1100, 220, 330, 370.5)

S = nxt(376.5)
title(S, ["Un compte", "[séparé]"], 376.6, "Pour le coussin", hl=W("séparé", 376.5), size=90)
tg(S, 450, "Pas trop facile à utiliser", W("facile", 376.5), "", 38)
tg(S, 540, "Pour ne pas dépenser par réflexe", W("réflexe", 376.5), "acc", 34)
stk(S, "baton-budget", 1100, 260, 380, 377.1)

S = nxt(381.8)
title(S, ["Un nom clair :", "« [imprévus] »"], 381.9, "Donne-lui", hl=W("imprévus", 381.8), size=84)
tg(S, 450, "Te rappeler à quoi il sert", W("rappeler", 381.8), "", 34)
tg(S, 540, "Uniquement pour une vraie urgence", W("urgence", 381.8), "acc", 34)
stk(S, "enveloppes-budget", 1100, 260, 340, 382.4, rot=-2)

S = nxt(389.1)
title(S, ["Étape 5 :", "[automatise]"], 389.2, "Étape 5", hl=W("automatise", 389.1), size=90)
tg(S, 450, "Un virement juste après le salaire", W("virement", 389.1), "", 34)
tg(S, 540, "Ce que tu ne vois pas, tu le dépenses moins", W("vois", 389.1), "acc", 32)
stk(S, "virement-automatique", 1050, 270, 520, 389.8)

S = nxt(396.4)
title(S, ["Salaire à dates", "[variables]"], 396.5, "Si c'est ton cas", hl=W("variables", 396.4), size=78)
tg(S, 450, "Un montant très simple", W("simple", 396.4), "", 38)
tg(S, 540, "L'augmenter quand tu reçois plus", W("augmente", 396.4), "acc", 34)
stk(S, "calendrier-prelevement", 1100, 260, 440, 397.0, rot=-2)

S = nxt(401.5)
title(S, ["L'astuce :", "le mois [précédent]"], 401.6, "Promise", hl=W("précédent", 401.5), size=78)
tg(S, 450, "Coussin = un mois de dépenses", W("coussin", 401.5), "", 34)
tg(S, 540, "Le salaire de ce mois paie le mois suivant", W("suivant", 401.5), "", 32)
tg(S, 630, "Plus de dépendance au prochain chèque", W("dépends", 401.5), "acc", 32)
stk(S, "calendriers-decalage", 1050, 280, 560, 402.2, rot=-1)

S = nxt(413.7)
title(S, ["Un peu de", "[patience]"], 413.8, "Pour y arriver", hl=W("patience", 413.7), size=90)
tg(S, 450, "Chaque palier franchi réduit le stress", W("stress", 413.7), "acc", 34)
stk(S, "escalier-trois-paliers", 1100, 250, 380, 414.4)

S = nxt(420.5)
title(S, ["Choisir plus", "[librement]"], 420.6, "Concrètement", hl=W("librement", 420.5), size=90)
tg(S, 450, "Plus besoin de surveiller ton compte chaque matin", W("surveiller", 420.5), "acc", 30)
stk(S, "baton-respire", 1100, 240, 330, 421.1)

S = nxt(425.8)
title(S, ["Quatre [pièges]", "à éviter"], 425.9, "Attention", hl=W("pièges", 425.8), size=84)
counter(S, 80, 450, 0, 4, 426.6, 0.8, " pièges", 110)
stk(S, "decouvert-rouge", 1150, 260, 400, 426.4, rot=-2)

tP = W("découvert", 425.8)
S = nxt(tP - 0.8)
title(S, ["Évite ces", "[pièges]"], tP - 0.7, "Les quatre", hl=tP + 0.1, size=84)
tg(S, 440, "1 · Découvert et crédit revolving", tP, "", 32)
tg(S, 520, "2 · Crédits rapides, très chers", W("offres", 425.8), "", 32)
tg(S, 600, "3 · Vider ton coussin sans urgence", W("vider", 425.8), "", 32)
tg(S, 680, "4 · Te décourager au premier faux pas", W("décourager", 425.8), "acc", 32)
stk(S, "baton-presse", 1250, 260, 420, tP, rot=-2)

S = nxt(439.9)
title(S, ["Un faux pas :", "[reprends]"], 440.0, "Pas de condamnation", hl=W("reprends", 439.9), size=84)
tg(S, 450, "Reprends le mois suivant", W("reprends", 439.9), "", 36)
tg(S, 530, "La grâce autant que la sagesse", W("grâce", 439.9), "", 34)
tg(S, 610, "Une information, pas une condamnation", W("condamnation", 439.9), "acc", 32)
stk(S, "colombe", 1100, 280, 300, 440.6, rot=3)
stk(S, "croix-verte", 1560, 340, 220, W("grâce", 439.9), rot=4)

S = nxt(449.1)
title(S, ["Demander de", "l'[aide]"], 449.2, "Si c'est trop lourd", hl=W("aide", 449.1), size=90)
tg(S, 440, "Un conseiller en budget", W("conseiller", 449.1), "", 36)
tg(S, 520, "Une association d'aide", W("association", 449.1), "", 36)
tg(S, 600, "Ton église", W("église", 449.1), "", 36)
tg(S, 680, "Pas une faiblesse", W("faiblesse", 449.1), "acc", 38)
stk(S, "baton-conseillers", 1050, 280, 470, 449.8, rot=-2)

# ================================================================ 08 · Exemple : Julie
S = nxt(460.5)
title(S, ["Un exemple :", "[Julie]"], 460.6, "Prenons", hl=W("Julie", 460.5), size=90)
tg(S, 450, "Un salaire modeste", W("modeste", 462.0), "", 36)
tg(S, 540, "Presque rien en fin de mois", W("presque", 462.0), "", 36)
tg(S, 630, "Un découvert qui revient", W("découvert", 462.0), "acc", 36)
stk(S, "baton-fin-mois", 1150, 220, 330, 461.2, rot=-2)

S = nxt(468.3)
title(S, ["Elle [note]", "ses dépenses"], 468.4, "Un soir", hl=W("note", 468.3), size=90)
tg(S, 450, "Trois abonnements oubliés", W("abonnements", 468.3), "", 36)
tg(S, 540, "Des achats de confort répétés", W("confort", 468.3), "acc", 36)
stk(S, "loupe-depenses", 1100, 260, 400, 469.0, rot=-2)

S = nxt(474.4)
title(S, ["Elle [réduit]", "et programme"], 474.5, "Puis", hl=W("réduit", 474.4), size=90)
tg(S, 450, "Un virement de 15 € après chaque salaire", W("virement", 474.4), "", 32)
tg(S, 540, "Ça paraît dérisoire", W("dérisoire", 474.4), "acc", 38)
stk(S, "virement-automatique", 1050, 270, 520, 475.1)

S = nxt(479.9)
title(S, ["Elle en [parle]", "à sa famille"], 480.0, "Elle prévient", hl=W("prévient", 479.9), size=84)
tg(S, 450, "Pour qu'ils comprennent", W("comprennent", 479.9), "acc", 38)
stk(S, "couple-budget", 1100, 260, 440, 480.5, rot=-2)

S = nxt(483.6)
title(S, ["Une semaine", "d'[avance]"], 483.7, "Après quelques mois", hl=W("avance", 483.6), size=90)
tg(S, 450, "Une petite facture imprévue", W("facture", 483.6), "", 36)
tg(S, 540, "Payée sans découvert", W("découvert", 483.6), "", 36)
tg(S, 630, "Pour la première fois, elle respire", W("respire", 483.6), "acc", 34)
stk(S, "baton-respire", 1100, 240, 330, 484.2)
stk(S, "bocal-reserve", 1520, 300, 300, W("respire", 483.6), rot=3)

S = nxt(492.5)
title(S, ["Un [exemple],", "pas un témoignage"], 492.6, "À retenir", hl=W("exemple", 492.5), size=78)
tg(S, 450, "Aucune méthode ne garantit un résultat", W("garantit", 492.5), "acc", 32)
stk(S, "colombe", 1100, 280, 300, 493.2, rot=3)

S = nxt(499.6)
title(S, ["Un petit pas", "[régulier]"], 499.7, "Le principe", hl=W("régulier", 499.6), size=90)
tg(S, 450, "Mieux que de grandes intentions", W("intentions", 499.6), "", 34)
tg(S, 540, "Pas de solution magique", W("magique", 499.6), "", 34)
tg(S, 630, "Commencer par ce qui est à portée", W("portée", 499.6), "acc", 32)
stk(S, "escalier-trois-paliers", 1100, 250, 380, 500.2)

# ================================================================ 09 · Récapitulatif et action
S = nxt(513.0)
title(S, ["L'[essentiel]"], 513.1, "Retenons", hl=513.5, size=96)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 513.3, rot=-3)

S = nxt(514.3)
title(S, ["La Bible nous", "[invite]"], 514.4, "Vivre au jour le jour n'est pas une fatalité", hl=W("invite", 514.3), size=84)
tg(S, 450, "Avoir une réserve", W("réserve", 514.3), "", 34)
tg(S, 530, "Te préparer, comme la fourmi", W("fourmi", 514.3), "", 34)
tg(S, 610, "Connaître l'état de tes finances", W("connaître", 514.3), "", 34)
tg(S, 690, "Agir avec méthode", W("méthode", 514.3), "", 34)
tg(S, 770, "Ne pas vivre dans l'angoisse", W("angoisse", 514.3), "acc", 34)
stk(S, "fourmi-graine", 1250, 260, 340, 515.0)

S = nxt(527.5)
title(S, ["Les cinq", "[étapes]"], 527.6, "Rappel", hl=528.2, size=90)
tg(S, 440, "1 · Décider d'avoir une réserve", W("1", 527.5), "", 32)
tg(S, 520, "2 · Suivre tes dépenses", W("2", 527.5), "", 32)
tg(S, 600, "3 · Trouver ton écart", W("3", 527.5), "", 32)
tg(S, 680, "4 · Un coussin en trois paliers", W("4", 527.5), "", 32)
tg(S, 760, "5 · Automatiser ton épargne", W("5", 527.5), "acc", 32)
stk(S, "liste-cinq-etapes", 1200, 260, 400, 528.0, rot=-1)

S = nxt(542.4)
title(S, ["Une seule chose", "cette [semaine]"], 542.5, "Ton action", hl=W("semaine", 542.4), size=78)
tg(S, 450, "Ouvre ton application bancaire", W("ouvre", 542.4), "", 36)
tg(S, 540, "Note tes dépenses des 7 derniers jours", W("note", 542.4), "acc", 34)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 543.0)
stk(S, "carnet-depenses", 1540, 460, 290, 544.0, rot=3)

S = nxt(548.8)
title(S, ["Le premier [pas],", "puis le suivant"], 548.9, "Pas tout changer d'un coup", hl=W("premier", 548.8) + 0.3, size=78)
tg(S, 450, "Un pas après l'autre", W("suivant", 548.8), "acc", 40)
stk(S, "escalier-trois-paliers", 1100, 250, 400, 549.4)

S = nxt(554.4)
title(S, ["Une petite", "[victoire]"], 554.5, "Remarque-la", hl=W("victoire", 554.4), size=90)
tg(S, 450, "Une semaine sans découvert", W("découvert", 554.4), "", 36)
tg(S, 540, "Le changement est possible", W("possible", 554.4), "acc", 36)
stk(S, "baton-content", 1150, 260, 300, 555.0)
stk(S, "croix-verte", 1560, 340, 220, W("possible", 554.4), rot=4)

S = nxt(561.6)
title(S, ["Ton plus grand", "[obstacle] ?"], 561.7, "Et toi", hl=W("obstacle", 561.6), size=84)
stk(S, "baton-pense", 1150, 230, 260, 562.2)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, W("commentaire", 566.1) - 0.6, 14)
sfx("click", W("commentaire", 566.1) - 0.6, 0.8)
tg(S, 620, "Abonne-toi", W("abonne", 569.4), "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 78.0), ("02", "Passages 1 et 2", 78.0, 180.2), ("03", "Passages 3 et 4", 180.2, 307.0),
              ("04", "Passage 5 et étapes", 307.0, 425.8), ("05", "Pièges et exemple", 425.8, 513.0), ("06", "À retenir", 513.0, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)

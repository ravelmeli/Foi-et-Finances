"""Vidéo longue « Black Friday et Noël : comment ne pas t'endetter (selon la Bible) » — style 02 en 16:9, ~10 min.
5 passages (séquence « Parole » identique), 3 questions à retenir, appel à s'abonner au milieu, 5 étapes, 5 pièges, exemple (Camille et Hugo), récapitulatif.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Black Friday et Noël sans dettes", "lang": "fr"}
COLS, ROWS = 10, 9
VOICE_END = 580.6
s.setup(here=HERE, duration=596.0, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
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
title(S, ["Black Friday,", "puis [Noël]"], 0.1, "Dans quelques jours", hl=W("noël", 0.0), size=90)
tg(S, 450, "Les promotions", W("promotions", 0.0), "", 36)
tg(S, 530, "Les publicités", W("publicités", 0.0), "", 36)
tg(S, 610, "Les cadeaux à acheter", W("cadeaux", 0.0), "acc", 36)
stk(S, "baton-tente-promo", 1100, 220, 480, 0.6, rot=-2)

S = nxt(11.4)
title(S, ["Décembre dépasse", "le [budget]"], 11.5, "Chaque année", hl=W("rembourser", 11.4), size=84)
tg(S, 450, "Plus que prévu", W("prévu", 11.4), "", 38)
tg(S, 540, "Janvier à rembourser", W("janvier", 11.4), "", 38)
tg(S, 630, "Le crédit tente de plus en plus", W("crédit", 11.4), "acc", 34)
stk(S, "pile-factures", 1100, 270, 340, 12.0)

S = nxt(21.2)
title(S, ["Une fête de [joie],", "pas de stress"], 21.3, "Noël devrait être", hl=W("joie", 21.2), size=78)
tg(S, 450, "Joie", W("joie", 21.2) + 0.2, "", 38)
tg(S, 530, "Paix", W("paix", 21.2), "", 38)
tg(S, 610, "Partage", W("partage", 21.2), "acc", 38)
stk(S, "famille-repas-noel", 1000, 260, 640, 21.8)

S = nxt(27.3)
title(S, ["La [pression]", "est partout"], 27.4, "Courriels, affiches, réseaux", hl=W("pression", 27.3), size=84)
tg(S, 450, "Les courriels", W("courriels", 27.3), "", 36)
tg(S, 530, "Les affiches", W("affiches", 27.3), "", 36)
tg(S, 610, "Les réseaux sociaux", W("réseaux", 27.3), "", 36)
tg(S, 690, "« Maintenant ou jamais »", W("jamais", 27.3), "acc", 36)
stk(S, "baton-presse", 1100, 250, 440, 28.0, rot=-2)

S = nxt(34.5)
title(S, ["Au [programme]"], 34.6, "Dans cette vidéo", hl=35.2)
tg(S, 420, "5 passages", W("cinq", 34.5, 0), "", 40)
tg(S, 510, "5 étapes concrètes", W("cinq", 34.5, 1), "", 40)
tg(S, 600, "Les pièges à éviter", W("pièges", 34.5), "", 40)
tg(S, 690, "Un exemple", W("exemple", 34.5), "acc", 40)
stk(S, "pupitre-parole", 1100, 260, 380, 35.2, rot=-2)

S = nxt(44.9)
title(S, ["Un budget en", "[10 minutes]"], 45.0, "Reste jusqu'à la fin", hl=W("dix", 44.9), size=90)
tg(S, 450, "Un budget de Noël très simple", W("budget", 44.9), "", 36)
tg(S, 540, "La règle des fausses bonnes affaires", W("règle", 44.9), "acc", 34)
stk(S, "budget-papier-noel", 1100, 250, 440, 45.6, rot=-2)

S = nxt(52.2)
title(S, ["Pas un conseil", "[personnalisé]"], 52.3, "Une précision importante", hl=W("personnalisé", 52.2), size=78)
tg(S, 450, "Une réflexion biblique générale", W("réflexion", 52.2), "", 36)
tg(S, 540, "À adapter à ta situation", W("adaptes", 52.2), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 53.0)
hit(W("personnalisé", 52.2), 0.8)

# ================================================================ 02 · Passage 1 : Luc 2.7
parole(61.2, "Luc 2.7", 63.3,
       f"« Elle enfanta {m(0, 'son fils premier-né')} ; elle l'emmaillota, et le coucha {m(1, 'dans une crèche')}. »",
       65.6, 70.3, [W("premier", 65.6), W("crèche", 65.6)], size=50)

S = nxt(70.4)
title(S, ["Noël commence", "dans la [simplicité]"], 70.5, "Dès le début", hl=W("simplicité", 70.4), size=72)
tg(S, 450, "Pas de luxe", W("luxe", 70.4), "", 38)
tg(S, 540, "Pas de grande fête", W("fête", 70.4), "", 38)
tg(S, 630, "Une crèche", W("crèche", 70.4), "acc", 40)
stk(S, "creche-simple", 1050, 250, 420, 71.0, rot=-2)

S = nxt(77.3)
title(S, ["Un lieu", "[simple]"], 77.4, "Dieu aurait pu choisir un palais", hl=W("modeste", 77.3), size=96)
tg(S, 450, "Un palais ?", W("palais", 77.3), "", 38)
tg(S, 540, "Une famille modeste", W("modeste", 77.3), "", 38)
tg(S, 630, "Ce qui a de la valeur", W("valeur", 77.3), "acc", 38)
stk(S, "baton-priere", 1100, 260, 300, 78.0)

S = nxt(84.7)
title(S, ["Pas des", "[vitrines]"], 84.8, "Le premier Noël", hl=W("vitrines", 84.7), size=100)
tg(S, 450, "Humilité", W("humilité", 84.7), "", 38)
tg(S, 540, "Amour", W("amour", 84.7), "", 38)
tg(S, 630, "Présence", W("présence", 84.7), "acc", 38)
stk(S, "baton-vitrine", 1100, 250, 380, 85.3)

S = nxt(91.6)
title(S, ["Au centre :", "la [personne]"], 91.7, "Pas supprimer les cadeaux", hl=W("centre", 91.6), size=90)
tg(S, 450, "Pas la dépense", W("dépense", 91.6), "", 38)
tg(S, 540, "La personne qu'on célèbre", W("célèbre", 91.6), "acc", 38)
stk(S, "cadeau-fait-main", 1100, 280, 440, 92.2, rot=-2)

S = nxt(99.5)
title(S, ["Étape 1 :", "[pourquoi] Noël ?"], 99.6, "Première étape", hl=W("pourquoi", 99.5), size=90)
tg(S, 450, "Te rappeler pourquoi tu fêtes", W("rappeler", 99.5), "", 36)
tg(S, 540, "En haut de ta feuille de budget", W("feuille", 107.5), "acc", 36)
stk(S, "baton-pense", 1150, 230, 270, 100.2)

# ================================================================ 03 · Passage 2 : Romains 12.2
parole(114.8, "Romains 12.2", 116.8,
       f"« {m(0, 'Ne vous conformez pas')} au siècle présent, mais {m(1, 'soyez transformés')} par le renouvellement de l'intelligence. »",
       119.7, 126.1, [W("conformez", 119.6), W("transformés", 119.7)], size=48)

S = nxt(126.2)
title(S, ["Acheter [plus],", "offrir plus ?"], 126.3, "Le monde nous répète", hl=W("impressionner", 126.2), size=88)
tg(S, 450, "Acheter plus", W("acheter", 126.2), "", 38)
tg(S, 540, "Offrir plus", W("offrir", 126.2), "", 38)
tg(S, 630, "Impressionner plus", W("impressionner", 126.2), "acc", 38)
stk(S, "baton-tente-promo", 1100, 250, 420, 126.9, rot=-2)

S = nxt(138.5)
title(S, ["Se conformer,", "ou être [transformé]"], 138.6, "Deux choix", hl=W("transformé", 138.5), size=78)
tg(S, 450, "Suivre le mouvement sans réfléchir", W("mouvement", 138.5), "", 34)
tg(S, 540, "Décider calmement", W("calmement", 138.5), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 139.2)

S = nxt(146.7)
title(S, ["Que veux-tu", "[vraiment] faire ?"], 146.8, "Avant le Black Friday", hl=W("vraiment", 146.7), size=84)
tg(S, 450, "De ton argent, cette année", W("argent", 146.7), "acc", 38)
stk(S, "baton-tiraille", 1150, 250, 300, 147.4)

S = nxt(152.9)
title(S, ["Si cette vidéo", "t'[aide]…"], 153.0, "Un instant", hl=W("aide", 152.9))
tg(S, 450, "Abonne-toi", W("abonne", 152.9) + 0.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", W("chaque", 156.0) + 0.2, "", 34)
stk(S, "croix-verte", 1200, 280, 260, 153.8, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 154.2, rot=2)
bw("Abonne-toi", W("abonne", 152.9) + 0.4, 1.0)

# ================================================================ 04 · Passage 3 : Luc 12.15
parole(161.5, "Luc 12.15", 163.5,
       f"« Gardez-vous avec soin de {m(0, 'toute avarice')} ; car la vie d'un homme, fût-il dans l'abondance, {m(1, 'ne dépend pas de ses biens')}. »",
       166.1, 172.3, [W("avarice", 166.1), W("dépend", 166.1)], size=46)

S = nxt(172.4)
title(S, ["Toujours", "[plus] ?"], 172.5, "L'avarice", hl=W("avarice", 172.4), size=110)
tg(S, 450, "L'envie d'avoir toujours plus", W("toujours", 172.4), "", 36)
tg(S, 540, "Stimulée pendant les soldes", W("soldes", 172.4), "acc", 36)
stk(S, "baton-fardeau", 1100, 260, 320, 173.0)

S = nxt(179.3)
title(S, ["Ton bonheur,", "pas dans l'[écran]"], 179.4, "Ni sous le sapin", hl=W("écran", 179.3), size=84)
tg(S, 450, "Pas du nombre de cadeaux", W("nombre", 179.3), "", 36)
tg(S, 540, "Ni de la taille de l'écran", W("taille", 179.3), "acc", 36)
stk(S, "baton-serein", 1100, 260, 300, 179.9)

S = nxt(184.6)
title(S, ["Une bonne affaire,", "[deux] conditions"], 184.7, "Pour être une bonne affaire", hl=W("payer", 184.6), size=78)
tg(S, 450, "Tu en avais besoin", W("besoin", 184.6), "", 38)
tg(S, 540, "Tu peux payer", W("payer", 184.6), "acc", 38)
stk(S, "etiquette-prix-gonfle", 1100, 260, 400, 185.2, rot=-2)

S = nxt(190.2)
title(S, ["Promotion,", "pas [économie]"], 190.3, "Pas prévu, pas économisé", hl=W("économie", 190.2), size=90)
tg(S, 450, "Pas prévu : c'est une dépense", W("dépense", 190.2), "", 36)
tg(S, 540, "Le test : sans réduction, l'achèterais-tu ?", W("test", 195.6), "acc", 30)
stk(S, "loupe-depenses", 1100, 260, 400, 190.8, rot=-2)

# ================================================================ 05 · Passage 4 : Proverbes 28.22
parole(202.4, "Proverbes 28.22", 204.4,
       f"« L'homme envieux est {m(0, 'impatient de s’enrichir')}, et il ne sait pas que {m(1, 'la disette')} viendra sur lui. »",
       206.9, 213.2, [W("impatient", 206.9), W("disette", 206.9)], size=50)

S = nxt(213.3)
title(S, ["L'[impatience]", "du Black Friday"], 213.4, "Tout te pousse", hl=W("impatience", 213.3), size=84)
tg(S, 450, "Le compte à rebours", W("rebours", 213.3), "", 36)
tg(S, 540, "Le stock limité", W("stock", 213.3), "", 36)
tg(S, 630, "L'offre qui se termine ce soir", W("soir", 213.3), "acc", 36)
stk(S, "sablier-offre-limitee", 1100, 250, 400, 214.0, rot=-2)

S = nxt(220.1)
title(S, ["Faite pour t'empêcher", "de [réfléchir]"], 220.2, "Cette pression", hl=W("réfléchir", 220.1), size=72)
tg(S, 450, "Une offre pressante cache une idée", W("pressante", 220.1), "", 32)
tg(S, 540, "La sagesse : prendre le temps", W("sagesse", 227.4), "acc", 36)
stk(S, "baton-attend", 1100, 260, 400, 220.8)

S = nxt(232.9)
title(S, ["Offre disparue ?", "[Presque] rien perdu"], 233.0, "Rassure-toi", hl=W("presque", 232.9), size=78)
tg(S, 450, "D'autres occasions toute l'année", W("occasions", 232.9), "acc", 34)
stk(S, "baton-patient-calme", 1100, 260, 400, 233.6)

# ================================================================ 06 · Passage 5 : Actes 20.35
parole(243.5, "Actes 20.35", 245.5,
       f"« Il y a {m(0, 'plus de bonheur à donner')} {m(1, 'qu’à recevoir')}. »",
       248.4, 251.2, [W("bonheur", 248.4), W("recevoir", 248.4)], size=60)

S = nxt(251.3)
title(S, ["La logique", "[renversée]"], 251.4, "Paul rapporte une parole de Jésus", hl=W("renverse", 251.3), size=90)
tg(S, 450, "Pas : ce que je peux obtenir", W("logique", 251.3), "", 34)
tg(S, 540, "Mais : ce que je peux offrir", W("tourne", 251.3), "acc", 34)
stk(S, "coeur-receptacle", 1100, 270, 340, 252.0, rot=-3)

S = nxt(257.3)
title(S, ["Le vrai esprit", "de [Noël]"], 257.4, "Le bonheur", hl=W("esprit", 257.3), size=90)
tg(S, 450, "Pas ce qu'on reçoit", W("reçoit", 257.3), "", 38)
tg(S, 540, "Ce qu'on offre", W("offre", 257.3), "acc", 40)
stk(S, "baton-donne", 1100, 250, 400, 257.9)

S = nxt(261.9)
title(S, ["Offrir sans", "[dépenser] cher"], 262.0, "Ça ne coûte pas forcément cher", hl=W("cher", 261.9), size=84)
tg(S, 440, "Un moment partagé", W("moment", 261.9), "", 36)
tg(S, 520, "Un repas", W("repas", 261.9), "", 36)
tg(S, 600, "Un mot sincère", W("sincère", 261.9), "", 36)
tg(S, 680, "Un objet fait main", W("fait", 261.9), "acc", 36)
stk(S, "baton-offre-temps", 1050, 270, 540, 262.6, rot=-2)

# ================================================================ 07 · Cinq étapes
S = nxt(282.3)
title(S, ["Cinq [étapes]", "pour traverser Noël"], 282.4, "Passons à la pratique", hl=W("étapes", 282.3), size=78)
counter(S, 80, 450, 0, 5, 283.4, 0.9, " étapes", 130)
stk(S, "liste-cinq-etapes", 1100, 240, 380, 283.0, rot=-1)

S = nxt(288.3)
title(S, ["Étape 1 :", "ton [budget]"], 288.4, "Avant les promotions", hl=W("budget", 288.3), size=96)
tg(S, 440, "Un montant total", W("montant", 288.3), "", 36)
tg(S, 520, "Que tu peux vraiment payer, sans crédit", W("crédit", 288.3), "", 32)
tg(S, 600, "Écrit sur une feuille", W("feuille", 288.3), "", 36)
tg(S, 680, "Une marge pour les imprévus", W("marge", 297.1), "acc", 36)
stk(S, "budget-papier-noel", 1100, 260, 440, 289.0, rot=-2)

S = nxt(304.6)
title(S, ["Le budget en", "[10 minutes]"], 304.7, "Promis", hl=W("dix", 304.6), size=90)
tg(S, 440, "1 · Liste les personnes", W("liste", 304.6), "", 32)
tg(S, 520, "2 · Un montant maximum chacune", W("maximum", 304.6), "", 32)
tg(S, 600, "3 · Repas, décoration, déplacements", W("décoration", 304.6), "", 32)
tg(S, 680, "4 · Fais le total", W("total", 304.6), "acc", 32)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 305.2)
stk(S, "carnet-depenses", 1540, 460, 290, 307.0, rot=3)

S = nxt(325.3)
title(S, ["Total trop", "[élevé] ?"], 325.4, "Ne cherche pas un crédit", hl=W("élevé", 325.3), size=100)
tg(S, 450, "Réduis la liste", W("réduis", 325.3), "", 38)
tg(S, 540, "Réduis les montants", W("montants", 325.3), "", 38)
tg(S, 630, "Un seul cadeau par personne", W("seul", 330.8), "acc", 36)
stk(S, "couple-budget", 1100, 260, 440, 326.0, rot=-2)

S = nxt(337.3)
title(S, ["Étape 2 :", "ta [liste]"], 337.4, "Avant les promotions", hl=W("liste", 337.3), size=96)
tg(S, 450, "Pas l'inverse", W("inverse", 337.3), "", 38)
tg(S, 540, "Ce qui est prévu, pas ce qui est en promo", W("prévu", 337.3), "", 32)
tg(S, 630, "Pas sur ta liste ? Passe ton chemin", W("chemin", 345.1), "acc", 34)
stk(S, "baton-liste-cadeaux", 1100, 260, 420, 338.0, rot=-2)

S = nxt(351.7)
title(S, ["Étape 3 :", "[24 heures]"], 351.8, "Compare et attends", hl=W("24", 351.7), size=96)
tg(S, 450, "Pas prévu ? Un jour d'attente", W("règle", 351.7), "acc", 38)
stk(S, "sablier-offre-limitee", 1100, 250, 400, 352.4, rot=-2)

S = nxt(363.4)
title(S, ["Vérifie le", "prix [normal]"], 363.5, "Avant de te réjouir", hl=W("normal", 363.4), size=90)
tg(S, 450, "Certaines réductions partent d'un prix gonflé", W("gonflé", 363.4), "", 30)
tg(S, 540, "Compare plusieurs magasins", W("plusieurs", 367.6), "", 36)
tg(S, 630, "Les frais de livraison", W("livraison", 367.6), "acc", 36)
stk(S, "etiquette-prix-gonfle", 1100, 260, 400, 364.0, rot=-2)

S = nxt(372.3)
title(S, ["Étape 4 :", "pas de [crédit]"], 372.4, "Ni paiement en plusieurs fois", hl=W("crédit", 372.3), size=90)
tg(S, 450, "Remboursé bien après l'avoir oublié", W("oublié", 372.3), "", 32)
tg(S, 540, "Les mensualités réduisent ta marge", W("mensualités", 382.0), "acc", 32)
stk(S, "carte-paiement-fractionne", 1100, 270, 480, 373.0, rot=-2)

S = nxt(389.5)
title(S, ["Étape 5 :", "offre [autrement]"], 389.6, "Et donne aussi", hl=W("autrement", 389.5), size=90)
tg(S, 440, "Du temps", W("temps", 389.5), "", 36)
tg(S, 520, "Un repas", W("repas", 389.5), "", 36)
tg(S, 600, "Un service", W("service", 389.5), "", 36)
tg(S, 680, "Un don à un voisin", W("quartier", 400.1), "acc", 36)
stk(S, "panier-don-voisin", 1100, 260, 440, 390.2, rot=-2)

# ================================================================ 08 · Pièges, grâce
S = nxt(407.2)
title(S, ["Cinq [pièges]", "à éviter"], 407.3, "Attention", hl=W("pièges", 407.2), size=84)
tg(S, 440, "1 · Acheter parce que l'offre se termine", W("offre", 407.2), "", 30)
tg(S, 515, "2 · Impressionner, ne pas être en reste", W("impressionner", 407.2), "", 30)
tg(S, 590, "3 · Tout mettre sur la carte", W("carte", 407.2), "", 30)
tg(S, 665, "4 · Les petits achats qui s'additionnent", W("oublier", 407.2), "", 30)
tg(S, 740, "5 · Culpabiliser d'offrir moins", W("culpabiliser", 407.2), "acc", 30)
stk(S, "drapeau-rouge", 1250, 260, 300, 407.8)

S = nxt(433.2)
title(S, ["Offrir moins,", "pas aimer [moins]"], 433.3, "Rappelle-toi", hl=W("aimer", 433.2), size=84)
tg(S, 450, "Un cadeau modeste, offert avec amour", W("modeste", 433.2), "acc", 32)
stk(S, "baton-content", 1100, 260, 300, 433.8)

S = nxt(442.3)
title(S, ["Trop dépensé ?", "Pas de [condamnation]"], 442.4, "Si c'est déjà fait", hl=W("condamne", 442.3), size=72)
tg(S, 440, "Regarde le montant", W("montant", 442.3), "", 34)
tg(S, 520, "Un plan de remboursement", W("remboursement", 442.3), "", 34)
tg(S, 600, "Recommence plus sagement", W("recommence", 442.3), "", 34)
tg(S, 680, "La grâce autant que la sagesse", W("grâce", 442.3), "acc", 34)
stk(S, "colombe", 1100, 270, 300, 443.0, rot=3)
stk(S, "croix-verte", 1560, 340, 220, W("grâce", 442.3), rot=4)

# ================================================================ 09 · Exemple : Camille et Hugo
S = nxt(460.1)
title(S, ["Un exemple :", "[Camille] et Hugo"], 460.2, "Prenons", hl=W("Camille", 460.1), size=78)
tg(S, 450, "Trois enfants, un budget serré", W("enfants", 461.6), "", 36)
tg(S, 540, "Toujours plus dépensé que prévu", W("prévu", 461.6), "acc", 36)
stk(S, "famille-sortie", 1050, 270, 560, 460.8)

S = nxt(467.7)
title(S, ["Ils écrivent ce", "qu'ils [peuvent]"], 467.8, "Cette année", hl=W("peuvent", 467.7), size=84)
tg(S, 450, "300 € pour les cadeaux et le repas", W("trois", 467.7), "acc", 34)
stk(S, "budget-papier-noel", 1100, 260, 420, 468.4, rot=-2)

S = nxt(474.9)
title(S, ["Un seul article", "[de la liste]"], 475.0, "Pendant le Black Friday", hl=W("article", 474.9), size=84)
tg(S, 450, "Parce que le prix est vraiment plus bas", W("bas", 474.9), "acc", 32)
stk(S, "baton-liste-cadeaux", 1100, 260, 400, 475.6, rot=-2)

S = nxt(481.4)
title(S, ["Offrir du", "[temps]"], 481.5, "Ils décident aussi", hl=W("temps", 481.4), size=96)
tg(S, 450, "Une sortie en famille", W("sortie", 481.4), "", 36)
tg(S, 540, "Un jeu de société", W("jeu", 481.4), "", 36)
tg(S, 630, "Un repas avec des voisins", W("voisins", 481.4), "acc", 36)
stk(S, "baton-offre-temps", 1050, 270, 540, 482.0, rot=-2)

S = nxt(495.4)
title(S, ["Noël", "[sans dette]"], 495.5, "Le jour de Noël", hl=W("dette", 495.4), size=104)
tg(S, 450, "Des souvenirs", W("souvenirs", 495.4), "", 38)
tg(S, 540, "Un janvier tranquille", W("janvier", 495.4), "acc", 38)
tg(S, 630, "La feuille gardée pour l'année suivante", W("gardent", 500.3), "", 30)
stk(S, "famille-repas-noel", 1000, 260, 640, 496.0)

S = nxt(505.5)
title(S, ["Un [exemple],", "pas un témoignage"], 505.6, "À retenir", hl=W("exemple", 505.5), size=78)
tg(S, 450, "Aucune méthode ne garantit un résultat", W("garantit", 505.5), "acc", 32)
tg(S, 540, "Décider avant, plutôt que réagir", W("décider", 515.5), "", 34)
stk(S, "colombe", 1100, 280, 300, 506.2, rot=3)

# ================================================================ 10 · Récapitulatif et action
S = nxt(522.5)
title(S, ["L'[essentiel]"], 522.6, "Retenons", hl=523.0, size=96)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 522.8, rot=-3)

S = nxt(524.8)
title(S, ["Ce qu'on [retient]"], 524.9, "Noël sans pression", hl=W("simplicité", 524.8), size=96)
tg(S, 420, "Noël commence dans la simplicité", W("simplicité", 524.8), "", 32)
tg(S, 500, "Ne pas se conformer à la pression", W("conformer", 524.8), "", 32)
tg(S, 580, "Le bonheur ne dépend pas des achats", W("achats", 524.8), "", 32)
tg(S, 660, "L'impatience coûte cher", W("impatience", 524.8), "", 32)
tg(S, 740, "Plus de bonheur à donner qu'à recevoir", W("recevoir", 524.8), "acc", 30)
stk(S, "creche-simple", 1250, 260, 330, 525.4)

S = nxt(537.9)
title(S, ["Les cinq", "[étapes]"], 538.0, "Rappel", hl=538.6, size=90)
tg(S, 440, "1 · Fixer ton budget avant les promos", W("1", 537.9), "", 32)
tg(S, 520, "2 · Faire ta liste de cadeaux", W("2", 537.9), "", 32)
tg(S, 600, "3 · Comparer et attendre 24 heures", W("3", 537.9), "", 32)
tg(S, 680, "4 · Éviter crédit et paiement fractionné", W("4", 537.9), "", 32)
tg(S, 760, "5 · Offrir autrement et donner", W("5", 537.9), "acc", 32)
stk(S, "liste-cinq-etapes", 1200, 260, 400, 538.4, rot=-1)

S = nxt(553.8)
title(S, ["Une seule chose", "cette [semaine]"], 553.9, "Ton action", hl=W("semaine", 553.8), size=78)
tg(S, 450, "Prends une feuille", W("feuille", 553.8), "", 38)
tg(S, 540, "Écris ton montant total", W("montant", 553.8), "", 38)
tg(S, 630, "Note-le sur ton téléphone", W("téléphone", 553.8), "acc", 38)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 554.4)
stk(S, "carnet-depenses", 1540, 460, 290, 555.4, rot=3)

S = nxt(560.6)
title(S, ["Joie, [sagesse],", "sans dette"], 560.7, "Tu n'as pas à faire comme tout le monde", hl=W("sagesse", 560.6), size=84)
tg(S, 450, "Un temps de joie", W("joie", 565.8), "", 38)
tg(S, 540, "De reconnaissance", W("reconnaissance", 565.8), "", 38)
tg(S, 630, "De paix", W("paix", 565.8), "acc", 38)
stk(S, "baton-patient-calme", 1100, 260, 400, 561.2)
stk(S, "croix-verte", 1560, 340, 220, W("paix", 565.8), rot=4)

S = nxt(571.6)
title(S, ["Ta plus grande", "[tentation] ?"], 571.7, "Et toi", hl=W("tentation", 571.6), size=84)
stk(S, "baton-pense", 1150, 230, 260, 572.2)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, W("commentaire", 574.7) - 0.6, 14)
sfx("click", W("commentaire", 574.7) - 0.6, 0.8)
tg(S, 620, "Abonne-toi", W("abonne", 577.8), "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 61.2), ("02", "Passages 1 et 2", 61.2, 161.5), ("03", "Passages 3 à 5", 161.5, 282.3),
              ("04", "Cinq étapes", 282.3, 407.2), ("05", "Pièges et exemple", 407.2, 522.5), ("06", "À retenir", 522.5, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)

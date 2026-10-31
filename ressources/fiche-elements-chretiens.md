# Fiche de style — éléments chrétiens dans les vidéos Foi et Finances

Objectif : que le spectateur reconnaisse la chaîne comme chrétienne dès les premières secondes, sans alourdir l'image et sans jamais promettre de richesse par la foi.

## 1. Principe : une présence discrète et récurrente

| Niveau | Où | Quoi |
| --- | --- | --- |
| Signature | toutes les vidéos | croix du logo à côté de « FOI ET FINANCES » (haut gauche) et sur la carte de fin. Nécessite le fichier du logo. |
| Station « verset » | 1 par vidéo (2 max.) | modèle fixe ci-dessous. |
| Objet ancien ou manuscrit | 1 à 2 apparitions par vidéo | photo libre de droits en autocollant (section 4). |
| Reste de la vidéo | scènes de dettes, dépenses, budget, couple | **aucun** symbole religieux : on reste concret, pour ne pas donner l'impression de juger. |

## 2. Modèle fixe de la station « verset »

À garder identique d'une vidéo à l'autre (déjà en place dans les Shorts « Proverbes 21.20 » et « Amos 3.3 »).

1. Kicker : « La Parole ».
2. Titre court : un mot clé souligné en vert (ex. « Marcher [ensemble] »).
3. Bandeau vert avec la référence exacte : « Proverbes 21.20 », « Amos 3.3 »…
4. Verset en grand, un à deux mots-clés soulignés au moment où ils sont prononcés.
5. Référence de traduction en petit : « LSG 1910 ».
6. Un autocollant : objet ancien (monnaie, vase) ou manuscrit/livre (section 4).
7. Sous-titres coupés pendant la citation (`suppress`).

Règles de texte : un seul verset principal par Short, le texte exact avec livre, chapitre et verset, jamais un verset inventé ni déformé. Vérifier la traduction avant de publier.

## 3. Ce qui est permis et ce qui est interdit

**Permis**
- Photos de manuscrits, pages de Bible, rouleaux, papyrus, psautiers (musées, CC0).
- Objets antiques : monnaies, vases, balances, tablettes.
- Un livre fermé ou ouvert sans texte lisible, dessiné.
- Une croix simple et sobre dans la signature, la carte de fin et la miniature.
- Typographie du verset en grand : c'est l'élément « religieux » principal.

**Interdit**
- Représenter Jésus, Dieu, le Saint-Esprit ou des anges (visages, mains célestes, halos, rayons de lumière divine). Ne pas cadrer en gros plan une miniature qui représente le Christ ou un saint, même si le manuscrit est libre de droits.
- Imagerie « évangile de la prospérité » : pluie de pièces, lumière dorée sur de l'argent, personnage béni qui s'enrichit.
- Vitraux, églises, mains jointes en stock : trop décoratif, effet kitsch.
- Symboles religieux dans les scènes de difficulté (dette, dispute de couple) : cela peut donner l'impression de culpabiliser.
- Texte ou mots lisibles dans les images générées par IA.

## 4. Première sélection de photos (Met Open Access, CC0)

Sources dans `ressources/photos-chretiennes/sources/`, autocollants dans `ressources/photos-chretiennes/stickers/` (détourage automatique, quelques bords irréguliers à reprendre avant usage définitif).

| Fichier source | Objet | Usage conseillé | Autocollant |
| --- | --- | --- | --- |
| `met-466297` | Bible française, vers 1250-75, ouverte | station verset, ouverture « La Bible dit » | `bible-ouverte.png` |
| `met-466281` | Page de Bible enluminée, vers 1280-1300 | station verset, version sobre | `page-bible-enluminee.png` |
| `met-469985` | Début du livre de Néhémie (Bible) | sujets travail, reconstruction, planification | à détourer |
| `met-470122` | Début de l'épître aux Éphésiens | sujets sur la famille, la vie quotidienne | à détourer |
| `met-474236` | Psautier byzantin, fin XIIe s. | sujets psaumes, sagesse (éviter le médaillon central : il figure un saint) | `psautier-byzantin.png` |
| `met-479659` | Fragment de papyrus copte, VIe-VIIe s. | idée d'« Écriture ancienne » | `papyrus-copte.png` |
| `met-926689` | Rouleau d'Esther et son étui, XVIIIe s. | sujets Esther, les rouleaux de la Parole | `rouleau-esther-etui.png` |

Déjà utilisés ailleurs : statère en or (247144), tétradrachme en argent (247146), lécythe (255214). Crédits complets : `ressources/photos-chretiennes/sources/credits-brouillon.md` (le CC0 n'impose pas d'attribution, mais on garde la trace).

Pour chercher d'autres photos : `python3 -I kit-style-02/outils/met_search.py chercher "<mots anglais>"`, puis `telecharger <id>`. Ne garder que les objets marqués CC0 / domaine public.

## 5. Images générées par IA (Nano Banana)

- Le mot **« Bible »** dans un prompt a bloqué une planche. Éviter : préférer « closed old book with a ribbon bookmark » ou utiliser une photo du Met.
- Éviter « praying », « angel », « God », « Jesus », « halo », « holy light ».
- Garder le bloc de style de la chaîne et la consigne « no text, no letters, no numbers, no logos ».

## 6. Ton, pour éviter l'effet « prosélyte » ou « promesse »

- Le religieux sert la sagesse pratique, jamais une promesse de richesse.
- Pas de culpabilisation visuelle ni dans les mots (dettes, pauvreté, difficultés de couple).
- Une phrase d'ouverture vers l'aide (conseiller, pasteur) quand le sujet est sensible.

## 7. Liste de contrôle avant de monter une vidéo

- [ ] Un seul verset, référence exacte, traduction vérifiée.
- [ ] Station verset conforme au modèle (section 2).
- [ ] 1 à 2 éléments chrétiens seulement dans le reste de la vidéo, aucun dans les scènes de difficulté.
- [ ] Aucun visage du Christ ni de saint en gros plan.
- [ ] Crédits des photos notés dans `credits-brouillon.md`.
- [ ] Disclaimer présent dans la description (`ressources/disclaimer.md`).
- [ ] Croix du logo sur la carte de fin (quand le logo est fourni).

## 8. Personnage récurrent (remplacé)

> **Remplacé par `ressources/fiche-style-definitive.md` :** les nouvelles vidéos utilisent des bonhommes bâtons, la Bible à la croix et des euros. Le texte ci-dessous ne vaut plus que pour les vidéos déjà montées.


À partir du Short « L'argent est-il une bénédiction ou une tentation ? », le personnage principal est **un homme à la peau claire** :
`a man in his early thirties with short wavy light brown hair, fair light skin with a warm peach tone, a navy blue sweater with a green collar edge, beige trousers and white sneakers`.
- Pour un couple : la femme est aussi à la peau claire (ex. `a woman in her early thirties with shoulder-length wavy chestnut hair, fair light skin, a terracotta sweater, dark blue jeans and white sneakers`).
- Les vidéos déjà montées gardent leur personnage d'origine (peau brune) ; on ne mélange pas les deux dans une même vidéo.
- Une fois ce personnage choisi, on ne change plus sa description d'une vidéo à l'autre.

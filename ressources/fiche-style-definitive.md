# Fiche de style définitive — Foi et Finances

Valable pour toutes les nouvelles vidéos (Shorts 9:16 et vidéos longues 16:9). Elle remplace les règles de personnage et d'éléments chrétiens des fiches précédentes quand elles se contredisent.
Établie à partir des 20 images des anciennes vidéos de la chaîne (`ressources/references-anciennes/`).

## 1. Ce qui ne change pas
- Le montage du kit style 02 : caméra continue, une station par moment du récit, sous-titres mot par mot, mode sombre pour la question finale, carte de fin « Foi et [Finances] ».
- L'accent vert `#178A4A` et la police Inter.
- Le verset : un seul par Short, texte exact affiché en grand avec sa référence, sous-titres coupés pendant la citation.
- Tout le texte lisible est ajouté au montage, jamais dans les images générées.
- Le disclaimer court dans chaque description (`ressources/disclaimer.md`).

## 2. Personnage : retour aux bonhommes bâtons
C'est l'identité d'origine de la chaîne. Description fixe, à copier telle quelle dans chaque prompt :

`a simple stick figure character with a large perfectly round white head outlined in thick black, minimal face (two small dot eyes, simple eyebrows, a small expressive mouth), thin black line body and limbs, small white rounded feet, no hair, no clothes except when stated, no skin color`

- Expressions lisibles et variées : soucieux, pensif (main au menton), serein (yeux fermés), joyeux, tiraillé.
- **Signe chrétien porté :** une petite croix au cou (`a tiny simple cross pendant on a thin black cord around the neck`) dans les poses de foi, de sagesse et de paix. Pas dans les poses de difficulté.
- Personnages secondaires (famille, couple, enfants) : même langage graphique. Variante autorisée pour la famille : silhouettes simples avec cheveux et vêtements pastel, comme dans la scène du repas.
- Plus de personnage à peau claire ou à peau brune détaillé : ces versions restent seulement dans les vidéos déjà montées.

## 3. Bloc de style des images (Nano Banana)
`Clean minimalist hand-drawn 2D illustration in a clear-line stickman explainer style, thick clean black outlines, flat soft colors, light pastel blue and soft green accents, warm golden coins, plenty of white space.`

Toujours : fond blanc pur, 2048 × 2048, éléments bien séparés pour la découpe, et la fin de prompt :
`No text, no letters, no numbers, no writing, no dollar signs, no logos, no watermark, no shadows on the background, no photorealism.`

## 4. Les 6 repères chrétiens (présents dans chaque vidéo)
| # | Repère | Où | Comment |
| --- | --- | --- | --- |
| 1 | **Bible à la croix** | 3 à 4 stations : posée sur la table, tenue ouverte comme guide, sur un pupitre | autocollant de la planche « kit chrétien » ; jamais le mot « Bible » dans le prompt |
| 2 | **Pupitre ou piédestal de la Parole** | station du choix, station verset | Bible ouverte sur pupitre en bois, petites croix vertes autour |
| 3 | **Petites croix flottantes** | arrière-plan de chaque station | automatiques dans le moteur (`THEME["crosses"]`, couleur `THEME["cross"]`) : 6 croix vert pâle par station, semi-transparentes, lente dérive ; jamais générées |
| 4 | **Geste de foi** | au moins une station par vidéo | bonhomme mains jointes yeux fermés, ou famille qui prie avant le repas, ou lecture |
| 5 | **Cœur** | quand le sujet touche l'attachement | cœur réceptacle avec des pièces, cœur relié par un fil rouge au tas de pièces, cœur ligoté |
| 6 | **Croix de signature** | haut d'écran et carte de fin | croix verte simple, automatique dans le moteur (signature et carte de fin) |

## 5. Codes couleur
- **Vert** = Dieu, la Parole, la paix, la croissance (croix vertes, halo vert léger autour de la Bible, feuilles, plantes).
- **Rouge / orange** = l'argent qui domine, le danger, l'attachement (fil rouge, lueur rouge sur l'argent, éclair de coupure).
- **Bleu pâle** = décor neutre (fonds, croix flottantes, flèches).
- **Doré** = les pièces.

## 6. Monnaie : euros
- Pièces dorées et argentées de style euro (deux tons, sans chiffres lisibles) et billets aux couleurs des euros, sans texte.
- Dans le prompt : `euro-style coins with a two-tone gold and silver look, no readable numbers` et `banknotes in soft euro colors, no text`.
- **Jamais de « $ »**. L'idole de l'argent se dessine comme une haute pile de pièces dorées sur un piédestal, pas comme un symbole dollar.
- Si un symbole est indispensable, « € » est ajouté au montage.

## 7. Mises en scène signature (à réutiliser)
1. **Les deux maîtres** : piédestal de l'argent (pièces, billets) à gauche, pupitre de la Parole à droite, bonhomme tiraillé au milieu. Pour Matthieu 6:24 et tout sujet de priorité.
2. **La Bible et le budget côte à côte** : bureau avec enveloppe de salaire, carnet de budget, pièces, Bible, plante.
3. **Le cœur et l'argent** : cœur réceptacle ou relié aux pièces par un fil rouge.
4. **Le repas en famille** : famille qui prie avant le repas, Bible ouverte sur un meuble, portefeuille et pièces au sol.
5. **Le bonhomme lecteur** : assis sur un banc ou debout, Bible ouverte, mot-clé à côté.

## 8. Ce qu'on garde comme limites
- Aucun visage de Jésus ou de Dieu, aucun halo au-dessus d'une tête, aucune main céleste.
- Pas d'imagerie de prospérité : pluie d'or, lumière divine sur l'argent, Bible qui rapporte de l'argent.
- La main sombre avec une chaîne (l'argent maître) : une fois de temps en temps au maximum, jamais effrayante.
- Pas de symbole religieux posé sur une scène de dette ou de pauvreté : le bonhomme en difficulté n'est jamais jugé.

## 9. Liste de contrôle avant montage
- [ ] Bonhomme bâton conforme à la description fixe
- [ ] Bible à la croix présente dans 3 stations au moins
- [ ] Croix flottantes activées dans le montage
- [ ] Un geste de foi au moins
- [ ] Monnaie en euros, aucun « $ »
- [ ] Aucun texte dans les images générées
- [ ] Un seul verset, traduction vérifiée
- [ ] Disclaimer court dans la description

## 10. Rétention (moteur et méthode, depuis « Besoin ou envie » v2)
Automatique dans le moteur :
- **Mouvement permanent** : chaque autocollant flotte et se balance jusqu'à la fin (`THEME["idle"]`).
- **Zoom-impact** sur chaque temps fort `hit()` (`THEME["punch"]`).
- **Sous-titres cinétiques** : 3 mots maximum, entrée en rebond, texte plus gros.
- **Croix flottantes** et croix de signature.

À utiliser dans chaque `build.py` :
- `bigword("Envie", T("envie"))` : mot géant au moment exact où il est prononcé (2 à 5 par vidéo).
- `bump(id, t)` : un élément déjà visible bat sur un mot-clé ; `shake(id, t)` : tremblement (stress).
- `coins(station, x, y, t)` : pièces de style euro qui tombent et rebondissent.
- Un changement visuel toutes les 1,5 à 2 s, jamais de station vide.

Méthode du script :
- **Accroche** dans les 2 premières secondes, puis **boucle ouverte** (« reste jusqu'au bout : la question n°3… ») refermée plus tard par un mot géant.
- **Fin en boucle** : la dernière phrase reprend la question d'ouverture et la caméra revient sur la première station (pas de carte de fin, pas de mode sombre).
- **Silences** : `python3 -I kit-style-02/outils/couper_silences.py montage/<projet>` après la transcription (originaux conservés).
- **Musique** : `python3 -I kit-style-02/outils/gen_musique_libre.py montage/<projet>/assets/audio/music.wav <durée>` — composition synthétisée, libre de droits ; mixée à 0,15 sous la voix.

## 11. Vidéos longues (16:9)
- **Format :** 1920 × 1080, `s.setup(..., fmt="16:9", cols=..., rows=...)`. Le moteur place la barre de chapitres en haut (y = 60) et les sous-titres à y = 880.
- **Mise en page d'une station :** titre et texte à gauche (x 80–900), illustration à droite (x 1000–1840) ; zone de contenu y 300–820 ; rien d'important sous y = 860 (sous-titres) ni dans le coin bas droit (boutons YouTube).
- **Nombre de stations :** une toutes les 5 à 8 s, soit environ 40 pour 5 minutes (toile 5 × 8 ou 6 × 7).
- **Chapitres :** 6 dans la barre du haut, repris en chapitres YouTube horodatés dans la description.
- **Séquence « Parole » :** une par verset (3 à 4 par vidéo), toujours identique : bandeau vert avec la référence, verset en grand à gauche, Bible ouverte à droite, son « spark », sous-titres coupés.
- **Abonnement au milieu :** bandeau « Abonne-toi » animé au moment du CTA oral, sans couper la caméra.
- **Fin :** carte de fin de 15 à 20 s (croix, « Foi et Finances », bouton) avec de l'espace libre pour les écrans de fin YouTube ; la musique continue.
- **Images :** il en faut davantage qu'un Short (3 planches spécifiques par vidéo en plus du kit), réutilisées avec des cadrages et des tailles différents.
- **Voix :** style « Narration » plutôt que « Promote » (plus posé sur la durée) ; voix générée en plusieurs morceaux, puis `couper_silences.py`.

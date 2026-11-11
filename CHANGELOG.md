# Changelog

Format inspiré de [Keep a Changelog](https://keepachangelog.com/).

## [1.6.0] — non publiée (2026-11-09)

### Ajouté

- **Aide → « Contact et support »** (repris d'omega-serv et d'omega-log), depuis l'aide (touche `a`) :
  payer un café (page PayPal), contacter le support (mail et formulaire de contact du site, affichés en
  clair ; aucun formulaire dans l'outil, aucun mail envoyé), se déclarer utilisateur anonyme, vérifier les
  mises à jour. Sans session graphique (SSH), l'adresse s'affiche au lieu d'ouvrir le navigateur.
- **Déclaration anonyme, une seule fois** (omega-suite n'a pas de service qui enverrait chaque jour) : clé
  tirée au hasard, nom et version de l'outil, continent et pays facultatifs (listes fermées, jamais de
  texte libre) ; le message exact est affiché avant l'envoi. Rien n'est enregistré si la réception est
  injoignable. « Ne plus me déclarer » supprime l'entrée à la réception et la clé locale
  (`var/declaration.json`, jamais livrée dans l'archive).
- Une seule déclaration dans la suite, `omega-suite` (`var/declaration.json`), depuis l'Accueil comme
  depuis l'aide d'un onglet ; un outil lancé seul se déclare sous son propre nom. On distingue ainsi
  qui se sert de la suite et qui se sert des outils à part.
- **Vérifier les mises à jour** : compare la version installée à la liste publiée sur le site
  (`download/sha.txt`), seulement sur clic ; « Voir les nouveautés » ouvre le fichier de la dernière
  version.
- README ×17 : section « Contact et support ».
- README ×17 : captures A-D (accueil, menu, aide de la suite, réglages) dans chaque langue ; site en 17 langues (index et readme.html).

### Modifié

- Écrans « Contact et support » et « Se déclarer » partagés dans omega-lib, avec leurs traductions
  (17 langues) : le même écran dans tous les outils omega.

### Corrigé

- Réglages : l'écran est centré comme dans le reste de la suite (le bloc « Langue / Language » prenait
  toute la largeur et repoussait tout à gauche).
- Réglages : plus de notification à l'ouverture de l'écran (« Comme l'interface », profil de rendu) ;
  seul un vrai changement est enregistré et annoncé.
- Langues : les 16 traductions sont validées, la mention « en test » disparaît du sélecteur.

## [1.5.0] — 2026-10-29

### Ajouté

- Interface en 17 langues (français, anglais, espagnol, portugais (Brésil), italien, allemand, néerlandais, polonais, russe, chinois simplifié, vietnamien, thaï, indonésien, japonais, coréen, hindi et arabe). Réglages → « Langue / Language » : la langue choisie dans la suite s'applique aux 7 outils (leurs propres sélecteurs sont alors remplacés par une note), après un redémarrage de l'interface.
- Réglage « Langue des exports » : une seule langue pour les rapports exportés des 7 outils (« Comme l'interface » par défaut), effet immédiat.
- Variable `OMEGA_SUITE_LANG` (par exemple `OMEGA_SUITE_LANG=en ./omega-suite.sh`) pour forcer une langue le temps d'une session.

### Modifié

- Les traductions communes aux outils omega sont partagées dans omega-lib (catalogue `omega-lib`) : un nouvel outil omega en profite sans rien traduire.
- Console texte Linux (TTY) : les langues à écriture non latine s'affichent en anglais pour la session (le réglage est conservé).

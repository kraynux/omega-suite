# Changelog

Format inspiré de [Keep a Changelog](https://keepachangelog.com/).

## [1.5.0] — 2026-10-29

### Ajouté

- Interface en 17 langues (français, anglais, espagnol, portugais (Brésil), italien, allemand, néerlandais, polonais, russe, chinois simplifié, vietnamien, thaï, indonésien, japonais, coréen, hindi et arabe). Réglages → « Langue / Language » : la langue choisie dans la suite s'applique aux 7 outils (leurs propres sélecteurs sont alors remplacés par une note), après un redémarrage de l'interface.
- Réglage « Langue des exports » : une seule langue pour les rapports exportés des 7 outils (« Comme l'interface » par défaut), effet immédiat.
- Variable `OMEGA_SUITE_LANG` (par exemple `OMEGA_SUITE_LANG=en ./omega-suite.sh`) pour forcer une langue le temps d'une session.

### Modifié

- Les traductions communes aux outils omega sont partagées dans omega-lib (catalogue `omega-lib`) : un nouvel outil omega en profite sans rien traduire.
- Console texte Linux (TTY) : les langues à écriture non latine s'affichent en anglais pour la session (le réglage est conservé).

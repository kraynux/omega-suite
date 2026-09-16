#!/usr/bin/env bash
# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
# ==============================================================================
# Script d'installation - OMEGA-SUITE (interface unifiee, D-014/D-015)
# A lancer depuis le dossier omega-suite : cd omega-suite && ./install.sh
# Resilient : peut etre relance sans erreur si une etape a deja ete faite.
#
# Different des 7 outils individuels (D-015 point 2, verifie par inspection
# des 7 pyproject.toml : aucune version epinglee en dur, memes bornes
# compatibles, meme backend hatchling - un seul venv partage est sans
# risque de conflit) : UN SEUL venv accueille omega-lib + les 7 outils +
# omega-suite lui-meme, plutot que 7 venvs isoles.
#
# Ce script ne vendore rien lui-meme (le vendoring est le role de
# build-release.sh) mais sert les DEUX scenarios sans modification :
# - clone de developpement (aucun vendor/) : chaque dependance est
#   installee en editable directement depuis son propre projet
#   ~/DEV/<TOOL>/omega-<tool>, comme avant.
# - archive distribuable (build-release.sh a rempli vendor/<nom>/) :
#   chaque dependance deja vendoree a cote de ce script est preferee,
#   jamais un chemin ~/DEV/ qui n'existe pas hors d'un poste de dev.
# ==============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
WHITE='\033[1;37m'
CYAN='\033[0;36m'
NC='\033[0m'

info() { echo -e "${CYAN}ℹ️  $1${NC}"; }
ok()   { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️  $1${NC}"; }
err()  { echo -e "${RED}❌ $1${NC}"; }
tip()  { echo -e "${WHITE}💡 $1${NC}"; }

echo -e "${WHITE}    ░▒▓█████████████████████████████████████████████████▓▒░${NC}"
echo -e "${WHITE}    ░▒▓ Ω M E G A - S U I T E — I N S T A L L A T I O N ▓▒░${NC}"
echo -e "${WHITE}    ░▒▓█████████████████████████████████████████████████▓▒░${NC}"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
cd "$SCRIPT_DIR"

# -------------------------------------------------------------------------
# 1. Localiser les 8 dependances (omega-lib + 7 outils) : vendor/<nom>/
#    d'abord (archive distribuable, rempli par build-release.sh), sinon
#    ~/DEV/ (clone de developpement) - override possible via variables
#    d'env pour quiconque a une arborescence de developpement differente.
# -------------------------------------------------------------------------
DEV_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

resolve_dep() {
    # $1: nom vendore (vendor/<nom>/) - $2: variable d'env d'override -
    # $3: chemin de repli en developpement (~/DEV/...).
    local vendored="$SCRIPT_DIR/vendor/$1"
    if [ -d "$vendored" ]; then
        echo "$vendored"
    else
        echo "${!2:-$3}"
    fi
}

OMEGA_LIB_SRC="$(resolve_dep omega-lib OMEGA_LIB_SRC "$DEV_ROOT/LIB/omega-lib")"
OMEGA_SCAN_SRC="$(resolve_dep omega-scan OMEGA_SCAN_SRC "$DEV_ROOT/SCAN/omega-scan")"
OMEGA_CHECK_SRC="$(resolve_dep omega-check OMEGA_CHECK_SRC "$DEV_ROOT/CHECK/omega-check")"
OMEGA_DEEP_SRC="$(resolve_dep omega-deep OMEGA_DEEP_SRC "$DEV_ROOT/DEEP/omega-deep")"
OMEGA_FOLD_SRC="$(resolve_dep omega-fold OMEGA_FOLD_SRC "$DEV_ROOT/FOLD/omega-fold")"
OMEGA_STRESS_SRC="$(resolve_dep omega-stress OMEGA_STRESS_SRC "$DEV_ROOT/STRESS/omega-stress")"
OMEGA_TRACK_SRC="$(resolve_dep omega-track OMEGA_TRACK_SRC "$DEV_ROOT/TRACK/omega-track")"
OMEGA_FUZZ_SRC="$(resolve_dep omega-fuzz OMEGA_FUZZ_SRC "$DEV_ROOT/FUZZ/omega-fuzz")"

for pair in "omega-lib:$OMEGA_LIB_SRC" "omega-scan:$OMEGA_SCAN_SRC" "omega-check:$OMEGA_CHECK_SRC" \
            "omega-deep:$OMEGA_DEEP_SRC" "omega-fold:$OMEGA_FOLD_SRC" "omega-stress:$OMEGA_STRESS_SRC" \
            "omega-track:$OMEGA_TRACK_SRC" "omega-fuzz:$OMEGA_FUZZ_SRC"; do
    name="${pair%%:*}"; path="${pair#*:}"
    if [ ! -d "$path" ]; then
        err "$name introuvable : $path"
        # ex: "omega-lib" -> "OMEGA_LIB_SRC" (bug pre-existant corrige au
        # passage : "OMEGA_${name^^}_SRC" produisait "OMEGA_OMEGA-LIB_SRC",
        # un nom de variable invalide et jamais le vrai nom lu plus haut).
        env_suffix="${name#omega-}"
        tip "Ni vendor/$name/ ni un chemin de developpement valide - definissez la variable d'environnement correspondante (ex: OMEGA_${env_suffix^^}_SRC) si votre arborescence differe."
        exit 1
    fi
done
ok "Les 8 dependances (omega-lib + 7 outils) sont localisees."

# -------------------------------------------------------------------------
# 2. Environnement virtuel Python UNIQUE (D-015 point 2)
# -------------------------------------------------------------------------
if [ -d ".venv" ]; then
    info ".venv existe deja, creation ignoree."
else
    if ! python3 -m venv .venv 2>/tmp/omega-suite-venv-err.log; then
        err "Echec de la creation de l'environnement virtuel."
        tip "Sur Debian/Ubuntu (et derivees) : sudo apt install python3-venv"
        cat /tmp/omega-suite-venv-err.log >&2
        rm -f /tmp/omega-suite-venv-err.log
        exit 1
    fi
    rm -f /tmp/omega-suite-venv-err.log
    ok "Environnement virtuel cree (.venv)."
fi

# -------------------------------------------------------------------------
# 3. Dependances - omega-lib d'abord (une seule fois, seul point de verite),
#    puis les 7 outils (chacun trouve omega-lib deja satisfait, ne recupere
#    que ses propres dependances PyPI additionnelles), puis omega-suite.
# -------------------------------------------------------------------------
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q -e "$OMEGA_LIB_SRC"
pip install -q -e "$OMEGA_SCAN_SRC" -e "$OMEGA_CHECK_SRC" -e "$OMEGA_DEEP_SRC" \
              -e "$OMEGA_FOLD_SRC" -e "$OMEGA_STRESS_SRC" -e "$OMEGA_TRACK_SRC" -e "$OMEGA_FUZZ_SRC"
pip install -q -e .
ok "Dependances installees (1 venv partage, 8 paquets)."

# -------------------------------------------------------------------------
# 4. Scripts executables
# -------------------------------------------------------------------------
chmod +x omega-suite.sh
chmod +x "$SCRIPT_DIR/install.sh"
ok "Scripts rendus executables."

# -------------------------------------------------------------------------
# 5. Alias (optionnel)
# -------------------------------------------------------------------------
ALIAS_LINE="alias suite=\"${SCRIPT_DIR}/omega-suite.sh\""

for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
    rc_name="$(basename "$rc")"
    if grep -qxF "$ALIAS_LINE" "$rc" 2>/dev/null; then
        info "Alias deja present dans $rc_name."
    elif echo "$ALIAS_LINE" >> "$rc" 2>/dev/null; then
        ok "Alias ajoute a $rc_name."
    else
        warn "Impossible d'ajouter l'alias a $rc_name."
    fi
done

echo ""
ok "Installation terminee."
tip "Lancez Omega-Suite avec : ${SCRIPT_DIR}/omega-suite.sh (ou 'suite' dans un nouveau terminal si l'alias vient d'etre ajoute)."

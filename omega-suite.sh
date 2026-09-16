#!/usr/bin/env bash
# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
# ==============================================================================
# Script de lancement - OMEGA-SUITE
# ==============================================================================

set -e

WHITE='\033[1;37m'
NC='\033[0m'
echo -e "${LIGHT_WHITE}${NC}"
echo -e "${LIGHT_WHITE}DÉMARRAGE DE L'APPLICATION${NC}"
echo -e "${LIGHT_WHITE}${NC}"
echo -e "${WHITE}    ░▒▓███████████████████████▓▒░${NC}"
echo -e "${WHITE}    ░▒▓ Ω M E G A - S U I T E ▓▒░${NC}"
echo -e "${WHITE}    ░▒▓███████████████████████▓▒░${NC}"
echo -e "${LIGHT_WHITE}${NC}"
echo -e "${LIGHT_WHITE}CHARGEMENT EN COURS...${NC}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Environnement virtuel introuvable : $VENV_DIR"
    echo ""
    echo "Lancez d'abord : $SCRIPT_DIR/install.sh"
    exit 1
fi

if ! "$VENV_DIR/bin/python" -c "import omega_suite" 2>/dev/null; then
    echo "⚠️  Le venv semble incomplet, relancez : $SCRIPT_DIR/install.sh"
    exit 1
fi

# Ancrer le repertoire runtime de la suite (et de chacun des 7 outils,
# var/<outil>/, D-015 point 8) sur l'emplacement du script, jamais sur le
# repertoire courant du shell appelant.
export OMEGA_SUITE_VAR_DIR="${OMEGA_SUITE_VAR_DIR:-$SCRIPT_DIR/var}"

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"
exec omega-suite "$@"

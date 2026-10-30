#!/usr/bin/env bash
# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
# ==============================================================================
# Construit l'archive distribuable omega-suite.tar.gz : copie le projet
# (sans artefacts dev/runtime ni bannière docs/assets/), vendore les 8
# dépendances internes non publiées sur PyPI (omega-lib + les 7 outils,
# voir install.sh), archive le tout dans ../dist/. Outil de maintenance,
# jamais lui-même inclus dans l'archive générée.
#
# Même patron que build-release.sh d'omega-track, étendu à 8 dépendances
# vendorées au lieu d'une seule.
# ==============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

info() { echo -e "${CYAN}ℹ️  $1${NC}"; }
ok()   { echo -e "${GREEN}✅ $1${NC}"; }
err()  { echo -e "${RED}❌ $1${NC}"; }

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEV_ROOT="${DEV_ROOT:-$(cd "$PROJECT_ROOT/../.." && pwd)}"
DIST_DIR="${DIST_DIR:-$PROJECT_ROOT/../dist}"
ARCHIVE_NAME="omega-suite.tar.gz"

OMEGA_LIB_SRC="${OMEGA_LIB_SRC:-$DEV_ROOT/LIB/omega-lib}"
OMEGA_SCAN_SRC="${OMEGA_SCAN_SRC:-$DEV_ROOT/SCAN/omega-scan}"
OMEGA_CHECK_SRC="${OMEGA_CHECK_SRC:-$DEV_ROOT/CHECK/omega-check}"
OMEGA_DEEP_SRC="${OMEGA_DEEP_SRC:-$DEV_ROOT/DEEP/omega-deep}"
OMEGA_FOLD_SRC="${OMEGA_FOLD_SRC:-$DEV_ROOT/FOLD/omega-fold}"
OMEGA_STRESS_SRC="${OMEGA_STRESS_SRC:-$DEV_ROOT/STRESS/omega-stress}"
OMEGA_TRACK_SRC="${OMEGA_TRACK_SRC:-$DEV_ROOT/TRACK/omega-track}"
OMEGA_FUZZ_SRC="${OMEGA_FUZZ_SRC:-$DEV_ROOT/FUZZ/omega-fuzz}"

for pair in "omega-lib:$OMEGA_LIB_SRC" "omega-scan:$OMEGA_SCAN_SRC" "omega-check:$OMEGA_CHECK_SRC" \
            "omega-deep:$OMEGA_DEEP_SRC" "omega-fold:$OMEGA_FOLD_SRC" "omega-stress:$OMEGA_STRESS_SRC" \
            "omega-track:$OMEGA_TRACK_SRC" "omega-fuzz:$OMEGA_FUZZ_SRC"; do
    name="${pair%%:*}"; path="${pair#*:}"
    if [ ! -d "$path" ]; then
        env_suffix="${name#omega-}"
        err "$name introuvable : $path (definissez OMEGA_${env_suffix^^}_SRC si le chemin differe)."
        exit 1
    fi
done
ok "Les 8 dependances (omega-lib + 7 outils) sont localisees."

STAGING_DIR="$(mktemp -d)"
trap 'rm -rf "$STAGING_DIR"' EXIT
DEST="$STAGING_DIR/omega-suite"
mkdir -p "$DEST"

info "Copie du projet omega-suite..."
rsync -a \
    --exclude='.venv/' --exclude='venv/' \
    --exclude='__pycache__/' --exclude='*.pyc' \
    --exclude='.pytest_cache/' --exclude='.mypy_cache/' --exclude='.ruff_cache/' \
    --exclude='.import_linter_cache/' --exclude='*.egg-info/' \
    --exclude='.git/' --exclude='.claude/' \
    --exclude='docs/assets/' \
    --exclude='var/' \
    --exclude='*~' --exclude='*.bak' --exclude='*.swp' \
    --exclude='.coverage' --exclude='htmlcov/' \
    --exclude='build-release.sh' --exclude='omega-suite.tar.gz' \
    --exclude='vendor/' \
    "$PROJECT_ROOT/" "$DEST/"

info "Vendoring des 8 dependances (omega-lib + 7 outils, non publiees sur PyPI)..."
for pair in "omega-lib:$OMEGA_LIB_SRC" "omega-scan:$OMEGA_SCAN_SRC" "omega-check:$OMEGA_CHECK_SRC" \
            "omega-deep:$OMEGA_DEEP_SRC" "omega-fold:$OMEGA_FOLD_SRC" "omega-stress:$OMEGA_STRESS_SRC" \
            "omega-track:$OMEGA_TRACK_SRC" "omega-fuzz:$OMEGA_FUZZ_SRC"; do
    name="${pair%%:*}"; path="${pair#*:}"
    mkdir -p "$DEST/vendor/$name"
    # '/tests/' (ANCRE a la racine de CHAQUE outil vendore), jamais 'tests/'
    # sans le '/' en tete (bug reel constate, 2026-10-16 : "le module
    # omega-fuzz gele le logiciel") : un motif rsync sans '/' en tete
    # exclut TOUT repertoire nomme "tests" a n'importe quelle profondeur,
    # pas seulement le tests/ racine (suite pytest) de chaque outil -
    # omega-fuzz a un VRAI module metier `domain/tests/` (Test/TestPlan/
    # TestResult, rien a voir avec pytest) que ce motif non ancre excluait
    # silencieusement du vendoring, provoquant un ModuleNotFoundError au
    # premier chargement de l'onglet Fuzz dans la version distribuee
    # uniquement (jamais reproduit en checkout dev, ou l'import est
    # editable et pointe directement sur la source). Verifie : aucun des
    # 6 autres outils n'a de sous-module nomme "tests", seul Fuzz etait
    # touche par cette collision de nom.
    rsync -a \
        --exclude='.venv/' --exclude='venv/' --exclude='__pycache__/' --exclude='*.pyc' \
        --exclude='.pytest_cache/' --exclude='.mypy_cache/' --exclude='.ruff_cache/' \
        --exclude='.import_linter_cache/' --exclude='*.egg-info/' --exclude='.git/' \
        --exclude='.claude/' --exclude='docs/assets/' --exclude='var/' --exclude='/tests/' \
        --exclude='*~' --exclude='*.bak' --exclude='*.swp' \
        --exclude='vendor/' --exclude='build-release.sh' \
        "$path/" "$DEST/vendor/$name/"
done
ok "8 dependances vendorees."

# Langues de l'interface et des exports (OMEGA-SUITE_PLAN-DETAILLE_I18N.md, lot N+1) : chaque
# .po de l'archive (outil, omega-lib vendoree et son catalogue partage) est recompile en .mo
# depuis sa source - jamais un .mo plus ancien que son .po ; .po et .pot ne sont pas livres.
if find "$DEST" -name '*.po' -path '*/LC_MESSAGES/*' | grep -q .; then
    if ! command -v msgfmt > /dev/null; then
        err "msgfmt introuvable (paquet gettext) : impossible de compiler les langues."
        exit 1
    fi
    info "Compilation des langues..."
    while IFS= read -r po; do
        msgfmt --check -o "${po%.po}.mo" "$po" || { err "Catalogue invalide : $po"; exit 1; }
        rm -f "$po"
    done < <(find "$DEST" -name '*.po' -path '*/LC_MESSAGES/*')
    find "$DEST" -name '*.pot' -path '*/locale/*' -delete
fi

info "Archivage..."
mkdir -p "$DIST_DIR"
tar -C "$STAGING_DIR" -czf "$DIST_DIR/$ARCHIVE_NAME" omega-suite

ok "Archive generee : $DIST_DIR/$ARCHIVE_NAME"
echo "sha256sum :"
sha256sum "$DIST_DIR/$ARCHIVE_NAME"

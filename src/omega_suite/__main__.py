# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Point d'entree `python -m omega_suite` / script console `omega-suite`."""
from __future__ import annotations


def install_language() -> None:
    """Langue de la suite installee AVANT tout import d'ecran, puis IMPOSEE aux 7 outils
    (plan i18n de la suite, Q2) : chaque outil la lit avant sa variable d'environnement et
    son propre reglage, au moment ou la suite l'importe (app/tool_adapters.py)."""
    import os

    from omega_lib.i18n.host import set_host_export_language, set_host_language
    from omega_lib.infrastructure.i18n.tool_language import EXPORT_LANGUAGE_KEY
    from omega_lib.infrastructure.terminal.detector import SystemTerminalDetector

    from omega_suite.infrastructure.config import paths
    from omega_suite.infrastructure.storage.json_settings_store import JsonSettingsStore
    from omega_suite.shared.i18n import LANGUAGE, STATE

    store = JsonSettingsStore(paths.default_settings_path(paths.resolve_var_dir()))
    LANGUAGE.install(
        settings_store=store,
        environ=os.environ,
        terminal_family=SystemTerminalDetector().detect().family,
    )
    set_host_language(STATE.language.code, "omega-suite")

    def export_language() -> str:
        # Lot N (Q5) : un seul reglage « Langue des exports » pour les 7 outils, relu a chaque export.
        try:
            return store.get(EXPORT_LANGUAGE_KEY, "") or ""
        except OSError:
            return ""

    set_host_export_language(export_language)


def main() -> int:
    import os
    import sys

    install_language()

    from omega_suite.app.bootstrap import bootstrap
    from omega_suite.interfaces.tui.app import OmegaSuiteApp

    container = bootstrap()
    app = OmegaSuiteApp(container)
    app.run()
    # `App.run()` est deja revenu ici - Textual entierement arrete, le
    # terminal restaure - avant tout appel a `os.execv()` (meme patron
    # que le "bascule execv" d'omega-serv, PendingInstanceSwitch) : un
    # profil de rendu ou un style de navigation change en Reglages ne se
    # recharge jamais a chaud (decides UNE FOIS au demarrage de l'App),
    # `SettingsScreen` propose donc de fermer puis relancer TOUT DE SUITE
    # plutot que de laisser "applique au prochain demarrage" sans action
    # concrete - `os.execv()` remplace ce processus par un nouveau
    # `python -m omega_suite`, qui relira alors les reglages a jour.
    if app.pending_language is not None:
        from omega_suite.shared.i18n import LANGUAGE

        LANGUAGE.prepare_restart_environment(os.environ, app.pending_language)
    if app.pending_restart or app.pending_language is not None:
        python_executable = sys.executable
        os.execv(python_executable, [python_executable, "-m", "omega_suite"])  # pragma: no cover
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

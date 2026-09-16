# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Point d'entree `python -m omega_suite` / script console `omega-suite`."""
from __future__ import annotations


def main() -> int:
    import os
    import sys

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
    if app.pending_restart:
        python_executable = sys.executable
        os.execv(python_executable, [python_executable, "-m", "omega_suite"])  # pragma: no cover
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

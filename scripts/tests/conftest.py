"""Fixtures et helpers communs : exécution des validateurs en sous-processus."""
from pathlib import Path
import subprocess
import sys

SCRIPTS = Path(__file__).resolve().parent.parent


def run_validator(script_name, arg):
    """Lance un validateur et renvoie (returncode, stdout)."""
    result = subprocess.run(
        [sys.executable, str(SCRIPTS / script_name), str(arg)],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout + result.stderr

import os
import subprocess
import sys
from pathlib import Path

LOG = Path("/tmp/mathpy.log")
IPYTHONDIR = Path.home() / ".cache" / "mathpy" / "ipython"


def main():
    startup = IPYTHONDIR / "profile_default" / "startup"
    startup.mkdir(parents=True, exist_ok=True)
    (startup / "00-mathpy.py").write_text("from mathpy.main import *\n")

    env = {
        **os.environ,
        "QT_QPA_PLATFORM": "xcb",
        "IPYTHONDIR": str(IPYTHONDIR),
    }
    cmd = [
        sys.executable, "-m", "qtconsole",
        "--style=vim",
        "--ConsoleWidget.font_size=10",
        "--JupyterConsoleApp.confirm_exit=False",
        *sys.argv[1:],
    ]

    with open(LOG, "w") as log:
        proc = subprocess.Popen(
            cmd,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=log,
            start_new_session=True,  # own session: survives terminal close / parent death
            close_fds=True,
        )

    # Catch immediate startup failures (missing Qt binding, etc.)
    try:
        rc = proc.wait(timeout=3)
    except subprocess.TimeoutExpired:
        return  # still running: detached successfully

    if rc != 0:
        print(f"qtconsole exited with {rc}, see {LOG}", file=sys.stderr)
        raise SystemExit(rc)

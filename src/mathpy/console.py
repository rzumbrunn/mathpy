import os
import subprocess
import sys
import tempfile
from pathlib import Path

def main():
    with tempfile.TemporaryDirectory() as tmp:
        startup = Path(tmp) / "profile_default" / "startup"
        startup.mkdir(parents=True)
        (startup / "00-mathpy.py").write_text("from mathpy.main import *\n")

        env = {**os.environ, "QT_QPA_PLATFORM": "xcb", "IPYTHONDIR": tmp}
        cmd = [
            sys.executable, "-m", "qtconsole",
            "--style=vim",
            "--ConsoleWidget.font_size=10",
            "--JupyterConsoleApp.confirm_exit=False",
            *sys.argv[1:],
        ]
        with open("/tmp/mathpy.log", "w") as log:
            rc = subprocess.call(cmd, env=env, stdout=log, stderr=log)
    if rc != 0:
        print(f"qtconsole exited with {rc}, see /tmp/mathpy.log", file=sys.stderr)
    raise SystemExit(rc)

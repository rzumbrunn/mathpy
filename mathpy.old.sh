# shell script to run mathpy.py
#ipython -i /mnt/SSHD/Speicher/02_Code/Random/utils/mathpy.py
QT_QPA_PLATFORM=xcb /mnt/SSHD/Speicher/02_Code/Random/utils/.venv/bin/jupyter  qtconsole --kernel=mathpy_kernel --style=vim --ConsoleWidget.font_size=10  --JupyterConsoleApp.confirm_exit=False

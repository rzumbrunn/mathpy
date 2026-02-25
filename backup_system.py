import os
import sys


NAS_PATH = "/mnt/NAS"

# check if nas is correctly mounted
nas_dir_files = os.listdir(NAS_PATH)

if 'not_mounted' in nas_dir_files:
    print("NAS is not mounted. Exiting...")
    sys.exit(1)
else:
    print("Nas is mounted, moving to backup")
    # sync files using rsync
    os.system("rsync -avP --delete --progress /mnt/SSHD/Speicher/ /mnt/NAS/00_Storage/")
    




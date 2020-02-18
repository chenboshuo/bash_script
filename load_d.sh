# #!/bin/sh
# reference https://unix.stackexchange.com/questions/131917/how-to-mount-the-d-disk-of-windows-in-linux-mint
sudo mkdir -p /media/data
sudo ntfs-3g /dev/sda4 /media/data

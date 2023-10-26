#! /bin/sh

DATE=`date +%Y-%m-%d`

hs=`hostname`

now=$(date +"%d_%m_%y")

BACKUPFILE=/mnt/backup/Pi_Backups/$hs-${now}.img
DONEFILE="$BACKUPFILE".done

printf "Current date and time %s\n" "$now"

echo Backup running "$now">> /var/log/backups

libsmount="/mnt/backup/Pi_Backups/";

dd bs=4M of=$BACKUPFILE if=/dev/mmcblk0 >>  /var/log/backups

echo "shrinking the image with pishrink" >> /var/log/backups

if test -f /usr/local/bin/pishrink.sh; then
        echo "shrinking the image with pishrink" >> /var/log/backups
    	pishrink.sh -s "$BACKUPFILE"
fi

now="$(date)"
echo Backup finished "$now">> /var/log/backups

touch "$DONEFILE"

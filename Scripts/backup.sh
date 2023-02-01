#! /bin/sh

DATE=`date +%Y-%m-%d`

hs=`hostname`

now=$(date +"%d_%m_%y")

printf "Current date and time %s\n" "$now"

echo Backup running "$now">> /var/log/backups

libsmount="/mount/nfs/backup/";

dd bs=4M of=/mnt/backup/Pi_Backups/$hs-${now}.img if=/dev/mmcblk0 >>  /var/log/backup
now="$(date)"

echo Backup finished "$now">> /var/log/backups


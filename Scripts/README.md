# Scripts and stuff

### backup.sh
  creates a backup of the raspberry pi SD card
  the backup image will have the filename of the hostname of the pi and the current date and will be stored on DLINK NAS drive
  in share Pi_Backups
  
  /mnt/backup/Pi_Backups/hostname-dd_mm_yy.img
    
  requires mount point /mnt/backup
  
  requires entry in fstab
  192.168.1.191:/mnt/HD/HD_a2/Pi_backups /mnt/backup nfs auto,_netdev,nofail,x-systemd.automount 0 0
  
  

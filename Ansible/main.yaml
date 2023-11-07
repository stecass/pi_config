---
- hosts: 192.168.2.32
  become: yes
  tasks:
    - name: Copy Backup file to source destination
      ansible.builtin.copy:
        src: /home/pi/working/Scripts/backup.sh
        dest: /usr/sbin/
        owner: pi
        group: pi
        mode: '0755'

    - name: Creates directory
      file:
        path: /mnt/backup
        state: directory
        owner: pi
        group: pi
        mode: '0777'

    - name: Mount an NFS volume
      ansible.posix.mount:
        src: 192.168.1.191:/mnt/HD/HD_a2/Pi_backups
        path: /mnt/backup
        opts: rw,sync,hard
        state: mounted
        fstype: nfs

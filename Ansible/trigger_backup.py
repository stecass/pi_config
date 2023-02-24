---
# Usage example ansible-playbook trigger_backup.py --extra-vars "server=192.168.2.98"

- hosts: "{{ server }}"
  gather_facts: no
  become: yes
  vars:
    server: "{{ server }}"
  
  #tasks:
  #  - name: Check if backup script already exists
  #    stat:
  #      path: /usr/sbin/backup.sh
  #    register: backup_script

    - name: Copy Backup file to source destination
      ansible.builtin.copy:
        src: /home/pi/working/Scripts/backup.sh
        dest: /usr/sbin/
        owner: pi
        group: pi
        mode: '0755'
      #when: not backup_script.stat.exists

    - name: Creates directory
      file:
        path: /mnt/backup
        state: directory 
        owner: pi
        group: pi
        mode: '0777' 

    - shell: "(/usr/sbin/backup.sh >/dev/null 2>&1 &)"
      async: 10
      poll: 0


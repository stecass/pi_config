---
- hosts: all
  become: yes
  tasks:
    - name: Ensure pishrink script exists at destination
      ansible.builtin.copy:
        src: /home/pi/working/pi_config/Scripts/pishrink.sh
        dest: /usr/local/bin/
        owner: root
        group: root
        mode: '0755'

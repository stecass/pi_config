---
- hosts: 192.168.2.52
  become: yes
  tasks:
    - name: Install Packges
      apt:
        pkg:
          - ntp
          - vim
          - locate
        state: latest
        update_cache: true

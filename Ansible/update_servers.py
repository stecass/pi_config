---
- hosts: main
  gather_facts: yes
  become: yes

  tasks:
    - name: Perform a dist-upgrade.
      ansible.builtin.apt:
        upgrade: dist
        update_cache: yes

    - name: Remove dependencies that are no longer required.
      ansible.builtin.apt:
        autoremove: yes

    - name: Check if a reboot is required.
      ansible.builtin.stat:
        path: /var/run/reboot-required
        get_md5: no
      register: reboot_required_file

    - name: Reboot the server (if required).
      ansible.builtin.reboot:
      when: reboot_required_file.stat.exists == true

#    - name: Restart the server after updates
#      ansible.builtin.reboot:

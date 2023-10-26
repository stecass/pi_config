---
- hosts: 192.168.2.53
  tasks:
    - name: find all files that are older than 10 days
      find:
        paths: /mnt/backup/Pi_Backups
        age: 10d
        patterns: '*.img'
        recurse: no
      register: filesOlderThan10
    - name: remove older than 10
      file:
        path: "{{ item.path }}" 
        state: absent
      with_items: "{{ filesOlderThan10.files }}"

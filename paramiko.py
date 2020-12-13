import paramiko
from getpass import getpass
import time
import os
import sys

def mikrotik1():
    print("Ping ke IP...\n")
    ip_add = True
    while ip_add:
        ip = "192.168.20.2"
        response = os.system("ping -c 2 "+ip)
        if response == 0:
            ip_add = False
            print("\nAktif\n")
        else:
            print("\nTidak Aktif\n")
            
    print("Login user...\n")
    user = input("Masukan Username : ")
    password = getpass("\nMauskan Password : ")
    port = 22
    remot = paramiko.SSHClient()
    remot.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    remot.connect(hostname=ip, username=user, password=password, port=port)
    print("Berhasil Login....!\n")

    while True:
        try:
            file_internet = input("Masukan File Internet : ")
            r_file_internet = open(file_internet, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!")
            continue

    for config in r_file_internet:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n")

    while True:
        try:
            file_blok_port = input("Masukan File Blok Port Gamming : ")
            r_file_blok_port = open(file_blok_port, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!")
            continue

    for config in r_file_blok_port:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n")

    while True:
        try:
            file_zoom = input("Masukan File Prioritas Zoom : ")
            r_file_zoom = open(file_zoom, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!")
            continue

    for config in r_file_zoom:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n")
    remot.close()
mikrotik1()

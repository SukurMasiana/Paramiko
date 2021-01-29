import paramiko
from getpass import getpass
import time
import os
import sys

ip = ["192.168.80.2","192.168.80.3","192.168.80.4","192.168.80.5","192.168.80.6"]
def Internet():
    print("\n"+45*"=","\n          Informasi Konfigurasi \n    Koneksi Internet, Prioritas Zooom \n\
           dan Blok Port Game\n"+45*"="+"\nPing ke IP...\n")
    while ip:
        lis1 = ip[0]
        response = os.system("ping -c 2 {}".format(lis1))
        if response == 0:
            print("\nAktif\n\n"+45*"*")
        else:
            print("\nTidak Aktif\n")
        break
    print("Login user...\n")
    while True:
        try:
            port = 22
            user = input("Masukan Username : ")
            password = getpass("Mauskan Password : ")
            remot = paramiko.SSHClient()
            remot.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            remot.connect(hostname=ip[0], username=user, password=password, port=port)
            print("\nLogin Berhasil...\n+"+45*"*")
            break
        except:
            print("\nUsername dan Password Salah \nMaukan Ulang\n")
            continue
    while True:
        try:
            file_internet = input("Masukan File Koneck Ke Internet : ")
            r_file_internet = open(file_internet, "r").readlines()
            break
        except IOError:
            print("\nFile Tidak Ada...!"+"\nMasukan Kembali\n")
            continue
    print("Sedang Melakukan Konfigurasi...")
    for config in r_file_internet:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*"+"\n")

    while True:
        try:
            file_ip_zoom = input("Masukan File IP Server Zoom : ")
            r_file_ip_zoom = open(file_ip_zoom, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!\nMasukan Kembali\n")
            continue
    print("Sedang Melakukan Konfigurasi IP Server Zoom...\n")
    for config in r_file_ip_zoom:
        remot.exec_command(config)
        time.sleep(1)
    print("Suksess....\n"+45*"*"+"\n")

    while True:
        try:
            file_zoom = input("Masukan File Prioritas Zoom : ")
            r_file_zoom = open(file_zoom, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...! \nMasukan Kembali\n")
            continue
    print("Sedang Melakukan Konfigurasi Prioritas Zoom...\n")
    for config in r_file_zoom:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*"+"\n")

    while True:
        try:
            file_zoom = input("Masukan File Simple Queue : ")
            r_file_zoom = open(file_zoom, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...! \nMasukan Kembali\n")
            continue
    print("Sedang Melakukan Konfigurasi Prioritas Zoom...\n")
    for config in r_file_zoom:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*"+"\n")

    while True:
        try:
            file_blok_port = input("Masukan File Blok Port Gamming : ")
            r_file_blok_port = open(file_blok_port, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...! \nMasukan Kembali\n")
            continue

    for config in r_file_blok_port:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*"+"\n")
    
    remot.close()
Internet()

def ospf_1():
    print("\n"+45*"="+"\n"+"         Informasi Konfigurasi OSPF\n"+45*"="+"\n\nPing ke IP R-1...\n")
    while ip:
        list2 = ip[0]
        response = os.system("ping -c 2 {}".format(list2))
        if response == 0:
            print("\nAktif\n\n"+45*"*")
        else:
            print("\nTidak Aktif\n")
        break
    print("Login user...\n")
    while True:
        try:
            port = 22
            user = input("Masukan Username : ")
            password = getpass("Mauskan Password : ")
            remot = paramiko.SSHClient()
            remot.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            remot.connect(hostname=ip[0], username=user, password=password, port=port)
            break
        except:
            print("\nUsername dan Password Salah \nMaukan Ulang\n")
            continue
    print("\nBerhasil Login...\n")

    while True:
        try:
            file_ospf_1 = input("Masukan File Konfigurasi OSPF R-1 : ")
            r_file_ospf_1 = open(file_ospf_1, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!\nMasukan Kembali\n")
            continue
    print("\nSedang Melakukan Konfigurasi...")
    for config in r_file_ospf_1:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*")
    remot.close()
ospf_1()

def ospf_2():
    print("\nPing ke IP R-2...\n")
    while ip:
        list3 = ip[1]
        response = os.system("ping -c 2 {}".format(list3))
        if response == 0:
            print("\nAktif\n\n"+45*"*")
        else:
            print("\nTidak Aktif\n")
        break
    print("Login user...\n")
    while True:
        try:
            port = 22
            user = input("Masukan Username : ")
            password = getpass("Mauskan Password : ")
            remot = paramiko.SSHClient()
            remot.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            remot.connect(hostname=ip[1], username=user, password=password, port=port)
            break
        except:
            print("\nUsername dan Password Salah \nMaukan Ulang\n")
            continue
    print("\nBerhasil Login...\n")

    while True:
        try:
            file_ospf_2 = input("Masukan File Konfigurasi OSPF R-2 : ")
            r_file_ospf_2 = open(file_ospf_2, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!\nMasukan Kembali\n")
            continue
    print("\nSedang Melakukan Konfigurasi...")
    for config in r_file_ospf_2:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*")
    remot.close()
ospf_2()

def ospf_3():
    print("\nPing ke IP R-3...\n")
    while ip:
        list4 = ip[2]
        response = os.system("ping -c 2 {}".format(list4))
        if response == 0:
            print("\nAktif\n\n"+45*"*")
        else:
            print("\nTidak Aktif\n")
        break
    print("Login user...\n")
    while True:
        try:
            port = 22
            user = input("Masukan Username : ")
            password = getpass("Mauskan Password : ")
            remot = paramiko.SSHClient()
            remot.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            remot.connect(hostname=ip[2], username=user, password=password, port=port)
            break
        except:
            print("\nUsername dan Password Salah \nMaukan Ulang\n")
            continue
    print("\nBerhasil Login...\n")

    while True:
        try:
            file_ospf_3 = input("Masukan File Konfigurasi OSPF R-3 : ")
            r_file_ospf_3 = open(file_ospf_3, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!\nMasukan Kembali\n")
            continue
    print("\nSedang Melakukan Konfigurasi...")
    for config in r_file_ospf_3:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*")
    remot.close()
ospf_3()

def ospf_4():
    print("\nPing ke IP R-4...\n")
    while ip:
        list5 = ip[3]
        response = os.system("ping -c 2 {}".format(list5))
        if response == 0:
            print("\nAktif\n\n"+45*"*")
        else:
            print("\nTidak Aktif\n")
        break
    print("Login user...\n")
    while True:
        try:
            port = 22
            user = input("Masukan Username : ")
            password = getpass("Mauskan Password : ")
            remot = paramiko.SSHClient()
            remot.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            remot.connect(hostname=ip[3], username=user, password=password, port=port)
            break
        except:
            print("\nUsername dan Password Salah \nMaukan Ulang\n")
            continue
    print("\nBerhasil Login...\n")

    while True:
        try:
            file_ospf_4 = input("Masukan File Konfigurasi OSPF R-4 : ")
            r_file_ospf_4 = open(file_ospf_4, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!\nMasukan Kembali\n")
            continue
    print("\nSedang Melakukan Konfigurasi...")
    for config in r_file_ospf_4:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*")
    remot.close()
ospf_4()

def ospf_5():
    print("\nPing ke IP R-5...\n")
    while ip:
        list6 = ip[4]
        response = os.system("ping -c 2 {}".format(list6))
        if response == 0:
            print("\nAktif\n\n"+45*"*")
        else:
            print("\nTidak Aktif\n")
        break
    print("Login user...\n")
    while True:
        try:
            port = 22
            user = input("Masukan Username : ")
            password = getpass("Mauskan Password : ")
            remot = paramiko.SSHClient()
            remot.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            remot.connect(hostname=ip[4], username=user, password=password, port=port)
            break
        except:
            print("\nUsername dan Password Salah \nMaukan Ulang\n")
            continue
    print("\nBerhasil Login...\n")

    while True:
        try:
            file_ospf_5 = input("Masukan File Konfigurasi OSPF R-5 : ")
            r_file_ospf_5 = open(file_ospf_5, "r").readlines()
            break
        except IOError:
            print("File Tidak Ada...!\nMasukan Kembali\n")
            continue
    print("\nSedang Melakukan Konfigurasi...")
    for config in r_file_ospf_5:
        remot.exec_command(config)
        time.sleep(1)
    print("\nSuksess....\n"+45*"*")
    remot.close()
ospf_5()

print("\n"+ 45*"*"+"\n")
print("                 SELESAI")
print("\n" + 45*"*" + "\n")


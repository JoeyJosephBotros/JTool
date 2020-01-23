import nmap
import socket 
from datetime import datetime 
import os 
import subprocess
import re
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
BLUE = Fore.BLUE
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
CYAN = Fore.CYAN



res = subprocess.Popen("arp-scan -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
res = str(res.stdout.read(), "utf-8")
ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
UpHosts = list(set(ips))


ipdic = {} 
iplist = []
portlist = []
plst = []


def givemeports():
    global ipdic, UpHosts
    for ip in UpHosts:  
        ipdic[ip] = []
        host = socket.gethostbyname(ip)
        for port in range(1, 1025):
            scannerTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            status = scannerTCP.connect_ex((host, port))
            if not status:
                try:
                    serv = str(socket.getservbyport(port))
                    ipdic[ip].append(str(port))
                except:
                    pass


def nmapscan():
    global ipdic ,plst
    for i in ipdic:
        portS =','.join(ipdic[i])
        nmapCMD = "nmap -sC -sV -p " + portS + " " + i
        res = os.popen(nmapCMD).read()
        ports = re.findall(r'\d+/tcp.+', res)
        x = "\n".join(ports)
        plst.append(x)
    return plst    

def task3():
    print("Please wait while Scanning..........")
    global ipdic
    x = []
    givemeports()
    x = nmapscan()
    j= 0
    for i in ipdic:
        
        print(f"\n\n==================Scanning {i}==================")
        print(x[j])
        j+=1


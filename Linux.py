from os import *
import sys
from time import *
#####################################
#.           banner 
def mh () :
    system ("sleep 0.3")
    print ("\033[0;34m      ___  ___ \033[0;32m  _   _ ") 
    system ("sleep 0.3")
    print ("\033[0;34m     /   |/   |\033[0;32m | | | |") 
    system ("sleep 0.3")
    print ("\033[0;34m    / /|   /| |\033[0;32m | |_| |") 
    system ("sleep 0.3")
    print ("\033[0;34m   / / |__/ | |\033[0;32m |  _  |") 
    system ("sleep 0.3")
    print ("\033[0;34m  / /       | |\033[0;32m | | | |") 
    system ("sleep 0.3")
    print ("\033[0;34m /_/        |_|\033[0;32m |_| |_|")
mh ()
#               codes
#####################################
# Black=  \033[0;30m
# Red=    \033[0;31m
# Green=  \033[0;32m
# Yellow= \033[0;33m
# Blue=   \033[0;34m
# Purple= \033[0;35m 
# Cyan=  \033[0;36m 
# White= \033[0;37m
#              codes
#####################################
system ("sleep 0.3")
print (" \033[0;31m_____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(1)\033[0;34m>>>\033[0;31mKali Linux\033[0;34m<<<")
system ("sleep 0.3")
print (" \033[0;31m_____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(2)\033[0;34m>>>\033[0;31mParrot\033[0;34m<<<")
system ("sleep 0.3")
print (" \033[0;31m_____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(3)\033[0;34m>>> \033[0;31mUpuntu\033[0;34m<<<")
system ("sleep 0.3")
print (" \033[0;31m_____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(4)\033[0;34m>>> \033[0;31mkali Nethunter\033[0;34m<<<")
system ("sleep 0.3")
print (" \033[0;31m_____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(5)\033[0;34m>>> \033[0;31mFedora\033[0;34m<<<")
system ("sleep 0.3")
print (" \033[0;31m_____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(6)\033[0;34m>>> \033[0;31mbackbox\033[0;34m<<<")
system ("sleep 0.3")
print ("\033[0;31m _____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(7)\033[0;34m>>> \033[0;31mAlpine\033[0;34m<<<")
system ("sleep 0.3")
print ("\033[0;31m _____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(8)\033[0;34m>>> \033[0;31mcentos\033[0;34m<<<")
system ("sleep 0.3")
print ("\033[0;31m _____ _____ _____ _____")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(9)\033[0;34m>>> \033[0;31mBlack Arch\033[0;34m<<<")
system ("sleep 0.3")
print ("\033[0;31m _____ _____ _____ _____")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(10)\033[0;34m>>> \033[0;31mDebian\033[0;34m<<<")
system ("sleep 0.3")
print ("\033[0;31m _____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")
print ("\033[0;32m(11)\033[0;34m>>> \033[0;31mArch Linux\033[0;34m<<<")
system ("sleep 0.3")
print ("\033[0;31m _____ _____ _____ _____ ")
print ("\033[0;31m|_____|_____|_____|_____|")
system ("sleep 0.3")

mh =input ("choose number to download:»»»")

if mh =="1" :
    system ("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")

if mh =="2" : 
    system ("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
    
if mh =="3" :
    system ("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
    
if mh =="4" :
    print ("it will take 1GB do you want it ")
    mk =input ("choose y/n: ")
    if mk == "y" :
        system ("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
    
if mh =="5" :
    system ("  pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
    
if mh =="6" :
    system ("        pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
    
if mh =="7" :
    system ("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")
    
    
if mh =="8" :
    system ("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")

if mh =="9" :
    system ("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")

if mh =="10" :
    system ("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")

if mh =="11" :
    print ("it will take 1.5 GB do you want it")
    ml =input ("choose y/n :")
    if ml =="y" or "Y" :
        system ("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh")

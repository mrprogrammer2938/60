#!/usr/bin/python3
# This Code write by Mr.nope
# Version: 1.3.0
'''
Imports
'''
import os, time, sys, platform, subprocess
from colorama import Fore,init
init()

line = '\033[4m'
End = '\033[0m'
banner = Fore.GREEN + """
 ██████   ██████  
██       ██  ████  """ + Fore.RED + "Version: " + Fore.CYAN + "1.3.0" + Fore.GREEN + """
███████  ██ ██ ██ 
██    ██ ████  ██ 
 ██████   ██████  
                  """ + Fore.WHITE
opt = Fore.GREEN + "\n60" + Fore.WHITE + line + "/> " + End
system = platform.uname()[0]

def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print("\nPleasem Run This Programm on Linux!\n")
        sys.exit()
def list():
    print("\n{1}.Black-Tool")
    print("{2}.Black-Tool For Termux")
    print("{3}.Big-Tool")
    print("{4}.DDos-Attack")
    print("{5}.IPz")
    print("{6}.Port Scan")
    print("{7}.Funny-Termux")
    print("{99}.Exit or Ctrl + D")
    choose = input(opt)
    if choose == '1':
        cls()
        run_1 = subprocess.getoutput("git clone https://github.com/Black-Tool/Black-Tool")
        print("Black-Tool Installed!\n")
        try1()
    elif choose == '2':
        cls()
        run_2 = subprocess.getoutput("git clone https://github.com/Black-Tool/Black-Tool-Termux")
        print("Black-Tool-Termux Installed!\n")
        try1()
    elif choose == '3':
        run_3 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Big-Tool")
        print("Big-Tool Installed!\n")
        try1()
    elif choose == '4':
        run_4 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/DDos-Attack")
        print("DDos-Attack Installed!\n")
        try1()
    elif choose == '5':
        run_5 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/IPz")
        print("IPz Installed!\n")
        try1()
    elif choose == '6':
        cls()
        run_6 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Port-Scan")
        print("PortScan Installed!\n")
        try1()
    elif choose == '7':
        cls()
        run_7 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Funny-Termux")
        print("Funny-Termux Installed!\n")
        try1()
    elif choose == '' or choose == ' ':
        main()
    else:
        cls()
        print(f'{choose} {Fore.RED} Not Found! {Fore.WHITE}')
        time.sleep(0.25)
        try1()
def try1():
    try_to_menu = input("\npress Enter...")
    if try_to_menu == '':
        main()
    else:
        main()
def main():
    os.system("printf '\033]2;60\a'")
    cls()
    print(banner)
    list()
if __name__ == '__main__':
    try:
        try:
            main()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        try1()
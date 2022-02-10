import string
from colorama import Fore, Back, Style
import datetime
import platform
import shutil
import subprocess
import windows_tools.antivirus
import pyfiglet
import sys
import socket
from datetime import datetime
import psutil
import requests
import urllib3
import socket
import speedtest
from collections import namedtuple, OrderedDict
def info():
    print(Fore.RED + "hello welcome")
    print(Fore.BLUE + "1- info and how this program work")
    print(Fore.BLUE + "2- get the system time and date")
    print(Fore.BLUE + "3- get Os information")
    print(Fore.BLUE + "4- get hard disk size")
    print(Fore.BLUE + "5- get fire wall status")
    print(Fore.BLUE + "6- check antivirus status")
    print(Fore.BLUE + "7- see all ports")
    print(Fore.BLUE + "8- its one helpful art you can see")
    print(Fore.BLUE + "9- get windows status")
    print(Fore.BLUE + "10- send email")
    print(Fore.BLUE + "11- download video from youtube")
    print(Fore.BLUE + "12- download picture from site")
    print(Fore.BLUE + "13- download music from spotify")
    print(Fore.BLUE + "14- get internet status")
    print(Fore.BLUE + "15- check your internet speed")
    print(Fore.BLUE + "16- code editors")
    print(Fore.BLUE + "17- colors code")
    op = input("please choose your operation : ")
    if op == "1":
        print(Fore.GREEN + "This program use for the systems work and you can have Better system management")
        print(Fore.GREEN + "First you must choose one operation and after that you can use that")
        print(Fore.GREEN + "This program have two version you can use version 1 of this program free in Git Hub")
        print(Fore.GREEN + "If you have problem or like report the bug you can report or say me in part (10)")
        print(Fore.GREEN + "Required System : ")
        print(Fore.GREEN + "You can use this program in systems but better you have this information : ")
        print(Fore.GREEN + "Os : windows 7 , 10 , 11 | you can use it in linux and mac too all version")
        print(Fore.GREEN + "Ram : 2 GB")
        print(Fore.GREEN + "Cpu : core i 3 intel")
        print(Fore.GREEN + "Gpu : 512 MB")
        print(Fore.GREEN + "* one of the important things is you must install python in your pc")
        print(Fore.GREEN + "* open cmd and open install program drive after it cd file location and say python file name with .py")
        print(Fore.GREEN + "This program developed by Dark-Security-Team")
        print(Fore.GREEN + "* If you cant use part (10) you can send message to this email (Dark-Security-Team-2000@protonmail.com)")
        print(Fore.GREEN + "My team hope you enjoy this program and its helpful for you")
        print(Fore.GREEN + "Good Luck")
        again2 = input("do you like try again ( y / n ) : ")
        if again2 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
    if op == "2":
        e = datetime.datetime.now()
        print ("Current date and time = %s" % e)
        print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
        print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second)) 
        again3 = input("do you like try again ( y / n ) : ")
        if again3 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ") 
    if op == "3":
        print(platform.system())  # e.g. Windows, Linux, Darwin
        print(platform.architecture())  # e.g. 64-bit
        print(platform.machine())  # e.g. x86_64
        print(platform.node())  # Hostname
        print(platform.processor())  # e.g. i386
        again4 = input("do you like try again ( y / n ) : ")
        if again4 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ") 
    if op == "4":       
        total, used, free = shutil.disk_usage("/")
        print("Total: %d GiB" % (total // (2**30)))
        print("Used: %d GiB" % (used // (2**30)))
        print("Free: %d GiB" % (free // (2**30)))
        again5 = input("do you like try again ( y / n ) : ")
        if again5 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ") 
    if op == "5":
        subprocess.check_call('netsh advfirewall show allprofiles') 
        again6 = input("do you like try again ( y / n ) : ")
        if again6 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
    if op == "6":
        result = windows_tools.antivirus.get_installed_antivirus_software()
        print(result)
        again7 = input("do you like try again ( y / n ) : ")
        if again7 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
    if op == "7":
        ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
        print(ascii_banner)
  
        # Defining a target
        if len(sys.argv) == 2:
     
            # translate hostname to IPv4
            target = socket.gethostbyname(sys.argv[1])
        else:
            print("Invalid amount of Argument")
 
        # Add Banner
        print("-" * 50)
        print("Scanning Target: " + target)
        print("Scanning started at:" + str(datetime.now()))
        print("-" * 50)
  
        try:
     
            # will scan ports between 1 to 65,535
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
         
                # returns an error indicator
                result = s.connect_ex((target,port))
                if result ==0:
                    print("Port {} is open".format(port))
                    s.close()
         
        except KeyboardInterrupt:
                print("\n Exiting Program !!!!")
                sys.exit()
        except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit()
        except socket.error:
                print("\ Server not responding !!!!")
                sys.exit()
        again8 = input("do you like try again ( y / n ) : ")
        if again8 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
    if op == "8":
        banner_1 = input("please enter your word or letter : ")
        banner_2 = pyfiglet.figlet_format(banner_1)
        print(banner_2)
        again9 = input("do you like try again ( y / n ) : ")
        if again9 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ") 
    if op == "9":
        def getService(name): 
 
            service = None 
            try: 
                service = psutil.win_service_get(name) 
                service = service.as_dict() 
            except Exception as ex: 
                print (str(ex)) 
 
            return service 
 
        service = getService('myservice') 
 
        print (service) 
 
        if service: 
 
            print ("service found") 
        else: 
 
            print ("service not found") 
 
 
        if service and service['status'] == 'running' : 
 
            print ("service is running") 
        else : 
 
            print ("service is not running")
    if op == "10":
        print(Fore.CYAN + "This part Available in version 2")
        print(Fore.CYAN + "For get the version 2 you can send email to Dark-Security-Team-2000@protonmail.com")
        print(Fore.CYAN + "version 2 is comming soon")
        print(Fore.CYAN + "Good Luck")
        again10 = input("do you like try again ( y / n ) : ")
        if again10 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
    if op == "11":
        print(Fore.CYAN + "This part Available in version 2")
        print(Fore.CYAN + "For get the version 2 you can send email to Dark-Security-Team-2000@protonmail.com")
        print(Fore.CYAN + "version 2 is comming soon")
        print(Fore.CYAN + "Good Luck")
        again11 = input("do you like try again ( y / n ) : ")
        if again11 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
    if op == "12":
        print(Fore.CYAN + "This part Available in version 2")
        print(Fore.CYAN + "For get the version 2 you can send email to Dark-Security-Team-2000@protonmail.com")
        print(Fore.CYAN + "version 2 is comming soon")
        print(Fore.CYAN + "Good Luck")
        again12 = input("do you like try again ( y / n ) : ")
        if again12 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
    if op == "13":
        print(Fore.CYAN + "This part Available in version 2")
        print(Fore.CYAN + "For get the version 2 you can send email to Dark-Security-Team-2000@protonmail.com")
        print(Fore.CYAN + "version 2 is comming soon")
        print(Fore.CYAN + "Good Luck")
        again13 = input("do you like try again ( y / n ) : ")
        if again13 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
    if op == "14":
        def internet(host="8.8.8.8", port=53, timeout=3):

            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
                return True
            except socket.error as ex:
                print(ex)
                return False

        internet()
    if op == "15":
        wifi  = speedtest.Speedtest()
        print("Wifi Download Speed is ", wifi.download())
        print("Wifi Upload Speed is ", wifi.upload())
    if op == "16":
        print("Atom")
        print("vs code")
        print("vs")
        print("sublime text")  
        print("Notepad ++")
        print("Notepad")
        print("Brackets")
        print("vim")
        print("Bluefish")   
        print("UltraEdit")
        print("KomodoEdit")
        print("Text Mate")
        print("pycharm")
        print("phpstorm")
        print("webstorm")
        print("intelij ide")
        print("rider ide")
        print("Emacs")
        print("jEdit")
        print("Geany")
        print("BBEdit")
        print("gedit")
        print("spacemacs")
        print("Text Wrangel")
        print("Crimson Editor")
        print("Dreameveare") 
        print("Coffe Cup")
        print("Code Share")
        print("JSFiddle")
        print("Code Sand box")
        print("CodeAnywhere")
        print("Stack Blitz")   
        print("AWS Cloud9")
        print("Git pod")
        print("Theia")
        print("GitHub")
        print("JetBrains")
        print("Code Tasty")
        print("Replit")
        print("PaizaCloud")
        print("Code Pen")
        print("w3school")
        print("JS Bin")
        print("Play Code")
        print("TryIt Editor")
        print("EditPad")
        print("TypeIt")
        print("Eclipse")
        print("This is best code editor")
        print("Its online and offline code editor for programmer")
        print("Good Luck")
    if op == "17":
        print(Fore.CYAN + "This part Available in version 2")
        print(Fore.CYAN + "For get the version 2 you can send email to Dark-Security-Team-2000@protonmail.com")
        print(Fore.CYAN + "version 2 is comming soon")
        print(Fore.CYAN + "Good Luck")
        again14 = input("do you like try again ( y / n ) : ")
        if again14 == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")    
    else:
        again = input("do you like try again ( y / n ) : ")
        if again == "y":
            info()
        else:
            ex = input("please enter one key to exit : ")
info()
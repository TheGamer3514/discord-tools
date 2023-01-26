#This file lets the user select which tool to run, no need to edit this!
import os
try:
    import colorama
except ImportError:
    print("Colorama Not Found...\nInstalling...")
    os.system("pip install colorama")
    print("Colorama Installed")
import colorama
from colorama import Fore
print(Fore.RED + "Discord Tools\nMultiple Discord Tools You Can Use!\nAll Made In Python\nTo Make Sure Everything Works Correctly, Make Sure To Fill Out The Config!\n" + Fore.BLUE + "[1] - Auto Send\n[2] - Nitro Gen\n[3] - Webhook Spammer\n[4] - soon\n[5] - soon")
choice = int(input(Fore.YELLOW + "Enter Here: "))
if choice == 1:
    os.system("python tools/autosend.py")
elif choice == 2:
    os.system("python tools/nitrogen.py")
elif choice == 3:
    os.system("python tools/webhookspam.py")
elif choice == 4:
    print("Coming Soon!")
elif choice == 5:
    print("Coming Soon!")
else:
    print("Unknown Choice")
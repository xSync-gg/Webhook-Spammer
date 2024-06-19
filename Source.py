import requests
import colorama
import time
import os
import sys

def _exit():
    time.sleep(5)
    sys.exit()

def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True

def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://tungskidder.000webhostapp.com/Profile/trans.png"})
            if data.status_code == 204:
                print(f"{colorama.Back.BLUE} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.BLUE}Webhook deleted...')
    print(f'{colorama.Fore.GREEN}Done...')

def initialize():
    print(f"""{colorama.Fore.BLUE}
     _         ____                     _____           _ 
    | | __  __/ ___| _   _ _ __   ___  |_   _|__   ___ | |
    | | \ \/ /\___ \| | | | '_ \ / __|   | |/ _ \ / _ \| |
    |_|  >  <  ___) | |_| | | | | (__    | | (_) | (_) | |
    (_) /_/\_\|____/ \__, |_| |_|\___|   |_|\___/ \___/|_|
                     |___/                                
     """)
    webhook = input("Enter webhook > ")
    name = input("Enter webhook name > ")
    message = input("Enter message > ")
    delay = input("Enter delay > ")
    amount = input("Enter amount > ")
    hookDeleter = input("Delete webhook after spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()

if __name__ == '__main__':
    os.system('cls')
    colorama.init()
    initialize()

from lib.terminal import rgb, custom_banner, clear_custom, set_console_title
import socket
import requests
import webbrowser
from threading import Thread
from time import sleep
from itertools import cycle
from shutil import get_terminal_size
import random

#=====================================================================#

def ip_lookup():
    enter_ip = input(f"{rgb(105, 67, 171, '~# ')}IP Address: ")
    response = requests.get(f"https://geolocation-db.com/json/{enter_ip}&position=true").json()
    print("\n")  
    for key, value in response.items():
        print(f"\t{rgb(105, 67, 171, key)}{rgb(255, 255, 255, ': ')}{rgb(105, 67, 171, value)}")
    print("\n")    

#=====================================================================#

def domain_name():
    try:
        print(socket.gethostbyname(input(f"{rgb(105, 67, 171, '~# ')}Domain name: ")))
    except:
        return

#=====================================================================#

def open_link(url):
    webbrowser.open(url, new=0, autoraise=True)

#=====================================================================#

class Loader:
    def __init__(self, desc="Loading", end="Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"] # "⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(rgb(105, 67, 171, f"\r{self.desc} {c}"), flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

#=====================================================================#

def load(loadingText:str):
    clear_custom()
    custom_banner("neon")
    set_console_title(f"Perses | {loadingText}")
    loader = Loader(loadingText).start()
    for i in range(10):
        sleep(0.25)
    set_console_title(f"Perses | Done!")
    loader.stop()

#=====================================================================#

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers
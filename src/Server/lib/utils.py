from lib.terminal import rgb, custom_banner, clear_custom, set_console_title
import socket
import requests
import webbrowser
from threading import Thread
from time import sleep
from itertools import cycle
from shutil import get_terminal_size

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
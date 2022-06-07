import sys
import os
from pyfiglet import figlet_format
from lib.settings import get_path

#=====================================================================#

def rgb(r, g, b, text):
    if get_path("useDefaultColors"):
        return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)
    else:
        if r != 255 and g != 255 and b != 255:
            return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(get_path("red"), get_path("green"), get_path("blue"), text)
        else:
            return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)

#=====================================================================#

def server_banner(text):
    print(rgb(105, 67, 171, figlet_format(text, font="slant"))) # Good Fonts: sblood, graffiti, katakana, starwars, slant
    print(rgb(105, 67, 171, f">> Type {rgb(255, 255, 255, 'help')}{rgb(105, 67, 171, ' to see all the available commands!')}"))
    print(rgb(255, 255, 255, f"\n{'▬'*100}"))
    print("\n")

#=====================================================================#

def log(text):
    print(rgb(105, 67, 171, f"[Perses] - {rgb(255, 255, 255, text)}"))

#=====================================================================#

# Clear
def clear():
    if os.name == "nt":
        os.system("cls")
        server_banner("Perses")
    else:
        os.system("clear")
        server_banner("Perses")

#=====================================================================#

def clear_main():
    if os.name == "nt":
        os.system("cls")
        banner("Perses")
    else:
        os.system("clear")
        banner("Perses")

#=====================================================================#

def clear_custom():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#=====================================================================#


def banner(text):
    print(rgb(105, 67, 171, figlet_format(text, font="slant"))) # Good Fonts: sblood, graffiti, katakana, starwars, slant
    print(rgb(105, 67, 171, f"By: {rgb(255, 255, 255, 'gokimax')}\n{rgb(105, 67, 171, 'For more visit: https://github.com/gokiimax')}"))
    print(rgb(255, 255, 255, f"\n{'▬'*100}"))
    print(rgb(105, 67, 171,"\n╔══════════════════════════╦══════════════════════╦═════════════════════╗"))
    print(rgb(105, 67, 171,"║     EDUCATIONAL          ║       EXTRAS         ║       CREDITS       ║"))
    print(rgb(105, 67, 171,"║                          ║                      ║                     ║"))
    print(rgb(105, 67, 171,"║ [1] Start RAT Server     ║   [5] Update Style   ║     [6] Github      ║"))
    print(rgb(105, 67, 171,"║ [2] Start Botnet Server  ║                      ║     [7] Twitter     ║"))
    print(rgb(105, 67, 171,"║ [3] IP lookup            ║                      ║     [8] Exit        ║"))
    print(rgb(105, 67, 171,"║ [4] Domain to IPv4       ║                      ║                     ║"))
    print(rgb(105, 67, 171,"║                          ║                      ║                     ║"))
    print(rgb(105, 67, 171,"╚══════════════════════════╩══════════════════════╩═════════════════════╝"))
    print("\n")

#=====================================================================#

def set_console_title(text:str):
    sys.stdout.write(f"\x1b]2;{text}\x07")

#=====================================================================#

def custom_banner(text):
    print(rgb(105, 67, 171, figlet_format(text, font="slant"))) # Good Fonts: sblood, graffiti, katakana, starwars, slant
    print(rgb(105, 67, 171, f"By: {rgb(255, 255, 255, 'gokimax')}\n{rgb(105, 67, 171, 'For more visit: https://github.com/gokiimax')}"))
    print(rgb(255, 255, 255, f"\n{'▬'*100}"))

#=====================================================================#

# Command List
commands = [
    ["exit", "Exits the connection on both sides"],
    ["cd", "Changes the current directory"],
    ["download", "Download filles from the Target"],
    ["upload", "Upload files from the server to the Target"],
    ["message", "Shows a message box on the Targets screen"],
    ["lock", "Put the client user back to the login screen"],
    ["shutdown", "Shutdown the Targets PC"],
    ["restart", "Restart the Targets PC"],
    ["clear", "Clears the console"],
    ["help", "You obviously know what this does"]
]


#=====================================================================#

# Help Command
def help_command():
    total = 0
    print(rgb(255, 255, 255, f"\n{'▬'*50}"))
    print(rgb(255, 255, 255, "\n\t× Riko | Help ×\n"))
    # loop through all available commands
    for x in commands:
        print(rgb(105, 67, 171, f"[{total}] × {commands[total][0]} | {commands[total][1]} ×"))
        total += 1

    print(rgb(105, 67, 171, f"[{total}] × Anything | Will run a command on the Targets PC like command prompt ×"))
    print(rgb(255, 255, 255, f"\n{'▬'*50}"))

#=====================================================================#


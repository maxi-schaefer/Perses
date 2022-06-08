import sys
import os
from pyfiglet import figlet_format
from lib.settings import get_path

#=====================================================================#

def rgb(r, g, b, text):
        return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)

#=====================================================================#

def server_banner(theme=None):
    if theme == "neon":
        print(server_bannerTheme(purple, neon))    

def custom_banner(theme=None):
    if theme == "neon":
        print(custom_bannerTheme(purple, neon))   

#=====================================================================#

def log(text):
    print(rgb(105, 67, 171, f"[Perses] - {rgb(255, 255, 255, text)}"))

#=====================================================================#

# Clear
def clear():
    if os.name == "nt":
        os.system("cls")
        server_banner("neon")
    else:
        os.system("clear")
        server_banner("neon")

#=====================================================================#

def clear_main():
    if os.name == "nt":
        os.system("cls")
        banner("neon")
    else:
        os.system("clear")
        banner("neon")

#=====================================================================#

def clear_custom():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#=====================================================================#

def purple(text):
    os.system(""); fade = "" 
    red = 255
    for line in text.splitlines():
        fade += (f"\033[38;2;{red};0;180m{line}\033[0m\n")
        if not red == 0:
            red -= 20
            if red < 0:
                red = 0
    return fade

def neon(text):
    os.system(""); fade = ""
    for line in text.splitlines():
        red = 255
        for char in line:
            red -= 2
            if red > 255:
                red = 255
            fade += (f"\033[38;2;{red};0;255m{char}\033[0m")
        fade += "\n"
    return fade

#=====================================================================#

def set_console_title(text:str):
    sys.stdout.write(f"\x1b]2;{text}\x07")

#=====================================================================#

def banner(theme=None):
    if theme == "neon":
        print(bannerTheme(purple, neon))

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
    help = ""
    total = 0
    print(rgb(255, 255, 255, f"\n{'▬'*50}"))
    print(rgb(255, 255, 255, "\n\t× Perses | Help ×\n"))
    # loop through all available commands
    for x in commands:
        help += f"\n[{total}] × {commands[total][0]} | {commands[total][1]} ×"
        total += 1
    help += f"\n[{total}] × Anything | Will run a command on the Targets PC like command prompt ×"

    print(purple(help))
    print(rgb(255, 255, 255, f"\n{'▬'*50}"))

#=====================================================================#

def bannerTheme(type1, type2):
    return type1(f'''
    
                                    ██████╗ ███████╗██████╗ ███████╗███████╗███████╗
                                    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
                                    ██████╔╝█████╗  ██████╔╝███████╗█████╗  ███████╗
                                    ██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██╔══╝  ╚════██║
> Created by gokimax                ██║     ███████╗██║  ██║███████║███████╗███████║
> Discord:maxシ#6858                ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝''')+type2(f'''
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       EDUCATIONAL PURPOSE                  |           DISCORD               |            CREDITS
[1] Start RAT Server                        | [5] Hypesquad Changer           | [8] Github
[2] Start Botnet Server                     | [6] Send Nitro Emoji            | [9] Twitter
[3] IP Lookup                               | [7] Status Changer              | [10] Exit
[4] Domain to IPv4                          |                                 |
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

def server_bannerTheme(type1, type2):
    return type1(f'''
    
                                    ██████╗ ███████╗██████╗ ███████╗███████╗███████╗
                                    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
                                    ██████╔╝█████╗  ██████╔╝███████╗█████╗  ███████╗
                                    ██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██╔══╝  ╚════██║
> Created by gokimax                ██║     ███████╗██║  ██║███████║███████╗███████║
> Discord:maxシ#6858                ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝''')+type2(f'''
                                    Type 'help' to see a list of commands!
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

def custom_bannerTheme(type1, type2):
    return type1(f'''
    
                                    ██████╗ ███████╗██████╗ ███████╗███████╗███████╗
                                    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
                                    ██████╔╝█████╗  ██████╔╝███████╗█████╗  ███████╗
                                    ██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██╔══╝  ╚════██║
> Created by gokimax                ██║     ███████╗██║  ██║███████║███████╗███████║
> Discord:maxシ#6858                ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝''')+type2(f'''
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')
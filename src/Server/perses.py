import sys
from time import sleep
from lib.terminal import rgb, log, clear, clear_main, clear_custom, set_console_title
from lib.utils import ip_lookup, domain_name, open_link, load
from lib.server import Server
from lib.settings import get_path, setup_config

# Setup Config
setup_config()

from Modules.botnet import BotnetServer

done = 'false'

# Set Console Title
set_console_title("Perses | Loading...")

def TakeCommand():
    clear_main()
    while True:
        try:
            command = input(rgb(105, 67, 171, f"┌── {rgb(255, 255, 255, '[')}{rgb(105, 67, 171, f'root@perses')}{rgb(255, 255, 255, ']')}\n{rgb(105, 67, 171, f'└──────#')} "))
            if command == "1":
                #=- RAT Server -=#
                load("Starting RAT Server...")
                sleep(2)
                # Start the server
                activeServer = Server(get_path("ServerIP"), get_path("ServerPort"))
                activeServer.run()
            elif command == "2":
                #=- Botnet Server -=#
                load("Starting Botnet Server...")
                sleep(2)
                # Start the server
                BotnetServer()
            elif command == "3":
                #=- IP lookup -=#
                ip_lookup()
            elif command ==  "4":
                #=- Domain to ip -=#
                domain_name()
            elif command ==  "5":
                #=- Update Styles -=#
                clear_main()
            elif command ==  "6":
                #=- Credits: Github -=#
                log("Opening browser...")
                sleep(2)
                open_link("https://github.com/gokiimax")    
            elif command ==  "7":
                #=- Credits: Twitter -=#
                log("Opening browser...")
                sleep(2)
                open_link("https://twitter.com/gokimax_x")
            elif command ==  "8":
                #=- Exit Application -=#
                exit()
            elif command ==  "clear":
                #=- Clear -=#
                clear_main()
            else:
                log("Enter a valid Method")
        except KeyboardInterrupt:
            clear()

def exit():
    log("Exiting...")
    sleep(2)
    clear_custom()
    sys.exit(-1)

def setup():
    load("Loading Modules...")
    sleep(1)
    set_console_title("Perses | Dashboard")
    TakeCommand()

if __name__ == "__main__":
    setup()
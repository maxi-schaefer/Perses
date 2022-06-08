import requests
from lib.terminal import rgb, clear_main
from lib.settings import get_path
import time

#=====================================================================#

def hypeSquadChanger():
    hypetoken = input(f"{rgb(105, 67, 171, '~# ')}Token: ")
    print(f"\n{rgb(105, 67, 171, '[1]')} - Bravery\n{rgb(105, 67, 171, '[2]')} - Briliance\n{rgb(105, 67, 171, '[3]')} - Balance\n")
    hypesquad = input(f"{rgb(105, 67, 171, '~# ')}Choice: ")
    headersosat = {
        'Authorization': str(hypetoken)
    }

    payloadsosat = {
        'house_id': str(hypesquad)
    }
    time.sleep(1)
    rep = requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headersosat)
    clear_main()

#=====================================================================#

def nitro_emojii():
    emoji_link = input(f"{rgb(105, 67, 171, '~# ')}Emoji Link: ")
    if not str(emoji_link).startswith("https://"):
        print("[-] Invalid link")
        return
    token = input(f"{rgb(105, 67, 171, '~# ')}Token: ")
    channelId = input(f"{rgb(105, 67, 171, '~# ')}Channel Id: ")
    authorize_header = {'Authorization': token}
    requests.post(f'https://discordapp.com/api/v6/channels/{channelId}/messages', headers=authorize_header, json={'content': f'{emoji_link}'})

#=====================================================================#
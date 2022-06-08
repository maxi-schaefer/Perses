from site import execsitecustomize
import requests
from lib.terminal import rgb, clear_main, log
from lib.utils import getheaders
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

def nitro_emoji():
    emoji_link = input(f"{rgb(105, 67, 171, '~# ')}Emoji Link: ")
    if not str(emoji_link).startswith("https://"):
        print("[-] Invalid link")
        return
    token = input(f"{rgb(105, 67, 171, '~# ')}Token: ")
    channelId = input(f"{rgb(105, 67, 171, '~# ')}Channel Id: ")
    authorize_header = {'Authorization': token}
    requests.post(f'https://discordapp.com/api/v6/channels/{channelId}/messages', headers=authorize_header, json={'content': f'{emoji_link}'})
    log("Emoji sent...")
    clear_main()

#=====================================================================#

def statusChanger():
    token = input(f"{rgb(105, 67, 171, '~# ')}Token: ")
    custom_text = input(f"{rgb(105, 67, 171, '~# ')}Status Text: ")
    emoji = input(f"{rgb(105, 67, 171, '~# ')}Status Emoji: ")
    custom_status = {"custom_status": {"text": custom_text, "emoji_name": emoji}}    
    authorize_header = {'Authorization': token}
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=authorize_header, json=custom_status)
        log(f"Status changed to: '{custom_text}'!")
    except Exception as e:
        print(f"[-] An Exception occured: {e}")
    time.sleep(2)
    clear_main()

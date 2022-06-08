import time
import json
from pypresence import Presence

class RichPresence():

    def __init__(self, cid):
        self.presence = Presence(cid)
        self.client_id = cid
        self.presence.connect()

    def main(self):
        while True:
            time.sleep(20)

    def update(self):
        start_time = time.time()
        buttons = [{"label": "Github", "url": "https://github.com/gokiimax/Perses"}, {"label": "Twitter", "url": "https://twitter.com/gokimax_x"}]
        try:
            self.presence.update(buttons=buttons,large_image="large", small_image="small", large_text="Perses", details="Multitool", start=start_time)
        except:
            print("[-] Invalid Richpresence")
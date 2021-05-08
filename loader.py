import threading
import time
class loading:
    def __init__(self, text, run) -> None:
        self.text = text
        self.run = True
    def loader(self):
        while True:
            for i in ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]:
                print(f"{self.text}{i}", end="\r")
                time.sleep(0.1)
            if not self.run:
                break
    def running(self):
        threading.Thread(target=self.loader, args=()).start()
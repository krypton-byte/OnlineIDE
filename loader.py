import colorama
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
help =f"""{colorama.Fore.LIGHTCYAN_EX}options:
    {colorama.Fore.LIGHTGREEN_EX}--port {colorama.Fore.LIGHTMAGENTA_EX}\t: {colorama.Fore.LIGHTRED_EX}7890 {colorama.Fore.LIGHTYELLOW_EX}default port
    {colorama.Fore.LIGHTGREEN_EX}--workspace {colorama.Fore.LIGHTMAGENTA_EX}: {colorama.Fore.LIGHTRED_EX}$HOME{colorama.Fore.LIGHTYELLOW_EX} default workspace
{colorama.Fore.LIGHTCYAN_EX}e.g:
    {colorama.Fore.LIGHTRED_EX}$ {colorama.Fore.LIGHTGREEN_EX}bash {colorama.Fore.LIGHTYELLOW_EX}termux.sh {colorama.Fore.LIGHTRED_EX}--port={colorama.Fore.LIGHTGREEN_EX}8753 {colorama.Fore.LIGHTRED_EX}--workspace={colorama.Fore.LIGHTGREEN_EX}$(pwd)
"""
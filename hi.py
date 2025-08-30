import time
import os

colors = ["\033[41m", "\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m"]
reset = "\033[0m"

try:
    while True:
        for color in colors:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(color + " " * 50 + reset)
            time.sleep(0.2)
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Stopped flashing safely!")

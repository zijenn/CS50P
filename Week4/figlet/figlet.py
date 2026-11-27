import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()
font = figlet.setFont(font = random.choice(fonts))

if len(sys.argv) not in (1,3):
    sys.exit()

if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit()
    font = figlet.setFont(font = sys.argv[2])

text = input("Input: ")
print(f"Output: {figlet.renderText(text)}")
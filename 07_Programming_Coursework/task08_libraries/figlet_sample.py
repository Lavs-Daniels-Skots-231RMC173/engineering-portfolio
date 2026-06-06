import sys
import pyfiglet
import random

def main():
    
    available_fonts = pyfiglet.FigletFont.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in available_fonts:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

    text = input("Input: ")

    if font:
        figlet = pyfiglet.Figlet(font=font)
    else:
        figlet = pyfiglet.Figlet()

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
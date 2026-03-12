
"""
Blacksmith
by Kaenan "Kaen" Cummins
3/11/26
-------------------------------------------------------------------------------------------------------------------------------------------
This program tasks users with constructing an ASCII weapon using pre-made and user-generated parts.
Users do this by selecting these parts from a sequence of lists, each displaying available parts corresponding to a piece of the weapon.
Once all parts are selected, the program assembles them into the shape of a weapon.
Users are additionally able to name and save this weapon to a .txt file.
From the menu, users are also able to generate their own parts for use in the main "Forge Weapon" mode, or delete already existing options.
"""

from menu import title, menu, customParts, instructions, forgeAgain, exitForge

from sword import Sword

# ANSI color codes
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
GRAY = '\033{90m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Main driver
def main():
    titleDisplayed = False
    if titleDisplayed == False:
        title()
    running = True
    FORGE = Sword()
    while running:
        answer = menu()
        if answer == '1':
            instructions()
        elif answer == '2':
            forging = True
            while forging:
                blade = FORGE.blade()
                guard = FORGE.guard()
                grip = FORGE.grip()
                pommel = FORGE.pommel()
                name = FORGE.name()
                sword = FORGE.sword()
                save =  FORGE.save()
                forging = forgeAgain()
        elif answer == '3':
            forging = True
            while forging:
                forging = customParts()
        elif answer == '4':
            running = exitForge()
        else:
            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")


# In the beginning...
if __name__ == "__main__":
    main()


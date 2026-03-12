
from sword import CustomPart, Remove

# ANSI color codes
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RESET = '\033[0m'
GRAY = '\033{90m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# title function, houses the really cool title text
def title():
    print(f"\n"
          f"{YELLOW}     ***** **   ***                             *                                                        *       \n"
          f"  ******  ***    ***                          **                                       *       {WHITE}***{YELLOW}     **        \n"
          f" **   *  * **     **                          **                                      ***      {WHITE}***{YELLOW}     **        \n"
          f"*    *  *  **     **                          **                                       *       {WHITE}***{YELLOW}     **        \n"
          f"    *  *   *      **                          **            ****                               {WHITE}***{YELLOW}     **        \n"
          f"   ** **  *       **       ****       ****    **  ***      * **** * *** **** ****    ***    {WHITE}*********{YELLOW}  **  ***   \n"
          f"   ** ** *        **      * ***  *   * ***  * ** * ***    **  ****   *** **** ***  *  ***      {WHITE}* *{YELLOW}     ** * ***  \n"
          f"   ** ***         **     *   ****   *   ****  ***   *    ****         **  **** ****    **      {WHITE}* *{YELLOW}     ***   *** \n"
          f"   ** ** ***      **    **    **   **         **   *       ***        **   **   **     **      {WHITE}* *{YELLOW}     **     ** \n"
          f"   ** **   ***    **    **    **   **         **  *          ***      **   **   **     **      {WHITE}* *{YELLOW}     **     ** \n"
          f"   *  **     **   **    **    **   **         ** **            ***    **   **   **     **      {WHITE}* *{YELLOW}     **     ** \n"
          f"      *      **   **    **    **   **         ******      ****  **    **   **   **     **      {WHITE}* *{YELLOW}     **     ** \n"
          f"  ****     ***    **    **    **   ***     *  **  ***    * **** *     **   **   **     **      {WHITE}* *{YELLOW}     **     ** \n"
          f" *  ********      *** *  ***** **   *******   **   *** *    ****      ***  ***  ***    *** *   {WHITE}* *{YELLOW}     **     ** \n"
          f"*     ****         ***    ***   **   *****     **   ***                ***  ***  ***    ***    {WHITE}* *{YELLOW}      **    ** \n"
          f"*                                                                                              {WHITE}* *{YELLOW}            *  \n"
          f" **                                                                                             {WHITE}*{YELLOW}            *   \n"
          f"                                                                                                            *    \n"
          f"                                                                                                           *     ")

# menu function, handles the main menu
def menu():
    print(f"\n{GREEN}1.{RESET} Instructions\n"
          f"{GREEN}2.{RESET} Forge Weapon\n"
          f"{GREEN}3.{RESET} Create Parts\n"
          f"{GREEN}4.{RESET} Exit")
    menu = True
    while menu:
        choice = input(f"Make your choice: ")
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        elif choice == "3":
            return "3"
        elif choice == "4":
            return "4"
        else:
            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

# instruction function, prints a sequence of instructions to help the user get started
def instructions():
    print(f"\nWelcome to Blacksmith!\n"
          f"The objective of this program is simple: Build a cool sword! (Or another kind of weapon, I won't stop you.)")
    input("\nPress ENTER to continue...")
    print("\nWhen you select Forge Weapon from the menu, you will be given a series of choices that look something like this:\n"
          f"{GREEN}1.{BLUE} ======>  |  Long\n"
          f"{GREEN}2.{BLUE}   ====>  |  Short\n"
          f"{GREEN}3.{BLUE}     ==>  |  Dagger\n"
          f"{RESET}Make your choice: <---- ONLY ACCEPTS NUMBERS\n"
          f"Once you've made four of these choices, a sword will be assembled based on the parts you chose, and you'll have\n"
          f"the opportunity to name it before it gets displayed.")
    input("\nPress ENTER to continue...")
    print(f"\nIf you select Create Parts from the menu, you'll be able to create (or destroy) custom parts that can be used\n"
          f"in the Forge Weapon mode.")
    input("\nPress ENTER to return to the menu...")

# forgeAgain function, asks the user if they would like to assemble another weapon
def forgeAgain():
    print(f"\nForge another weapon?\n"
          f"{GREEN}1.{RESET} Yes\n"
          f"{GREEN}2.{RESET} No")
    menu = True
    while menu:
        choice = input(f"Make your choice: ")
        if choice == "1":
            return
        elif choice == "2":
            return False
        else:
            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

# customParts function, handles most of the menu-ing in the Create Parts mode
def customParts():
    create = CustomPart()
    remove = Remove()
    running = True
    while running:
        print(f"\n{GREEN}1.{BLUE} Blades O==I{UNDERLINE}====>{RESET}\n"
              f"{GREEN}2.{BLUE} Guards O=={UNDERLINE}I{RESET}{BLUE}====>\n"
              f"{GREEN}3.{BLUE} Grips O{UNDERLINE}=={RESET}{BLUE}I====>\n"
              f"{GREEN}4.{BLUE} Pommels {UNDERLINE}O{RESET}{BLUE}==I====>\n"
              f"{GREEN}5.{RESET} Back to menu")
        crafting = True
        choice1 = input(f"What kind of parts do you want to create?: ")
        while crafting:
            try:
                choice = int(choice1)
                while choice == 1:
                    print(f"\n{UNDERLINE}Blades{RESET}\n"
                          f"{GREEN}1.{RESET} Create new parts\n"
                          f"{GREEN}2.{RESET} Remove old parts\n"
                          f"{GREEN}3.{RESET} Back\n")
                    choice = input(f"Make your choice (Numbers only): ")
                    if choice == '1':
                        create.blade()
                        print(f"Blade successfully created!")
                        crafting = False
                    elif choice == '2':
                        remove.blade()
                        print(f"Blade successfully destroyed!")
                        crafting = False
                    elif choice == '3':
                        crafting = False
                    else:
                        print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

                while choice == 2:
                    print(f"\n{UNDERLINE}Guards{RESET}\n"
                          f"{GREEN}1.{RESET} Create new parts\n"
                          f"{GREEN}2.{RESET} Remove old parts\n"
                          f"{GREEN}3.{RESET} Back\n")
                    choice = input(f"Make your choice (Numbers only): ")
                    if choice == '1':
                        create.guard()
                        print(f"Guard successfully created!")
                        crafting = False
                    elif choice == '2':
                        remove.guard()
                        print(f"Guard successfully destroyed!")
                        crafting = False
                    elif choice == '3':
                        crafting = False
                    else:
                        print(f"{RED}{BOLD}That wasn't a choice.(Numbers only){RESET}")

                while choice == 3:
                    print(f"\n{UNDERLINE}Grips{RESET}\n"
                          f"{GREEN}1.{RESET} Create new parts\n"
                          f"{GREEN}2.{RESET} Remove old parts\n"
                          f"{GREEN}3.{RESET} Back\n")
                    choice = input(f"Make your choice (Numbers only): ")
                    if choice == '1':
                        create.grip()
                        print(f"Grip successfully created!")
                        crafting = False
                    elif choice == '2':
                        remove.grip()
                        print(f"Grip successfully destroyed!")
                        crafting = False
                    elif choice == '3':
                        crafting = False
                    else:
                        print(f"{RED}{BOLD}That wasn't a choice.(Numbers only){RESET}")

                while choice == 4:
                    print(f"\n{UNDERLINE}Pommels{RESET}\n"
                          f"{GREEN}1.{RESET} Create new parts\n"
                          f"{GREEN}2.{RESET} Remove old parts\n"
                          f"{GREEN}3.{RESET} Back\n")
                    choice = input(f"Make your choice (Numbers only): ")
                    if choice == '1':
                        create.pommel()
                        print(f"Pommel successfully created!")
                        crafting = False
                    elif choice == '2':
                        remove.pommel()
                        print(f"Pommel successfully destroyed!")
                        crafting = False
                    elif choice == '3':
                        crafting = False
                    else:
                        print(f"{RED}{BOLD}That wasn't a choice. {RESET}({GREEN}Numbers{RESET} only)")

                while choice == 5:
                    return

                while int(choice) > 5 or int(choice) < 1:
                    print(f"{RED}{BOLD}That wasn't a choice. {RESET}({GREEN}Numbers{RESET} only)")

            except ValueError:
                print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

# exitForge function, closes the program
def exitForge():
    print(f"\nAre you sure you want to quit?\n"
          f"{GREEN}1.{RESET} Yes\n"
          f"{GREEN}2.{RESET} No")
    menu = True
    while menu:
        choice = input(f"Make your choice: ")
        if choice == "1":
            print("Thanks for forging!")
            return False
        elif choice == "2":
            return
        else:
            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")
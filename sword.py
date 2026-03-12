
# ANSI color codes
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RESET = '\033[0m'
GRAY = '\033{90m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# CustomPart class, for when users generate custom parts
class CustomPart:
    def __init__(self): #Init
        self.shape = ''
        self.name = ''

    # blade method, handles custom blades
    def blade(self):
        shapeMaker = True
        nameMaker = True
        while shapeMaker:
            shape = input(f"\nWhat should the blade look like?(Max. 10 char.): ")
            if len(shape) > 10:
                print(f"{RED}{BOLD}That's too long!{RESET}")
            else:
                self.shape = shape
                shapeMaker = False
        while nameMaker:
            name = input(f"What should the blade be called?(Max. 25 char.): ")
            if len(name) > 25:
                print(f"{RED}{BOLD}That's too long!{RESET}")
            elif len(name) < 1:
                print(f"{RED}{BOLD}That's too short!{RESET}")
            else:
                self.name = name
                nameMaker = False

        try:
            with open('sword blade.txt', "a") as f:
                f.write(f"{self.name},{self.shape}\n")
        except FileNotFoundError:
            with open('sword blade.txt', "w") as f:
                f.write("Long,======>\n"
                        "Short,====>\n"
                        "Dagger,==>\n"
                        "Great,:::::::>\n"
                        "Catch,tttt>\n"
                        "Thin,------\n"
                        f"{self.name},{self.shape}\n")

    # guard method, handles custom guards
    def guard(self):
        shapeMaker = True
        nameMaker = True
        while shapeMaker:
            shape = input(f"\nWhat should the guard look like?(Max. 3 char.): ")
            if len(shape) > 3:
                print(f"{RED}{BOLD}That's too long!{RESET}")
            else:
                self.shape = shape
                shapeMaker = False
        while nameMaker:
            name = input(f"What should the guard be called?(Max. 25 char.): ")
            if len(name) > 25:
                print(f"{RED}{BOLD}That's too long!{RESET}")
            elif len(name) < 1:
                print(f"{RED}{BOLD}That's too short!{RESET}")
            else:
                self.name = name
                nameMaker = False
        try:
            with open('sword guard.txt', "a") as f:
                f.write(f"{self.name},{self.shape}\n")
        except FileNotFoundError:
            with open('sword guard.txt', "w") as f:
                f.write("Straight,|\n"
                        "Ornate,I\n"
                        "Thick,K\n"
                        "Cross,+\n"
                        "Catch,{\n"
                        "Deflect,)\n"
                        "Clamshell,l\n"
                        f"{self.name},{self.shape}\n")

    # grip method, handles custom grips
    def grip(self):
        shapeMaker = True
        nameMaker = True
        while shapeMaker:
            shape = input(f"\nWhat should the grip look like?(Max. 8 char.): ")
            if len(shape) > 8:
                print(f"{RED}{BOLD}That's too long!{RESET}")
            else:
                self.shape = shape
                shapeMaker = False
        while nameMaker:
            name = input(f"What should the grip be called?(Max. 25 char.): ")
            if len(name) > 25:
                print(f"{RED}{BOLD}That's too long!{RESET}")
            elif len(name) < 1:
                print(f"{RED}{BOLD}That's too short!{RESET}")
            else:
                self.name = name
                nameMaker = False

        try:
            with open('sword grip.txt', "a") as f:
                f.write(f"{self.name},{self.shape}\n")
        except FileNotFoundError:
            with open('sword grip.txt', "w") as f:
                f.write("One-Handed,==\n"
                        "Hand-and-a-Half,===\n"
                        "Two-Handed,====\n"
                        "Pole,======\n"
                        f"{self.name},{self.shape}\n")

    # pommel method, handles custom pommels
    def pommel(self):
        shapeMaker = True
        nameMaker = True
        while shapeMaker:
            shape = input(f"\nWhat should the pommel look like?(Max. 2 char.): ")
            if len(shape) > 2:
                print(f"{RED}{BOLD}That's too long!{RESET}")
            else:
                self.shape = shape
                shapeMaker = False
        while nameMaker:
            name = input(f"What should the pommel be called?(Max. 25 char.): ")
            if len(name) > 25:
                print(f"{RED}{BOLD}That's too long!{RESET}")
            elif len(name) < 1:
                print(f"{RED}{BOLD}That's too short!{RESET}")
            else:
                self.name = name
                nameMaker = False

        try:
            with open('sword pommel.txt', "a") as f:
                f.write(f"{self.name},{self.shape}\n")
        except FileNotFoundError:
            with open('sword pommel.txt', "w") as f:
                f.write("Round,O\n"
                        "Ring,¤\n"
                        "Spike,<\n"
                        "No,\n"
                        f"{self.name},{self.shape}\n")

# Remove class, for when users want to delete a part
class Remove:
    def __init__(self):
        pass

    # blade method, handles blade destruction
    def blade(self):
        print(f"\nSelect the blade to be destroyed. O==I{UNDERLINE}====>{RESET}\n"
              f"{GREEN}0.{RESET} Cancel selection")
        bladeList = []
        maker = True
        while maker:
            try:
                with open("sword blade.txt", "r") as f:
                    counter = 0
                    for line in f:
                        counter += 1
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            name,shape = parts
                            bladeList.append(f"{parts}")
                            print(f"{GREEN}{counter}. {BLUE}{shape:>2} | {name} Blade{RESET}")
                    while maker:
                        choice = input("Make your choice: ")
                        if choice == "0":
                            return
                        try:
                            blade = int(choice) - 1
                            if 0 <= blade <= counter:
                                bladeList.pop(blade)
                                with open("sword blade.txt", "w") as f:
                                    for i in bladeList:
                                        f.write(f"{i.replace("[","").replace("]","").replace("'","").replace(" ","")}\n")
                                return
                            else:
                                print(f"{RED}{BOLD}That wasn't a choice. (Numbers only){RESET}")
                        except ValueError:
                            print(f"{RED}{BOLD}That wasn't a choice. (Numbers only){RESET}")
            except FileNotFoundError:
                with open("sword blade.txt", "w") as f:
                    f.write("Long,======>\n"
                            "Short,====>\n"
                            "Dagger,==>\n"
                            "Great,:::::::>\n"
                            "Catch,tttt>\n"
                            "Thin,------\n")

    # guard method, handles guard destruction
    def guard(self):
        print(f"\nSelect the guard to be destroyed. O=={UNDERLINE}I{RESET}====>\n"
              f"{GREEN}0.{RESET} Cancel selection")
        guardList = []
        maker = True
        while maker:
            try:
                with open("sword guard.txt", "r") as f:
                    counter = 0
                    for line in f:
                        counter += 1
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            name, shape = parts
                            guardList.append(f"{parts}")
                            print(f"{GREEN}{counter}. {BLUE}{shape:>2} | {name} Guard{RESET}")
                    while maker:
                        choice = input("Make your choice: ")
                        if choice == "0":
                            return
                        try:
                            guard = int(choice) - 1
                            if 0 <= guard <= counter:
                                guardList.pop(guard)
                                with open("sword guard.txt", "w") as f:
                                    for i in guardList:
                                        f.write(
                                            f"{i.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")}\n")
                                return
                            else:
                                print(f"{RED}{BOLD}That wasn't a choice. (Numbers only){RESET}")
                        except ValueError:
                            print(f"{RED}{BOLD}That wasn't a choice. (Numbers only){RESET}")
            except FileNotFoundError:
                with open("sword guard.txt", "w") as f:
                    f.write("Straight,|\n"
                            "Ornate,I\n"
                            "Thick,K\n"
                            "Cross,+\n"
                            "Catch,{\n"
                            "Deflect,)\n"
                            "Clamshell,l\n")

    # grip method, handles grip destruction
    def grip(self):
        print(f"\nSelect the grip to be destroyed. O{UNDERLINE}=={RESET}I====>\n"
              f"{GREEN}0.{RESET} Cancel selection")
        gripList = []
        maker = True
        while maker:
            try:
                with open("sword grip.txt", "r") as f:
                    counter = 0
                    for line in f:
                        counter += 1
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            name, shape = parts
                            gripList.append(f"{parts}")
                            print(f"{GREEN}{counter}. {BLUE}{shape:>2} | {name} Grip{RESET}")
                    while maker:
                        choice = input("Make your choice: ")
                        if choice == "0":
                            return
                        try:
                            grip = int(choice) - 1
                            if 0 <= grip <= counter:
                                gripList.pop(grip)
                                with open("sword grip.txt", "w") as f:
                                    for i in gripList:
                                        f.write(
                                            f"{i.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")}\n")
                                return
                            else:
                                print(f"{RED}{BOLD}That wasn't a choice. (Numbers only){RESET}")
                        except ValueError:
                            print(f"{RED}{BOLD}That wasn't a choice. (Numbers only){RESET}")
            except FileNotFoundError:
                with open("sword grip.txt", "w") as f:
                    f.write("One-Handed,==\n"
                            "Hand-and-a-Half,===\n"
                            "Two-Handed,====\n"
                            "Pole,======\n")

    # pommel method, handles pommel destruction
    def pommel(self):
        print(f"\nSelect the pommel to be destroyed. {UNDERLINE}O{RESET}==I====>\n"
              f"{GREEN}0.{RESET} Cancel selection")
        pommelList = []
        maker = True
        while maker:
            try:
                with open("sword pommel.txt", "r") as f:
                    counter = 0
                    for line in f:
                        counter += 1
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            name, shape = parts
                            pommelList.append(f"{parts}")
                            print(f"{GREEN}{counter}. {BLUE}{shape:>2} | {name} Pommel{RESET}")
                    while maker:
                        choice = input("Make your choice: ")
                        if choice == "0":
                            return
                        try:
                            pommel = int(choice) - 1
                            if 0 <= pommel <= counter:
                                pommelList.pop(pommel)
                                with open("sword pommel.txt", "w") as f:
                                    for i in pommelList:
                                        f.write(
                                            f"{i.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")}\n")
                                return
                            else:
                                print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")
                        except ValueError:
                            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")
            except FileNotFoundError:
                with open("sword pommel.txt", "w") as f:
                    f.write("One-Handed,=\n"
                            "Hand-and-a-Half,==\n"
                            "Two-Handed,===\n"
                            "Pole,=====\n")

# Where the magic happens...
# Sword class, for when users want to generate a weapon
class Sword:
    def __init__(self):
        #self.__swordValue = 150
        self._pommel = ""
        self._grip = ""
        self._guard = ""
        self._blade = ""
        self._name = ""

    # sword method, assembles the completed sword
    def sword(self):
        # Code that used to handle users not choosing a name
        # if self._name == "":
        #     print("\nBehold!")
        #     return print(f"{self._pommel}{self._grip}{self._guard}{self._blade}")
        #else:
            print(f"\nBehold: {self._name}")
            print(f"{self._pommel}{self._grip}{self._guard}{self._blade}")

    # blade method, prints blade options then prompts for a choice/validates
    def blade(self):
        print(f"\nSelect your blade. O==I{UNDERLINE}====>{RESET}")
        bladeList = []
        maker = True
        while maker:
            try:
                with open("sword blade.txt", "r") as f:
                    counter = 0
                    for line in f:
                        counter += 1
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            name, shape = parts
                        bladeList.append(f"{shape}")
                        print(f"{GREEN}{counter}. {BLUE}{shape:>1} {"|":>2} {name} Blade{RESET}")
                    while maker:
                        choice = input("Make your choice (Numbers only): ")
                        try:
                            blade = int(choice) - 1
                            if 0 <= blade <= counter:
                                self._blade = f"{bladeList[blade]}"
                                return
                            else:
                                print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")
                        except ValueError:
                            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

            except FileNotFoundError:
                with open("sword blade.txt", "w") as f:
                    f.write("Long,======>\n"
                            "Short,====>\n"
                            "Dagger,==>\n"
                            "Great,:::::::>\n"
                            "Catch,tttt>\n"
                            "Thin,------\n")

    #grip method, prints grip options then prompts for a choice/validates
    def grip(self):
        print(f"\nSelect your grip. O{UNDERLINE}=={RESET}I====>")
        gripList = []
        maker = True
        while maker:
            try:
                with open("sword grip.txt", "r") as f:
                    counter = 0
                    for line in f:
                        counter += 1
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            name, shape = parts
                        gripList.append(f"{shape}")
                        print(f"{GREEN}{counter}. {BLUE}{shape:>2} | {name} Grip{RESET}")
                    while maker:
                        choice = input(f"Make your choice: ")
                        try:
                            grip = int(choice) - 1
                            if 0 <= grip <= counter:
                                self._grip = f"{gripList[grip]}"
                                return
                            else:
                                print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")
                        except ValueError:
                            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

            except FileNotFoundError:
                with open("sword grip.txt", "w") as f:
                    f.write("One-Handed,==\n"
                            "Hand-and-a-Half,===\n"
                            "Two-Handed,====\n"
                            "Pole,======\n")

    # guard method, prints guard options then prompts for a choice/validates
    def guard(self):
        print(f"\nSelect your guard. O=={UNDERLINE}I{RESET}====>")
        guardList = []
        maker = True
        while maker:
            try:
                with open("sword guard.txt", "r") as f:
                    counter = 0
                    for line in f:
                        counter += 1
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            name, shape = parts
                        guardList.append(f"{shape}")
                        print(f"{GREEN}{counter}. {BLUE}{shape:>2} | {name} Guard{RESET}")
                    while maker:
                        choice = input(f"Make your choice: ")
                        try:
                            guard = int(choice) - 1
                            if 0 <= guard <= counter:
                                self._guard = f"{guardList[guard]}"
                                return
                            else:
                                print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")
                        except ValueError:
                            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

            except FileNotFoundError:
                with open("sword guard.txt", "w") as f:
                    f.write("Straight,|\n"
                            "Ornate,I\n"
                            "Thick,K\n"
                            "Cross,+\n"
                            "Catch,{\n"
                            "Deflect,)\n"
                            "Clamshell,l\n")

    # pommel method, prints pommel options then prompts for a choice/validates
    def pommel(self):
        print(f"\nSelect your pommel. {UNDERLINE}O{RESET}==I====>")
        pommelList = []
        maker = True
        while maker:
            try:
                with open("sword pommel.txt", "r") as f:
                    counter = 0
                    for line in f:
                        counter += 1
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            name, shape = parts
                        pommelList.append(f"{shape}")
                        print(f"{GREEN}{counter}. {BLUE}{shape:>2} | {name} Pommel{RESET}")
                    while maker:
                        choice = input(f"Make your choice: ")
                        try:
                            pommel = int(choice) -1
                            if 0 <= pommel <= counter:
                                self._pommel = f"{pommelList[pommel]}"
                                return
                            else:
                                print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")
                        except ValueError:
                            print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

            except FileNotFoundError:
                with open ("sword pommel.txt", "w") as f:
                    f.write("Round,O\n"
                            "Ring,¤\n"
                            "Spike,<\n"
                            "No,\n")

    # name method, sets weapon name
    def name(self):
        print(f"\nName your weapon!")
        self._name = input(f"Name: ")

    # save method, user may choose to save their sword to a .txt file
    def save(self):
        saving = True
        print(f"\nSave your sword?\n"
              f"{GREEN}1.{RESET} Yes\n"
              f"{GREEN}2.{RESET} No")
        while saving:
            choice = input("Make your choice: ")
            if choice == "1":
                with open (f"{self._name}.txt", "w") as f:
                    f.write(f"{self._pommel}{self._grip}{self._guard}{self._blade}")
                    print(f"Saving weapon... Done!")
                    saving = False
            elif choice == "2":
                saving = False
            else:
                print(f"{RED}{BOLD}That wasn't a choice.{RESET} ({GREEN}Numbers{RESET} only)")

# Deprecated partsValue method, would have assigned a gold value to each part and added it to the total value of the finished weapon
# Scrapped due to time constraints, keeping it around in case I want to expand on Blacksmith one day.
    # def partsValue(self, material, guard, blade):
    #     # Blades
    #     if blade == "a":
    #         self.__swordValue += 500
    #     elif blade == "b":
    #         self.__swordValue += 350
    #     elif blade == "c":
    #         self.__swordValue += 250
    #     elif blade == "d":
    #         self.__swordValue += 750
    #     elif blade == "e":
    #         self.__swordValue += 650
    #     elif blade == "f":
    #         self.__swordValue += 450
    #     else:
    #         self.__swordValue += 1000
    #     # Guards
    #     if guard == "b":
    #         self.__swordValue += 200
    #     else:
    #         self.__swordValue += 100
    #     # Material multiplier
    #     if material == "a":
    #         pass
    #     elif material == "b":
    #         self.__swordValue = self.__swordValue * 1.25
    #     elif material == "c":
    #         self.__swordValue = self.__swordValue * 1.50
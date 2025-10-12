from imobiledevice import event_unsubscribe
from samba.dcerpc.netlogon import netr_LogonSamLogonEx

Battle_Ground = {"Mountain Of Wisdom": ["spoon", "pen"],
                 "Waterfall": [],
                 "Stone Cave": ["Black smith anville"],
                 "Farm": [],
                 "Field": ["Knights Sword"]
                 }
current = "Field"

paths = {"Mountain Of Wisdom": ["spoon", "pen"],
                 "Waterfall": [],
                 "Stone Cave": ["Black smith anville"],
                 "Farm": [],
                 "Field": ["Knights Sword"]
                 }
current = "Field"
inventory = []


def greeting():


    Welcome_Screen = r""" WELCOME TO
     _____ ___  _   _ ____ _____ _   _    _   _ ___ ____ _   _ _____
    |  ___/ _ \| | | |  _ \_   _| | | |  | \ | |_ _/ ___| | | |_   _|
    | |_ | | | | | | | |_) || | | |_| |  |  \| || | |  _| |_| | | |
    |  _|| |_| | |_| |  _ < | | |  _  |  | |\  || | |_| |  _  | | |
    |_|   \___/ \___/|_| \_\|_| |_| |_|  |_| \_|___\____|_| |_| |_|

    """
    print(f"{Welcome_Screen}")
    user_input = input(f"For you're first trial take the {Battle_Ground["Field"][0]} infront of you.\n").lower().strip()

    while user_input != "take":
        user_input = input(f"You sure you don't want to take the sword? \nyou might neeed it later.\nuse 'take' to proceed ").lower().strip()
    else:
        print(f"Great wise Knight now try using the 'explore' spell to have a look around\n")

        if user_input == "take":
            equip = Battle_Ground["Field"].pop(0)
            inventory.append(equip)
            print("NOTE: ")
            c = input(f"You've obtained the {equip} \nyou can now finally start the game.\nType 'HELP' to see other spells.\n").lower().strip()

    game_loop()

def game_loop():
    global current
    while True:
        command = input(f"[{current}] >>").lower().strip()

        if command == "help":
                print("\033[1m||| SO YOU WISH TO LEARN THE WAYS OF THE FOURTH NIGHT  ||| \033[0m")
                print(       "||| Explore: This will help look around.               |||")
                print(       "||| Drop: If you don't have need for something dip it. |||")
                print(       "||| Inspect: Helps you inspect items.                  |||")
                print(       "||| Move: move -> [Direction].                         |||")
                print(       "||| Quit: If you're to weak to continue.               |||")
                print(       "||| Use: Use -> use and the name of the item.          |||")

        elif command == "explore" or command == "look":
            look_commend()

        elif command.startswith("move"):
            Move()

        elif command == "drop":
            drop()

        elif command == "quit":
            Quite()
        else:
            print("I'm am not familiar whit the spell please try again \nor try 'help' to see what spells you can use.")


def look_commend():
    print(f"You are currently at the {current}.")

    if Battle_Ground[current]:
        print("You see:", ", ".join(Battle_Ground[current]))
    else:
        print("There is nothing interesting here...")

    if paths[current]:
        print("Paths from here:", ", ".join(paths[current]))
    else:
        print("There are no clear paths from here.")



def drop():
    # unwanted = []
    if not inventory:
        print("You do not have that, that you think you do\nhance there's noting to be dropped.")
        return
    item = input("What would you like to dip").strip().title()
    if item in inventory:
        inventory.pop(item)
        # unwanted = inventory.pop(item)
        Battle_Ground[current].append(item)
        print(f"You dipped the  {item}.")
    else:
        print("You do not posses such an item")
    # Drop a specified item:
    ...

def Move():
    global current
    print("Paths from here:",",".join(paths[current]))
    dest = input("Whither dost thou disire to go").strip().title()
    if dest in paths[current]:
        current = dest
        print(f"You journey sto {current}.")
        look_commend()
    else:
        print("knee you can't venture that way")
    #  move
    ...

def Quite():
    leaving = input("So You wish to Leave").strip().lower()
    if leaving == "yes":
        exit()
    else:
        print("Great wise one i heath thought of you\nto be scared for a second wise choice.")
    #quite game
    ...

def Use():
    if not inventory:
        print("You don't have that, that you believe youself to have obtained.")
        return
    # if inventory >= 1:
    #     print("I see you have many new toys but the great one says do not attempt to use any just yet.")
    item = input("which item do you wish to use? ").strip().title()
    if item in inventory:
        print(f"So you wish to test the game lord by tyring to use {item}\niyyy wise one give him more time\nhe is yet to add logi for the items you wish to use.")
    else:
        print("You are mistaken wise one for you have not obtained such an item.")

    # use item
    ...


greeting()



# notes
# add goals and trails

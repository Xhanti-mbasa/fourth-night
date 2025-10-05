
Battle_Ground = {"Mountain Of Wisdom": ["spoon", "pen"],
                 "Waterfall": [],
                 "Stone Cave": ["Black smith anville"],
                 "Farm": [],
                 "Field": ["Knights Sword"]
                 }
current = "Field"

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
            print("NOTE: ")
            c = input(f"You've obtained the {equip} \nyou can now finally start the game.\nType 'HELP' to see other spells.\n").lower().strip()

            if c == "help":
                print("\033[1m||| SO YOU WISH TO LEARN THE WAYS OF THE FOURTH NIGHT  ||| \033[0m")
                print(       "||| Explore: This will help look around.               |||")
                print(       "||| Drop: If you don't have need for something dip it. |||")
                print(       "||| Inspect: Helps you inspect items.                  |||")
                print(       "||| Move: move -> [Direction].                         |||")
                print(       "||| Quit: If you're to weak to continue.               |||")
                print(       "||| Use: Use -> use and the name of the item.          |||")


def look_commend():
    x = input()


greeting()

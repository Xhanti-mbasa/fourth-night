
Looby_item = ["knights sword"]
def greeting():


    Welcome_Screen = r""" WELCOME TO
     _____ ___  _   _ ____ _____ _   _    _   _ ___ ____ _   _ _____ 
    |  ___/ _ \| | | |  _ \_   _| | | |  | \ | |_ _/ ___| | | |_   _|
    | |_ | | | | | | | |_) || | | |_| |  |  \| || | |  _| |_| | | |  
    |  _|| |_| | |_| |  _ < | | |  _  |  | |\  || | |_| |  _  | | |  
    |_|   \___/ \___/|_| \_\|_| |_| |_|  |_| \_|___\____|_| |_| |_|  
                                                                                                            
    """
    print(f"{Welcome_Screen}")
    user_input = input("For you're first trial take the knights sword infront of you.\n").lower()

    while user_input != "take":
        user_input = input(f"You sure you don't want to take the sword? \nyou might neeed it later.\n ").lower()
    else:
        print(f"Great wise night now try using the 'explore' spell to have a look arround")

        if user_input == "take":
            equip = Looby_item.pop()
            print(f"You've obtained the {equip} \nyou can now finally start the game.")

greeting()

# def take_command():
#     if user_input == "take":
#      equip = room.pop()
def hub_entrance():
    input("As you walk into the castle, all you see is darkness. However, in the distance you see something glowing.")
    print("\n" * 100)
    input("As you approach it, you realize that it's a fountain in the middle of a enclosed gigantic courtyard.")
    print("\n" * 100)
    input("Above you is a skylight that would normally allow the moons light to illuminate the room.")
    print("\n" * 100)
    input("To your right is a massive door that bares the stench of death")
    input("In front of you is a hallway blocked by a set of doors.")
    input("To your left is a door rotting off its hinges. You can see through the cracks another source of light")
    hub_decision()
    return


def hub_decision():
    print("What would you like to do?\n")
    print("1.Approach the fountain\n")
    print("2.Approach the right door\n")
    print("3.Approach the double doors\n")
    print("4.Approach the left door\n")
    first_hub_choice = input()
    if first_hub_choice == "1":
        print("Distribute stats")
    elif first_hub_choice == "2":
        print("You approach the right door and the stench of death is unbearable.")
        first_right_door = input("1.Enter the room \n 2.Go back to hub\n")
        if first_right_door == "1":
            print("this is where the player enters room1function")
        elif first_right_door == "2":
            print("You go back to the to the center of the courtyard")
            hub_decision()
    elif first_hub_choice == "3":
        print("You approach the double doors. You notice two strange locks on the doors. What would you like to do?")
        first_double_door = input("1.Try to open the doors \n 2.Go back to the courtyard\n")
        if first_double_door == "1":
            print("You shake at the doors but they don't open")
        elif first_double_door == "2":
            print("You go back to the to the center of the courtyard")
            hub_decision()
    elif first_hub_choice == "4":
        print("You approach the left door and see the very wood on the hinges is rotten. Do you wish to enter?")
        first_left_door = input("1.Yes \n 2.No\n")
        if first_left_door == "1":
            print("This is where the player enters room2function")
        elif first_left_door == "2":
            print("You go back to the to the center of the courtyard")
            hub_decision()
    return


hub_entrance()

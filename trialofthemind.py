def trial_of_mind():
    global time
    time = 3
    input("To your left you feel what seems to be the source of the cold.\n")
    print("\n" * 100)
    input("To your right is a hallway shrouded in darkness except for a faint blue light in the distance obstructed by three gates\n")
    print("Which direction would you like to go?\n")
    hall_decision = input("1.Right\n2.Left")
    while True:
        if hall_decision == "1":
            input("As you head down the right hallway you hear a scream behind you and the hallway slowly gets colder")
            print("Do you turn around to see the source of the noise?\nY/N")
            turn_around_right = input().capitalize()
            while True:
                if turn_around_right == "Y":
                    death_trial_of_mind()
                    break
                elif turn_around_right == "N":
                    input("Knowing the danger behind you you run forward")
                    input("As you keep running forward you see a gate locked ahead.")
                    input("You see a simple padlock on the door but you don't know the code.")
                    input("In a panic you look around and see three numbers crudely scratched into the wall")
                    print("9")
                    print("7")
                    print("3")
                    first_gate_puzzle()
                    break
                else:
                    print("Please enter Y/N")
                    turn_around_right = input().capitalize()
            break
        elif hall_decision == "2":
            input("As you head into the frigid hallway you hear a horrifying noise and see what appears to be a woman.")
            input("As you look closer you realize that she has no face.")
            input("In the blink of an eye you see her directly in front of yo not inches away from your face.")
            input("Suddenly you feel a sharp cold pain in your chest")
            input("You look down and see the woman's arm completely through your chest")
            input("As you collapse the woman is standing over you and is now puling your skin off of your face")
            input("In a panic you you grab your knife from your cloak and stab at her but your blade glances off")
            input("Knowing you will soon die you scratch something into the hall floor, because you know this isn't the end")
            floor_carving = True
            death_trial_of_mind()
            break
        else:
            hall_decision = input("Please enter 1 or 2")
    return


def death_trial_of_mind():
    input("As you look into the hallway you see what appears to be a woman")
    input("As you look closer you realize that she has no face, only a mouth.")
    input("In the blink of an eye you see her directly in front of you not inches away from your face.")
    input("In a panic you shove past her and try to run back to the hall entrance")
    input("Once again she is behind you but now she is laughing loudly")
    input("As you get to the gate you feel a sharp pain in your chest")
    input("You look down and see her arm completely through you")
    input("Suddenly you collapse to the ground")
    input("In a panic you attempt to stab her with your knife but the blade glances off her skin")
    input("She grins as she begins to peel the very skin off of your face.")
    input("In one final act you carve something into the ground because you know this isn't the end.")
    input("You have died")
    print("\n" * 100)
    trial_of_mind_after_death()
    return


def first_gate_puzzle():
    global time
    while True:
        print("Enter the first number into the padlock")
        first_number_first_gate = input()
        print("Enter the second number into the padlock")
        second_number_first_gate = input()
        print("Enter the third number into the padlock")
        third_number_first_gate = input()
        if first_number_first_gate == "9" and second_number_first_gate == "7" and third_number_first_gate == "3":
            print("the lock opens")
            second_gate_puzzle()
            break
        else:
            print("The lock doesn't open and the cold is getting closer")
            time -= 1
            if time == 0:
                "Feeling the intense cold breathing down your neck you turn around."
                death_trial_of_mind()
                break
            else:
                first_gate_puzzle()
                break
    return


def second_gate_puzzle():
    global time
    input("The lock clicks open and you are able to continue forward.")
    input("As you keep going forward you feel the sensation of cold behind you grow closer")
    input("Soon you run into another gate with a more complicated lock.")
    input("Instead of three digits, this one has five.")
    input("remembering last time, you look onto the walls and see another set of numbers on the wall")
    input("however, this time some of the number are unrecognizable with age")
    input("the numbers read")
    input("15")
    input("--")
    input("9")
    input("--")
    while True:
        print("Please enter the first number")
        first_number_second_gate = input()
        print("Please enter the second number")
        second_number_second_gate = input()
        print("Please enter the third number")
        third_number_second_gate = input()
        print("Please enter the fourth number")
        fourth_number_second_gate = input()
        if first_number_second_gate == "15" and second_number_second_gate == "13" and third_number_second_gate == "9" and fourth_number_second_gate == "1":
            print("the lock opens")
            third_gate_puzzle()
            break
        else:
            print("The lock doesn't open and the cold is getting closer")
            time -= 1
            if time == 0:
                "Feeling the intense cold breathing down your neck you turn around."
                death_trial_of_mind()
                break
            else:
                second_gate_puzzle()
                break
    return


def third_gate_puzzle():
    global time
    input("As the door opens you dash forward through the hall the light at the end of the hallway is even closer")
    input("You notice however, that it is blocked by one last gate")
    input("The cold behind you is creeping ever closer")
    input("Once again you look upon the walls and see numbers scratched in crudely")
    print("79")
    print("--")
    print("--")
    print("65")
    print("--")
    print("15")
    while True:
        first_number_third_gate = input("Please enter the first number")
        second_number_third_gate = input("Please enter the second number")
        third_number_third_gate = input("Please enter the third number")
        fourth_number_third_gate = input("Please enter the fourth number")
        fifth_number_third_gate = input("Please enter the fifth number")
        sixth_number_third_gate = input("Please enter the sixth number")
        if first_number_third_gate == "79" and second_number_third_gate == "77" and third_number_third_gate == "73" and fourth_number_third_gate == "65" and fifth_number_third_gate == "49" and sixth_number_third_gate== "15":
            print("The lock opens")
            trial_of_mind_victory()
            break
        else:
            print("The lock doesn't open and the cold is getting closer")
            time -= 1
            if time == 0:
                "Feeling the intense cold breathing down your neck you turn around."
                death_trial_of_mind()
                break
            else:
                third_gate_puzzle()
                break
    return


def trial_of_mind_victory():
    print("you have won")
    return


def trial_of_mind_after_death():
    input("Suddenly you regain consciousness")
    input("You are standing at the door to the hallway that seems familiar")
    input("In front of you is a rotten door with a chilling sensation coming from behind it.")
    input("As you open it you see something carved on the ground.")
    input("'DONT LOOK AT HER")
    print('Do you wish to continue? Y/N')
    back_to_hub_decision = input().capitalize()
    while True:
        if back_to_hub_decision == "Y":
            trial_of_mind()
            break
        elif back_to_hub_decision == "N":
            print("You go back to the central hub")
    return


def trial_of_mind_intro():
    input("As you grab the rotten door you feel a sense of terror, but you press on\n")
    print("\n" * 100)
    input("You open the door and see a long hallway.")
    trial_of_mind()
    return


trial_of_mind_intro()


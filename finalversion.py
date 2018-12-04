def opening_sequence():
    global name
    input("(press enter to continue)")
    print("\n" * 100)
    print("You struggle to remember your name")
    print("(Enter your name)")
    name = input()
    print("it's a dark and rainy night", name, "\n")
    input("You have been here before. You don't remember when or why, but you know that you have been here before.\n")
    print("\n" * 100)
    input("You don't even know why you're here now for that matter.\n")
    print("\n" * 100)
    input("You just know there is some force that has been pushing you here for some time.\n")
    print("\n" * 100)
    input("You look down and you see a strange pocket watch attached to your vest that you don't remember getting.\n")
    print("\n" * 100)
    input("As you look upon the black walls of the castle in the distance, you feel the presence of a million fleeting memories\n")
    print("\n" * 100)
    input("Regardless you press on, throwing caution to the wind.\n")
    print("\n" * 100)
    input("As you keep walking, you grow ever closer to the castle\n")
    print("\n" * 100)
    input("You finally arrive at the castle doors. How do you want to open them\n")
    print("(input how you want to open the doors)\n")
    door_open = input()
    print("You", door_open, "the doors exposing the castle interior\n")
    input("You take one last look around at the open sky before you head into the castle\n")
    print("\n" * 100)
    input("As you walk in you hear the doors close behind you, sealing shut.\n")
    hub_entrance()
    return


def hub_entrance():
    global strength
    global intelligence
    global agility
    global trial_of_body_completion
    global trial_of_mind_completion
    global fountain_completion

    strength = 0
    intelligence = 0
    agility = 0
    trial_of_body_completion = 0
    trial_of_mind_completion = 0
    fountain_completion = 0
    input("As you walk into the castle, all you see is darkness. However, in the distance you see something glowing.\n")
    print("\n" * 100)
    input("As you approach it, you realize that it's a fountain in the middle of a gigantic enclosed courtyard.\n")
    print("\n" * 100)
    input("Above you is a skylight that would normally allow the moons light to illuminate the room.\n")
    print("\n" * 100)
    input("To your right is a massive door that bares the stench of death.\n")
    input("In front of you is a hallway blocked by a set of doors.\n")
    input("To your left is a door rotting off its hinges. You can see through the cracks another source of light\n")
    hub_decision()
    return


def hub_decision():
    global strength
    global intelligence
    global agility
    global trial_of_body_completion
    global trial_of_mind_completion
    global fountain_completion

    print("What would you like to do?\n")
    print("1.Approach the fountain\n")
    print("2.Approach the right door\n")
    print("3.Approach the double doors\n")
    print("4.Approach the left door\n")
    first_hub_choice = input()
    while True:
        if first_hub_choice == "1":
            if fountain_completion == 0:
                input("You approach the fountain.")
                print("\n" * 100)
                input("As you get closer you look into it and see your reflection\n")
                print("\n" * 100)
                input("However, there is something about it that startles you\n")
                print("\n" * 100)
                input("You see thousands of reflections of you, each looking slightly different\n")
                print("\n" * 100)
                input("There is something inscribed on the fountain\n")
                print("\n" * 100)
                input("CLAIM YOUR PAST AND FUTURE STRENGTH\n")
                print("\n" * 100)
                input("Something in the back of your mind tells you to touch the fountain water\n")
                print("\n" * 100)
                input("As you do you feel the presence of thousands of unfamiliar memories\n")
                print("\n" * 100)
                for x in range(0, 6)
                    input("Add a skill point to one of your stats:\n")
                    print("1.Stength\n")
                    print("2.Intelligence\n")
                    print("3.Agility\n")
                    print("Enter 1-3")
                    skill_choose = input()
                    if skill_choose == "1":
                        strength += 1
                        print("your strength is:", strength)
                    elif skill_choose == "2":
                        intelligence += 1
                        print("your intelligence is:", intelligence)
                    elif skill_choose == "3":
                        agility += 1
                        print("your agility is", agility)
                print("Your final stats are: Strength:", strength, "Agility:", agility, "Intelligence:", intelligence)
                input("(Press enter to continue")
                fountain_completion += 1
                hub_decision()
            else:
                input("You look at the fountain and see nothing but yourself in the reflection\n")
                print("\n" * 100)
                hub_decision()
            break
        elif first_hub_choice == "2":
            print("You approach the right door and the stench of death is unbearable.\n")
            first_right_door = input("1.Enter the room \n 2.Go back to hub\n")
            while True:
                if first_right_door == "1":
                    if trial_of_body_completion == 1:
                        input("You have already been to this room")
                        input("You go back to the hub")
                        print("\n" * 100)
                        hub_decision()
                    else:
                        trial_of_body_intro()
                    break
                elif first_right_door == "2":
                    print("You go back to the to the center of the courtyard")
                    hub_decision()
                    break
                else:
                    print("Please choose 1 or 2")
                    first_right_door = input()
            break
        elif first_hub_choice == "3":
            print(
                "You approach the double doors. You notice two strange locks on the doors. What would you like to do?")
            first_double_door = input("1.Try to open the doors \n 2.Go back to the courtyard\n")
            while True:
                if first_double_door == "1":
                    if trial_of_mind_completion == 1 and trial_of_body_completion == 1:
                        input("The energy you abosrbed from the two trials has allowed you to open the doors")
                        penultimate_room()
                    else:
                        input("You shake at the doors but they won't open")
                        hub_decision()
                    break
                elif first_double_door == "2":
                    print("You go back to the to the center of the courtyard")
                    hub_decision()
                    break
                else:
                    print("Please enter 1 or 2")
                    first_double_door = input()
            break
        elif first_hub_choice == "4":
            print("You approach the left door and see the very wood on the hinges is rotten. Do you wish to enter?")
            first_left_door = input("1.Yes \n 2.No\n")
            while True:
                if first_left_door == "1":
                    if trial_of_mind_completion == 1:
                        input("You have already been to this room")
                        input("You go back to the hub")
                        print("\n" * 100)
                        hub_decision()
                    else:
                        trial_of_mind_intro()
                    break
                elif first_left_door == "2":
                    print("You go back to the to the center of the courtyard")
                    hub_decision()
                    break
                else:
                    print("Please enter 1 or 2")
            break
        else:
            print("Please choose a room:")
            print("1.Approach the fountain\n")
            print("2.Approach the right door\n")
            print("3.Approach the double doors\n")
            print("4.Approach the left door\n")
            first_hub_choice = input()

    return


def trial_of_mind():
    global time
    time = 3
    input("To your left you feel what seems to be the source of the cold.\n")
    print("\n" * 100)
    input(
        "To your right is a hallway shrouded in darkness except for a faint blue light in the distance obstructed by three gates\n")
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
        if first_number_third_gate == "79" and second_number_third_gate == "77" and third_number_third_gate == "73" and fourth_number_third_gate == "65" and fifth_number_third_gate == "49" and sixth_number_third_gate == "15":
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
    global trial_of_mind_completion
    global strength
    global agility
    global intelligence
    input("As you walk through the final gate you feel the cold behind you fade away.")
    input("You approach a pedestal that looks like it has a glowing distortion on it.")
    input("You reach out and grab it as you and you feel an intense energy wash over you.")
    input("Suddenly you are back in the hub.")
    strength += 1
    agility += 1
    intelligence += 1
    print("Your stats are: Strength:", strength, "Agility:", agility, "Intelligence:", intelligence)
    trial_of_mind_completion += 1
    hub_decision()
    return


def trial_of_mind_after_death():
    input("Suddenly you regain consciousness\n")
    input("You are standing at the door to the hallway that seems familiar\n")
    input("The pocket watch on your hip is warm to the touch")
    input("In front of you is a rotten door with a chilling sensation coming from behind it.\n")
    input("As you open it you see something carved on the ground.\n")
    input("'DONT LOOK AT HER\n")
    print('Do you wish to continue? Y/N\n')
    back_to_hub_decision = input().capitalize()
    while True:
        if back_to_hub_decision == "Y":
            trial_of_mind()
            break
        elif back_to_hub_decision == "N":
            print("You go back to the central hub\n")
            hub_decision()
            break
        else:
            print("Please enter y/n")
            back_to_hub_decision = input().capitalize()
    return


def trial_of_mind_intro():
    input("As you grab the rotten door you feel a sense of terror, but you press on\n")
    print("\n" * 100)
    input("You open the door and see a long hallway.\n")
    trial_of_mind()
    return


def trial_of_body_intro():
    input("as you approach the door the smell of rotting flesh becomes more and more powerful\n")
    print("\n" * 100)
    input("when you open the door the stench almost becomes unbearable, but you find the strength to press on\n")
    print("\n" * 100)
    input("as you enter the room you can see almost nothing.\n")
    print("\n" * 100)
    trial_of_body_main()
    return


def trial_of_body_main():
    global intelligence
    global strength
    global agility

    input("Suddenly you hear a hideous scream from the darkness\n")
    print("\n" * 100)
    input("Hobbling into view you see what appears to be a creature made up of stitched body parts from multiple"
          " people\n")
    print("\n" * 100)
    input("Its arms look like they're made of hundreds of stitched together muscles\n")
    print("\n" * 100)
    print("It screams again as it starts to run at you. You instinctively draw your dagger. What do you do?\n")
    print("1.Try to run\n")
    print("2.Wait for it to make the first strike\n")
    print("3.Strike first while it is charging\n")
    first_combat_decision = input()
    while True:
        if first_combat_decision == "1":
            input("Seeing the horror in front of you, you attempt to run.\n")
            print("\n" * 100)
            input("As you turn around to go back the way you came, the door is empty\n")
            print("\n" * 100)
            input("Your vision goes black as you hear a loud thud against your head.\n")
            print("\n" * 100)
            trial_of_body_death()
            break
        elif first_combat_decision == "2":
            intelligence += 1
            print("Intelligence +1")
            input("You wait for the abomination to attack\n")
            print("\n" * 100)
            input("As it makes a large swing with one of its arms you are able to duck under it.\n")
            print("\n" * 100)
            input("In mid swing you see something glowing in its armpit\n")
            print("\n" * 100)
            input("As you see this you have no time to think because it's attacking again\n")
            print("\n" * 100)
            print("What do you do?\n")
            print("1.Attempt to dodge again\n")
            print("2.Attempt to attack the glowing spot under its arm.\n")
            intell_route_1 = input()
            while True:
                if intell_route_1 == "1":
                    input("You attempt to dodge again\n")
                    print("\n" * 100)
                    if agility >= 3:
                        input("Once again you dodge it as it swings over its head, revealing the glowing point\n")
                        input("However this time it attacks again quickly after with its other arm.\n")
                        if agility >= 4:
                            input("You dodge once again and the monster seems to be reeling from the attack\n")
                            input("This time the glowing spot is wide open\n")
                            print("Enter X to plunge your dagger\n")
                            dagger_kill = input().capitalize()
                            while True:
                                if dagger_kill == "X":
                                    input("You kill the monster\n")
                                    agility += 1
                                    print("Agility + 1")
                                    trial_of_body_victory()

                                    break
                                else:
                                    print("Enter X\n")
                                    dagger_kill = input().capitalize()
                        else:
                            input("You fail to dodge as the abominations arm makes full contact with your chest.\n")
                            print("\n" * 100)
                            input("The sudden impact has made your heart explode.\n")
                            trial_of_body_weakness()
                    else:
                        input("You were not agile enough to dodge the attack and the abomination breaks your arm\n")
                        input("Your consciousness starts to dwindle from the pain.\n")
                        input("In a panic you lash out in one more desperate attack for the glowing spot.\n")
                        if strength >= 3:
                            input("In your moment of panic your instincts take over and your blade strike true\n")
                            trial_of_body_victory()
                        else:
                            input(
                                "Perhaps distracted by the incredible amount of pain you are in your blade misses the weak spot.\n")
                            input(
                                "As your blade glances off its hard skin it swings again and hits you directly in the chest\n")
                            input(
                                "You struggle to stay awake as more and more blood comes up with each struggled breath.\n")
                            trial_of_body_weakness()
                    break
                elif intell_route_1 == "2":
                    input("You attempt to dodge this next attack at strike the glowing spot at the same time\n")
                    print("\n" * 100)
                    if strength >= 4:
                        input("Due to your vast knowledge of combat you accomplish this with ease\n")
                        trial_of_body_victory()
                    else:
                        input("You attempt to attack while you are dodging.\n")
                        input("However you haven't experienced much combat and are too slow \n")
                        input("The monsters giant arm hits you in the head and everything is black\n")
                        trial_of_body_weakness()
                    break
                else:
                    print("Please input 1 or 2\n")
                    intell_route_1 = input()
            break
        elif first_combat_decision == "3":
            input("Knowing that it doesn't expect you to make the first attack, you lunge forward with your dagger.\n")
            print("\n" * 100)
            input("You jab your blade with all of your might at the abominations chest\n")
            print("\n" * 100)
            input("To your disbelief however, your blade deflects off and the abomination stops hobbling towards you.\n")
            print("\n" * 100)
            input("the abomination stands for a second and starts retching\n")
            print("\n" * 100)
            input("suddenly from its mouth it erupts a red liquid that lands on you\n")
            print("\n" * 100)
            input("you can feel a slight burning sensation from where it lands.\n")
            print("\n" * 100)
            print("What do you do?\n")
            print("1.Run")
            print("2.Study the abomination")
            print("3.Attack again")
            combat_path_1 = input()
            while True:
                if combat_path_1 == "1":
                    agility += 1
                    print("Agility + 1")
                    input("Seeing the horror in front of you, you attempt to run.")
                    input("As you turn around to go back the way you came, the door is empty")
                    input("Your vision goes black as you hear a loud thud against your head.")
                    trial_of_body_death()
                    break
                elif combat_path_1 == "2":
                    intelligence += 1
                    print("Intelligence + 1")
                    input("After it vomited on you it needs time to recover")
                    print("\n" * 100)
                    input("You notice as it's recovering it's making sure to guard a spot under its arm.")
                    print("\n" * 100)
                    input("The vomit is burning more and more")
                    print("\n" * 100)
                    print("What do you do?")
                    print("1.Attempt to run")
                    print("2.Attempt to strike at where it's guarding.")
                    combat_path_2 = input()
                    while True:
                        if combat_path_2 == "1":
                            input("Seeing the horror in front of you, you attempt to run.")
                            print("\n" * 100)
                            input("As you turn around to go back the way you came, the door is empty")
                            print("\n" * 100)
                            input("Your vision goes black as you hear a loud thud against your head.")
                            trial_of_body_weakness()
                            break
                        elif combat_path_2 == "2":
                            input("In a wild and desperate strike you attempt to stab where it is guarding")
                            print("\n" * 100)
                            input("Your blade finds success as it sinks into the soft material under its arm")
                            trial_of_body_victory()
                            break
                        else:
                            print("Please enter 1 or 2")
                            combat_path_2 = input()
                    break
                elif combat_path_1 == "3":
                    input("You strike again at its chest")
                    print("\n" * 100)
                    if strength >= 5:
                        input("Due to expert knowledge of combat you are able to find vulnerability where others can't")
                        input("The monster screams as your blade digs deeper and deeper")
                        trial_of_body_victory()
                    else:
                        input("Once again your blade glances off the monsters skin")
                        input("The monster has time to strike you this time")
                        input("It grabs you by the throat and suddenly everything is dark as you hear one last snap.")
                        trial_of_body_death()
                    break
                else:
                    print("Please enter 1, 2, or 3")
                    combat_path_1 = input()
            break
        else:
            print("Please enter 1, 2, or 3")
            first_combat_decision = input()
    return


def trial_of_body_death():
    input("Suddenly you regain consciousness")
    input("The pocket watch on your hip is warm to the touch")
    input("You're standing at a door that has the smell of rotting flesh")
    input("Do you wish to continue?")
    print("Enter y/n")
    death_retry = input().capitalize()
    while True:
        if death_retry == "Y":
            trial_of_body_main()
            break
        elif death_retry == "N":
            print("back to hub")
            break
        else:
            print("Please enter y/n")
            death_retry = input().capitalize()
    return


def trial_of_body_victory():
    global strength
    global intelligence
    global agility
    global trial_of_body_completion
    input("Suddenly a light emanates from the monsters body and covers you.")
    input("You feel a surge of energy as the room goes white.")
    input("Suddenly you are back in the hub")
    strength += 1
    intelligence += 1
    agility += 1
    print("Your stats are: Strength:", strength, "Agility:", agility, "Intelligence:", intelligence)
    trial_of_body_completion += 1
    hub_decision()
    return


def trial_of_body_weakness():
    input("Suddenly you regain consciousness")
    input("The pocket watch on your hip is warm to the touch")
    input("You're standing at a door that has the smell of rotting flesh")
    input("Do you wish to continue?")
    print("Enter y/n")
    death_retry = input().capitalize()
    while True:
        if death_retry == "Y":
            input("You enter the room and you hear a strangely familiar scream come from the darkness")
            input("You see a monster that you've never seen before but there is something familiar about it.")
            input("As it run towards you, you draw your dagger")
            input("It swings at you and you have just enough time to dodge its massive arm")
            input("Something in you screams to stab under its arm.")
            print("Enter X to stab it")
            stab_it = input().capitalize()
            while True:
                if stab_it == "X":
                    input("Your blade strikes true and sinks deep into the monster")
                    trial_of_body_victory()
                    break
                else:
                    print("Please enter X to stab the monster")
                    stab_it = input().capitalize()
            break
        elif death_retry == "N":
            print("back to hub")
            break
        else:
            print("Please enter y/n")
            death_retry = input().capitalize()
    return


def penultimate_room():
    input("As the two massive doors open you see a hall that is lit by an ethereal light")
    print("\n" * 100)
    input("You walk down the hallway and in front of you are two massive doors")
    print("\n" * 100)
    input("To your left however is a small room with the door cracked open")
    input("it looks like there's a fire in there")
    print("Where would you like to go?")
    print("1.Big Room Ahead")
    print("2.Small Room to the Left")
    room_decision = input()
    while True:
        if room_decision == "1":
            input("You open the giant doors and walk in, you feel a heat come from your watch as you do.")
            break
        elif room_decision == "2":
            input("You open the door to your left and step into a warm room illuminated by a fire in a hearth")
            small_room()
            break
        else:
            print("Please enter 1 or 2")
            room_decision = input()
    return


def small_room():
    input("As you enter the room the door behind you closes and the fire starts to flicker")
    print("\n" * 100)
    input("Suddenly a distortion opens in front of you and out walks an elderly man wearing a robe")
    print("\n" * 100)
    input("'Judging by the look on your face you don't know who I am'")
    input("'Or should I say this you doesn't know who I am'")
    input("As you open your mouth to ask who he is he repeats at the same time as you 'Who are you?'")
    input("'Yes we've been through this many times before.'")
    input("'To cut to the chase I'm here to help you. Ask all of your repetitive questions like you always do.'")
    return


def father_time():
    print("Questions to ask")
    print("1.Who are you?")
    print("2.What do you mean we've been through this before? I don't know you.")
    print("3.Can you get me out of here")
    print("4. Leave the room")
    ask_question = input().capitalize()
    while True:
        if ask_question == "1":
            input("'call me god, call me time, call me a janitor, call me whatever you like.'")
            input("'Who I am isn't important, it's what I do'")
            input("'I exist for one reason, to keep time going'")
            input("(Press Enter to Continue)")
            print("\n" * 100)
            father_time()
            break
        elif ask_question == "2":
            input("'Well maybe me and you haven't done this before, BUT I'VE done this before with you.'")
            input("'I'm sure you've noticed by now that your pocket watch is something else'")
            input("'I know you've used it to avoid death whether you know it or not'")
            input("'But what you probably don't realize is that you aren't going back in time'")
            input("'You're going to a new timeline all together'")
            input("'So you're still dying'")
            input("'You're just creating a new timeline'")
            input("'And every time you die you lose a little piece of you. The piece that understands what's happening.'")
            input("'However you are still able to retain fractures of memory'")
            input("'How else would everything seem so familiar?'")
            input("'So we've had this very conversation before thousands of times.'")
            input("'But this time is going to be the last time.'")
            input("'What is this pocket watch?' you ask")
            input("'Years ago there lived a very smart man in this castle'")
            input("'That man lost a woman very dear to him.'")
            input("'By using the occult he brought her soul ")
            input("'Using surgery he tried to piece her pack together'")
            input("'He even gave it a piece of her soul'")
            input("'But he failed")
            input("'What he created was a something so terrible he locked it away to never see the light of day ")
            input("'He wasn't deterred however, he persisted'")
            input("'So again he turned to science for his answers'")
            input("'He would use another body, but this one belonged to a woman from a village not far away'")
            input("'He even stripped her of all of her features, except her mouth'")
            input("'Once again he would use a piece of the soul from his lover'")
            input("'But this time the body rejected it'")
            input("'Not before it gave the featureless body life though'")
            input("'Again he sealed his abomination in a wing of the castle not having the will to kill it.'")
            input("'The man was at the end of his rope so he decided to try one more thing.'")
            input("'So he sealed himself inside his laboratory with the last bit of soul he summoned from his lover'")
            input("'If he couldn't bring her back to him, he would bring himself back to her")
            input("'And that's where your watch came from.'")
            input("'The plan was to go back and prevent her from dying at all'")
            input("'Unfortunately when he used the watch something went wrong and only it went back'")
            input("'And you must be the poor soul who found it'")
            input("'There's something about that watch that is pushing it back to here'")
            input("'And you're its instrument'")
            input("'He's about to make it again in this timeline and now is when I explain why I need you.'")
            input("'Just one of these devices is destroying time itself, creating timeline after timeline'")
            input("'You need to stop him from doing it again and this time I know how to help.'")
            input("(Press Enter to Continue)")
            print("\n" * 100)
            father_time()
            break
        elif ask_question == "3":
            input("'I can't get you out of here but I'm going to help you get you out of here and that's with this'")
            input("Suddenly in his hands appears a sabre with intricately carved designs")
            input("Where the hilt meets the blade is an empty slot")
            input("'You like it?'")
            input("'I call it the time saber'")
            input("'The old man created it so that he could erase those two mistakes downstairs with the watch'")
            input("'But seeing as how the watch left he never could do it'")
            input("'So I snatched it from another timeline'")
            input("'With this we can redirect all of the energy coming from that watch into one point.'")
            input("'You can you use it to make things to never have existed at all'")
            input("'And that's exactly what you're going to do to him.'")
            input("'We're going to stop that watch from ever getting made'")
            input("'And you will end up back in your normal timeline as if you had never found the watch to begin with'")
            input("(Press Enter to Continue)")
            print("\n" * 100)
            father_time()
            break
        elif ask_question == "4":
            leave_room()
            break
        else:
            print("Questions to ask")
            print("1.Who are you?")
            print("2.What do you mean we've been through this before? I don't know you.")
            print("3.Can you get me out of here")
            print("type 'Exit' to leave")
            ask_question = input().capitalize()
    return


def leave_room():
    global time_saber
    time_saber = 0
    input("'Well we're all counting on you'")
    input("'At least if you fail another one of you may get the job done'")
    input("He throws the sword at you and vanishes")
    input("You know what you must do as you head back to the hallway. and up to the two massive doors")
    input("You push them open and feel a heat from your watch")
    print("\n" * 100)
    time_saber += 1
    final_room()
    return


def final_room():
    global strength
    global agility
    global intelligence
    global time_saber
    health = 3
    input("You enter through the giant doors and you see a familiar old man working in a laboratory.")
    print("\n" * 100)
    input("'So you've finally come.'")
    input("'And I was so close'")
    input("He pulls out a revolver with intricate designs on it and aimes it at you")
    input("'But what's stopping me from killing you?'")
    print("What do you do?")
    print("1.Stay still")
    print("2.Rush him")
    print("3.'Stop I just want to ask you some questions'")
    final_question = input()
    while True:
        if final_question == "1":
            final_room_death()
            break
        elif final_question == "2":
            input("Suddenly you sprint behind cover behind a shelf with beakers on it")
            if agility >= 3:
                input("You make it safely behind cover as he misses his first shot")
                print("You are behind the table with chemicals on it what do you do?")
                print("1. Sprint at him and try to stab him")
                print("2. Push the table at him to catch him off guard")
                print("3. try to mix some of the chemicals near you to create smoke as a cover")
                cover_question = input()
                while True:
                    if cover_question == "1":
                        input("Due to your superior agility and his poor reflexes you are right next to him")
                        final_kill()
                        break
                    elif cover_question == "2":
                        input("You push the shelf forward and keep driving it forward as you pin him against the wall.")
                        input("As you are pushing it he unloads the gun into it and runs out of bullets")
                        input("You are now next to him and he has no bullets")
                        final_kill()
                        break
                    elif cover_question == "3":
                        input("Knowing the chemicals near you, you put together a smoke bomb of sorts and throw it at him.")
                        final_kill()
                        break
                    else:
                        print("You are behind the table with chemicals on it what do you do?")
                        print("1. Sprint at him and try to stab him")
                        print("2. Push the table at him to catch him off guard")
                        print("3. try to mix some of the chemicals near you to create smoke as a cover")
                        cover_question = input()
            else:
                input("The bullet hits you in the arm as you're too slow to get behind a shelf with beakers on it")
                health -= 1
                print("You are behind the table with chemicals on it what do you do?")
                print("1. Sprint at him and try to stab him")
                print("2. Push the table at him to catch him off guard")
                print("3. try to mix some of the chemicals near you to create smoke as a cover")
                cover_question = input()
                while True:
                    if cover_question == "1":
                        input("Due to your superior agility and his poor reflexes you are right next to him")
                        final_kill()
                        break
                    elif cover_question == "2":
                        input("You push the shelf forward and keep driving it forward as you pin him against the wall.")
                        input("As you are pushing it he unloads the gun into it and runs out of bullets")
                        input("You are now next to him and he has no bullets")
                        final_kill()
                        break
                    elif cover_question == "3":
                        input("Knowing the chemicals near you, you put together a smoke bomb of sorts and throw it at him.")
                        final_kill()
                        break
                    else:
                        print("You are behind the table with chemicals on it what do you do?")
                        print("1. Sprint at him and try to stab him")
                        print("2. Push the table at him to catch him off guard")
                        print("3. try to mix some of the chemicals near you to create smoke as a cover")
                        cover_question = input()
            break
        elif final_question == "3":
            final_room_death()
            break
        else:
            print("What do you do?")
            print("1.Stay still")
            print("2.Rush him")
            print("3.'Stop I just want to ask you some questions'")
            final_question = input()
    return


def final_room_death():
    input("He shoots you square in the chest")
    input("As you fall he sprints toward you and tries to grab your pocket watch")
    input("The last thing you see is your pocket watch dissapear in his hands as he screams.")
    final_room()
    return


def final_kill():
    global time_saber
    if time_saber == 1:
        input("You stab him with the time saber")
        input("He looks down and his eyes go wide")
        input("'Where did you get this??? WHAT HAVE YOU DONE???'")
        time_saber_end()
    else:
        input("You stab him in the heart with your dagger")
        input("As he begins to pass you notice a sinister smile on his face")
        normal_kill()
    return

def time_saber_end():
    input("Suddenly everything stops as your body starts to fade")
    input("At the same time his body fades as well.")
    input("This feels different from the other times you've died.")
    input("This time it feels like nothingness.")
    input("As you and the old man both are about to dissapear you notice something on his belt.")
    input("Your dagger that you've had with you the whole time.")
    input("Just as you realize who this man is you stop existing.")
    return

def normal_kill():
    input("Not knowing who this man was or why he was shooting at you, you feel a sigh of relief as he dies.")
    input("As he finally passes you see a strange source of light come from his jacket")
    input("the light then vanishes with the breeze")
    input("You decide you've had enough of the room and try to leave but the doors are stuck.")
    input("You try to pull open the doors but nothing will work.")
    input("months go by")
    input("years go by")
    input("you feel insanity grip your mind")
    input("Until one day the doors open")
    input("and through them walks you, years younger.")
    return


opening_sequence()

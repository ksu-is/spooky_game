def opening_sequence():
    input("(press enter to continue)")
    print("\n" * 100)
    input("it's a dark and rainy night\n")
    print("\n" * 100)
    input("You have been here before. You don't remember when or why, but you know that you have been here before.\n")
    print("\n" * 100)
    input("You don't even know why you're here now for that matter.\n")
    print("\n" * 100)
    input("You just know there is some force that has been pushing you here for some time.\n")
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
    print("\n" * 100)
    input("You take one last look around at the open sky before you head into the castle")
    print("\n" * 100)
    input("As you walk in you hear the doors close behind you, sealing shut.")
    hub_entrance()
    return


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
    global strength
    global intelligence
    global agility
    global trial_of_body_completion
    global trial_of_mind_completion
    
    strength = 0
    intelligence = 0
    aglitily = 0
    trial_of_body_completion = 0
    trial_of_mind_completion = 0
    fountain_completion = 0
    
    print("What would you like to do?\n")
    print("1.Approach the fountain\n")
    print("2.Approach the right door\n")
    print("3.Approach the double doors\n")
    print("4.Approach the left door\n")
    while True:
        first_hub_choice = input()
        if first_hub_choice == "1":
            if fountain_completion == 0:
                input("You approach the fountain.")
                print("\n" * 100)
                input("As you get closer you look into it and see your reflection")
                print("\n" * 100)
                input("However, there is something about it that atrtles you")
                print("\n" * 100)
                input("You see thousands of reflections of you, each looking slightly different")
                print("\n" * 100)
                input("There is something inscribed on the fountain")
                print("\n" * 100)
                input("CLAIM YOUR PAST AND FUTURE STRENGTH")
                print("\n" * 100)
                input("Something in the back of your mind tells you to touch the fountain water")
                print("\n" * 100)
                input("As you do you feel the presence of thousands of unfamiliar memories")
                print("\n" * 100)
                for x in range(0, 6):
                    input("You have six skill points")
                    input("Distribute them to your three skills:")
                    print("1.Stength")
                    print("2.Intelligence")
                    print("3.Agility")
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
                print("Your final stats are: Strength:", strength, "Agility:", aglitily, "Intelligence:", intelligence)
                fountain_completion += 1
                hub_decision()
            else:
                "You look at the fountain and see nothing but yourself in the reflection"
            break
        elif first_hub_choice == "2":
            print("You approach the right door and the stench of death is unbearable.")
            first_right_door = input("1.Enter the room \n 2.Go back to hub\n")
            while True:
                if first_right_door == "1":
                    if trial_of_body_completion > 0:
                        print("You have already been to this room")
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
            print("You approach the double doors. You notice two strange locks on the doors. What would you like to do?")
            first_double_door = input("1.Try to open the doors \n 2.Go back to the courtyard\n")
            while True:
                if first_double_door == "1":
                    if trial_of_mind_completion > 0 and trial_of_body_completion > 0:
                        input("The energy you abosrbed from the two trials has allowed you to open the doors")
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
                    if trial_of_mind_completion > 0:
                        input("You have already completed this room")
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
    input("As you walk through the final gate you feel the cold behind you fade away.")
    input("You approach a pedestal that looks like it has a glowing distortion on it.")
    input("You reach out and grab it as you and you feel an intense energy wash over you.")
    input("Suddenly you are back in the hub.")
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


def trial_of_body_intro():
    input("as you approach the door the smell of rotting flesh becomes more and more powerful")
    print("\n" * 100)
    input("when you open the door the stench almost becomes unbearable, but you find the strength to press on")
    print("\n" * 100)
    input("as you enter the room you can see almost nothing.")
    print("\n" * 100)
    trial_of_body_main()
    return


def trial_of_body_main():
    global intelligence
    global strength
    global agility
    intelligence = 0
    strength = 0
    agility = 0

    input("Suddenly you hear a hideous scream from the darkness")
    print("\n" * 100)
    input("Hobbling into view you see what appears to be a creature made up of stitched body parts from multiple"
          " people")
    print("\n" * 100)
    input("Its arms look like they're made of hundreds of stitched together muscles")
    print("\n" * 100)
    print("It screams again as it starts to run at you. You instinctively draw your dagger. What do you do?")
    print("1.Try to run")
    print("2.Wait for it to make the first strike")
    print("3.Strike first while it is charging")
    first_combat_decision = input()
    while True:
        if first_combat_decision == "1":
            input("Seeing the horror in front of you, you attempt to run.")
            print("\n" * 100)
            input("As you turn around to go back the way you came, the door is empty")
            print("\n" * 100)
            input("Your vision goes black as you hear a loud thud against your head.")
            print("\n" * 100)
            trial_of_body_death()
            break
        elif first_combat_decision == "2":
            intelligence + 1
            print("Intelligence +1")
            input("You wait for the abomination to attack")
            print("\n" * 100)
            input("As it makes a large swing with one of its arms you are able to duck under it.")
            print("\n" * 100)
            input("In mid swing you see something glowing in its armpit")
            print("\n" * 100)
            input("As you see this you have no time to think because it's attacking again")
            print("\n" * 100)
            print("What do you do?")
            print("1.Attempt to dodge again")
            print("2.Attempt to attack the glowing spot under its arm.")
            intell_route_1 = input()
            while True:
                if intell_route_1 == "1":
                    input("You attempt to dodge again")
                    print("\n" * 100)
                    if agility >= 3:
                        input("Once again you dodge it as it swings over its head, revealing the glowing point.")
                        input("However this time it attacks again quickly after with its other arm.")
                        if agility >= 4:
                            input("You dodge once again and the monster seems to be reeling from the attack")
                            input("This time the glowing spot is wide open")
                            print("Enter X to plunge your dagger")
                            dagger_kill = input().capitalize()
                            while True:
                                if dagger_kill == "X":
                                    input("You kill the monster")
                                    agility + 1
                                    print("Agility + 1")
                                    trial_of_body_victory()

                                    break
                                else:
                                    print("Enter X")
                                    dagger_kill = input().capitalize()
                        else:
                            input("You fail to dodge as the abominations arm makes full contact with your chest.")
                            print("\n" * 100)
                            input("The sudden impact has made your heart explode.")
                            trial_of_body_weakness()
                    else:
                        input("You were not agile enough to dodge the attack and the abomination breaks your arm")
                        input("Your consciousness starts to dwindle from the pain.")
                        input("In a panic you lash out in one more desperate attack for the glowing spot.")
                        if strength >= 3:
                            input("In your moment of panic your instincts take over and your blade strike true")
                            trial_of_body_victory()
                        else:
                            input("Perhaps distracted by the incredible amount of pain you are in your blade misses the weak spot.")
                            input("As your blade glances off its hard skin it swings again and hits you directly in the chest")
                            input("You struggle to stay awake as more and more blood comes up with each struggled breath.")
                            trial_of_body_weakness()
                    break
                elif intell_route_1 == "2":
                    input("You attempt to dodge this next attack at strike the glowing spot at the same time")
                    print("\n" * 100)
                    if strength >= 4:
                        input("Due to your vast knowledge of combat you accomplish this with ease")
                        trial_of_body_victory()
                    else:
                        input("You attempt to attack while you are dodging.")
                        input("However you haven't experienced much combat and are too slow ")
                        input("The monsters giant arm hits you in the head and everything is black")
                        trial_of_body_weakness()
                    break
                else:
                    print("Please input 1 or 2")
                    intell_route_1 = input()
            break
        elif first_combat_decision == "3":
            input("Knowing that it doesn't expect you to make the first attack, you lunge forward with your dagger.")
            print("\n" * 100)
            input("You jab your blade with all of your might at the abominations chest")
            print("\n" * 100)
            input("To your disbelief however, your blade deflects off and the abomination stops hobbling towards you.")
            print("\n" * 100)
            input("the abomination stands for a second and starts retching")
            print("\n" * 100)
            input("suddenly from its mouth it erupts a red liquid that lands on you")
            print("\n" * 100)
            input("you can feel a slight burning sensation from where it lands.")
            print("\n" * 100)
            print("What do you do?")
            print("1.Run")
            print("2.Study the abomination")
            print("3.Attack again")
            combat_path_1 = input()
            while True:
                if combat_path_1 == "1":
                    agility + 1
                    print("Agility + 1")
                    input("Seeing the horror in front of you, you attempt to run.")
                    input("As you turn around to go back the way you came, the door is empty")
                    input("Your vision goes black as you hear a loud thud against your head.")
                    trial_of_body_death()
                    break
                elif combat_path_1 == "2":
                    intelligence + 1
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
    input("Suddenly a light emanates from the monsters body and covers you.")
    input("You feel a surge of energy as the room goes white.")
    input("Suddenly you are back in the hub")
    hub_decision()
    return


def trial_of_body_weakness():
    input("Suddenly you regain consciousness")
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
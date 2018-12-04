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
    input("back to hub")
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


trial_of_body_intro()
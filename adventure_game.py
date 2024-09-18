import random
import time


def print_time(message, wtime):
    print(message)
    time.sleep(wtime)


def fight(weapon):
    print_time(f"The {enemy} has not noticed you yet!", 3)
    if weapon == "pistol":
        print_time("You realize that you're not equipped for this fight, "
                   f"all you have is a {weapon}.", 3)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("Will you still (1) fight or will you (2) run?\n")
        if choice == '1':
            if weapon == "pistol":
                print_time(f"Whether a brave soul or a buffoon you "
                           "charge in...", 2)
                print_time(f"But your meager {weapon} is no use against "
                           f"the {enemy}.", 2)
                print_time(f"You fought valiantly till your last breath!", 2)
                print_time("Failed to complete simulation.", 1)
            elif weapon == "assault rifle":
                print_time(f"As the doors slide open, the {enemy} is "
                           "startled by you.", 2)
                print_time(f"They never imagined that you would be so "
                           "heavily armed!", 2)
                print_time(f"All it takes is one burst of your rifle "
                           "to pierce them.", 2)
                print_time(f"Thanks to you the {enemy} is no more, and "
                           "your crew is safe!", 2)
                print_time("Simulation completed successfully!", 1)
        elif choice == '2':
            print_time("Whether a coward or a clever soul, you decide "
                       "against rushing "
                       "the control room of the ship.", 2)
            wheretogo()


def play_now():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Want to run the simulation again? (y,n)")
        if choice == 'n':
            print_time("Thanks for the run captain! Until next time.", 2)
            return 'game_over'
        elif choice == 'y':
            print_time("Great! restarting simulation...", 2)
            weapon = 'pistol'
            return 'simulating'


def intro():
    print_time("You log on to the virtual simulation device, "
               "and find yourself waking in your Quarters.", 2)
    print_time("You're a captain on a ship currently orbiting Titan.", 2)
    print_time("This simulation will test your prepardness in a possible "
               "hostage situation.", 3)
    print_time("The computer informs you that your crew is being held in "
               f"the control room by a {enemy}.", 2)
    print_time("You step out,", 2)
    print_time("to your left is the control room, to your right "
               "the armory.", 2)
    print_time(f"Attached to your hip is a {weapon}, but will it "
               "be enough?", 3)


def wheretogo():
    print_time(" ", 1)
    print_time("Press a to rush to the control room.", 2)
    print_time("Press d to check the armory.", 2)
    print_time("Which way do you go?", 1)
    choice = ''
    while choice not in ['a', 'd']:
        choice = input("(Please press a or d.)\n")

    if choice == 'a':
        conroom()
    elif choice == 'd':
        armory()


def conroom():
    print_time(f"You're in front of the doors when you hear the {enemy}.", 2)
    print_time("They are standing directly on the other side of the doors.", 2)
    fight(weapon)


def armory():
    global armorylooted
    global weapon
    print_time("You scan the armory to make sure it is safe.", 2)
    if armorylooted:
        print_time("You checked the armory already, it has been looted.", 2)
    elif armorylooted is False:
        print_time(f"The {enemy} is not here, and the armory is untouched.", 2)
        print_time("In fact, you see an assault rifle ready and waiting "
                   "to be used.", 2)
        print_time(f"You holster your {weapon}, and equip the "
                   "assault rifle.", 2)
        weapon = 'assault rifle'
    armorylooted = True
    print_time("You step out into the hallway.", 2)
    wheretogo()


runsim = 'simulating'
while runsim == 'simulating':

    enemies = ['crazed alien', 'rogue machine', 'manic pirate', 'wild stowaway']
    enemy = random.choice(enemies)
    weapon = 'pistol'
    armorylooted = False

    intro()
    wheretogo()

    runsim = play_now()
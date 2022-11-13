from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much - int(choice)
    else:
        dead("man, learn to type a number")

    if how_much < 50:
        print("Nice, you are not greedy. You Win!")
        exit(0)
    else:
        dead("you greedy bastard!")


def bear_room():
    print("there is a bear here.\n"
          "the bear has a bunch of honey.\n"
          "The fat bear is in front of another room...\n"
          "How are you going to move the bear?\n")
    bear_moved = False

    while True:
        choice = input("> ").strip().lower()

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door.")
            print("you can go through now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">> ").strip().lower()

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good Job!")
    exit(0)


def start():
    print("You are in a dark room.\n"
          "There is a door to your right and left.\n"
          "Which one do you take?\n")

    choice = input(">> ").strip().lower()

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

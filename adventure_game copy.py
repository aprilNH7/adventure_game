import time
import random
illness = ['the flu', 'COVID', 'SARS', 'rhinovirus']
illness_choice = random.choice(illness)


def print_hesitate(memo):
    print(memo)
    time.sleep(2.5)


print_hesitate("Welcome to my game, friend.")
print_hesitate("I hope you decide to play!")


def ask_user():
    answer = str(input("Would you like to play? (yes/no): ")).lower().strip()
    if answer == "yes":
        print_hesitate("Thanks for the support, hope you enjoy!")
    elif answer == "no":
        print("Aw, maybe next time friend! ")
        exit()
    else:
        print("Invalid response, try again. ")
        return ask_user()


def intro():
    illness = ['the flu', 'COVID', 'SARS', 'rhinovirus']
    illness_choice = random.choice(illness)
    print_hesitate(f"Oh no, {illness_choice} is still around!")
    print_hesitate("But you already planned for a vacation a year ago.")


def ask_trip():
    print_hesitate("A trip to the bahamas, your dream vacation!")
    print_hesitate("You finally have the funds, and time to make it happen.")
    print_hesitate("You don't know if you will ever have the opportunity to go"
                   " again.")
    print_hesitate("Would you like to go on the trip?")
    while True:
        answer = input("(Enter yes or no.)")
        if answer == "yes":
            print_hesitate("Once you made it to the bahamas, you see a bar in"
                           " front of you, and a lobby behind you.")
            forward_back()
        elif answer == "no":
            print_hesitate("You decide that you are safer at home.")
            print_hesitate("You are positive that you will have another chance"
                           " to go.")
            print_hesitate("You decide to go to the mall to get out of the"
                           " house.")
            print_hesitate("You arrive at the mall.")
            print_hesitate("Oh no! You forgot your mask.")
            print_hesitate("You walk into the mall.")
            print_hesitate("The store that holds the shoes you wanted for a"
                           " decade is to your left.")
            print_hesitate("But there is only one pair left.")
            print_hesitate("However, there may be a mask store somewhere in"
                           " the mall to your right.")
            print_hesitate("Is it worth it?")
            print_hesitate("To lose the pair of shoes you waited for over"
                           " a decade to have?")
            print_hesitate("Especially, for a mask store that may not exist?")
            print_hesitate("You have a very hard decision to make.")
            ask_direction()
        else:
            print("Invalid response, try again. ")
            return ask_trip()
            break


def forward_back():
    while True:
        answer = input("Would you like to go forward or back?")
        if answer == "back":
            print_hesitate("You  walk into the lobby, and they hand you a"
                           " face mask.")
            print_hesitate("You put the face mask on.")
            print_hesitate("You head over to the bar.")
            print_hesitate("You made new friends, you danced, and you had lots"
                           " of fun.")
            print_hesitate("Your dream vacation was a success!")
            print_hesitate("You won!")
            play_again()
        elif answer == "forward":
            print_hesitate("You walk into the bar.")
            print_hesitate("You made new friends, you danced, and had lots"
                           " of fun.")
            print_hesitate("However, once you made it to your hotel, you"
                           " felt sick.")
            print_hesitate("You arrived at hospital 3 days later.")
            print_hesitate(f"Oh no! You have {illness_choice}.")
            print_hesitate("You get admitted, and surrcum to your illness.")
            print_hesitate("You lost!")
            play_again()
        else:
            print("Invalid response, try again. ")
            return forward_back()


def ask_direction():
    while True:
        answer = input("Would you like to go left or right?")
        if answer == "right":
            print_hesitate("You walk right for what seems like hours.")
            print_hesitate("With all hope lost for finding a mask store...")
            print_hesitate("Or purchasing your favorite shoes...")
            print_hesitate("You reach the last store in the mall.")
            print_hesitate("...........")
            print_hesitate("The mask store! YAY!")
            print_hesitate("You run in, and purchase your mask.")
            print_hesitate("You head over to the shoe store as fast as"
                           " you can.")
            print_hesitate("You made it just in time before store closure.")
            print_hesitate("Luckily, your shoes are still there!")
            print_hesitate("You purchase your shoes.")
            print_hesitate("With a big smile on your face, you put them on.")
            print_hesitate("Once you made it home, you started dancing in"
                           " them.")
            print_hesitate("The trip to the mall was a success!")
            print_hesitate("You won!")
            play_again()
        elif answer == "left":
            print_hesitate("You walk into the store, and purchase your shoes.")
            print_hesitate("With a big smile on your face, you put them on.")
            print_hesitate("Once you made it home, you started dancing in"
                           " them.")
            print_hesitate("Oh no! As you are dancing you start to feel weak.")
            print_hesitate("You faint!")
            print_hesitate("You wake up in the hospital.")
            print_hesitate("You ask the doctor what happened to you.")
            print_hesitate("The Dr. informed you that you tested positive for"
                           f" {illness_choice}.")
            print_hesitate("The next day you surrcumed to your illness.")
            print_hesitate("You lost!")
            play_again()
        else:
            print("Invalid response, try again. ")
            return ask_direction()


def play_again():
    answer = str(input("Would you like to play again?"
                       "(yes/no): ")).lower().strip()
    if answer == "yes":
        print_hesitate("Great, friend! Restarting game..")
        start_game()
    elif answer == "no":
        print("Aw, maybe next time friend! ")
        exit()
    else:
        print("Invalid response, try again. ")
        return play_again()


def start_game():
    intro()
    ask_trip()
    forward_back()
    ask_direction()
    play_again()


ask_user()
intro()
ask_trip()
forward_back()
ask_direction()
play_again()
start_game()

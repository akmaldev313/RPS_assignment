from ART import logo
from ART import vs
import Choices
import random

print(logo)

game = Choices.Game()

end_game = False
while end_game is False:
    mode = game.type()

    if mode == 1:
        select = input("What do you choose? rock = 0, paper = 1, scissors = 2\n")
        weapon = Choices.Weapon()

        player1_choice = weapon.selected(int(select))
        print(vs)
        player2_choice = weapon.selected(random.randint(0, 2))

        end_game = weapon.compare(player1_choice, player2_choice)
    elif mode == 2:
        weapon = Choices.Weapon()

        player1_choice = weapon.selected(random.randint(0, 2))
        print(vs)
        player2_choice = weapon.selected(random.randint(0, 2))

        end_game = weapon.compare(player1_choice, player2_choice)

    correct_input = False
    while correct_input is False:
        new = input(str("Would you like to play again?(Y/N)".lower()))
        if new == "y":
            correct_input = True
            game.clear()
            end_game = False
            '''
            returns to the first while loop, requesting user input for game.type()
            '''

        elif new == "n":
            print("Thank you for playing! Done by AK")
            correct_input = True
            break
        else:
            print("Invalid Input")
            correct_input = False

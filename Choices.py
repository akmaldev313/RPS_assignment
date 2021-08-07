#Includes all possible choices

#Game Type
class Game:
    def __init__(self):
        pass


    def type(self):
        selection = False
        while selection is False:
            game_type = int(input("Select Game Mode\n1)Human vs Computer\n2)Computer vs Computer\n"))
            if game_type == 1 or game_type == 2:
                selection = True
                return game_type
            else:
                print("Invalid input")
                selection = False

    def clear(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')



# Below class is for 'weapons'
# Can be added on for future additions (i.e Spock, Lizard)

class Weapon:
    def __init__(self):
        self.weapons = {
            #rock
            0: '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        ''',
            #paper
            1 :  '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        ''',
            #scissors
            2 :'''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''
        }

    def selected(self, sel):
        for selection in self.weapons:
            if sel == selection:
                print(self.weapons[selection])
                weapon_key = selection
                return weapon_key


    def compare(self, first,second):
        if first == 0:
            if second == 0:
                print("Its a DRAW!")
                end_game = True
                return end_game
            elif second == 1:
                print("PAPER beats ROCK, Player 2 wins!")
                end_game = True
                return end_game
            elif second == 2:
                print("ROCK beats SCISSORS, Player 1 wins!")
                end_game = True
                return end_game
        elif first == 1:
            if second == 0:
                print("PAPER beats ROCK, Player 1 wins!")
                end_game = True
                return end_game
            elif second == 1:
                print("Its a DRAW!")
                end_game = True
                return end_game
            elif second == 2:
                print("SCISSORS beats PAPER, Player 2 wins!")
                end_game = True
                return end_game
        elif first == 2:
            if second == 0:
                print("ROCK beats SCISSORS, Player 2 wins!")
                end_game = True
                return end_game
            elif second == 1:
                print("SCISSORS beats PAPER! Player 1 wins")
                end_game = True
                return end_game
            elif second == 2:
                print("Its a DRAW!")
                end_game = True
                return end_game


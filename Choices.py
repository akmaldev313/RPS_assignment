"""
Includes all possible choices

"""


class Game:
    """
    This class is a blueprint for
    1)Type of game User wants to play
    2)New game when User wants to play again
    """
    def __init__(self):
        pass


    def type(self):
        """
            This method is to choose between the two type of Game Modes
            1) Human vs Computer
            2) Computer vs Computer
            :return: Returns a 1 or 2, for mode variable in rps.py
            ********try & exception was used to solve the bug where it woul;d crash if input was other than an integer*******
            """
        selection = False
        while selection is False:
            try:
                game_type = int(input("Select Game Mode\n1)Human vs Computer\n2)Computer vs Computer\n"))

                if game_type == 1 or game_type == 2:
                    selection = True
                    return game_type
                else:
                    print("Invalid input, please enter 1 or 2")
            except ValueError:
                print("Invalid input, please enter 1 or 2")
                continue




    def clear(self):
        """"
        This method is to clear screen and begin new game
        """
        import os
        os.system('cls' if os.name == 'nt' else 'clear')





class Weapon:
    """
    Below class is for 'weapons'
    dictionary can be added on for future additions (e.g Spock, Lizard)
    """
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

    def selected(self, select):
        """

        :param select: from input requested in rps.py
        :return: Returns int value matching the selected 'weapon'. used for arguement in rps.py to compare
        """
        for selection in self.weapons:
            if select == selection:
                print(self.weapons[selection])
                weapon_key = selection
                return weapon_key


    def compare(self, first,second):
        """
        compares player1 vs player2 weapon_key.
        determines outcome of the game (win/lose/draw)

        :param first: int, to capture player1 'weapon'
        :param second: int, to capture player2 'weapon'
        :return: returns end_game as True or False, for end_game variable in rps.py
        """
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


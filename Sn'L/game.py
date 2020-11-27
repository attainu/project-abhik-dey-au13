from snake import Snake
from ladder import Ladder
from dice import Dice
from board import Board
from player import Player



class Game:
    def __init__(self):
        self.winner = None
    

    def play(self):
        # snake and ladder positions
        snakes = [Snake(7,3) , Snake(37,13) , Snake(80,60)]
        ladders = [Ladder(1,27) , Ladder(33,60) , Ladder(70,79)]

        # details for 2 players
        players = [ Player("A" , 1), Player("B" , 1)]
        turns = 0

        # initializing board and Dice
        board = Board().populate(snakes , ladders)
        dice = Dice()
        
        while True:
            play = input("Press Enter to Play and Exit to quit the game: ")
            if play == "":
                turns += 1
                print(f"\n--------------Turn : {turns}--------------")

                for player in players:

                    dice_value = dice.roll()
                    player.move(dice_value)
                    
                #encounter event for snake / ladder
                encounter = board[player.position]
                if encounter:
                    end_point = encounter.end_point
                    print(f"--ENCOUNTER : {encounter.message}--")
                    player.move(end_point , encounter = True)

                #checking if player won
                if player.is_winner:
                    self.winner = player
                    break

        print("\n--------------GAME OVER--------------")
        print(f"Player {self.winner.name} Has won the game after {turns} turns")
        print("--------------GAME OVER--------------\n")


# Snakes and Ladders

A text based Snake and ladder game in terminal.

## Few basic concepts used in this code are:
    - Dictionary
    - List
    - Generating random number
    - Selecting a Random value from a list
    - Conditional Statements i.e. IF and ELSE
    - Getting input from user to make the move of the dice
    - OOPs


## Contents of the Game:

    - Display the welcome message
    - Display the match between the two players (A & B)
    - Display the number of turns taken during the match and also displays the total number of turns taken when a player wins.
    - Until one of the player wins the following is done :
        - Roll the dice
        - Move the player forward for the value got on dice roll.
        - If player is on snake's head, move down to its tail
        - If player is on ladder's bottom, take it to its top
        - else remain there and let second player roll the dice
        - Shows the number of turn taken to win after a player wins the game, then stops the program.

## Requirements:
    Python 3.6+

## Usage:

Run the following command inside the root directory to let the script play one game

###### Run the file using Python3 - main.py after copying the repo

## Output :

* Output for a regular turn :

--------------Turn : 5--------------
Player A has rolled a 3
Player A has been moved from 21 to 24
Player B has rolled a 2
Player B has been moved from 15 to 17


* Output for a Ladder encounter :

--------------Turn : 23--------------
Player A has rolled a 4
Player A has been moved from 79 to 83
Player B has rolled a 5
Player B has been moved from 65 to 70
--ENCOUNTER : LADDER -> CLIMB TO 79--
Player B has been moved from 70 to 79


* Output for Snake encounter :

--------------Turn : 24--------------
Player A has rolled a 4
Player A has been moved from 74 to 78
Player B has rolled a 6
Player B has been moved from 74 to 80
--ENCOUNTER : SNAKE BITE -> GO TO 60--
Player B has been moved from 80 to 60



* Output for out of bounds :

--------------Turn : 30--------------
Player A has rolled a 4
Player A has not been moved from 99 to 103 <OUT OF BOUNDS>
Player B has rolled a 6
Player B has been moved from 82 to 88



* Output for Winner :

--------------GAME OVER--------------
Player B Has won the game after 40 turns
--------------GAME OVER--------------


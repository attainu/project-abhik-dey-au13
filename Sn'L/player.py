class Player:
    def __init__(self , name = None , position = None):
        self.name = name
        self.position = position
        self.is_winner = False

    def move(self , dice_value , encounter = None):
        '''
        moving a player from one position to another 
        checks for index out of bounds
        moves according to encounters if any
        '''
        
        if not encounter:
            print(f"Player {self.name} has rolled a {dice_value}")
            new_position = self.position + dice_value
        
        else:
            new_position = dice_value

        if new_position > 100:
            print(f'Player {self.name} has not been moved from {self.position} to {new_position} <OUT OF BOUNDS>')
            return

        elif new_position == 100:
            self.is_winner = True

        print(f'Player {self.name} has been moved from {self.position} to {new_position}')
        self.position = new_position

    #Getters , Setters
    def get_name (self):
        return self.name

    def get_position(self):
        return self.position

    def set_name (self , name):
        return self.name
    
    def set_position (self , position):
        return self.position
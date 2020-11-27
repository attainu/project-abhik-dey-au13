class Board:
    def __init__(self):
        self.board = [None for x in range(101)]

    def populate(self, snakes , ladders ):

        #placing snakes
        for snake in snakes:
            start_point = snake.get_start_point()
            self.board[start_point] = snake

        #placing ladders
        for ladder in ladders:
            start_point = ladder.get_start_point()
            self.board[start_point] = ladder

        return self.board
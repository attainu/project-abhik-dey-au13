class Ladder:
    def __init__(self , start_point = None , end_point = None):
        self.start_point = start_point
        self.end_point = end_point
        self.message = f"LADDER -> CLIMB TO {self.end_point}"

    #Getters , Setters
    def get_start_point(self):
        return self.start_point

    def get_end_point(self):
        return self.end_point

    def set_start_point(self , start_point):
        self.start_point = start_point

    def set_end_point(self, end_point):
        self.end_point = end_point
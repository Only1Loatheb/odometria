class Map():
    def __init__(self):
        self.i = 0
        self.turns = [
	        [0,  0],
	        [100, 0],
	        [100, 100]
	        ]

    def position(self):
        t = self.turns[self.i]
        self.i = self.i + 1
        if self.i==len(self.turns):
            self.i = 0
        return t
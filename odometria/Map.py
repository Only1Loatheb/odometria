class Map():
    def __init__(self):
        self.i = 0
        self.turns = [
	    [0,  0],
	    [0, 100],
        [40, 100],
        [40,60],
        [80,60],
        [80,100],
        [120,100],
        [120,60],
        [100,60],
        [100,40],
        [120,40],
        [120,0]
	    ]
        """
        self.turns = [
        [0,0],
        [0,100],
        [100,100],
        [100,0]
        ]
        """	
    def position(self):
        t = self.turns[self.i]
        self.i = self.i + 1
        if self.i==len(self.turns):
            self.i = 0
        return t

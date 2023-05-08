from player import Player;

class Ia(Parent):

	def __init__(self, symbol = 'X'):		
		super().__init__(symbol);

    def doPlay(self, x = 0, y = 0):
		super().doPlay(x, y);
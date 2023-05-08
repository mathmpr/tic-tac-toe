from player import Player;

class Human(Player):

	def __init__(self, symbol = 'X'):		
		super().__init__(symbol);

	def doPlay(self, x = 0, y = 0):
		cords = self.getPrompt().getCords();
		if cords:
			return super().doPlay(cords[0], cords[1]);
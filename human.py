from player import Player;

class Human(Player):

	def __init__(self, prompt):		
		super().__init__(prompt);

	def doPlay(self, x = 0, y = 0):
		cords = self.getPrompt().getCords();
		if cords:
			return super().doPlay(cords[0], cords[1]);

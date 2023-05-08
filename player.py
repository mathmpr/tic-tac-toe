class Player:

	def __init__(self, prompt):
		self.setPrompt(prompt);
		self.getPrompt().setPlayer(self);

	def getPrompt(self):
		return self.prompt;

	def setPrompt(self, prompt):
		self.prompt = prompt;
		return self;

	def getGame(self):
		return self.game;

	def setGame(self, game):
		self.game = game;
		return self;

	def reset(self):
		return self;

	def doPlay(self, x = 0, y = 0):
		if self.getGame().board[x][y] != "":
			print('board at row ' + str(x + 1) + ' and column ' + str(y + 1) + ' is not empty');
			return False;
		return self.getGame().doPlay(x, y);

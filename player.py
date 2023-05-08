class Player:

	def __init__(self, symbol = 'X'):
		self.symbol = symbol;

	def setGame(self, game):
		self.game = game;

	def doPlay(self, x = 0, y = 0):
		x = 0 if x > 0 else x - 1;
		y = 0 if y > 0 else y - 1;
		if self.game.board[x][y] != "":
			print('board at row ' + str(x + 1) + ' and column ' + str(y + 1) + ' is not empty');
			return False;
		self.game.board[x][y] = self.current;
		return True;
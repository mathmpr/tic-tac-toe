from human import Human;

class Game:

	def __init__(self, playerOne, playerTwo):
		self.playerOne = playerOne;
		self.playerTwo = playerTwo;
		self.playerOne.setGame(self);
		self.playerTwo.setGame(self);
		self.state = 'reseted';

		self.turn = self.playerOne;
		self.reset();
		self.combs = [
			['00', '01', '02'],
			['10', '11', '12'],
			['20', '21', '22'],
			['00', '10', '20'],
			['01', '11', '21'],
			['02', '12', '22'],
			['00', '11', '22'],
			['20', '11', '02'],
		];

	def getState(self):
		return self.state;

	def getTurn(self):
		return self.turn;

	def reset(self):
		self.state = 'reseted';
		self.playerOne.reset();
		self.playerTwo.reset();
		self.board = [["" for _ in range(3)] for _ in range(3)];

	def isTie(self):
		for x in range(3):
			for y in range(3):
				if self.board[x][y] == "":
					return False;
		return True;

	def checkWinner(self):
		for conditions in self.combs:
			count = 0;
			found = "";
			for cords in conditions:
				x = int(cords[0]);
				y = int(cords[1]);
				if self.board[x][y] != "" and (found == "" or found == self.board[x][y]):
					found = self.board[x][y]
					count = count + 1;
			if count == 3:
				return found;
		return False;


	def render(self):
		for x in range(3):
			print ("");
			for y in range(3):
				print("|   |" if self.board[x][y] == "" else "| " + str(self.board[x][y]) + " |", end="");
		print ("", end="\n\n");

	def renderEnd(self, message):
		self.render();
		print(message);
		input("press any key to reset game and continue...\n");
		self.reset();

	def doPlay(self, x, y):
		self.state = 'restart';
		self.board[x][y] = self.turn.getPrompt().getSymbol();
		self.changeTurn();

	def changeTurn(self):
		self.turn = self.playerTwo if id(self.turn) == id(self.playerOne) else self.playerOne;

	def start(self):

		self.render();

		while True:

			command = input('(p)play, (r)restart, (e)exit: ');

			if command == 'p':
				self.turn.doPlay();
			elif command == 'r':
				if isinstance(self.turn, Human):
					self.changeTurn();
				self.reset();
			elif command == 'e':
				break;

			winner = self.checkWinner();
			if winner:
				self.renderEnd("\nThe symbol " + winner + " won the game!");
			elif self.isTie():
				self.renderEnd("\nThe game have a tie");
			else:
				self.render();

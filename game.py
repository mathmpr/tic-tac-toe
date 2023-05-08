class Game:

	def __init__(self, playerOne, playerTwo):
		self.playerOne = playerOne;
		self.playerTwo = playerTwo;
		self.playerOne.setGame(self);
		self.playerTwo.setGame(self);

		self.turn = self.playerOne;
		self.board = [["" for _ in range(3)] for _ in range(3)];
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

	def reset(self):
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
		print(message);
		input("press any key to reset game and continue...\n");
		self.reset();

	def doPlay(self, x, y):
		self.board[x][y] = self.turn.getPrompt().getSymbol();
		self.turn = self.playerTwo if id(self.turn) == id(self.playerOne) else self.playerOne;

	def start(self):

		self.render();

		while True:

			command = input('(p)play, (r)restart, (e)exit: ');

			if command == 'p':
				self.turn.doPlay();
			elif command == 'r':
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


class Prompt:
	def __init__(self, _except = []):
		while True:
			self.symbol = (input('choose a symbol for player: ')).upper();
			if self.symbol == '':
				print("symbol can't be empty.");
			elif self.symbol.isnumeric():
				print("symbol can't be numberic.");
			elif len(self.symbol) > 1:
				print("symbol have to be one single letter.");
			elif self.symbol in _except:
				print("one player already choosen this symbol, please choose another symbol.");
			else:
				break;

	def getSymbol(self):
		return self.symbol;

	def getPlayer(self):
		return self.player;

	def setPlayer(self, player):
		self.player = player;
		return self;

	def getCords(self):
		try:
			x = int(input('type row number (from 1 to 3): '));
			y = int(input('type column number (from 1 to 3): '));
			if (x < 1 or x > 3) or (y < 1 or y > 3):
				raise Exception('invalid x or y range');
		except:
			print('invalid y or x range (from 1 to 3) or typed text can\'t be parsed to integer');
			return False;
		return [(x - 1), (y - 1)];
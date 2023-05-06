class Game:

	def __init__(self):
		self.current = 'X';
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
		self.current = 'X';

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
		x = x - 1;
		y = y - 1;
		if self.board[x][y] != "":
			print('board at row ' + str(x + 1) + ' and column ' + str(y + 1) + ' is not empty');
			return;
		self.board[x][y] = self.current;
		self.current = 'O' if self.current == 'X' else 'X';

	def start(self):

		self.render();

		while True:

			command = input('(p)play, (r)restart, (e)exit: ');

			if command == 'p':
				try:
					x = int(input('type row number (from 1 to 3): '));
					y = int(input('type column number (from 1 to 3): '));
					if (x < 1 or x > 3) or (y < 1 or y > 3):
						raise Exception('invalid x or y range');
				except:
					print('invalid y or x range (from 1 to 3) or typed text can\'t be parsed to integer');
				self.doPlay(x, y);
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


game = Game();
game.start();
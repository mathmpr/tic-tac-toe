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

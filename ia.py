from player import Player;

class Ia(Player):

	def __init__(self, prompt):		
		super().__init__(prompt);
		self.iBegin = False;
		self.prevents = [
			('11,22', '02'),
			('11,02', '22'),
			('11,00', '20'),
			('11,20', '00'),
			('00,22', '01,10,12,21'),
			('20,02', '01,10,12,21'),
			('00', '11'),
			('02', '11'),
			('20', '11'),
			('22', '11')
		];
		self.tricks = [
			('02,20', '00,22'),
			('00,22', '02,20'),
			('00', '22'),
			('22', '00'),
			('02', '20'),
			('20', '02'),
			('20', '00'),
			('00', '02'),
			('00', '20'),
			('22', '02'),
			('22', '20'),
			('20', '22'),
			('02', '00'),
			('02', '22')			
		];

	def reset(self):
		if self.getGame().getState() == 'reseted' and id(self.getGame().getTurn()) == id(self):
			self.iBegin = True;
		else:
			self.iBegin = False;
		return super().reset();

	def isEmpty(self, x, y):
		return self.getGame().board[x][y] == "";

	def isEnemySymbol(self, x, y):
		return not self.isEmpty(x, y) and self.getGame().board[x][y] != self.getPrompt().getSymbol();

	def isSelfSymbol(self, x, y):
		return not self.isEmpty(x, y) and self.getGame().board[x][y] == self.getPrompt().getSymbol();

	def checkIfICanWinInCurrentTurn(self):
		for conditions in self.getGame().combs:
			count = 0;
			emptyCords = [];
			for cords in conditions:
				x = int(cords[0]);
				y = int(cords[1]);
				if self.isSelfSymbol(x, y):
					count = count + 1;
				elif self.isEmpty(x, y):
					emptyCords = [x, y];
				if count == 2 and len(emptyCords) > 0:
					return emptyCords;
		return False;

	def checkIfEnemyCanWinNextTurn(self):
		for conditions in self.getGame().combs:
			count = 0;
			emptyCords = [];
			for cords in conditions:
				x = int(cords[0]);
				y = int(cords[1]);
				if self.isEnemySymbol(x, y):
					count = count + 1;
				elif self.isEmpty(x, y):
					emptyCords = [x, y];
				if count == 2 and len(emptyCords) > 0:
					return emptyCords;
		return False;

	def preventTricks(self):
		for _check,_prevent in (self.prevents + self.tricks):
			if len(_check.split(',')) > 1:
				_checks = _check.split(',');
				_prevents = _prevent.split(',');

				checkCount = 0;
				for check in _checks:
					x = int(check[0]);
					y = int(check[1]);
					if self.isEnemySymbol(x, y):
						checkCount = checkCount + 1;
					if checkCount == len(_checks):
						print(checkCount);
						for prevent in _prevents:
							x_prevent = int(prevent[0]);
							y_prevent = int(prevent[1]);
							if self.isEmpty(x_prevent, y_prevent):
								return [x_prevent, y_prevent];
			else:	
				x = int(_check[0]);
				y = int(_check[1]);
				x_prevent = int(_prevent[0]);
				y_prevent = int(_prevent[1]);
				if self.isEnemySymbol(x, y) and not self.isSelfSymbol(x_prevent, y_prevent):
					return [x_prevent, y_prevent];
		return False;

	def applyTricks(self, force = False):

		if not self.iBegin and not force:
			return False;

		initialTricks = [];

		for _check,_target in self.tricks:

			_checks = _check.split(',');
			_targets = _target.split(',');

			checkCount = 0;
			for check in _checks:
				x = int(check[0]);
				y = int(check[1]);
				if self.isSelfSymbol(x, y):
					checkCount = checkCount + 1;
				else:
					initialTricks.append([x, y]);

			if checkCount == len(_checks):
				for target in _targets:
					x = int(target[0]);
					y = int(target[1]);
					if self.isEmpty(x, y):
						return [x, y];		

		if len(initialTricks) > 0:
			return initialTricks[0];

		return False;

	def basicCordsAttack(self):
		for conditions in self.getGame().combs:
			count = 0;
			emptyCords = [];
			for cords in conditions:
				x = int(cords[0]);
				y = int(cords[1]);
				if self.isSelfSymbol(x, y):
					count = count + 1;
				elif self.isEmpty(x, y):
					emptyCords = [x, y];
				if count > 1 and len(emptyCords) > 0:
					return emptyCords;
		return self.applyTricks(True) or False;

	def doPlay(self, x = 0, y = 0):
		
		cords = self.checkIfICanWinInCurrentTurn() or self.checkIfEnemyCanWinNextTurn()	or self.applyTricks() or self.preventTricks() or self.basicCordsAttack();
		if cords:
			return super().doPlay(cords[0], cords[1]);

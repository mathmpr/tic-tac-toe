from game import Game;
from game import Prompt;
from ia import Ia;
from human import Human;


choose = input('you want to play (h) 1 vs 1 or (a) 1 vs IA: ');

while choose != 'h' and choose != 'a':
	print('wrong choose. choose (h) or (a)');
	choose = input('you want to play (h) 1 vs 1 or (a) 1 vs IA: ');

p1 = Prompt();
p2 = Prompt([p1.getSymbol()]);

if choose == 'a':
	p1 = Human(p1);
	p2 = Ia(p2);
else:
	p1 = Human(p1);
	p2 = Human(p2);

game = Game(p1, p2);
game.start();
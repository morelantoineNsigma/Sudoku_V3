from Strategies.solvedCells import solvedCells
from Strategies.showPossibles import showPossibles
from Strategies.hiddenSingles import hiddenSingles
from Strategies.hiddenPairs import hiddenPairs
from Strategies.hiddenTriples import hiddenTriples
from Strategies.nakedPairs import nakedPairs
from Strategies.nakedTriples import nakedTriples


order = [solvedCells, hiddenSingles, hiddenPairs, hiddenTriples, nakedPairs, nakedTriples]


def apply_step(grille, possibles):
	effect, i = False, 0
	possibles = showPossibles(grille, possibles)
	while not effect and i < len(order):
		grille, possibles, effect = order[i](grille, possibles)
		i += 1
	return grille, possibles, effect



from Strategies.solvedCells import solvedCells
from Strategies.showPossibles import showPossibles
from Strategies.hiddenSingles import hiddenSingles


order = [solvedCells, hiddenSingles]


def apply_step(grille, possibles):
	effect, i = False, 0
	possibles = showPossibles(grille, possibles)
	while not effect and i < len(order):
		grille, possibles, effect = order[i](grille, possibles)
		i += 1
	return grille, possibles, effect



# effect  len(order) >= i   	continue
# 0		0					1
# 1		0					0
# 0		1					0
# 1		1					0
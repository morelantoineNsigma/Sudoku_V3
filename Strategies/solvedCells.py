


def solvedCells(grille, possibles):
	effect = False
	for i in range(9):
		for j in range(9):
			if grille[i][j] == 0 and len(possibles[i][j]) == 1:
				grille[i][j] = possibles[i][j].pop()
				effect = True
	return grille, possibles, effect
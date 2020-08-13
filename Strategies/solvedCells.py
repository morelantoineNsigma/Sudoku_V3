import logging


def solvedCells(grille, possibles):
	effect = False
	for i in range(9):
		for j in range(9):
			if grille[i][j] == 0 and len(possibles[i][j]) == 1:
				value = possibles[i][j].pop()
				grille[i][j] = value
				logging.info('Single for value ' + str(value) + ' in (' + str(i) + ', ' + str(j) + ')')
				effect = True
	return grille, possibles, effect
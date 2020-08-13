import logging


def possible(grille, i, j, n):
	for k in range(9):
		if grille[i][k] == n:
			return False  # ligne
		if grille[k][j] == n:
			return False  # colonne
	for k in range(3):
		for l in range(3):
			if grille[i - i % 3 + k][j - j % 3 + l] == n:
				return False  # carre
	return True


def showPossibles(grille, possibles):
	logging.info('updating possibles')
	for i in range(9):
		for j in range(9):
			for n in range(1, 10):
				if grille[i][j] == 0:
					if n in possibles[i][j] and not possible(grille, i, j, n):
						possibles[i][j].discard(n)
	return possibles

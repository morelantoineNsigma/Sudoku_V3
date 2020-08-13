import logging


def nakedPairsLine(grille, possibles, i):
	effect = False
	for j1 in range(8):
		if grille[i][j1] == 0 and len(possibles[i][j1]) == 2:
			for j2 in range(j1 + 1, 9):
				if grille[i][j2] == 0 and possibles[i][j1] == possibles[i][j2]:
					str_cases = ""
					for k in range(9):
						if k != j1 and k!= j2 and grille[i][k] == 0:
							for n in possibles[i][j1]:
								if n in possibles[i][k]:
									possibles[i][k].discard(n)
									str_cases += "(" + str(i) + "," + str(k) + ")"
					if str_cases != "":
						logging.info("Naked Pair for values " + str(possibles[i][j1]) + " on Line " + str(i) + " removed possibles for cases " + str_cases)
						effect = True

	return grille, possibles, effect


def nakedPairsColumn(grille, possibles, j):
	effect = False
	for i1 in range(8):
		if grille[i1][j] == 0 and len(possibles[i1][j]) == 2:
			for i2 in range(i1 + 1, 9):
				if grille[i2][j] == 0 and possibles[i1][j] == possibles[i2][j]:
					str_cases = ""
					for k in range(9):
						if k != i1 and k!= i2 and grille[k][j] == 0:
							for n in possibles[i1][j]:
								if n in possibles[k][j]:
									possibles[k][j].discard(n)
									str_cases += "(" + str(k) + "," + str(j) + ")"
					if str_cases != "":
						logging.info("Naked Pair for values " + str(possibles[i1][j]) + " on Column " + str(j) + " removed possibles for cases " + str_cases)
						effect = True
	return grille, possibles, effect


def nakedPairsBox(grille, possibles, box):
	effect = False
	for c1 in range(8):
		i1, j1 = (box // 3) * 3 + c1 // 3, (box % 3) * 3 + c1 % 3
		if grille[i1][j1] == 0 and len(possibles[i1][j1]) == 2:
			for c2 in range(c1 + 1, 9):
				i2, j2 = (box // 3) * 3 + c2 // 3, (box % 3) * 3 + c2 % 3
				if grille[i2][j2] == 0 and possibles[i1][j1] == possibles[i2][j2]:
					str_cases = ""
					for k in range(9):
						ik, jk = (box // 3) * 3 + k // 3, (box % 3) * 3 + k % 3
						if k != c1 and k!= c2 and grille[ik][jk] == 0:
							for n in possibles[i1][j1]:
								if n in possibles[ik][jk]:
									possibles[ik][jk].discard(n)
									str_cases += "(" + str(ik) + "," + str(jk) + ")"
					if str_cases != "":
						logging.info("Naked Pair for values " + str(possibles[i1][j1]) + " on Box " + str(box) + " removed possibles for cases " + str_cases)
						effect = True
	return grille, possibles, effect


def nakedPairs(grille, possibles):
	effect = False
	for t in range(9):
		grille, possibles, effectL = nakedPairsLine(grille, possibles, t)
		grille, possibles, effectC = nakedPairsColumn(grille, possibles, t)
		grille, possibles, effectB = nakedPairsBox(grille, possibles, t)
		effect = effectL or effectC or effectB or effect
	return grille, possibles, effect
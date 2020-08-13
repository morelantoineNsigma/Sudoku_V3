import logging


def hiddenSinglesLine(grille, possibles, i):
	effect = False
	for n in range(1,9):
		if n not in grille[i]:
			count, addr = 0, 0
			for j in range(9):
				if grille[i][j] == 0 and n in possibles[i][j]:
					count += 1
					addr = j
			if count == 1:
				grille[i][addr] = n
				logging.info("Hidden Single for value " + str(n) + " in (" + str(i) + ", " + str(addr) + ") on Line " + str(i))
				effect = True
	return grille, possibles, effect


def hiddenSinglesColumn(grille, possibles, j):
	effect = False
	for n in range(1,9):
		if n not in [grille[i][j] for i in range(9)]:
			count, addr = 0, 0
			for i in range(9):
				if grille[i][j] == 0 and n in possibles[i][j]:
					count += 1
					addr = i
			if count == 1:
				grille[addr][j] = n
				logging.info("Hidden Single for value " + str(n) + " in (" + str(addr) + ", " + str(j) + ") on Column " + str(j))
				effect = True
	return grille, possibles, effect


def hiddenSinglesBox(grille, possibles, box):
	effect = False
	x, y = box // 3, box % 3
	for n in range(1,9):
		if n not in [grille[i][j] for i in range(x * 3, x * 3 + 3) for j in range(y * 3, y * 3 + 3)]:
			count, addr = 0, 0
			for i in range(x * 3, x * 3 + 3):
				for j in range(y * 3, y * 3 + 3):
					if grille[i][j] == 0 and n in possibles[i][j]:
						count += 1
						addr = (i, j)
			if count == 1:
				grille[addr[0]][addr[1]] = n
				logging.info("Hidden Single for value " + str(n) + " in (" + str(addr[0]) + ", " + str(addr[1]) + ") on Box " + str(box))
				effect = True

	return grille, possibles, effect


def hiddenSingles(grille, possibles):
	effect = False
	for i in range(9):
		grille, possibles, effectL = hiddenSinglesLine(grille, possibles, i)
		grille, possibles, effectC = hiddenSinglesColumn(grille, possibles, i)
		grille, possibles, effectB = hiddenSinglesBox(grille, possibles, i)
		effect = effectL or effectC or effectB or effect

	return grille, possibles, effect
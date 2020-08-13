import logging

from Strategies.strategies import apply_step


def init_log(level=logging.INFO):
	logging.basicConfig(filename='log.log', level=level, format='%(asctime)s %(message)s', filemode='w')


def finished(grille):
	for i in range(9):
		for j in range(9):
			if grille[i][j] == 0:
				return False
	return True


def main(grille):
	init_log()

	possibles = [[{1,2,3,4,5,6,7,8,9} for _ in range(9)] for _ in range(9)]

	logging.info('Start Solving')

	effect = True
	i = 1
	while effect and not finished(grille):
		logging.info('Step' + str(i))
		grille, possibles, effect = apply_step(grille, possibles)
		i += 1
	print(grille)
	print(possibles)
	logging.info('Finished')


if __name__ == '__main__':
	# grille = [[1, 5, 0, 2, 0, 0, 9, 0, 4],
	# 		  [0, 8, 7, 0, 0, 9, 0, 0, 3],
	# 		  [4, 0, 9, 0, 0, 0, 0, 5, 0],
	# 		  [3, 2, 8, 0, 9, 0, 0, 0, 0],
	# 		  [0, 0, 0, 0, 0, 7, 0, 0, 0],
	# 		  [0, 0, 0, 0, 8, 0, 0, 0, 6],
	# 		  [0, 0, 0, 4, 0, 1, 5, 7, 8],
	# 		  [0, 1, 0, 0, 0, 0, 0, 0, 0],
	# 		  [0, 3, 4, 9, 0, 0, 6, 0, 1]]
	grille = [[0, 0, 0, 0, 2, 0, 0, 0, 3],
			  [6, 0, 0, 0, 0, 0, 0, 2, 0],
			  [0, 2, 0, 4, 7, 1, 0, 5, 0],
			  [2, 1, 0, 5, 0, 0, 0, 3, 0],
			  [0, 0, 5, 0, 0, 0, 2, 0, 0],
			  [0, 6, 0, 0, 0, 9, 0, 8, 1],
			  [0, 8, 0, 6, 5, 4, 0, 7, 0],
			  [0, 5, 0, 0, 0, 0, 0, 0, 2],
			  [4, 0, 0, 0, 8, 0, 0, 0, 0]]
	main(grille)

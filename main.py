from Strategies.strategies import apply_step


def main(grille):
	possibles = [[{1,2,3,4,5,6,7,8,9} for _ in range(9)] for _ in range(9)]


	print('hello world')

	effect = True
	i = 1
	while effect:
		print("step", i)
		grille, possibles, effect = apply_step(grille, possibles)
		i += 1
	print(grille)
	print(possibles)



if __name__ == '__main__':
	grille = [[1, 5, 0, 2, 0, 0, 9, 0, 4],
			  [0, 8, 7, 0, 0, 9, 0, 0, 3],
			  [4, 0, 9, 0, 0, 0, 0, 5, 0],
			  [3, 2, 8, 0, 9, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 7, 0, 0, 0],
			  [0, 0, 0, 0, 8, 0, 0, 0, 6],
			  [0, 0, 0, 4, 0, 1, 5, 7, 8],
			  [0, 1, 0, 0, 0, 0, 0, 0, 0],
			  [0, 3, 4, 9, 0, 0, 6, 0, 1]]
	main(grille)

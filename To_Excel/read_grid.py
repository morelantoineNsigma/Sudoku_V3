import xlrd


def read_grid(file, sheet=0, row=0, col=0):
	grille = [[0 for _ in range(9)] for j in range(9)]

	wb = xlrd.open_workbook(file)
	s = wb.sheet_by_index(sheet)

	for i in range(9):
		for j in range(9):
			value = s.cell_value(row + i, col + j)
			try:
				grille[i][j] = int(value)
			except ValueError:
				pass

	return grille





if __name__ == '__main__':
	grille = read_grid("sudoku_test.xlsx", row=1, col=1)
	print(grille)
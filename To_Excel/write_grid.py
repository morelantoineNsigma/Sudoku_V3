import xlwt
import xlrd
from xlutils.copy import copy


def write_grid(grille, file, sheet=0, row=0, col=0):
	wb_r = xlrd.open_workbook(file)
	wb = copy(wb_r)
	s = wb.get_sheet(sheet)

	for i in range(9):
		for j in range(9):
			if grille[i][j]:
				s.write(row + i, col + j, grille[i][j])

	wb.save(file[:-5] + "_1.xls")


if __name__ == '__main__':
	grille = write_grid("sudoku_test.xlsx", row=11, col=1)
	print(grille)

from To_Excel.read_grid import read_grid
from To_Excel.write_grid import write_grid


def read_solve_write(file, sheet_r=0, sheet_w=0, rw_r=0, cl_r=0, rw_w=0, cl_w=0):
	grille = read_grid(file, sheet_r, rw_r, cl_r)
	write_grid(grille, file, sheet_w, rw_w, cl_w)


if __name__ == '__main__':
	read_solve_write("sudoku_test.xlsx", rw_r=1, cl_r=1, rw_w=11, cl_w=1)


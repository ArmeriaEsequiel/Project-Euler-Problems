import numpy as np
from operator import add

a1 = [75]
a2 = [95, 64]
a3 = [17, 47, 82]
a4 = [18, 35, 87, 10]
a5 = [20, 4, 82, 47, 65]
a6 = [19, 1, 23, 75, 3, 34]
a7 = [88, 2, 77, 73, 7, 63, 67]
a8 = [99, 65, 4, 28, 6, 16, 70, 92]
a9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
a10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
a11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
a12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
a13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
a14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
a15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

triangular_matrix = [a1, a2, a3, a4, a5, a6, a7,
					 a8, a9, a10, a11, a12, a13, a14, a15]
max_from_row = []
max_sum_row = a15

for row in reversed(triangular_matrix[0:14]):
	for i in range(len(max_sum_row)-1):
		max_num = max(max_sum_row[i], max_sum_row[i+1])
	#	print(max_num)
		max_from_row.append(max_num)# + row[i])
	max_sum_row = list(map(add, max_from_row,row))
	print(f' max sum is {max_sum_row}')
	max_from_row = []


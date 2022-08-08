import numpy as np 

num = 2**1000
full_sum = 0
for digit in str(num):
	full_sum += int(digit)

print(full_sum)
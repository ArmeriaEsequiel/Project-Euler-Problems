import numpy as np


fact = np.math.factorial(100)

result = 0
for num in str(fact):
	result += int(num)

print(result)
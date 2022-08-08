import math

number = 600851475143
LargestPrime = 0
for i in range(2,math.floor(math.sqrt(number))):
	while (number % i == 0):
		number /= i
		if number == 1 or number == i:
			print(i)
			break
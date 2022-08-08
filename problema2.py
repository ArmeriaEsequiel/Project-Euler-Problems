fiboArray =[55, 89]
sum = 2 + 8 +34
fiboResult = 0
while fiboResult < 4000000:
	fiboResult = fiboArray[0] + fiboArray[1]
	fiboArray[0] = fiboArray[1]
	fiboArray[1] = fiboResult
	if (fiboResult % 2 == 0):
		sum = fiboResult + sum


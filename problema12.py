import math as math

def getDivisors(n):
	i = 1
	count = 0
	while(i <= math.sqrt(n)):
		if(n % i == 0):
			if(n/i == i):
				count += 1
			else:
				count += 2
		i = i+1
	return(count)


def getTriangular(n):
	lastTriangular = 1
	i = lastTriangular + 1 
	maxdivisor = n
	while(getDivisors(lastTriangular)<=maxdivisor):
		lastTriangular = lastTriangular + i
		#print("el triangular {} es {}".format(i,lastTriangular))
		i+=1
	return(lastTriangular)

result = getTriangular(500)
print(result)
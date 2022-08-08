import math as math

def is_prime(n):
	result = True
	helper = 7
	#Consultamos por los casos basicos.
	if(n %2 == 0 or n %3 ==0 or n%5 ==0):
		result = False
	else:
	#Vemos los casos que son cuadrados de primos.
		while(helper <= math.ceil(math.sqrt(n))): # "!"
			if(n%helper == 0):
				return(False)
			if(n%(helper+2) == 0): return(False)
			helper+= 4
	return(result)

# !) Sabemos que N = a*b, con a <= b < N
#entonces (a*b) >= a*a,
#           N >= a**2
#           sqrt(N) >= a

def get_new_prime(n,primeList):
	prime_check_B = 6*n-1
	prime_check_A = 6*n+1
	if(is_prime(prime_check_B)): primeList.append(prime_check_B)
	if(is_prime(prime_check_A)): primeList.append(prime_check_A)
   
def upper_bound(n): #Limite superior para el n-esimo primo.
	if(n>6):
		return(math.floor(n*(math.log(n) + math.log(math.log(n)))))
	else:
		return(13)

def N_prime_count(n):
	currentCheck =1
	primeList = [2,3,5]
	bound = upper_bound(n)
	while(primeList[-1] < bound):
		get_new_prime(currentCheck,primeList)
		currentCheck += 1
	return(primeList)
a = NprimeCount(10001)
print(a[10000])
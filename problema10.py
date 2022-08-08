import math

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


def get_new_prime(n,primeList,prime_sum):
	prime_check_B = 6*n-1
	prime_check_A = 6*n+1
	if(is_prime(prime_check_B)):
		primeList.append(prime_check_B)
		prime_sum += prime_check_B
	if(is_prime(prime_check_A)):
		primeList.append(prime_check_A)
		prime_sum += prime_check_A
#	print(prime_sum)
	return(prime_sum)

def prime_sum():
	current_check = 1
	prime_sum = 10 
	bound = 1999993 # Last prime lower than 2M
	prime_list = [2,3,5]
	while (prime_list[-1] < bound):
		prime_sum = get_new_prime(current_check,prime_list,prime_sum)
		current_check +=1
	return(prime_sum)

print(prime_sum())
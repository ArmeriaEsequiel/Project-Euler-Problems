import math as math
import numpy as np

def divSum(num) :
     
    # Final result of summation of divisors
    result = 0
     
    # find all divisors which divides 'num'
    i = 2
    while i<= (math.sqrt(num)) :
       
        # if 'i' is divisor of 'num'
        if (num % i == 0) :
       
            # if both divisors are same then
            # add it only once else add both
            if (i == (num / i)) :
                result = result + i;
            else :
                result = result +  (i + num/i);
        i = i + 1
         
    # Add 1 to the result as 1 is also
    # a divisor
    return (result + 1);



amicable_sum = 0
divisors_sum = [-1]
for i in range(1,10001):
	sumation = divSum(i)
	divisors_sum.append(int(sumation))
	if sumation <= (len(divisors_sum)-1):
		if(divisors_sum[int(sumation)] == i) and i != int(sumation):
			print(f'amicable numbers are {i} and {sumation}')
			amicable_sum = amicable_sum + (i + int(sumation))

print(amicable_sum)



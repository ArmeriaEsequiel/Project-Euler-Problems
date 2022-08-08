def es_divisible(num):
    result = False
    suma = 0
    for i in range(1,20):
        suma = suma + (num % i)
    if (suma == 0):
        return(True)
    return(result)


divisible = False
i = 1
while(divisible != True):
    divisible = es_divisible(i)
    i = i + 1
print(i-1)
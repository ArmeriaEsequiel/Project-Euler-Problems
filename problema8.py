import math as math
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
#La idea es multiplicar los primero 13 numeros, para los siguientes 13, al ultimo producto
# le divididimos el primer valor de los 13 anterores (tail) y le multiplicamos el siguiente del ultimo (head)
# de los 13 anteriores:
# Veamos un ejemplo con la multiplicacion de 3 digitos
# ej: [1,2,3,4] = 6 (primero 3)
#     para el siguiente hacemos:
#     6/1 = 6
#     6 * 4 = 24
# 

def new_product(num_list,j,n):
	max_product = 1
	current_product = 0
	for i in range(j,n):
		max_product = max_product * num_list[i]
	current_product = max_product
	return(current_product)


def adjacenProduct():
	num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	max_product = 1
	cant_adjacente = 13
	current_product = 1
	#Transformamos el numero en un array
	num_list = [int(x) for x in str(num)]
	tail = num_list[0] #Conservamos el ultimo elemento
	head = num_list[cant_adjacente]
	#Calculamos el producto
	for i in range(cant_adjacente):
	    max_product = max_product * num_list[i]
	current_product = max_product
	print("el primer producto es {}".format(current_product))
	bound = len(num_list) - cant_adjacente
	for i in range(1,bound+1):
			# Si tail es cero, tendremos que volver a calcular un
			# primer valor para poder seguir operando, las demas 
			# multiplicaciones y divisiones
			# seran 0 siempre.		
			if(tail == 0):
				tail = 1
				current_product = new_product(num_list,i, i+cant_adjacente)
			else:
				#Calculamos el nuevo valor
				current_product = (current_product / tail) * head
				if(max_product < current_product):# Vemos si es mas maximo
					max_product = current_product
				#Paramos cuando alcanzmos el final
				if(cant_adjacente+i >= len(num_list)):
					return(max_product)
			tail = num_list[i]# Aumentamos tail
			head = num_list[cant_adjacente+i] #Aumentamos head

max_product = adjacenProduct()
print(max_product)
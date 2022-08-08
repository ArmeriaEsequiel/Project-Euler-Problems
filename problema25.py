Fibarray = [0, 1]
for i in range(2,10000):
	Fibarray.append(Fibarray[i - 1] + Fibarray[i - 2])
	if len(str(Fibarray[-1])) >= 1000:
		print(i)
		break
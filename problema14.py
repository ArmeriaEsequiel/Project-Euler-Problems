longest_chain = []
compare_chain = []

for i in reversed(range(1,1000001)):
	compare_chain.append(i)
	while(compare_chain[-1] != 1):
#		print(compare_chain)
		if(compare_chain[-1]%2 == 0):
			 compare_chain.append(compare_chain[-1]/2)
		else:
			 compare_chain.append(3*compare_chain[-1] + 1)

#	print(len(compare_chain))
	if len(longest_chain) < len(compare_chain):
		longest_chain = compare_chain
		compare_chain = []
	else:
		compare_chain = []

print(f'longest_chain es: {longest_chain}')
print(f' largo longest_chain es: {len(longest_chain)}')
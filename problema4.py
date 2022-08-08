def is_palindrome(num):
	temp=num
	rev=0
	while(num>0):
		dig=num%10
		print(dig)
		rev=rev*10+dig
		num=num//10
	if(temp==rev):
		return(True)
	else:
		return(False)


max_3_dig_num = 999
max_palindrome = 0
upper_limit = max_3_digit_num + 1
lower_limit = 100
for i in range(lower_limit,upper_limit,1,1):
	for j in range(i,upper_limit,1,1):
		num = i*j
		result = is_palindrome(num)
		if (result == True and num > max_palindrome):
				max_palindrome = num
print(max_palindrome)
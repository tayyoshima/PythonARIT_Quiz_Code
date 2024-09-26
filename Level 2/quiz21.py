x = "Hello World"
... x != "QUIT" :
	num = 0
	... char ... x:
		num += 1
	print(num)
	x = input("Enter a new word or QUIT to exit: ")
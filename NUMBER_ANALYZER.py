def number_analyzer():
	num = int(input("enter a number: "))
	if num % 2 == 0:
		print("even")
	else:
		print("odd")
	if num > 0:
		print("positive")
	elif num < 0:
		print("negative")
	else:
		print("zero")
number_analyzer()

def isLeap(year):
	isLeap = False

	if (year % 4 == 0):
		if(year % 100 != 0 or year % 400 == 0): 
			isLeap = True	
	return isLeap
		

print(isLeap(1991))
print(isLeap(2100))
print(isLeap(1996))

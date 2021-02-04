def secondLowestGrade(input):
	grades  = open(input,"r")
	grades.seek(1)
	lines = grades.readlines()
	
	

	nestedList = []
	
	for line in lines:
		print(line.strip())
		nestedList.append(line.strip())
	print(nestedList)

#not sure why this one is taking me so long gonna sleep on it	
#print(secondLowestGrade("/Users/ryanremaly/Documents/workspace/HackerRank/input.txt"))
print(secondLowestGrade("input.txt"))

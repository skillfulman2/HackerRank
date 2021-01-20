def secondLowestGrade(input):
	grades  = open(input,"r") 
	lines = grades.readlines()
	nestedList = [[]]
	
	for line in lines:
		print(line.strip())
		nestedList.append(line.strip())
	print(nestedList)

	
#print(secondLowestGrade("/Users/ryanremaly/Documents/workspace/HackerRank/input.txt"))
print(secondLowestGrade("input.txt"))

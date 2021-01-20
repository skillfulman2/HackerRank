
# Brute force method, not pretty
def runnerUp(n, arr):
	highest = bubbleSort(arr)
	arr.remove(highest)
	runner = bubbleSort(arr)
	return runner


#Ugly bubble sort
def bubbleSort(arr) -> int:
	max = 0
	for num in arr:
		if num > max:
			max = num
	return max

print(runnerUp(10, [1,2,3,4,5,6,7,8,9,10]))

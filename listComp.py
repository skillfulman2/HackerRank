def permutationPrint(x, y, z, n):

	Numbers = ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n])
	print(Numbers)


def permutationPractice(x, y, n):

	Numbers = ([[a,b] for a in range(x+4) for b in range(x+7) if a + b != n ])
	print(Numbers)


#permutationPrint(1,2,3,2)
permutationPractice(2, 8, 12)

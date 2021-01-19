def permutationPrint(x, y, z, n):

	Numbers = ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n])
	print(Numbers)

permutationPrint(1,2,3,2)

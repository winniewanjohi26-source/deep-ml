def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	product = []
	if len(a[0]) == len(b):
		for i in range(len(a)):
			sum = 0
			for j in range(len(b)):
				dot = a[i][j]*b[j]
				sum += dot
			product.append(sum)
		return product
	else:
		return -1
	pass
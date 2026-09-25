def scalar_multiply(a: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = []
	for i in range(len(a)):
		row = []
		for j in range(len(a[i])):
			row.append(a[i][j] * scalar)
		result.append(row)
	return result 
	pass
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	"""
	det = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
	trace = matrix[0][0] + matrix[1][1]
	return det,trace
	"""
	trace = 0
	for i in range(len(matrix)):
		trace += matrix[i][i]
	x = 1
	for i in range(len(matrix)):
		x *= matrix[i][i]
	n = len(matrix)
	if n == 2:
		det = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
	elif n == 3:
		det = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]) - matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]) + matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])

	return det, trace
	# Your code here
	pass
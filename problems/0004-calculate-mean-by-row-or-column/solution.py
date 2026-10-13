def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	#means = []
	if mode == "row":
		means = []
		for row in matrix:
			means.append(sum(row)/len(row))
	elif mode == "column":
		means = []
		for j in range(len(matrix[0])):
			column = []
			for row in matrix:
				column.append(row[j])
			means.append(sum(column)/len(column))
	return means
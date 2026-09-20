def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	if len(a) == len(b):
		result = []
		for i in range(len(a)):
			result.append(a[i]+b[i])
		return result
	# If vectors have different lengths, return -1.
	else:
		return -1
pass
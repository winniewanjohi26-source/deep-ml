import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if len(v1) == len(v2):
		numerator = np.dot(v1, v2)
		denominator = np.linalg.norm(v1, 2)*np.linalg.norm(v2, 2)
		return numerator/denominator
	else:
		return -1
	pass
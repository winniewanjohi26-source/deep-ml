def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	E = (n+1)/2
	exp_sq = ((n+1)*(2*n+1))/6
	V = exp_sq - E**2
	return (E, V)
	pass
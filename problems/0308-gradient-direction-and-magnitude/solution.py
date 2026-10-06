import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = np.linalg.norm(gradient, 2)
	if magnitude == 0:
		direction = []
		descent_direction = []
		for i in range(len(gradient)):
			direction.append(0)
			descent_direction.append(0)
	else:
		direction = []
		descent_direction = []
		for i in range(len(gradient)):
			direction.append(float(gradient[i]/magnitude))
		for j in range(len(direction)):
			descent_direction.append(-direction[j])
	return {
		"magnitude": magnitude,
		"direction": direction,
		"descent_direction": descent_direction
	}
	pass
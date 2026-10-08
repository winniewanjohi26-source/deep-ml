import numpy as np

def linear_regression_gradient_descent(x: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = x.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    # Your code here: implement gradient descent
    for i in range(iterations):
        y_pred = np.dot(x, theta)
        error = y_pred - y
        x_t = x.T
        g = (1/m)*(np.dot(x_t, error))
        theta = theta - alpha*g

    return theta.flatten()
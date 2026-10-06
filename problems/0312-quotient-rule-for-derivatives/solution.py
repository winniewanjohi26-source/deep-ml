import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g_x = 0
    g_deriv = 0
    for i in range(len(g_coeffs)):
        n = len(g_coeffs)-1
        g_x = g_x + g_coeffs[i]*x**(n-i)
    for i in range(len(g_coeffs)-1):
        g_deriv = g_deriv + (n-i)*g_coeffs[i]*x**(n-i-1) 
    h_x = 0
    h_deriv = 0
    for i in range(len(h_coeffs)):
        n = len(h_coeffs)-1
        h_x = h_x + h_coeffs[i]*x**(n-i)
    for i in range(len(h_coeffs)-1):
        h_deriv = h_deriv + (n-i)*h_coeffs[i]*x**(n-i-1)

    num = g_deriv*h_x - g_x*h_deriv
    den = (h_x)**2
    return num/den
    pass
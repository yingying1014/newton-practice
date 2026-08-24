def deriv(f, x, eps = 1e-8):
    return (f(x+eps) - f(x)) / eps


def deriv2(f, x, eps = 1e-8):
    return (deriv(f, x+eps, eps) - deriv(f, x, eps)) / eps


def optimize(x0, f, tol =1e-4):
    """Run Newton's method to minimize a function.
    
    Parameters
    ----------
    x0: starting value
    f: function to minimize
    tol: blah blah blah
    """
    x_new = x0 - deriv(f, x0)/ deriv2(f, x0)
    x = x0
    while abs(x_new - x) < tol:
        x = x_new
        x_new = x0 - deriv(f, x0) / deriv2(f, x0)
    return {"x": x_new,
            'value': f(x_new)}

print("hi!")
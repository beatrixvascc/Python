def bhaskara(a: float, b: float, c: float) -> (float, float):
    delta = b**2 - 4*a*c
    x1 = (-b + delta**(1/2))/2*a
    x2 = (b + delta**(1/2))/2*a
    return x1, x2

print(bhaskara(3.5,6.7,8.9))

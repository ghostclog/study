def gcd(a,b):
    a = a
    b = b
    while b != 0:
        a, b = b, a % b
    return a

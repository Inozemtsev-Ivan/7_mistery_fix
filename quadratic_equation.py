from math import sqrt


def get_roots(a, b, c):
    try:
        discriminant = b ** 2 - 4 * a * c
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return (root1, root2) if root1 != root2 else (root1, None)
    except ValueError:
        return None, None

from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    def root_1():
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        return root1
    if discriminant == 0:
        root1 = root_1()
        return root1, None
    elif discriminant < 0:
        return None, None
    else:
        root1 = root_1()
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2

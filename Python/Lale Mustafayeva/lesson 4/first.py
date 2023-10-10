def calculate_roots(a, b, c):
    discriminant = b * b - 4 * a * c
    if a == 0:
       return (-c / b, ) if b != 0 else "No solution"
    elif discriminant == 0:
        return -b / (2 * a),
    elif discriminant < 0:
        return "Yoxdu"
    else:
        sqrt_discriminant = discriminant ** 0.5
        return (-b + sqrt_discriminant) / (2 * a), (-b - sqrt_discriminant) / (2 * a)

a = 0
b = 1
c = -3
x = calculate_roots(a, b, c)

if isinstance(x, str):
    print(x)
elif len(x) == 1:
    print("D: 0")
    print("x:", x[0])
else:
    discriminant = (b**2 - 4 * a * c) ** 0.5
    print("D:", discriminant)
    print("x1:", x[0])
    print("x2:", x[1])

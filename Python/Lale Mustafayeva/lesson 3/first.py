d = lambda a, b, c: b * b - 4 * a * c
roots = lambda a, b, c: (
    (-b + (d(a, b, c) ** 0.5)) / (2 * a),
    (-b - (d(a, b, c) ** 0.5)) / (2 * a)
)

a = 2
b = 1
c = -3
discriminant = d(a, b, c) ** 0.5
if discriminant == 0: 
    print("D:", discriminant)
    x = roots(a, b, c)
    print("x:", x)
elif discriminant<0:
    print("Yoxdu")
else:
    x1, x2 = roots(a, b, c)
    print("D:", discriminant)
    print("x1:", x1)
    print("x2:", x2)

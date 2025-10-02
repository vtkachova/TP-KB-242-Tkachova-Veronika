def discr(a, b, c):
    return b*b - 4*a*c   

# Вводимо коефіцієнти
a = int(input("What's A: "))
b = int(input("What's B: "))
c = int(input("What's C: "))

# Рахуємо дискримінант
D = discr(a, b, c)
print("Дискримінант =", D)

# Шукаємо корені
if D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print("Два корені: x1 =", x1, ", x2 =", x2)
elif D == 0:
    x = -b / (2*a)
    print("Один корінь: x =", x)
else:
    print("Коренів немає (D < 0)")
import math

side = math.ceil(float((input("Введите сторону квадрата: "))))

def square(line):
    return (line * side)
print(f"Площадь квадрата:  {square(side)}")

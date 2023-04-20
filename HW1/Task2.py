origin = input("Введите трёх значное число: ")
origin = int(origin)

first = origin % 10
origin = origin // 10
second = origin % 10
origin = origin // 10

print("Сумма цифр :", origin + first + second)

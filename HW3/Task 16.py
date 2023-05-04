N = abs(int(input('Введите количество элементов ')))
A = input("Введите через пробел элементы : ").split()
A_num = list(map(int, A))

X = int(input('Введите число которое необходимо найти '))
num = 0
for i in range(N):
    if A_num[i] == X:
        num += 1
print(num)
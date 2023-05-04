N = abs(int(input('Введите количество элементов ')))
A = input("Введите через пробел элементы : ").split()
A_num = list(map(int, A))

X = int(input("Введите число"))
mn = abs(X - A_num[0])
index = 0
for i in range(1, N):
    count = abs(X - A_num[i])
    if count < mn:
        mn = count
        index = i
print(f'Число {A_num[index]}  близко по величине к числу {X}, их разница  {abs(X - A_num[index])}')

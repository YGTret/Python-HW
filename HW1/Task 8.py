print("Введите размер шоколадки")
m, n = int(input()), int(input())
print("Введите колличество долек которые вы хотите отломить")
k = int(input())

if k % m == 0 or k % n ==0 :
    print("Можно отломить")
else:
    print("Нельзя отломить")
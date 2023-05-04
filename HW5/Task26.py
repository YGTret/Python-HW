def stepenrec(a,b):
    if b == 0:
        return 1
    return a * stepenrec(a, b - 1)

a = int(input("Число:"))
b = int(input("Степень:"))
print(stepenrec(a, b))
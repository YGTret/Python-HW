def summarec(a, b):
    if b == 0:
        return a
    return 1 + summarec(a, b - 1)

print(summarec(2, 2))
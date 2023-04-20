number = int(input("Введите номер билета"))
FirstThreeNumber = number // 100000 + number % 100000 // 10000 + number % 10000 // 1000
SecondThreeNumber = number % 1000 // 100 + number % 100 // 10 + number % 10

if FirstThreeNumber == SecondThreeNumber:
    print("Ваш билет Счастливый!!")
else:
    print("Ваш билет не счастливый((")

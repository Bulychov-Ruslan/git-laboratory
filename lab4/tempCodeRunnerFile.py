while True:
    a = input("Бірінші сан: ")
    b = input("Екінші сан: ")
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        print("Сумма", a + b)
        break
    else:
        print("Қате. Санді енгіз.")
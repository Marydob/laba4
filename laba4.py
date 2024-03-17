def laba41():
    a = int(input("введите число "))
    if a % 3 == 0:
        print("число делится на 3")
    else:
        print("число не делится на 3")
def laba42():
    try:
        a = int(input("введите число: "))
        tmp = 100 / a
        print(tmp)
    except Exception as e:
        print("Error! " + str("некорректный ввод"))
def laba43():
    a=input("введите дату через точку(ДД.ММ.ГГГГ): ")
    d=int(a[0]+a[1])
    m=int(a[3]+a[4])
    y=int(a[8]+a[9])
    if d*m==y:
        print("True")
    else:
        print("False")
def laba44():
    a = input("Введите номер билета: ")
    if a.isdigit():
        if len(a) % 2 == 0:
            b = len(a) // 2
            f = a[:b]
            s = a[b:]

            if sum(map(int, f)) == sum(map(int, s)):
                print("это счастливый билет")
            else:
                print("это несчастливый билет")
        else:
            print("введите чётное кол-во цифр")
    else:
        print("введите цифры")
laba41()
laba42()
laba43()
laba44()

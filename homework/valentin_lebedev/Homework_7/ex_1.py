i = 9

while True:
    num = int(input("Введите число: "))
    if num != i:
        print("попробуйте снова")
        continue
    else:
        print("Поздравляю! Вы угадали!")
        break

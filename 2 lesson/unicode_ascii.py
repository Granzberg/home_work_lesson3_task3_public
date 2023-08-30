word = input("Введіть 10 літер: ")
num = 0

while True:
    if len(word) != 10:
        print("Ви ввели неправильну кількість літер!!")
        word = input("Введіть 10 літер: ")
    elif len(word) == 10:
        for i in word:
            num += ord(i)
        break
print("Сума ASCII-кодів символів введеного рядка: ", num)

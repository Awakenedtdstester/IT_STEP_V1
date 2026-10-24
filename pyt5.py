n = int(input("Введіть число n: "))

print("Результат:")
for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")

a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))

c = input("Введіть математичну дію (+, -, *, /): ")

if c == "+":
    res = a + b
    print(f"Результат: {res}")
elif c == "-":
    res = a - b
    print(f"Результат: {res}")
elif c == "*":
    res = a * b
    print(f"Результат: {res}")
elif c == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        res = a / b
        print(f"Результат: {res}")
else:
    print("Помилка: введено невідому математичну дію.")

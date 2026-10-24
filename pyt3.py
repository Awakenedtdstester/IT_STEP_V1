import random

a = random.randint(1, 10)
attempts = 3

print("Ласкаво просимо до гри 'Вгадай число'!")
print("Я загадав число від 1 до 10. У вас є 3 спроби.")

for c in range(1, attempts + 1):
    print(f"\nСпроба №{c}")
    b = int(input("Введіть ваше число: "))
    
    if b == a:
        print(" Вітаю! Ви вгадали число!")
        break
    elif b > a:
        print("Менше")
    else:
        print("Більше")
    
    if c == attempts:
        print(f"\nНа жаль, спроби закінчилися. Я загадав число: {a}")

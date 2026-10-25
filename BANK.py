class BankAccount:
    def __init__(self, a_num, balance=0.0):
        self.a_num = a_num
        self.b = balance

    def deposit(self, a):
        if a > 0:
            self.b += a
            print(f"Рахунок {self.a_num} поповнено на {a}. Баланс: {self.b}")
        else:
            print("Сума поповнення має бути більшою за нуль.")

    def withdraw(self, a):
        if a > self.b:
            print(f"Помилка: недостатньо коштів на рахунку {self.a_num}! Доступно: {self.b}")
        elif a <= 0:
            print("Сума для зняття має бути більшою за нуль.")
        else:
            self.b -= a
            print(f"З рахунку {self.a_num} знято {a}. Залишок: {self.b}")
#example
# acc = BankAccount("example", 1000)
# acc.deposit(400)
# acc.withdraw(200)            

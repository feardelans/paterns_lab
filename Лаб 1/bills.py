class Bill:
    #клас bill представляє рахунок клієнта за послуги оператора

    def __init__(self, limiting_amount: float) -> None:
        #конструктор для класу Bill
        self.limiting_amount: float = limiting_amount             #макс сума боргу
        self.current_debt: float = 0.0

    def check(self) -> bool:
        #перевірка чи перевищено ліміт
        return self.current_debt >= self.limiting_amount

    def add_debt(self, debt: float) -> None:
        #додавання боргу до рахунку
        tentative_debt = debt + self.current_debt               #попередній - tentative
        if tentative_debt <= self.limiting_amount:
            self.current_debt += debt
        else:
            print(f"Ви перевищили ліміт! Ваш борг становитиме {tentative_debt}")

    def pay(self, amount: float) -> None:
        #оплата рахунку
        self.current_debt -= amount
        if self.current_debt < 0:
            self.limiting_amount += abs(self.current_debt)
            self.current_debt = 0
        print(f"Оплачено {amount}. Борг: {self.current_debt}")

    def change_limit(self, amount: float) -> None:
        #зміна ліміту рахунку
        self.limiting_amount += amount
        print(f"Ліміт змінено. Новий ліміт: {self.limiting_amount}")

    def get_limiting_amount(self) -> float:
        return self.limiting_amount

    def get_current_debt(self) -> float:
        return self.current_debt

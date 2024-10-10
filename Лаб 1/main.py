from customers import Customer
from operators import Operator
from bills import Bill


def main():
    # ініціалізація операторів
    operators = [Operator(0, 0.4, 0.2, 0.2, 10), Operator(1, 0.6, 0.2, 0.2, 5)]

    bills = [Bill(1000), Bill(500)]

    customers = [Customer(0, 'Влад', 'Припотнюк', 19, operators, bills),
                 Customer(1, 'Дмитро', 'Ролін', 25, operators, bills)]
    #виклик дій для клієнтів
    customers[0].talk(10, customers[1], 0)  #Рома говорить з Антон
    customers[1].message(5, customers[0], 1)  # Антон відправляє повідомлення Ромі
    customers[0].connection(100, 0)    #Рома використовує інтернет

   # оплата рахунку
    customers[0].get_bill(0).pay(150)

    # зміна ліміту рахунку
    customers[0].get_bill(0).change_limit(150)


if __name__ == "__main__":
    main()   #щоб запускався як головна програма



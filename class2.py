# Класс Покупатель: Фамилия, Имя, Отчество, Адрес, Номер
# кредитной карточки, Номер банковского счета; Конструктор(`__init__`);
# Методы: установка значений атрибутов, получение значений
# атрибутов, вывод информации. Создать список объектов
# данного класса.


class Customer:
    def __init__(self, firstname=None, secondName=None, patronymic=None, address=None,
                 creditCard=None, bankNumber=None):
        self.__customer = {
            "First Name": firstname,
            "Second Name": secondName,
            "Patronymic": patronymic,
            "Address": address,
            "credit Card": creditCard,
            "bank Number": bankNumber}

    def print(self):
        for customer in self.__customer:
            print(customer)

    def update(self):
        thing = str(input("Что вы хотите поменять? "))
        self.__customer.update({thing: input()})

    def attribut(self):
        print(self.__customer.get(input("Значение какого атрибута вам необходимо? ")))


customersList = []
for i in range(10):
    customersList.append(input("Введите имя: "))
for i in range(len(customersList)):
    customersList[i] = Customer()
    print(customersList[i])



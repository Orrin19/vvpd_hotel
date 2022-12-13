"""Модуль содержит класс Room"""


class Room:
    """
    Информация о комнате в гостинице

    Класс содержит основную информацию о комнате:
    её номер, вместимость, комфортабельность и цена за сутки
    
    Attributes:
        number (str): Номер комнаты
        capacity (str): Вместительность комнаты
        comfort (str): Комфортабельность комнаты
        price (str): Цена комнаты
    """
    def __init__(
        self,
        number: str,
        capacity: str,
        comfort: str,
        price: str
    ) -> None:
        """
        Конструктор класса Room

        Parameters:
            number (str): Номер комнаты
            capacity (str): Вместительность комнаты
            comfort (str): Комфортабельность комнаты
            price (str): Цена комнаты
        """
        self.number = number
        self.capacity = capacity
        self.comfort = comfort
        self.price = price

    @classmethod
    def console_create(cls, hotel):
        """
        Создание экземпляра класса Room через консольный интерфейс

        Parameters:
            hotel (Hotel): Класс гостиницы

        Returns:
            Room: Экземпляр комнаты, если создание успешно
            None: В случае, если произошла ошибка при создании комнаты
        """
        number = input('Введите номер комнаты >>> ')
        if not number:
            print('Необходимо ввести номер комнаты!')
            return None
        if hotel.find_room(number, absence=False):
            print('Комната с таким номером уже существует!')
            return None
        capacity = input('Введите вместительность комнаты >>> ')
        comfort = input('Введите комфортабельность номера >>> ')
        price = input('Введите цену номера за сутки >>> ')
        print('Комната успешно создана!')
        return cls(number, capacity, comfort, price)

    def __str__(self) -> str:
        """
        Представляет экземпляр комнаты в виде строки

        Returns:
            str: Строковое представление объекта

        Examples:
            >>> Room('25', '2 человека', '5 звёзд', '300 долларов')
            25, вместительность: 2 человека, комфортабельность: 5 звёзд, цена: 300 долларов
        """
        room_string = self.number
        if self.capacity:
            room_string += ', вместительность: ' + self.capacity
        if self.comfort:
            room_string += ', комфортабельность: ' + self.comfort
        if self.price:
            room_string += ', цена: ' + self.price
        return room_string

    def print_room(self) -> None:
        """Печатает данные об экземпляре клиента"""
        print('\nНомер:', self.number)
        if self.capacity:
            print('Вместительность:', self.capacity)
        if self.comfort:
            print('Комфортабельность:', self.comfort)
        if self.price:
            print('Цена:', self.price)

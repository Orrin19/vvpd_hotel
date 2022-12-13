"""Модуль содержит класс Room"""


class Room:
    """В классе содержится информация о гостиничном номере:
    его номер, вместимость, комфортабельность и цена за сутки."""
    def __init__(self, number, capacity, comfort, price):
        self.number = number
        self.capacity = capacity
        self.comfort = comfort
        self.price = price

    @classmethod
    def console_create(cls, hotel):
        """Создать номер через консоль"""
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

    def get_room(self):
        """Возвращает строку с данными о комнате"""
        room_string = self.number
        if self.capacity:
            room_string += ', вместительность: ' + self.capacity
        if self.comfort:
            room_string += ', комфортабельность: ' + self.comfort
        if self.price:
            room_string += ', цена: ' + self.price
        return room_string

    def print_room(self):
        """Выводит данные о комнате"""
        print('\nНомер:', self.number)
        if self.capacity:
            print('Вместительность:', self.capacity)
        if self.comfort:
            print('Комфортабельность:', self.comfort)
        if self.price:
            print('Цена:', self.price)

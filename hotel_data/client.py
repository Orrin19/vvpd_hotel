"""Модуль содержит класс Client"""


class Client:
    """В классе содержится информация о клиенте гостиницы:
    ФИО, паспортные данные, комментарий"""
    def __init__(self, full_name, passport_details, commentary=''):
        self.full_name = full_name
        self.passport_details = passport_details
        self.commentary = commentary

    @classmethod
    def console_create(cls, hotel):
        """Создать клиента через консоль"""
        full_name = input('Введите ФИО клиента >>> ')
        if not full_name:
            print('Необходимо указать полное имя клиента!')
            return None
        passport_details = input('Введите паспортные данные >>> ')
        if hotel.find_client(passport_details, absence=False):
            print('Клиент с такими паспортными данными уже зарегистрирован!')
            return None
        commentary = input('Добавьте комментарий (опционально) >>> ')
        print('Клиент успешно зарегистрирован!')
        return cls(full_name, passport_details, commentary)

    def get_client(self):
        """Возвращает строку с данными о клиенте"""
        client_string = self.full_name + ', паспортные данные: ' + self.passport_details
        if self.commentary:
            client_string += ', ' + self.commentary
        return client_string

    def print_client(self):
        """Выводит данные о клиенте"""
        print('\nФИО:', self.full_name)
        print('Паспортные данные:', self.passport_details)
        if self.commentary:
            print('Комментарий:', self.commentary)

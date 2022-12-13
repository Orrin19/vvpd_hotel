"""Модуль содержит класс Client"""


class Client:
    """
    Информация о клиенте гостиницы

    Класс содержит основную информацию о клиенте как о личности:
    ФИО, паспортные данные, опциональный комментарий
    
    Attributes:
        full_name (str): ФИО клиента
        passport_details (str): Паспортные данные клиента
        commentary (str): Опциональный комментарий
    """
    def __init__(
        self,
        full_name: str,
        passport_details: str,
        commentary: str = ''
    ) -> None:
        """
        Конструктор класса Client

        Parameters:
            full_name (str): ФИО клиента
            passport_details (str): Паспортные данные клиента
            commentary (str): Опциональный комментарий
        """
        self.full_name = full_name
        self.passport_details = passport_details
        self.commentary = commentary

    @classmethod
    def console_create(cls, hotel):
        """
        Создание экземпляра класса Client через консольный интерфейс

        Parameters:
            hotel (Hotel): Класс гостиницы

        Returns:
            Client: Экземпляр клиента, если создание успешно
            None: В случае, если произошла ошибка при создании клиента
        """
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

    def __str__(self) -> str:
        """
        Представляет экземпляр клиента в виде строки

        Returns:
            str: Строковое представление объекта

        Examples:
            >>> Client('Иванов Иван Иванович', '12345', 'Клиент')
            Иванов Иван Иванович, паспортные данные: 12345, Клиент
        """
        client_string = self.full_name + ', паспортные данные: ' + self.passport_details
        if self.commentary:
            client_string += ', ' + self.commentary
        return client_string

    def print_client(self) -> None:
        """Печатает данные об экземпляре клиента"""
        print('\nФИО:', self.full_name)
        print('Паспортные данные:', self.passport_details)
        if self.commentary:
            print('Комментарий:', self.commentary)

"""Модуль содержит основной класс Hotel"""


import pickle
from client import Client
from lodger import Lodger
from room import Room


class Hotel:
    """
    Информация о гостинице и основные функции

    Класс содержит списки клиентов, постояльцев и комнат, а также
    основные методы программы
    
    Attributes:
        clients (list): Список клиентов
        lodgers (list): Список постояльцев
        rooms (list): Список комнат
    """
    def __init__(self, clients: list, lodgers: list, rooms: list) -> None:
        """
        Конструктор класса Hotel

        Parameters:
            clients (list): Список клиентов
            lodgers (list): Список постояльцев
            rooms (list): Список комнат
        """
        self.clients = clients
        self.lodgers = lodgers
        self.rooms = rooms

    @classmethod
    def empty(cls):
        """
        Создание пустого экземпляра класса Hotel

        Returns:
            Hotel: Экземпляр гостиницы с пустыми списками
        """
        return cls([], [], [])

    def save(self) -> None:
        """Запись объекта в файл"""
        filename = input(
            'Введите имя файла для записи (по умолчанию database) >>> '
            ) or 'database'
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
            print(f"Информация успешно записана в {filename}!")

    def load(self) -> None:
        """Загрузка объекта из файла"""
        filename = input(
            'Введите имя файла для загрузки (по умолчанию database) >>> '
            ) or 'database'
        try:
            with open(filename, 'rb') as file:
                print(f"Информация успешно загружена из {filename}!")
                data = pickle.load(file)
                self.clients = data.clients
                self.lodgers = data.lodgers
                self.rooms = data.rooms
        except FileNotFoundError:
            print('Такого файла не найдено!')

    def create_client(self) -> None:
        """Создаёт нового клиента через консольный интерфейс"""
        client = Client.console_create(self)
        if not client:
            print('Не удалось зарегистрировать клиента!')
        else:
            self.clients.append(client)

    def create_room(self) -> None:
        """Создаёт новую комнату через консольный интерфейс"""
        room = Room.console_create(self)
        if not room:
            print('Не удалось создать комнату!')
        else:
            self.rooms.append(room)

    def create_lodger(self) -> None:
        """Создаёт нового постояльца через консольный интерфейс"""
        lodger = Lodger.console_create(self)
        if not lodger:
            print('Не удалось заселить постояльца!')
        else:
            self.lodgers.append(lodger)

    def find_client(
        self,
        passport_details: str,
        absence: bool = True
    ) -> (Client | None):
        """
        Находит клиента в списке по паспортным данным

        Parameters:
            passport_details (str): Паспортные данные клиента
            absence (bool): Нужно ли уведомить об отсутствии клиента в базе

        Returns:
            Client: Экземпляр клиента, если он найден в списке
            None: В случае, если клиент не найден
        """
        try:
            return list(filter(
                lambda c: c.passport_details == passport_details,
                self.clients
            ))[0]
        except IndexError:
            if absence:
                print('Клиент с такими данными не найден!')
            return None

    def find_room(
        self,
        number: str,
        absence: bool = True
    ) -> (Room | None):
        """
        Находит комнату в списке по её номеру

        Parameters:
            number (str): Номер комнаты
            absence (bool): Нужно ли уведомить об отсутствии комнаты в базе

        Returns:
            Room: Экземпляр комнаты, если она найдена в списке
            None: В случае, если комната не найдена
        """
        try:
            return list(filter(
                lambda r: r.number == number,
                self.rooms
            ))[0]
        except IndexError:
            if absence:
                print('Такая комната не найдена!')
            return None

    def find_lodger(
        self,
        passport_details: str,
        number: str,
        absence: bool = True
    ) -> (Lodger | None):
        """
        Находит постояльца в списке по его паспортным данным и номеру комнаты

        Parameters:
            passport_details (str): Паспортные данные клиента
            number (str): Номер комнаты
            absence (bool): Нужно ли уведомить об отсутствии постояльца в базе

        Returns:
            Lodger: Экземпляр постояльца, если он найден в списке
            None: В случае, если постоялец не найден
        """
        client = self.find_client(passport_details)
        if not client:
            return None
        room = self.find_room(number)
        if not room:
            return None

        try:
            return list(filter(
                lambda l: l.client == client and l.room == room,
                self.lodgers
            ))[0]
        except IndexError:
            if absence:
                print('Такой записи не найдено!')
            return None

    def delete_client(self) -> None:
        """Удаляет запись клиента из списка"""
        passport_details = input('Введите паспортные данные >>> ')
        client = self.find_client(passport_details)
        if client in map(lambda l: l.client, self.lodgers):
            for lodger in filter(lambda l: l.client == client, self.lodgers):
                self.lodgers.pop(self.lodgers.index(lodger))
        if client:
            self.clients.pop(self.clients.index(client))
            print('Запись клиента удалена!')

    def delete_room(self) -> None:
        """Удаляет запись комнаты из списка"""
        number = input('Введите номер комнаты >>> ')
        room = self.find_room(number)
        if room in map(lambda l: l.room, self.lodgers):
            for lodger in filter(lambda l: l.room == room, self.lodgers):
                self.lodgers.pop(self.lodgers.index(lodger))
        if room:
            self.rooms.pop(self.rooms.index(room))
            print('Запись комнаты удалена!')

    def delete_lodger(self) -> None:
        """Удаляет запись постояльца из списка"""
        passport_details = input('Введите паспортные данные >>> ')
        number = input('Введите номер комнаты >>> ')
        lodger = self.find_lodger(passport_details, number)
        if lodger:
            self.lodgers.pop(self.lodgers.index(lodger))
            print('Запись постояльца удалена!')

    def evict_lodger(self) -> None:
        """Изменяет дату выселения постояльца"""
        passport_details = input('Введите паспортные данные >>> ')
        number = input('Введите номер комнаты >>> ')
        lodger = self.find_lodger(passport_details, number)
        if lodger:
            lodger.evict()

    def get_free_rooms(self, check_in_date, check_out_date) -> list:
        """
        Печатает список свободных номеров в указанный период

        Parameters:
            check_in_date (datetime): Дата заселения
            check_out_date (datetime): Дата выселения

        Returns:
            list: Список свободных комнат (может быть пустым)
        """
        rooms = set(map(lambda r: r.number, self.rooms))
        occupied_rooms = []
        for room_number, room_check_in, room_check_out in map(
            lambda l: (l.room.number, l.check_in_date, l.check_out_date),
            self.lodgers
        ):
            if not (room_check_in > check_out_date or room_check_out < check_in_date):
                occupied_rooms.append(room_number)

        free_rooms = sorted(list(filter(
            lambda r: r not in occupied_rooms,
            rooms
        )))

        if not free_rooms:
            print('Свободные номера отсутствуют!')
        else:
            print('Список свободных номеров:', ', '.join(free_rooms))
        return free_rooms

    def print_clients(self) -> None:
        """Печатает список клиентов"""
        for client in self.clients:
            client.print_client()

    def print_rooms(self) -> None:
        """Печатает список комнат"""
        for room in self.rooms:
            room.print_room()

    def print_lodgers(self) -> None:
        """Печатает список постояльцев"""
        for lodger in self.lodgers:
            lodger.print_lodger(self)

"""Модуль содержит основной класс Hotel"""


import pickle
from client import Client
from lodger import Lodger
from room import Room


class Hotel:
    """В классе содержатся списки клиентов, постояльцев и комнат,
    а также основные методы программы"""
    def __init__(self, clients, lodgers, rooms):
        self.clients = clients
        self.lodgers = lodgers
        self.rooms = rooms

    @classmethod
    def empty(cls):
        """Создаёт пустой экземпляр класса"""
        return cls([], [], [])

    def save(self):
        """Запись данных в файл"""
        filename = input(
            'Введите имя файла для записи (по умолчанию database) >>> '
            ) or 'database'
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
            print(f"Информация успешно записана в {filename}!")

    def load(self):
        """Загрузка данных из файла"""
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

    def create_client(self):
        """Создаёт нового клиента через консоль"""
        client = Client.console_create(self)
        if not client:
            print('Не удалось зарегистрировать клиента!')
        else:
            self.clients.append(client)

    def create_room(self):
        """Создаёт новый номер через консоль"""
        room = Room.console_create(self)
        if not room:
            print('Не удалось создать комнату!')
        else:
            self.rooms.append(room)

    def create_lodger(self):
        """Создаёт нового постояльца через консоль"""
        lodger = Lodger.console_create(self)
        if not lodger:
            print('Не удалось заселить постояльца!')
        else:
            self.lodgers.append(lodger)

    def find_client(self, passport_details, absence=True):
        """Находит клиента по паспортным данным"""
        try:
            return list(filter(
                lambda c: c.passport_details == passport_details,
                self.clients
            ))[0]
        except IndexError:
            if absence:
                print('Клиент с такими данными не найден!')
            return None

    def find_room(self, number, absence=True):
        """Находит комнату по её номеру"""
        try:
            return list(filter(
                lambda r: r.number == number,
                self.rooms
            ))[0]
        except IndexError:
            if absence:
                print('Такая комната не найдена!')
            return None

    def find_lodger(self, passport_details, number, absence=True):
        """Находит постояльца по паспортным данным и номеру комнаты"""
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

    def delete_client(self):
        """Удаляет запись клиента"""
        passport_details = input('Введите паспортные данные >>> ')
        client = self.find_client(passport_details)
        if client in map(lambda l: l.client, self.lodgers):
            for lodger in filter(lambda l: l.client == client, self.lodgers):
                self.lodgers.pop(self.lodgers.index(lodger))
        if client:
            self.clients.pop(self.clients.index(client))
            print('Запись клиента удалена!')

    def delete_room(self):
        """Удаляет запись комнаты"""
        number = input('Введите номер комнаты >>> ')
        room = self.find_room(number)
        if room in map(lambda l: l.room, self.lodgers):
            for lodger in filter(lambda l: l.room == room, self.lodgers):
                self.lodgers.pop(self.lodgers.index(lodger))
        if room:
            self.rooms.pop(self.rooms.index(room))
            print('Запись комнаты удалена!')

    def delete_lodger(self):
        """Удаляет запись постояльца"""
        passport_details = input('Введите паспортные данные >>> ')
        number = input('Введите номер комнаты >>> ')
        lodger = self.find_lodger(passport_details, number)
        if lodger:
            self.lodgers.pop(self.lodgers.index(lodger))
            print('Запись постояльца удалена!')

    def evict_lodger(self):
        """Изменяет дату выселения постояльца"""
        passport_details = input('Введите паспортные данные >>> ')
        number = input('Введите номер комнаты >>> ')
        lodger = self.find_lodger(passport_details, number)
        if lodger:
            lodger.evict()

    def get_free_rooms(self, check_in_date, check_out_date):
        """Получить список пустых номеров"""
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

    def print_clients(self):
        """Выводит список клиентов"""
        for client in self.clients:
            client.print_client()

    def print_rooms(self):
        """Выводит список комнат"""
        for room in self.rooms:
            room.print_room()

    def print_lodgers(self):
        """Выводит список постояльцев"""
        for lodger in self.lodgers:
            lodger.print_lodger(self)

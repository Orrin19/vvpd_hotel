"""Модуль содержит класс Lodger"""


from datetime import datetime


class Lodger:
    """В классе содержится информация о постояльце:
    экземпляры клиента и номера, даты заселения и выселения, примечания.
    Возможно изменить дату выселения отдельным методом."""
    def __init__(self, client, room, check_in_date, check_out_date, notes=''):
        self.client = client
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.notes = notes

    def evict(self):
        """Изменить дату выселения постояльца"""
        try:
            check_out_date = datetime.strptime(
                input('Введите дату выселения (в формате д.м.г) >>> '),
                '%d.%m.%Y'
            )
        except ValueError:
            print('Неверно указана дата!')
            return None
        self.check_out_date = check_out_date
        print('Дата выселения изменена!')
        return None

    @classmethod
    def console_create(cls, hotel):
        """Создать постояльца через консоль"""
        passport_details = input('Введите паспортные данные >>> ')
        client = hotel.find_client(passport_details)
        if not client:
            return None

        try:
            check_in_date = datetime.strptime(
                input('Введите дату заселения (в формате д.м.г) >>> '),
                '%d.%m.%Y'
            )
        except ValueError:
            print('Неверно указана дата!')
            return None

        try:
            check_out_date = datetime.strptime(
                input('Введите дату выселения (в формате д.м.г) >>> '),
                '%d.%m.%Y'
            )
        except ValueError:
            print('Неверно указана дата!')
            return None

        if check_in_date > check_out_date:
            print('Мы не допускаем временных парадоксов!')
            return None

        free_rooms = hotel.get_free_rooms(check_in_date, check_out_date)
        if not free_rooms:
            return None

        number = input('Введите номер комнаты >>> ')
        if number not in free_rooms:
            print('Неподходящий номер!')
            return None
        room = hotel.find_room(number)
        if not room:
            return None

        notes = input('Добавьте примечания по постояльцу (опционально) >>> ')

        print('Постоялец успешно заселен!')
        return cls(client, room, check_in_date, check_out_date, notes)

    def print_lodger(self, hotel):
        """Выводит данные о постояльце"""
        print(
            '\nКлиент: ',
            hotel.find_client(self.client.passport_details).get_client()
        )
        print(
            'Комната: ',
            hotel.find_room(self.room.number).get_room()
        )
        print('Дата заселения:', self.check_in_date.date())
        print('Дата выселения:', self.check_out_date.date())
        if self.notes:
            print('Примечания:', self.notes)

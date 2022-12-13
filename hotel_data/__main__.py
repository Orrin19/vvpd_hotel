"""Модуль для демонстрации работы программы"""


import sys
from hotel import Hotel


def main():
    """
    Создаёт пустой объект гостиницы и реализует работу пользователя с меню
    """
    hotel = Hotel.empty()
    options = {
        '0': sys.exit,
        '1': hotel.create_client,
        '2': hotel.create_room,
        '3': hotel.create_lodger,
        '4': hotel.delete_client,
        '5': hotel.delete_room,
        '6': hotel.delete_lodger,
        '7': hotel.evict_lodger,
        '8': hotel.print_clients,
        '9': hotel.print_rooms,
        '10': hotel.print_lodgers,
        '11': hotel.load,
        '12': hotel.save
    }
    while True:
        print('\nВыберите нужное действие:')
        print('1.  Зарегистрировать нового клиента')
        print('2.  Создать новый гостиничный номер')
        print('3.  Заселить постояльца')
        print('4.  Удалить запись клиента')
        print('5.  Удалить запись номера')
        print('6.  Удалить запись постояльца')
        print('7.  Выселить постояльца')
        print('8.  Вывести информацию о клиентах')
        print('9.  Вывести информацию о номерах')
        print('10. Вывести информацию о постояльцах')
        print('11. Загрузить базу из файла')
        print('12. Сохранить базу в файл')
        print('0.  Завершить работу')
        try:
            request = input('Введите номер выбранного пункта >>> ')
            options[request]()
        except KeyError:
            print('Введите корректный номер действия!')


if __name__ == '__main__':
    main()

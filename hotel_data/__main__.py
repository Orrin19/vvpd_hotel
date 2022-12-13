"""Модуль для демонстрации работы программы"""


import sys
from hotel import Hotel


def main():
    """Реализует меню"""
    hotel = Hotel.empty()
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
        options = [
            sys.exit,
            hotel.create_client,
            hotel.create_room,
            hotel.create_lodger,
            hotel.delete_client,
            hotel.delete_room,
            hotel.delete_lodger,
            hotel.evict_lodger,
            hotel.print_clients,
            hotel.print_rooms,
            hotel.print_lodgers,
            hotel.load,
            hotel.save
        ]
        try:
            request = int(input('Введите номер выбранного пункта >>> '))
            if request < 0:
                request += 1000
            options[request]()
        except ValueError:
            print('Введите корректный номер действия!')
        except IndexError:
            print(f"Введите номер от 0 до {len(options) - 1}!")


if __name__ == '__main__':
    main()

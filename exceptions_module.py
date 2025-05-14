import os


class MyError(Exception):
    pass


def make_shop_code(code: str) -> int:
    '''Обрабатываем значение введенное в поле Начальный код точек
    Если значение текст или меньше 1, возбуждаем исключение
    Если значение - целое число больше 0, то возвращаем его'''

    try:
        code = int(code)
    except:
        raise MyError('Значение должно быть числом больше 0')
    else:
        if code < 1:
            raise MyError('Значение должно быть числом больше 0')
        else:
            return code


def correct_brand(brand_name):
    '''Проверяем, что папка с таким названием бренда - уникальна'''

    if os.path.isdir(f'{brand_name}'):
        raise MyError('Папка бренда с таким названием уже существует')
    else:
        return brand_name


def correct_stores_list(stores_list):
    '''Проверяем, что список торговых точек не пуст и в нем нет повторяющихся значений'''

    if len(stores_list) == 1 and stores_list[0] == '':
        raise MyError('Список не может быть пустым')
    else:
        if any([row == '' for row in stores_list]):
            raise MyError('В списке не может быть пустых строк')
        else:
            if len(stores_list) != len(set(stores_list)):
                raise MyError('В списке есть повторяющиеся значения')
            else:
                return stores_list


def correct_api(api_key):
    '''Проверяем, что поле не пустое'''

    if api_key == '':
        raise MyError('Поле не может быть пустым')
    else:
        return api_key

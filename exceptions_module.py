class MyError(Exception):
    pass


def make_shop_code(code:str) -> int:
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

import os
import shutil


def plagins_editor(shop_code:int, stores:list[str], key:str, brand:str, port:str, sms:bool):
    '''Основная функция, которая:
    1. Создает папку с названием бренда
    2. В этой папке создает папки с названиеми торговых точек
    3. В папку копирует плагин из папки "Донор"
    4. Запускает функцию config_changer, чтобы изменить конфиг
    '''

    def config_changer():
        '''Второстепенная функция, которая:
        1. Открывает файл конфига
        2. Находит нужные строки
        3. Вставляет пользовательские значения
        '''

        with open(f'{brand}/{t_name}/Resto.Front.Api.CloudLoyalty.V6.1.0.84/Resto.Front.Api.CloudLoyalty.dll.config',
                  'r', encoding='utf-8') as infile:
            a = infile.readlines()
            res_list = []

            for i in a:
                if 'X-Processing-Key' in i:
                    b = i.split('X-Processing-Key')
                    i = f'{key}'.join(b)
                if 'Код торговой точки' in i:
                    b = i.split('Код торговой точки')
                    i = f'{shop_code}'.join(b)
                if 'Название торговой точки' in i:
                    b = i.split('Название торговой точки')
                    i = f'{t_name}'.join(b)
                if 'send_sms' in i:
                    row_index = a.index(i) + 1
                    b = a[row_index].split('False')
                    a[row_index] = f'{sms}'.join(b)
                if 'server_port' in i:
                    if port != '':
                        row_index = a.index(i) + 1
                        b = a[row_index].split('0')
                        a[row_index] = f'{port}'.join(b)

                res_list.append(i)

            with open(
                    f'{brand}/{t_name}/Resto.Front.Api.CloudLoyalty.V6.1.0.84/Resto.Front.Api.CloudLoyalty.dll.config',
                    'w', encoding='utf-8') as infile:
                infile.writelines(res_list)

    os.mkdir(brand)
    stores_codes_list = []

    for t_name in stores:
        shutil.copytree('Донор', f'{brand}/{t_name}')
        config_changer()
        stores_codes_list.append((t_name, shop_code))
        shop_code += 1

    with open(f'{brand}/Названия и коды точек.txt', 'w', encoding='utf-8') as code_file:
        max_len = len(max(stores_codes_list, key=lambda x: len(x[0]))[0])
        column_1 = 'Название точки'

        if max_len < len(column_1):
            max_len = len(column_1)

        column_2 = 'Код точки'
        code_file.write(f'{column_1}:{' ' * (max_len - len(column_1) + 1)}  {column_2}:\n')
        for row in stores_codes_list:
            code_file.write(f'{row[0]}{' ' * (max_len - len(row[0]) + 1)} | {row[1]}\n')





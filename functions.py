import os
import shutil


def plagins_editor(shop_code:int, stores:list[str], key:str, brand:str, port:str, sms:bool):
    '''Основная функция, которая:
    1. Создает папку с названием бренда
    2. В этой папке создает папки с названиеми торговых точек
    3. В папку копирует плагин из папки "Донор"
    4. Запускает функцию config_changer, чтобы изменить конфиг
    '''

    os.mkdir(brand)
    for t_name in stores:
        shutil.copytree('Донор', f'{brand}/{t_name}')
        config_changer(brand, t_name, key, shop_code, port, sms)
        shop_code += 1



def config_changer(brand:str, t_name:str, key:str, shop_code:int, port:str, sms:bool):
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

        with open(f'{brand}/{t_name}/Resto.Front.Api.CloudLoyalty.V6.1.0.84/Resto.Front.Api.CloudLoyalty.dll.config',
                  'w', encoding='utf-8') as infile:
            infile.writelines(res_list)



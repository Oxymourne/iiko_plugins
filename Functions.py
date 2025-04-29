import os
import shutil


def plagins_editor(data, brand, key):
    '''Функция создает папку с названием бренда.
    Далее проходит по списку ТТ, создает в этой папке папку с названием ТТ
    и перемещает в нее исходный плагин'''

    os.mkdir(brand)
    for t_name in data:
        shutil.copytree('Донор', f'{brand}/{t_name}')
        config_changer(brand, t_name, key)


def config_changer(brand, t_name, key):
    '''Функция редактирует файл конфигурации плагина, подставляя нужные значения'''

    global shop_code

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
                shop_code += 1
            if 'Название торговой точки' in i:
                b = i.split('Название торговой точки')
                i = f'{t_name}'.join(b)
            res_list.append(i)

        with open(f'{brand}/{t_name}/Resto.Front.Api.CloudLoyalty.V6.1.0.84/Resto.Front.Api.CloudLoyalty.dll.config',
                  'w', encoding='utf-8') as infile:
            infile.writelines(res_list)


magazins_list = []
brand_name = input('Введи название бренда: ')
api_key = '11112222233333'
shop_code = 1

plagins_editor(magazins_list, brand_name, api_key)

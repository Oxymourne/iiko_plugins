from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from datetime import datetime
import os
import shutil


class MyError(Exception):
    pass


def plagins_editor(shop_code):
    '''Функция создает папку с названием бренда.
    Далее проходит по списку ТТ, создает в этой папке папку с названием ТТ
    и перемещает в нее исходный плагин'''

    stores = text_edit.toPlainText().strip().split('\n')
    stores = list(map(lambda x: x.strip(), stores))

    key = line_api.text().strip()
    brand = line_brand.text().strip()
    port = line_port.text().strip()

    os.mkdir(brand)
    for t_name in stores:
        shutil.copytree('Донор', f'{brand}/{t_name}')
        config_changer(brand, t_name, key, shop_code, port)
        shop_code += 1


def config_changer(brand, t_name, key, shop_code, port):
    '''Функция редактирует файл конфигурации плагина, подставляя нужные значения'''

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
                a[row_index] = f'{check_sms.isChecked()}'.join(b)
            if 'server_port' in i:
                if port != '':
                    row_index = a.index(i) + 1
                    b = a[row_index].split('0')
                    a[row_index] = f'{port}'.join(b)

            res_list.append(i)

        with open(f'{brand}/{t_name}/Resto.Front.Api.CloudLoyalty.V6.1.0.84/Resto.Front.Api.CloudLoyalty.dll.config',
                  'w', encoding='utf-8') as infile:
            infile.writelines(res_list)


def make_shop_code() -> int:
    '''Обрабатываем значение введенное в поле Начальный код точек
    Если значение текст или меньше 1, возбуждаем исключение
    Если значение - целое число больше 0, то возвращаем его'''

    try:
        code = int(line_shopcode.text())
    except:
        raise MyError('Значение должно быть числом больше 0')
    else:
        if code < 1:
            raise MyError('Значение должно быть числом больше 0')
        else:
            return code


def start_func():
    current_date = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
    log = []
    with open('logs.txt', 'a', encoding='utf-8') as log_outfile:
        try:
            try:
                text_errors.clear()
                shop_code = make_shop_code()
            except MyError as e:
                message_error = f'Код точки: {e}'
                text_errors.append(message_error)
            else:
                plagins_editor(shop_code)
        except Exception as e:
            log.append(f'{current_date}\n')
            log.append(f'Тип ошибки: {type(e).__name__}\n')
            log.append(f'Текст ошибки: {e}\n')
            log.append(f'{'='*20}\n')
            log_outfile.writelines(log)
        else:
            log.append(f'{current_date}\n')
            log.append('Плагины успешно созданы\n')
            log.append(f'{'=' * 20}\n')
            log_outfile.writelines(log)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = QtWidgets.QMainWindow()
    window.setWindowTitle("MaKo v1.1")
    window.setFixedSize(800, 600)
    window.setStyleSheet("background-color: #4AD8FB;")

    central_widget = QtWidgets.QWidget()
    window.setCentralWidget(central_widget)

    '''=== Создаем поле для ввода текста ==='''

    text_edit = QtWidgets.QTextEdit()

    text_edit.setStyleSheet("""
         QTextEdit {
            color: #000000;
             background-color: #FFFFFF;
             font-size: 14px;
             border: 2px solid #7f8c8d;
             border-radius: 10px;
         }
         QTextEdit::cursor {
            background-color: #000000;
            width: 2px;
         }
     """)

    text_errors = QtWidgets.QTextEdit()
    text_errors.setReadOnly(True)
    text_errors.setStyleSheet("""
         QTextEdit {
            color: #000000;
             background-color: #FFFFFF;
             font-size: 14px;
             border: 2px solid #7f8c8d;
             border-radius: 10px;
         }
         QTextEdit::cursor {
            background-color: #000000;
            width: 2px;
         }
     """)

    '''=== Создаем лейблы ==='''

    label_text = QtWidgets.QLabel('Список торговых точек')

    label_api = QtWidgets.QLabel('API ключ')
    label_api.setStyleSheet("margin: 10px;")

    label_brand = QtWidgets.QLabel('Название бренда')
    label_brand.setStyleSheet("margin: 10px;")

    label_sms = QtWidgets.QLabel('Списание по СМС')
    label_sms.setStyleSheet("margin: 10px;")

    label_shopcode = QtWidgets.QLabel('Начальный код точек')
    label_shopcode.setStyleSheet("margin: 10px;")

    label_port = QtWidgets.QLabel('Порт для Waiter')
    label_port.setStyleSheet("margin: 10px;")

    label_error = QtWidgets.QLabel('==ОШИБКИ==')

    '''=== Создаем строки ввода ==='''

    line_api = QtWidgets.QLineEdit()
    line_api.setStyleSheet("""
             QLineEdit {
                color: #000000;
                 background-color: #FFFFFF;
                 font-size: 14px;
                 border: 2px solid #7f8c8d;
                 border-radius: 5px;
             }
             QLineEdit::cursor {
                background-color: #000000;
                width: 2px;
             }
         """)

    line_brand = QtWidgets.QLineEdit()
    line_brand.setStyleSheet("""
                 QLineEdit {
                    color: #000000;
                     background-color: #FFFFFF;
                     font-size: 14px;
                     border: 2px solid #7f8c8d;
                     border-radius: 5px;
                 }
                 QLineEdit::cursor {
                    background-color: #000000;
                    width: 2px;
                 }
             """)

    line_shopcode = QtWidgets.QLineEdit()
    line_shopcode.setFixedWidth(35)
    line_shopcode.setStyleSheet("""
                 QLineEdit {
                    color: #000000;
                     background-color: #FFFFFF;
                     font-size: 14px;
                     border: 2px solid #7f8c8d;
                     border-radius: 5px;
                 }
                 QLineEdit::cursor {
                    background-color: #000000;
                    width: 2px;
                 }
             """)

    line_port = QtWidgets.QLineEdit()
    line_port.setFixedWidth(100)
    line_port.setStyleSheet("""
                 QLineEdit {
                    color: #000000;
                     background-color: #FFFFFF;
                     font-size: 14px;
                     border: 2px solid #7f8c8d;
                     border-radius: 5px;
                 }
                 QLineEdit::cursor {
                    background-color: #000000;
                    width: 2px;
                 }
             """)

    '''=== Создаем чек-бокс ==='''

    check_sms = QtWidgets.QCheckBox()

    '''=== Создаем кнопку ==='''

    button1 = QtWidgets.QPushButton('Сделать плагины')
    button1.setStyleSheet("""
             QPushButton {
                color: #000000;
                background-color: #FFFFFF;
                font-size: 14px;
             }
         """)
    button1.clicked.connect(start_func)

    '''=== Наполнение контейнера ==='''

    grid = QtWidgets.QGridLayout()
    grid.addWidget(label_text, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_api, 0, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_brand, 1, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_sms, 4, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_shopcode, 3, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_port, 2, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_error, 5, 1, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
    grid.addWidget(text_edit, 1, 0, 6, 1)
    grid.addWidget(text_errors, 6, 1, 1, 2)
    grid.addWidget(line_api, 0, 2)
    grid.addWidget(line_brand, 1, 2)
    grid.addWidget(line_shopcode, 3, 2)
    grid.addWidget(line_port, 2, 2)
    grid.addWidget(check_sms, 4, 2)
    grid.addWidget(button1, 7, 2)

    central_widget.setLayout(grid)

    window.show()
    app.exec()

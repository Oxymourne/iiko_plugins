from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
import os
import shutil


def plagins_editor(shop_code):
    '''Функция создает папку с названием бренда.
    Далее проходит по списку ТТ, создает в этой папке папку с названием ТТ
    и перемещает в нее исходный плагин'''

    stores = text_edit.toPlainText().split('\n')
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


def make_shop_code():
    if line_shopcode.text() != '' and int(line_shopcode.text()) > 1:
        code = int(line_shopcode.text())
    else:
        code = 1
    return code


def start_func():
    shop_code = make_shop_code()
    plagins_editor(shop_code)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = QtWidgets.QMainWindow()
    window.setWindowTitle("MAXMA plugins for IIKO")
    window.setFixedSize(800, 600)
    window.setStyleSheet("background-color: #4AD8FB;")

    central_widget = QtWidgets.QWidget()
    window.setCentralWidget(central_widget)

    '''=== Создаем поле для ввода текста ==='''

    text_edit = QtWidgets.QTextEdit()
    text_edit.setFixedSize(330, 490)

    text_edit.setStyleSheet("""
         QTextEdit {
            color: #000000;  /* Цвет текста */
             background-color: #FFFFFF;  /* Цвет фона */
             font-size: 14px;
             border: 2px solid #7f8c8d;  /* Рамка (опционально) */
             border-radius: 10px;
         }
         QTextEdit::cursor {
            background-color: #000000;  /* Цвет курсора */
            width: 2px;  /* Толщина курсора */
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

    '''=== Создаем строки ввода ==='''

    line_api = QtWidgets.QLineEdit()
    line_api.setStyleSheet("""
             QLineEdit {
                color: #000000;  /* Цвет текста */
                 background-color: #FFFFFF;  /* Цвет фона */
                 font-size: 14px;
                 border: 2px solid #7f8c8d;  /* Рамка (опционально) */
                 border-radius: 5px;
             }
             QLineEdit::cursor {
                background-color: #000000;  /* Цвет курсора */
                width: 2px;  /* Толщина курсора */
             }
         """)

    line_brand = QtWidgets.QLineEdit()
    line_brand.setStyleSheet("""
                 QLineEdit {
                    color: #000000;  /* Цвет текста */
                     background-color: #FFFFFF;  /* Цвет фона */
                     font-size: 14px;
                     border: 2px solid #7f8c8d;  /* Рамка (опционально) */
                     border-radius: 5px;
                 }
                 QLineEdit::cursor {
                    background-color: #000000;  /* Цвет курсора */
                    width: 2px;  /* Толщина курсора */
                 }
             """)

    line_shopcode = QtWidgets.QLineEdit()
    line_shopcode.setFixedWidth(35)
    line_shopcode.setStyleSheet("""
                 QLineEdit {
                    color: #000000;  /* Цвет текста */
                     background-color: #FFFFFF;  /* Цвет фона */
                     font-size: 14px;
                     border: 2px solid #7f8c8d;  /* Рамка (опционально) */
                     border-radius: 5px;
                 }
                 QLineEdit::cursor {
                    background-color: #000000;  /* Цвет курсора */
                    width: 2px;  /* Толщина курсора */
                 }
             """)

    line_port = QtWidgets.QLineEdit()
    line_port.setFixedWidth(100)
    line_port.setStyleSheet("""
                 QLineEdit {
                    color: #000000;  /* Цвет текста */
                     background-color: #FFFFFF;  /* Цвет фона */
                     font-size: 14px;
                     border: 2px solid #7f8c8d;  /* Рамка (опционально) */
                     border-radius: 5px;
                 }
                 QLineEdit::cursor {
                    background-color: #000000;  /* Цвет курсора */
                    width: 2px;  /* Толщина курсора */
                 }
             """)

    '''=== Создаем чек-бокс ==='''

    check_sms = QtWidgets.QCheckBox()

    '''=== Создаем кнопку ==='''

    button1 = QtWidgets.QPushButton('Сделать плагины')
    button1.setStyleSheet("""
             QPushButton {
                color: #000000;  /* Цвет текста */
                background-color: #FFFFFF;  /* Цвет фона */
                font-size: 14px;
             }
         """)
    button1.clicked.connect(start_func)

    '''=== Наполнение контейнера ==='''

    grid = QtWidgets.QGridLayout()
    grid.addWidget(label_text, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(text_edit, 1, 0, 5, 1)
    grid.addWidget(label_api, 0, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_brand, 1, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_sms, 4, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_shopcode, 3, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_port, 2, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(line_api, 0, 2)
    grid.addWidget(line_brand, 1, 2)
    grid.addWidget(line_shopcode, 3, 2)
    grid.addWidget(line_port, 2, 2)
    grid.addWidget(check_sms, 4, 2)
    grid.addWidget(button1, 6, 2)

    central_widget.setLayout(grid)

    window.show()
    app.exec()

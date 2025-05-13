from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from datetime import datetime
from functions import *
from exceptions_module import *



def values_from_fields() -> tuple[list, str, str, int, bool]:
    '''В этой функции, мы получаем информацию со всех полей.
    Возвращаем кортеж с полученными значениями'''

    user_stores = text_edit.toPlainText().strip().split('\n')
    user_stores = list(map(lambda x: x.strip(), user_stores))

    user_api_key = line_api.text().strip()
    user_brand_name = line_brand.text().strip()
    user_port = line_port.text().strip()
    sms = check_sms.isChecked()

    return user_stores, user_api_key, user_brand_name, user_port, sms


def start_func():
    '''Стартовая функция, в которой мы:
    1. Проверяем, что значение в поле "Стартовый код" введено корректно
    2. Запускаем основной алгоритм plagins_editor
    3. Формируем логи по итогу работы
    '''
    current_date = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
    log = []
    with open('logs.txt', 'a', encoding='utf-8') as log_outfile:
        try:
            try:
                text_errors.clear()
                shop_code = make_shop_code(line_shopcode.text())
            except MyError as e:
                message_error = f'Код точки: {e}'
                text_errors.append(message_error)
            else:
                plagins_editor(shop_code, *values_from_fields())
        except Exception as e:
            log.append(f'{current_date}\n')
            log.append(f'Тип ошибки: {type(e).__name__}\n')
            log.append(f'Текст ошибки: {e}\n')
            log.append(f'{'=' * 20}\n')
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
    window.setStyleSheet("background-color: #F4F7F9;")

    central_widget = QtWidgets.QWidget()
    window.setCentralWidget(central_widget)

    '''=== Создаем поле для ввода текста ==='''

    text_edit = QtWidgets.QTextEdit()

    text_edit.setStyleSheet("""
         QTextEdit {
            color: #1F2937;
             background-color: #FFFFFF;
             font-size: 14px;
             border: 2px solid #D1D9E6;
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
             border: 2px solid #D1D9E6;
             border-radius: 10px;
         }
         QTextEdit::cursor {
            background-color: #000000;
            width: 2px;
         }
     """)

    '''=== Создаем лейблы ==='''

    label_text = QtWidgets.QLabel('Список торговых точек')
    label_text.setStyleSheet("""
        color: #2E3A59;
        font-size: 14px;
        font-weight: bold;
        margin: 10px;
    """)

    label_api = QtWidgets.QLabel('API ключ')
    label_api.setStyleSheet("""
        color: #2E3A59;
        font-size: 14px;
        font-weight: bold;
        margin: 10px;
    """)

    label_brand = QtWidgets.QLabel('Название бренда')
    label_brand.setStyleSheet("""
        color: #2E3A59;
        font-size: 14px;
        font-weight: bold;
        margin: 10px;
    """)

    label_sms = QtWidgets.QLabel('Списание по СМС')
    label_sms.setStyleSheet("""
        color: #2E3A59;
        font-size: 14px;
        font-weight: bold;
        margin: 10px;
    """)

    label_shopcode = QtWidgets.QLabel('Начальный код точек')
    label_shopcode.setStyleSheet("""
        color: #2E3A59;
        font-size: 14px;
        font-weight: bold;
        margin: 10px;
    """)

    label_port = QtWidgets.QLabel('Порт для Waiter')
    label_port.setStyleSheet("""
        color: #2E3A59;
        font-size: 14px;
        font-weight: bold;
        margin: 10px;
    """)

    label_error = QtWidgets.QLabel('==ОШИБКИ==')
    label_error.setStyleSheet("""
        color: #2E3A59;
        font-size: 14px;
        font-weight: bold;
        margin: 10px;
    """)

    '''=== Создаем строки ввода ==='''

    line_api = QtWidgets.QLineEdit()
    line_api.setStyleSheet("""
             QLineEdit {
                color: #000000;
                 background-color: #FFFFFF;
                 font-size: 14px;
                 border: 1px solid #7f8c8d;
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
                     border: 1px solid #7f8c8d;
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
                     border: 1px solid #7f8c8d;
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
                     border: 1px solid #7f8c8d;
                     border-radius: 5px;
                 }
                 QLineEdit::cursor {
                    background-color: #000000;
                    width: 2px;
                 }
             """)

    '''=== Создаем чек-бокс ==='''

    check_sms = QtWidgets.QCheckBox()
    check_sms.setStyleSheet("""
                QCheckBox::indicator {
                    width: 16px;
                    height: 16px;
                    background-color: #F0F2F5;
                    border: 1px solid #D1D9E6;
                    border-radius: 3px;
                }
            
                QCheckBox::indicator:checked {
                    background-color: #E0E7FF;
                    border: 1px solid #4F46E5;
                }
            """)


    '''=== Создаем кнопку ==='''

    button1 = QtWidgets.QPushButton('Сделать плагины')
    button1.setFixedHeight(40)
    button1.setStyleSheet("""
             QPushButton {
                color: #FFFFFF;
                background-color: #4F46E5;
                border: none;
                border-radius: 6px;
                font-size: 12px;
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

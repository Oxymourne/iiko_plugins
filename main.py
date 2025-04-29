from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

import sys

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

    '''=== Наполнение контейнера ==='''

    grid = QtWidgets.QGridLayout()
    grid.addWidget(label_text, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(text_edit, 1, 0, 4, 1)
    grid.addWidget(label_api, 0, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_brand, 1, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(label_sms, 2, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
    grid.addWidget(line_api, 0, 2)
    grid.addWidget(line_brand, 1, 2)
    grid.addWidget(check_sms, 2, 2)
    grid.addWidget(button1, 5, 2)

    central_widget.setLayout(grid)

    window.show()
    app.exec()

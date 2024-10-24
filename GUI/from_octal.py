from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget
from GUI.style import CONST_WINDOW

class FromOctal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше восьмиричное число для перевода")
        entering_a_number = QLineEdit()
        binary = QPushButton(text="из восьмиричного в двоичное")
        decimal = QPushButton(text="из восьмиричного в десятичное")
        hexadecimal = QPushButton(text="из восьмиричного в шестнадцатеричное")
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(entering_a_number)
        control_UI.addWidget(binary)
        control_UI.addWidget(decimal)
        control_UI.addWidget(hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
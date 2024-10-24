from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget
from GUI.style import CONST_WINDOW

class FromDecimal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше десятичное число для перевода")
        entering_a_number = QLineEdit()
        binary = QPushButton(text="из десятичного в двоичное")
        octal = QPushButton(text="из десятичного в восьмиричное")
        hexadecimal = QPushButton(text="из десятичного в шестнадцатеричное")
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(entering_a_number)
        control_UI.addWidget(binary)
        control_UI.addWidget(octal)
        control_UI.addWidget(hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
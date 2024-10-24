from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget
from GUI.style import CONST_WINDOW

class FromHexadecimal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше шестнадцатеричное число для перевода")
        entering_a_number = QLineEdit()
        binary = QPushButton(text="из шестнадцатеричного в двоичное")
        octal = QPushButton(text="из шестнадцатеричного в восьмиричное")
        decimal = QPushButton(text="из шестнадцатеричного в десятичное")
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(entering_a_number)
        control_UI.addWidget(binary)
        control_UI.addWidget(octal)
        control_UI.addWidget(decimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
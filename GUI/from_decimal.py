from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget, QMessageBox
from GUI.style import CONST_WINDOW
from CallingFunctions.call_decimal import to_binary, to_octal, to_hex

class FromDecimal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_WINDOW)
        
        self.result = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше десятичное число для перевода")
        self.entering_a_number = QLineEdit()
        
        binary = QPushButton(text="Из десятичного в двоичное")
        binary.clicked.connect(self.to_binary)
        
        octal = QPushButton(text="Из десятичного в восьмиричное")
        octal.clicked.connect(self.to_octal)
        
        hexadecimal = QPushButton(text="Из десятичного в шестнадцатеричное")
        hexadecimal.clicked.connect(self.to_hexadecimal)
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(self.entering_a_number)
        control_UI.addWidget(binary)
        control_UI.addWidget(octal)
        control_UI.addWidget(hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def to_binary(self):
        temp = self.entering_a_number.text()
        call = to_binary(temp)
        
        self.result = QMessageBox()
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
        
    def to_octal(self):
        temp = self.entering_a_number.text()
        call = to_octal(temp)
        
        self.result = QMessageBox()
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
        
    def to_hexadecimal(self):
        temp = self.entering_a_number.text()
        call = to_hex(temp)
        
        self.result = QMessageBox()
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
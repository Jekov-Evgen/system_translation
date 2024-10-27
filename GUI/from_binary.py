from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget, QMessageBox
from GUI.style import CONST_WINDOW
from CallingFunctions.call_binary import to_octal, to_decimal, to_hex

class FromBinary(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_WINDOW)
        
        self.result = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше бинарное число для перевода")
        self.entering_a_number = QLineEdit()
        
        octal = QPushButton(text="Из двоичного в восьмиричное")
        octal.clicked.connect(self.to_octal)
        
        decimal = QPushButton(text="Из двоичного в десятичное")
        decimal.clicked.connect(self.to_decimal)
        
        hexadecimal = QPushButton(text="Из двоичного в шестнадцатеричное")
        hexadecimal.clicked.connect(self.to_hexadecimal)
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(self.entering_a_number)
        control_UI.addWidget(octal)
        control_UI.addWidget(decimal)
        control_UI.addWidget(hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def to_octal(self):
        temp = self.entering_a_number.text()
        call = to_octal(temp)
        
        self.result = QMessageBox()
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
        
    def to_decimal(self):
        temp = self.entering_a_number.text()
        call = to_decimal(temp)
        
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
        
        
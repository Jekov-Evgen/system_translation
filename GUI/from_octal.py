from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget, QMessageBox
from PyQt6.QtGui import QIcon
from GUI.style import CONST_WINDOW, CONST_RESULT_WINDOW
from CallingFunctions.call_octal import to_binary, to_decimal, to_hex

class FromOctal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_WINDOW)
        img = 'Image/icon.png'
        self.setWindowIcon(QIcon(img))
        
        self.result = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше восьмиричное число для перевода")
        self.entering_a_number = QLineEdit()
        binary = QPushButton(text="Из восьмиричного в двоичное")
        binary.clicked.connect(self.to_binary)
        
        decimal = QPushButton(text="Из восьмиричного в десятичное")
        decimal.clicked.connect(self.to_decimal)
        
        hexadecimal = QPushButton(text="Из восьмиричного в шестнадцатеричное")
        hexadecimal.clicked.connect(self.to_hexadecimal)
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(self.entering_a_number)
        control_UI.addWidget(binary)
        control_UI.addWidget(decimal)
        control_UI.addWidget(hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def to_binary(self):
        temp = self.entering_a_number.text()
        call = to_binary(temp)
        
        self.result = QMessageBox()
        
        self.result.setStyleSheet(CONST_RESULT_WINDOW)
        img = 'Image/icon.png'
        self.result.setWindowIcon(QIcon(img))
        
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
    
    def to_decimal(self):
        temp = self.entering_a_number.text()
        call = to_decimal(temp)
        
        self.result = QMessageBox()
        
        self.result.setStyleSheet(CONST_RESULT_WINDOW)
        img = 'Image/icon.png'
        self.result.setWindowIcon(QIcon(img))
        
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
    
    def to_hexadecimal(self):
        temp = self.entering_a_number.text()
        call = to_hex(temp)
        
        self.result = QMessageBox()
        
        self.result.setStyleSheet(CONST_RESULT_WINDOW)
        img = 'Image/icon.png'
        self.result.setWindowIcon(QIcon(img))
        
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
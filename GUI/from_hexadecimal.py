from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget, QMessageBox
from GUI.style import CONST_WINDOW, CONST_RESULT_WINDOW
from CallingFunctions.call_hex import to_binary, to_octal, to_decimal

class FromHexadecimal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_WINDOW)
        
        self.result = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше шестнадцатеричное число для перевода")
        self.entering_a_number = QLineEdit()
        binary = QPushButton(text="Из шестнадцатеричного в двоичное")
        binary.clicked.connect(self.to_binary)
        
        octal = QPushButton(text="Из шестнадцатеричного в восьмиричное")
        octal.clicked.connect(self.to_octal)
        
        decimal = QPushButton(text="Из шестнадцатеричного в десятичное")
        decimal.clicked.connect(self.to_decimal)
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(self.entering_a_number)
        control_UI.addWidget(binary)
        control_UI.addWidget(octal)
        control_UI.addWidget(decimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def to_binary(self):
        temp = self.entering_a_number.text()
        call = to_binary(temp)
        
        self.result = QMessageBox()
        self.result.setStyleSheet(CONST_RESULT_WINDOW)
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
        
    def to_octal(self):
        temp = self.entering_a_number.text()
        call = to_octal(temp)
        
        self.result = QMessageBox()
        self.result.setStyleSheet(CONST_RESULT_WINDOW)
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
        
    def to_decimal(self):
        temp = self.entering_a_number.text()
        call = to_decimal(temp)
        
        self.result = QMessageBox()
        self.result.setStyleSheet(CONST_RESULT_WINDOW)
        self.result.setWindowTitle("Окно результата")
        self.result.setText(call)
        
        self.result.show()
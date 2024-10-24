from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget, QMessageBox
from GUI.style import CONST_WINDOW

class FromOctal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_WINDOW)
        
        self.result = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше восьмиричное число для перевода")
        entering_a_number = QLineEdit()
        binary = QPushButton(text="из восьмиричного в двоичное")
        
        binary.clicked.connect(self.to_binary)
        
        decimal = QPushButton(text="из восьмиричного в десятичное")
        decimal.clicked.connect(self.to_decimal)
        
        hexadecimal = QPushButton(text="из восьмиричного в шестнадцатеричное")
        hexadecimal.clicked.connect(self.to_hexadecimal)
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(entering_a_number)
        control_UI.addWidget(binary)
        control_UI.addWidget(decimal)
        control_UI.addWidget(hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def to_binary(self):
        self.result = QMessageBox()
        self.result.setWindowTitle("Окно результата")
        self.result.setText("Результат")
        
        self.result.show()
    
    def to_decimal(self):
        self.result = QMessageBox()
        self.result.setWindowTitle("Окно результата")
        self.result.setText("Результат")
        
        self.result.show()
    
    def to_hexadecimal(self):
        self.result = QMessageBox()
        self.result.setWindowTitle("Окно результата")
        self.result.setText("Результат")
        
        self.result.show()
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QWidget
from PyQt6.QtGui import QIcon
from GUI.style import CONST_MAIN_WINDOW
from GUI.from_binary import FromBinary
from GUI.from_decimal import FromDecimal
from GUI.from_octal import FromOctal
from GUI.from_hexadecimal import FromHexadecimal

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        img = 'Image/icon.png'
        self.setWindowIcon(QIcon(img))
        
        self.from_bin = None
        self.from_dec = None
        self.from_oct = None
        self.from_hex = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Выберите какой перевод вам нужен")
        
        from_binary = QPushButton(text="Из двоичной")
        from_binary.clicked.connect(self.binary_button)
        
        from_decimal = QPushButton(text="Из десятичной")
        from_decimal.clicked.connect(self.decimal_button)
        
        from_octal = QPushButton(text="Из восьмеричной")
        from_octal.clicked.connect(self.octal_button)
        
        from_hexadecimal = QPushButton(text="Из шестнадцатеричной")
        from_hexadecimal.clicked.connect(self.hexadecimal_button)
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(from_binary)
        control_UI.addWidget(from_octal)
        control_UI.addWidget(from_decimal)
        control_UI.addWidget(from_hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def binary_button(self):
        self.from_bin = FromBinary()
        
    def decimal_button(self):
        self.from_dec = FromDecimal()
        
    def octal_button(self):
        self.from_oct = FromOctal()
        
    def hexadecimal_button(self):
        self.from_hex = FromHexadecimal()
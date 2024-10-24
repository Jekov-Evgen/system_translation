from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget


class FromBinary(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ваше бинарное число для перевода")
        entering_a_number = QLineEdit()
        octal = QPushButton(text="из двоичного в восьмиричное")
        decimal = QPushButton(text="из двоичного в десятичное")
        hexadecimal = QPushButton(text="из двоичного в шестнадцатеричное")
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(entering_a_number)
        control_UI.addWidget(octal)
        control_UI.addWidget(decimal)
        control_UI.addWidget(hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
        
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QLineEdit, QWidget
from GUI.style import CONST_MAIN_WINDOW

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 450)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Выберите какой перевод вам нужен")
        from_binary = QPushButton(text="Из двоичной")
        from_decimal = QPushButton(text="Из десятичной")
        from_octal = QPushButton(text="Из восьмеричной")
        from_hexadecimal = QPushButton(text="Из шестнадцатеричной")
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(from_binary)
        control_UI.addWidget(from_octal)
        control_UI.addWidget(from_decimal)
        control_UI.addWidget(from_hexadecimal)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
from GUI.from_hexadecimal import FromHexadecimal
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    
    start = FromHexadecimal()
    
    app.exec()
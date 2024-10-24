CONST_WINDOW = """
            QWidget {
                background-color: #2E2E2E;
                color: #FFFFFF;
                font-family: Arial;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4E4E4E;
                color: #FFFFFF;
                border: 1px solid #FFFFFF;
                border-radius: 5px;
                padding: 10px;
                qproperty-alignment: 'AlignCenter';
            }
            QPushButton:hover {
                background-color: #6E6E6E;
            }
            QPushButton:pressed {
                background-color: #5A5A5A;
            }
            QLineEdit {
                background-color: #3E3E3E;
                color: #FFFFFF;
                border: 1px solid #FFFFFF;
                border-radius: 5px;
                padding: 5px;
            }
            QLabel {
                font-size: 16px;
                margin-bottom: 10px;
                qproperty-alignment: 'AlignCenter';
            }
        """
        
CONST_MAIN_WINDOW = """
            QWidget {
                background-color: #2B2B2B;
                color: #E0E0E0;
                font-family: 'Arial';
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #D3D3D3;
                padding: 15px;
                margin-bottom: 20px;
                qproperty-alignment: 'AlignCenter';
            }
            QPushButton {
                background-color: #3C3C3C;
                color: #E0E0E0;
                font-size: 16px;
                border: 1px solid #5C5C5C;
                border-radius: 8px;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #4C4C4C;
            }
            QPushButton:pressed {
                background-color: #5C5C5C;
            }
            QVBoxLayout {
                alignment: 'AlignCenter';
            }
        """
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton

class MultipleSum_Application(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Multiple Sum Application")
        self.setGeometry(100, 100, 400, 300)

        app_layout = QVBoxLayout()

        # Labels and Textboxes
        range_label = QLabel('Range:')
        self.range_entry = QLineEdit()
        rangeExample_label = QLabel("Example: 'Lower limit : Upper limit' -> 1 : 10 ")
        app_layout.addWidget(range_label)
        app_layout.addWidget(self.range_entry)
        app_layout.addWidget(rangeExample_label)

        factor_label = QLabel('Factor:')
        self.factor_entry = QLineEdit()
        factorExample_label = QLabel("Example: 'factor[1], factor[2], ...' -> 2, 4, 5")
        app_layout.addWidget(factor_label)
        app_layout.addWidget(self.factor_entry)
        app_layout.addWidget(factorExample_label)

        # Display Box (TextEdit)
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)  # Make it read-only
        app_layout.addWidget(self.output_display)

        # Button
        display_button = QPushButton('Calculate')
        display_button.clicked.connect(self.display_input)  # Connect to the display function
        app_layout.addWidget(display_button)

        #Button
        clear_btn = QPushButton('Clear')
        clear_btn.clicked.connect(self.clear_input)
        app_layout.addWidget(clear_btn)

        self.setLayout(app_layout)

    def display_input(self):
        range = self.range_entry.text()
        factor = self.factor_entry.text()

        output_text = f"Range: {range}\nfactor: {factor}"
        self.output_display.setPlainText(output_text)

    def clear_input(self):
        self.range_entry.clear()
        self.factor_entry.clear()
        self.output_display.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultipleSum_Application()
    window.show()
    sys.exit(app.exec_())

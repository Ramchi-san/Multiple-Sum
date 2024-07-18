import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton

class MultipleSum_Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt Sample GUI')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Labels and Textboxes
        name_label = QLabel('Name:')
        self.name_edit = QLineEdit()
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)

        age_label = QLabel('Age:')
        self.age_edit = QLineEdit()
        layout.addWidget(age_label)
        layout.addWidget(self.age_edit)

        # Display Box (TextEdit)
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)  # Make it read-only
        layout.addWidget(self.output_display)

        # Button
        display_button = QPushButton('Display')
        display_button.clicked.connect(self.display_input)  # Connect to the display function
        layout.addWidget(display_button)

        self.setLayout(layout)

    def display_input(self):
        name = self.name_edit.text()
        age = self.age_edit.text()

        output_text = f"Name: {name}\nAge: {age}"
        self.output_display.setPlainText(output_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SampleGUI()
    window.show()
    sys.exit(app.exec_())

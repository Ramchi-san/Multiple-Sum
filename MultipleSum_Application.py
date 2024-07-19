import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton
from typing import List

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
        rangeExample_label = QLabel("Example: 'Lower limit - Upper limit' -> 1 - 10 ")
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
        range_string = self.range_entry.text()
        factor_string = self.factor_entry.text()
        factor = self.data_cleaner(range_string, factor_string)
        print(f"Final received items: {factor}")
        lower_limit = factor.pop(0)
        print(f"Lower limit: {lower_limit}")
        upper_limit = factor.pop(0)
        print(f"Upper limit: {upper_limit}")
        factor_multiples = MultipleSum_Application.factor_multiples(factor, lower_limit, upper_limit)
        multiples_sum = MultipleSum_Application.multiple_adder(factor_multiples)
        factorMultiples_string = ""
        for some_value in factor_multiples.items():
            factorMultiples_string += f"\n\t[{some_value[0]}] = {some_value[1]}"

        output_text = f"Range: {lower_limit} - {upper_limit}\nfactor: {factor}\nFactor Multiples:{factorMultiples_string} \nResult: {multiples_sum}"
        self.output_display.setPlainText(output_text)

    #Cleared
    def data_cleaner(self, range_string, factor_string) -> List[int]:
        range_string = range_string.replace(" ", "")
        factor_string = factor_string.replace(" ", "")
        lower_limit = int(range_string.split("-")[0])
        print(f"Lower limit: {lower_limit}")
        upper_limit = int(range_string.split("-")[1])
        print(f"Upper limit: {upper_limit}")
        factors = [int(_) for _ in factor_string.split(",")]
        result = []
        result.append(lower_limit)
        result.append(upper_limit)
        print(f"Initial Items:  {result}")
        print(f"Final Items: {result + factors}")
        return result + factors 

    """
    The factor_multiples function is about finding the multiples of certain list of factors
    storing them in a dictionary with the factors as the key and the list of multiples as the 
    value
    """ 
    def factor_multiples(factors: List[int], lower_limit : int, upper_limit : int):
        multiples = {}
        for number in factors:
            multiples[number] = MultipleSum_Application.multiple_finder(number, lower_limit, upper_limit)
        return multiples
    

    """
    The multiple_finder function is a utility function of factor_multiples
    which determines the multiples of a number within a certain range.
    """
    def multiple_finder(factor: int, lower_limit : int, upper_limit: int) -> List[int]:
        counter = 1
        result = []
        temp_result = 0
        while int(temp_result) < upper_limit:
            temp_result = factor * counter
            if temp_result >= lower_limit and temp_result <= upper_limit:
                result.append(temp_result)
            counter+=1
        return result
    
    """
    The multiple_adder function is about adding all the multiples within a list
    that is stored in a dictionary except those that are repeating.
    """
    def multiple_adder(multiples):
        temp_copy = multiples.popitem()
        popped_set = set(temp_copy[1])
        for multiple_list in multiples.values():
            popped_set = popped_set.union(set(multiple_list))
        multiples[temp_copy[0]] = temp_copy[1]
        return sum(popped_set)

    def clear_input(self):
        self.range_entry.clear()
        self.factor_entry.clear()
        self.output_display.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultipleSum_Application()
    window.show()
    sys.exit(app.exec_())

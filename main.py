from PySide6 import QtWidgets, QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
app = QtWidgets.QApplication()
window = loader.load("form.ui", None)

class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.but_data(window.press_button, "1")
        self.but_data(window.press_button_2, "2")
        self.but_data(window.press_button_3, "3")
        self.but_data(window.press_button_4, "4")
        self.but_data(window.press_button_5, "5")
        self.but_data(window.press_button_7, "6")
        self.but_data(window.press_button_9, "7")
        self.but_data(window.press_button_6, "8")
        self.but_data(window.press_button_8, "9") 
        self.but_data(window.press_button_10,"+")
        self.but_data(window.press_button_11,"-")
        self.but_data(window.press_button_12,"/")
        self.but_data(window.press_button_13,"*")
        self.but_data(window.press_button_14,"0")
        self.but_data(window.press_button_15,"=")
        self.but_data(window.press_button_16,"clear")
        
    def but_data(self, button, text):
        if text == "clear":
            button.clicked.connect(lambda:self.clear())
        elif text == "=":
            button.clicked.connect(lambda:self.equal())
        else:
            button.clicked.connect(lambda: self.but_clicked(text))
        

    def but_clicked(self, data):
        
        window.line_edit.insert(data) 

    def clear(self):
        window.line_edit.clear()
    
    def equal(self):
        entered_numbers = window.line_edit.text()
        result = eval(entered_numbers)
        window.line_edit.clear()
        window.line_edit.insert(str(result))

        
calc = Calculator()
window.show()
app.exec()

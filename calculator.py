import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit,QGridLayout,QVBoxLayout,QPushButton

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.calculator_GUI()

    def calculator_GUI(self):
        central_widget = QWidget()

        main_layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setPlaceholderText("0")
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 40px; font-family: Arial; font-weight: bold;")
        main_layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [("AC",0,1), ("%",0,2), ("/",0,3),
                   ("7",1,0), ("8",1,1), ("9",1,2), ("*",1,3),
                   ("4",2,0), ("5",2,1), ("6",2,2), ("-",2,3),
                   ("1",3,0), ("2",3,1), ("3",3,2), ("+",3,3),
                   ("00",4,0), ("0",4,1), (".",4,2), ("=",4,3)]
        
        for text,row,col in buttons:
            button = QPushButton(text)
            button.setFixedSize(100,100)
            if text == "=":
                button.setStyleSheet("font-size: 50px; font-weight: bold; font-family: Arial; border-radius: 20px; background-color: hsl(27, 100%, 49%); color: white")
            else:
                button.setStyleSheet("font-size: 50px; font-weight: bold; font-family: Arial; border-radius: 20px; background-color: black; color: white")


            grid.addWidget(button,row,col)
            button.clicked.connect(self.on_button_click)

        
        main_layout.addLayout(grid)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self):
        btn = self.sender()
        text = btn.text()

        if text == "AC":
            self.display.clear()
        elif text == "=":
            try:
                exp = self.display.text()
                result = str(eval(exp))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)
        

def main():
    app = QApplication(sys.argv)
    my_window = Window()
    my_window.show()
    sys.exit(app.exec_())

main()
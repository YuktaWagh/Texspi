from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyttsx3 as pyt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Texspi")
        self.setGeometry(250, 100, 900, 600)
        self.setStyleSheet('Background-color: #E7CBF9')
        self.setWindowIcon(QIcon('Texspi-Icon.ico'))
        self.setFixedSize(900, 600)

        #Label
        self.l = QLabel(self)
        self.l.setPixmap(QPixmap('Texspi.png'))
        self.l.adjustSize()
        self.l.move(270, 20)

        #Textbox
        #self.text = QTextEdit(self, LineWrapMode=QTextEdit.FixedColumnWidth, LineWrapColumnOrWidth = 50,
           # placeholderText = "Type to convert Text to Speech",
            #readOnly = False)
        #self.layout().addWidget(text)
        self.text = QTextEdit(self)
        self.text.setFixedSize(600, 200)
        self.text.setFont(QFont('Open Sans', 18))
        self.text.move(150, 235)
        self.text.setPlaceholderText('Type to convert text to speech')
        self.text.setStyleSheet('Background: #FFE7FA; border-radius: 15; border: 5px solid #B149AC')


        #Button
        self.button = QPushButton("Speak!", self)
        self.button.setFixedSize(170, 80)
        self.button.setFont(QFont('Ludica Handwriting', 22))
        self.button.move(370, 455)
        #self.button.adjustSize()
        self.button.setStyleSheet('Background: #FC978C; border-radius: 15; border: 5px solid #E01E30')
        self.button.clicked.connect(lambda: self.press())
        # self.font = QFont(self.button)
        # self.font.setItalic(True)

        #Show the app
        self.show()

    #Button function
    def press(self):

        #Convert text to speech

        words = self.text.toPlainText()
        engine = pyt.init()
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[1].id)
        engine.setProperty('rate', 150)
        engine.say(words)
        engine.runAndWait()




app = QApplication([])
w = Window()

app.exec_()
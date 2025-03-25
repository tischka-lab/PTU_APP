import sys
import Error_Handeling
import MasterSettings as MasSet
import random

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *   


#__________________________________________________Images and icons__________________________________________________

company_logo        :str =   MasSet.img_company_logo

#__________________________________________________Decorative constants__________________________________________________

DarkmodeColor       :str =    MasSet.DarkmodeColor # to be replaced by function
Transparencolor     :str =    MasSet.Transparencolor
Fonttype_1          :str =    MasSet.Fonttype_1
letter_size_Big     :int =    MasSet.letter_size_Big
letter_size_Medium  :int =    MasSet.letter_size_Medium
letter_size_Smal    :int =    MasSet.letter_size_Smal
hello                    =    MasSet.hello_txt


#__________________________________________________Start of Code__________________________________________________

class StartWindow (QMainWindow):

    def __init__(self, size_W :int = 2560, size_H :int = 1600):
        super().__init__()


        self.hello = hello
        self.Transparent_color   = Transparencolor
        self.Font                   = Fonttype_1
        self.size_W = size_W
        self.size_H = size_H
        self.setWindowTitle(f"Start Screen")
        self.setWindowIcon(QIcon(company_logo))
        label_background = QPushButton (self)
        label_background.setGeometry(-10,-10,self.size_W+15,self.size_H+15)
        label_background.setStyleSheet("QWidget {background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #910710, stop: 1 #2a43d1)};") 
        self.central_widget = QWidget()   
        self.setCentralWidget(self.central_widget)
        self.Letter_size_s = letter_size_Smal
        self.Letter_size_M = letter_size_Medium
        self.letter_size_L = letter_size_Big*4
        #self.btn_continiue = QPushButton

        self.central_widget = QWidget()  
        self.setCentralWidget(self.central_widget)

    
        self.initUI()



    def initUI(self): #Buttons and layout


        self.welcome = QLabel("Welcome")
        self.welcome.setFixedSize(self.size_W,self.size_H)
        self.welcome.setStyleSheet(f"background-color : {self.Transparent_color};")
        self.welcome.setFont(QFont(self.Font,self.letter_size_L))
        self.welcome.setAlignment(Qt.AlignCenter)


        self.organization = QGridLayout()

        self.organization.addWidget (self.welcome,0,0)

        self.central_widget.setLayout(self.organization)


        # Set up a timer to update the label every 10 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(10000)  # 10000 milliseconds = 10 seconds
        
    def update_label(self):
        self.welcome.setText(random.choice(self.hello))


class Handeler():

    def __init__ (self):
        super().__init__()
        self.open()

    def open(self):
        self.window = StartWindow()
        self.window.showFullScreen()
    




def main():

    app = QApplication(sys.argv)
    window = Handeler()
    sys.exit(app.exec_())




if __name__ == "__main__":

    main()

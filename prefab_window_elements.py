import sys
import MasterSettings as MasSet
import prefab_window_elements as prefab
import Error_Handeling
import Logger
from functools import reduce
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import MasterSettings as MasSet



class window_header():

    def init_Header (window_icon = MasSet.no_image, window_title_key = "no_data",Translation_Dict = MasSet.Translate_Dictonary_Fallback):

        """ generates the window header ( Requires: path to the icon, current dictionary, the key to the windowname for the dictionary )
        """

        window_icon:       str     = window_icon
        Translation_Dict:  dict    = Translation_Dict
        window_title_key:  str     = window_title_key
        Transparent                = MasSet.Transparencolor
        Font                       = MasSet.Fonttype_1
        Letter_size                = MasSet.letter_size_Big
        close_window_icon          = MasSet.close_window_icon_RD


        window_icon_pixmap = QPixmap(window_icon)
        window_icon_scaled = window_icon_pixmap.scaledToWidth(100)
        label_1 = QLabel ("")
        label_1.setFixedSize(100,100)
        label_1.setPixmap(window_icon_scaled)
        label_1.setStyleSheet(f"background-color : {Transparent}; border : none")
        label_1.setAlignment(Qt.AlignLeft)
            
        label_2 = QLabel (Translation_Dict.get(window_title_key))
        label_2.setStyleSheet(f"background-color :{Transparent}; font-weight : bold;")
        label_2.setFont(QFont(Font,Letter_size))
        label_2.setAlignment(Qt.AlignCenter)


        close_window_pixmap = QPixmap(close_window_icon)
        close_window_scaled = close_window_pixmap.scaledToWidth(100)

        close_window = QLabel ("")
        close_window.setPixmap(close_window_scaled)
        close_window.setFixedSize(104,104)
        close_window.setStyleSheet(f"background-color : {Transparent}; border : none")
        close_window.setAlignment(Qt.AlignRight)
                
        layout = QHBoxLayout()
        layout.addWidget(label_1)
        layout.addWidget(label_2) 
        layout.addWidget(close_window)

        return layout


class Keypad(QWidget):


    password_IO         = pyqtSignal(bool)
    int_data_signal     = pyqtSignal(int)

    def __init__(self, width:int, heith:int, pass_code:int = None, log_all: bool = False, Translation_Dictionary: dict = MasSet.Translate_Dictonary_Fallback):
        super().__init__()
        
        self.code = pass_code
        self.see_pasword = True
        self.window_size_W = width
        self.window_size_H = heith
        self.Translation_Dictionary = Translation_Dictionary
        self.setWindowTitle("Keypad")                                              #window title + GUI version
        self.setMinimumSize(800,900)                                                                   #windowstartsize
        self.setWindowIcon(QIcon(MasSet.img_company_logo))                                             #window icon
        label_background = QLabel (self)
        label_background.setGeometry(-10,-10,self.window_size_W+15,self.window_size_H+15)
        label_background.setStyleSheet("background-color :" + MasSet.DarkmodeColor)
                 
        self.input                          = []
        self.text_line_str                  = ""


        self.btn_window_header              = QPushButton ("")
        self.text_line                      = QLabel ("")
        self.btn_see_key                    = QPushButton ("")
        self.btn_0                          = QPushButton ("0")
        self.btn_1                          = QPushButton ("1")
        self.btn_2                          = QPushButton ("2")
        self.btn_3                          = QPushButton ("3")
        self.btn_4                          = QPushButton ("4")
        self.btn_5                          = QPushButton ("5")
        self.btn_6                          = QPushButton ("6")
        self.btn_7                          = QPushButton ("7")
        self.btn_8                          = QPushButton ("8")
        self.btn_9                          = QPushButton ("9")
        self.btn_C                          = QPushButton ("C")
        self.btn_enter                      = QPushButton ("ENTER")

        def close_window():
            self.close()


        def see_key_pressed():              # for th eye button to see the password 

            if self.see_pasword == False:
                self.see_pasword = True
                self.image.setPixmap(icon_blind_scaled)
                self.text_line.setText(self.text_line_str)

            else:
                self.see_pasword = False
                self.image.setPixmap(icon_eye_scaled)
                self.text_line.setText(self.text_line_str)
            

        def num_pressed(num):  # in a numberbutton is pressed the number si apendet to a list, 

            max_length_of_input =  50   # a safeguard that a random person cant do something unwanted by pressing to many buttons 

            self.input.append(num)

            if self.see_pasword == True:                            # if a password is providet the default setting is to hide the numbers
                number_str = [str(num) for num in self.input] 
            else:
                number_str = [str("*") for num in self.input]

            if number_str.__len__() > max_length_of_input:

                if log_all == True:
                    Logger.logger(f"number input keypad to long : {self.input}")
                clear_input()

            self.text_line_str = "".join(number_str)
            self.text_line.setText(self.text_line_str)


        def clear_input():
            self.input.clear()
            self.text_line_str = ""
            self.text_line.setText(self.text_line_str)

        def Enter_pressed():
            number_input = 0    
            try: number_input = reduce(lambda x,y: x*10 + y, self.input) # https://sparkbyexamples.com/python/python-list-to-integer/
        
            except TypeError as err:
                if log_all == True:
                    Logger.logger(f"enter pressed: TypeError : {err}")
            
            except Exception as err:
                if log_all == True:
                    Logger.logger(f"enter pressed: exeption {err}")

            if self.code is not None:

                if number_input == self.code:
                    self.password_IO.emit(True)
                    clear_input()
                    close_window()

                else:
                    # the list and texfield get cleard, and the texfield gets a ligth red hue 
                    if log_all == True:
                        Logger.logger(f"keypad wrong pasword {number_input}")
                    
                    self.text_line.setStyleSheet(f"border-radius : 20px; background-color: rgba(255, 0, 0, 50); border: 4px solid black")
                    clear_input()

            else:
                self.int_data_signal.emit(number_input)
                clear_input()
                close_window()

        
        #____________________________KEYPAD____________________________
        self.keypad_num_layout      = QGridLayout()
        self.main_content           = QVBoxLayout()

        self.btn_window_header.setFixedHeight(125)
        self.btn_window_header.setStyleSheet(f"background-color : {MasSet.DarkmodeColor_header};border : none")
        self.btn_window_header.setLayout(window_header.init_Header(MasSet.keypad_icon,"window_title_6",self.Translation_Dictionary))
        self.btn_window_header.clicked.connect(close_window)

        self.text_line.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.text_line.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.text_line.setMinimumSize(600,100)

        self.btn_0.setMinimumSize(100,100)
        self.btn_0.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_0.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_0.clicked.connect(lambda: num_pressed(0))
        
        self.btn_1.setMinimumSize(100,100)
        self.btn_1.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_1.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_1.clicked.connect(lambda: num_pressed(1))

        self.btn_2.setMinimumSize(100,100)
        self.btn_2.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_2.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_2.clicked.connect(lambda: num_pressed(2))

        self.btn_3.setMinimumSize(100,100)
        self.btn_3.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_3.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_3.clicked.connect(lambda: num_pressed(3))

        self.btn_4.setMinimumSize(100,100)
        self.btn_4.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_4.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_4.clicked.connect(lambda: num_pressed(4))

        self.btn_5.setMinimumSize(100,100)
        self.btn_5.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_5.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_5.clicked.connect(lambda: num_pressed(5))

        self.btn_6.setMinimumSize(100,100)
        self.btn_6.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_6.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_6.clicked.connect(lambda: num_pressed(6))

        self.btn_7.setMinimumSize(100,100)
        self.btn_7.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_7.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_7.clicked.connect(lambda: num_pressed(7))

        self.btn_8.setMinimumSize(100,100)
        self.btn_8.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_8.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_8.clicked.connect(lambda: num_pressed(8))

        self.btn_9.setMinimumSize(100,100)
        self.btn_9.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_9.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_9.clicked.connect(lambda: num_pressed(9))

        self.btn_C.setMinimumSize(100,100)
        self.btn_C.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_C.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_C.clicked.connect(clear_input)

        self.btn_enter.setMinimumSize(100,100)
        self.btn_enter.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
        self.btn_enter.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Medium))
        self.btn_enter.clicked.connect(Enter_pressed)
        


        if self.code is not None:
            self.see_pasword    = False
            self.image          = QLabel("")
            self.eye_pixmap     = MasSet.icon_eye
            self.blind_pixmap   = MasSet.icon_blind
            self.pixmap_eye     = QPixmap(self.eye_pixmap)
            self.pixmap_blind   = QPixmap(self.blind_pixmap)
            icon_eye_scaled     = self.pixmap_eye.scaledToHeight(100)
            icon_blind_scaled   = self.pixmap_blind.scaledToHeight(100)

            self.image.setPixmap(icon_eye_scaled)
            self.image.setStyleSheet("border : none; ")
            self.image.setAlignment(Qt.AlignCenter)


            self.layout_image = QHBoxLayout()
            self.layout_image.addWidget(self.image)
            
            self.btn_see_key.setMinimumSize(100,100)
            self.btn_see_key.setLayout(self.layout_image)
            self.btn_see_key.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Transparencolor}; border: 4px solid black")
            self.btn_see_key.clicked.connect(see_key_pressed)


            self.keypad_num_layout.addWidget(self.btn_see_key,5,2)

        self.keypad_num_layout.addWidget(self.btn_0,4,2)
        self.keypad_num_layout.addWidget(self.btn_1,3,1)
        self.keypad_num_layout.addWidget(self.btn_2,3,2)
        self.keypad_num_layout.addWidget(self.btn_3,3,3)
        self.keypad_num_layout.addWidget(self.btn_4,2,1)
        self.keypad_num_layout.addWidget(self.btn_5,2,2)
        self.keypad_num_layout.addWidget(self.btn_6,2,3)
        self.keypad_num_layout.addWidget(self.btn_7,1,1)
        self.keypad_num_layout.addWidget(self.btn_8,1,2)
        self.keypad_num_layout.addWidget(self.btn_9,1,3)
        self.keypad_num_layout.addWidget(self.btn_C,4,1)
        self.keypad_num_layout.addWidget(self.btn_enter,4,3)


        self.main_content.addWidget(self.text_line)
        self.main_content.addLayout(self.keypad_num_layout)
        self.main_content.setAlignment(Qt.AlignCenter)


        # _________________________ Final layout _________________________

        self.organization           = QVBoxLayout()


        self.organization.setContentsMargins (0,0,0,0)
        self.organization.addWidget (self.btn_window_header)
        self.organization.addLayout (self.main_content)
        self.setLayout(self.organization)


class Keypad_Handeler():

    def __init__ (self, pass_code: int = None , log_all: bool = False ):
        super().__init__()

            
        Desktop = QDesktopWidget()
        screen_geometry = Desktop.screenGeometry()
        self.window_size_W = screen_geometry.width()
        self.window_size_H = screen_geometry.height()
        self.pass_code = pass_code

        if self.pass_code is not None: 
            self.window = Keypad(self.window_size_W,self.window_size_H,self.pass_code,log_all)
        else:
            self.window = Keypad(self.window_size_W,self.window_size_H,log_all)

        self.window.show()




def main():

    testpasscode = 1234

    app = QApplication(sys.argv)
    Desktop = QDesktopWidget()
    screen_geometry = Desktop.screenGeometry()
    width = screen_geometry.width()
    heith = screen_geometry.height()
    window = Keypad_Handeler(testpasscode, True)                          # constructs the window
    #window.show()                                   # opens a window
#    window.showFullScreen()                        # opens the window in fullscren


    sys.exit(app.exec_())                           # exits the window constructor

if __name__ == "__main__":
    main()


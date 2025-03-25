
import sys
import datetime
import MasterSettings as MasSet
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#Error_massage = "General Error"
    #   numbers and thier meaning
    #   1000 - 3000 Notification type message
    #   4000 - 6000 Warning
    #   9000 - 9999 Error

#__________________________________________________Images and icons__________________________________________________
warning_triangle_icon:  str =   MasSet.warning_triangle_icon
Warning_Triangle_BL:    str =   MasSet.img_Warning_Triangle_BL
Warning_Triangle_H:     int =   MasSet.img_Warning_Triangle_H
Warning_Triangle_W:     int =   MasSet.img_Warning_Triangle_W

bell_icon:              str =   MasSet.bell_icon
bell_icon_W:            int =   MasSet.bell_icon_WxH
bell_icon_H:            int =   MasSet.bell_icon_WxH


close_window_icon_RD:   str =   MasSet.close_window_icon_RD    
close_window_icon_BL:   str =   MasSet.close_window_icon_BL    

#__________________________________________________Decorative constants__________________________________________________

Red_color:              str =   MasSet.Red_color                            
Yellow_color:           str =   MasSet.Yellow_color                     
Blue_color:             str =   MasSet.Blue_color                  


Transparencolor:        str =   MasSet.Transparencolor
Fonttype_1:             str =   MasSet.Fonttype_1
letter_size_Massive:    int =   MasSet.letter_size_Massive
letter_size_Big:        int =   MasSet.letter_size_Big
letter_size_Medium:     int =   MasSet.letter_size_Medium
letter_size_Smal:       int =   MasSet.letter_size_Medium


#__________________________________________________File Paths__________________________________________________
Log_Files:              str =  MasSet.Error_Log_Files



#--------------------------------------------------------------------------------Begin of code--------------------------------------------------------------------------------




class RedAlert(QMainWindow):        #Crittical Error e.g.tranlation modul unavailabile/hard Error


    def __init__(self,Error_message, Error_Code):
        super().__init__()

        self.Color              = Red_color
        self.Transparent        = Transparencolor
        self.ImagePath          = Warning_Triangle_BL
        self.ImageH             = Warning_Triangle_H
        self.ImageW             = Warning_Triangle_W
        self.error_type         = "CRITICAL ERROR"
        self.error_txt          = Error_message
        self.error_code         = Error_Code
        self.Letter_size_XL     = letter_size_Massive
        self.Letter_size_L      = letter_size_Big
        self.Letter_size_M      = letter_size_Medium
        self.Letter_size_S      = letter_size_Smal
        self.Font               = Fonttype_1
        self.window_icon        = warning_triangle_icon
        self.close_window_icon  = close_window_icon_BL
        self.time               = datetime.datetime.now().strftime("%H:%M:%S")
        self.date               = datetime.date.today()


        self.setWindowTitle (f"Critical ERROR {self.error_code}")
        self.setWindowIcon(QIcon(self.window_icon))
        self.setStyleSheet(f"background-color : {self.Color};")
        self.central_widget = QWidget()   
        self.setCentralWidget(self.central_widget)
                
        self.btn_closewindow = QPushButton ("",self)


        #close window
        self.close_window_pixmap = QPixmap(self.close_window_icon)
        self.icon_close_window = QIcon (self.close_window_pixmap)

        self.btn_closewindow.setFixedSize(104,104)
        self.btn_closewindow.setIconSize(self.close_window_pixmap.size())
        self.btn_closewindow.setIcon(self.icon_close_window)
        self.btn_closewindow.setStyleSheet(f"background-color : {self.Transparent}; border : none")
        self.btn_closewindow.clicked.connect(self.close_window)

        self.init_UI()


    def init_UI(self):  #layout and orgaasation of the info text`s and image 

        self.Image=QLabel("",self)
        self.Image.setFixedSize (self.ImageW,self.ImageH)
        self.Image.setStyleSheet(f"  background-image : url({self.ImagePath});  background-color : {self.Transparent};")


        self.error_type_text = QLabel(f"{self.error_type}",self)
        self.error_type_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_type_text.setFont(QFont(self.Font,self.Letter_size_XL))
        self.error_type_text.setAlignment(Qt.AlignCenter)

        self.error_code_text = QLabel(f"{self.error_code}",self)
        self.error_code_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_code_text.setFont(QFont(self.Font,self.Letter_size_M))
        self.error_code_text.setAlignment(Qt.AlignCenter)

        self.error_time= QLabel(f"{self.time} : {self.date}",self)
        self.error_time.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_time.setFont(QFont(self.Font,self.Letter_size_S))
        self.error_time.setAlignment(Qt.AlignCenter)


        self.empty=QLabel("")
        self.empty.setStyleSheet(f"background-color : {self.Transparent};")

        self.error_=QLabel("Error Code:")
        self.error_.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_.setFont(QFont(self.Font,self.Letter_size_M))
        self.error_.setAlignment(Qt.AlignCenter)

        self.error_text=QLabel(f"{self.error_txt}",self)
        self.error_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_text.setFont(QFont(self.Font,self.Letter_size_M))
        self.error_text.setAlignment(Qt.AlignCenter)
        

        self.help_info_EN=QLabel(f"Please contact your supervisor",self)
        self.help_info_EN.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.help_info_EN.setFont(QFont(self.Font,self.Letter_size_M))
        self.help_info_EN.setAlignment(Qt.AlignCenter)

        self.help_info_MULTI_LANG=QLabel(f"""   
DE : Bitte kontaktieren sie ihren Teamleiter
PL : Skontaktuj się ze swoim przełożonym    
RO : Vă rugăm să contactați supervizorul dvs
FR : Veuillez contacter votre superviseur   
                                         """,self)
        self.help_info_MULTI_LANG.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.help_info_MULTI_LANG.setFont(QFont(self.Font,self.Letter_size_S))
        self.help_info_MULTI_LANG.setAlignment(Qt.AlignCenter)
        



        self.organization   =   QGridLayout()
        self.error_org      =   QVBoxLayout()
        self.contact_org    =   QVBoxLayout()
        self.txt_1_widget   =   QWidget() 
        self.txt_2_widget   =   QWidget()
        self.txt_main_wid   =   QVBoxLayout()
        self.txt_main_grd   =   QWidget()



        self.error_org.addWidget (self.error_type_text,1)
        self.error_org.addWidget (self.empty,2)
        self.error_org.addWidget (self.error_,3)
        self.error_org.addWidget (self.empty,4)
        self.error_org.addWidget (self.error_code_text,5)
        self.error_org.addWidget (self.empty,6)
        self.error_org.addWidget (self.error_text,7)
        self.error_org.addWidget (self.error_time,8)

        self.contact_org.addWidget (self.help_info_EN,1)
        self.contact_org.addWidget (self.help_info_MULTI_LANG,2)

        self.txt_1_widget.setLayout(self.error_org)
        self.txt_2_widget.setLayout(self.contact_org)


        self.txt_main_wid.addWidget(self.txt_1_widget,1)
        self.txt_main_wid.addWidget(self.txt_2_widget,2)

        self.txt_main_grd.setLayout(self.txt_main_wid)


        self.organization.addWidget (self.btn_closewindow,1,5)
        self.organization.addWidget (self.Image,2,1)
        self.organization.addWidget (self.txt_main_grd,2,2)
    
        self.central_widget.setLayout (self.organization)


    def close_window(self): #closes the window on buttonpress
        self.close()



class YellowAlert(QMainWindow):        #WARNING e.g.sensor permablocked, miner module missing / soft Error


    def __init__(self,Error_message, Error_Code):
        super().__init__()

        self.Color              = Yellow_color
        self.Transparent        = Transparencolor
        self.ImagePath          = Warning_Triangle_BL
        self.ImageH             = Warning_Triangle_H
        self.ImageW             = Warning_Triangle_W
        self.error_type         = "WARNING"
        self.error_code         = Error_Code
        self.error_txt          = Error_message
        self.Letter_size_XL     = letter_size_Massive
        self.Letter_size_L      = letter_size_Big
        self.Letter_size_M      = letter_size_Medium
        self.Letter_size_S      = letter_size_Smal
        self.Font               = Fonttype_1
        self.window_icon        = warning_triangle_icon
        self.close_window_icon  = close_window_icon_BL
        self.time               = datetime.datetime.now().strftime("%H:%M:%S")
        self.date               = datetime.date.today()


        self.setWindowTitle (f"WARNING {self.error_code}")
        self.setWindowIcon(QIcon(self.window_icon))
        self.setStyleSheet(f"background-color : {self.Color};")
        self.central_widget = QWidget()   
        self.setCentralWidget(self.central_widget)
                
        self.btn_closewindow = QPushButton ("",self)


        #close window
        self.close_window_pixmap = QPixmap(self.close_window_icon)
        self.icon_close_window = QIcon (self.close_window_pixmap)

        self.btn_closewindow.setFixedSize(104,104)
        self.btn_closewindow.setIconSize(self.close_window_pixmap.size())
        self.btn_closewindow.setIcon(self.icon_close_window)
        self.btn_closewindow.setStyleSheet(f"background-color : {self.Transparent}; border : none")
        self.btn_closewindow.clicked.connect(self.close_window)

        self.init_UI()


    def init_UI(self):  #layout and orgaasation of the info text`s and image 

        self.Image=QLabel("",self)
        self.Image.setFixedSize (self.ImageW,self.ImageH)
        self.Image.setStyleSheet(f"  background-image : url({self.ImagePath});  background-color : {self.Transparent};")


        self.error_type_text= QLabel(f"{self.error_type}",self)
        self.error_type_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_type_text.setFont(QFont(self.Font,self.Letter_size_XL))
        self.error_type_text.setAlignment(Qt.AlignCenter)
        
        self.error_code_text = QLabel(f"{self.error_code}",self)
        self.error_code_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_code_text.setFont(QFont(self.Font,self.Letter_size_M))
        self.error_code_text.setAlignment(Qt.AlignCenter)

        self.error_time= QLabel(f"{self.time} : {self.date}",self)
        self.error_time.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_time.setFont(QFont(self.Font,self.Letter_size_S))
        self.error_time.setAlignment(Qt.AlignCenter)


        self.empty=QLabel("")
        self.empty.setStyleSheet(f"background-color : {self.Transparent};")

        self.error_=QLabel("WARNING:")
        self.error_.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_.setFont(QFont(self.Font,self.Letter_size_M))
        self.error_.setAlignment(Qt.AlignCenter)

        self.error_text=QLabel(f"{self.error_txt}",self)
        self.error_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_text.setFont(QFont(self.Font,self.Letter_size_M))
        self.error_text.setAlignment(Qt.AlignCenter)
        

        self.help_info_EN=QLabel(f"Please contact your supervisor",self)
        self.help_info_EN.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.help_info_EN.setFont(QFont(self.Font,self.Letter_size_M))
        self.help_info_EN.setAlignment(Qt.AlignCenter)

        self.help_info_MULTI_LANG=QLabel(f"""   
DE : Bitte kontaktieren sie ihren Teamleiter
PL : Skontaktuj się ze swoim przełożonym    
RO : Vă rugăm să contactați supervizorul dvs
FR : Veuillez contacter votre superviseur   
                                         """,self)
        self.help_info_MULTI_LANG.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.help_info_MULTI_LANG.setFont(QFont(self.Font,self.Letter_size_S))
        self.help_info_MULTI_LANG.setAlignment(Qt.AlignCenter)
        



        self.organization   =   QGridLayout()
        self.error_org      =   QVBoxLayout()
        self.contact_org    =   QVBoxLayout()
        self.txt_1_widget   =   QWidget() 
        self.txt_2_widget   =   QWidget()
        self.txt_main_wid   =   QVBoxLayout()
        self.txt_main_grd   =   QWidget()



        self.error_org.addWidget (self.error_type_text,1)
        self.error_org.addWidget (self.empty,2)
        self.error_org.addWidget (self.error_,3)
        self.error_org.addWidget (self.empty,4)
        self.error_org.addWidget (self.error_code_text,5)
        self.error_org.addWidget (self.empty,6)
        self.error_org.addWidget (self.error_text,7)
        self.error_org.addWidget (self.error_time,8)

        self.contact_org.addWidget (self.help_info_EN,1)
        self.contact_org.addWidget (self.help_info_MULTI_LANG,2)

        self.txt_1_widget.setLayout(self.error_org)
        self.txt_2_widget.setLayout(self.contact_org)


        self.txt_main_wid.addWidget(self.txt_1_widget,1)
        self.txt_main_wid.addWidget(self.txt_2_widget,2)

        self.txt_main_grd.setLayout(self.txt_main_wid)


        self.organization.addWidget (self.btn_closewindow,1,5)
        self.organization.addWidget (self.Image,2,1)
        self.organization.addWidget (self.txt_main_grd,2,2)
    
        self.central_widget.setLayout (self.organization)


    def close_window(self): #closes the window on buttonpress
        self.close()



class BlueAlert(QMainWindow):        #NOTICE e.g. tape on roll 
        

    def __init__(self,Error_message,Error_Code):
        super().__init__()

        self.Color              = Blue_color
        self.Transparent        = Transparencolor
        self.ImagePath          = bell_icon
        self.ImageH             = bell_icon_H
        self.ImageW             = bell_icon_W
        self.error_type         = "Notification"
        self.error_code         = Error_Code
        self.error_txt          = Error_message
        self.Letter_size_XL     = letter_size_Massive
        self.Letter_size_L      = letter_size_Big
        self.Letter_size_M      = letter_size_Medium
        self.Letter_size_S      = letter_size_Smal
        self.Font               = Fonttype_1
        self.window_icon        = warning_triangle_icon
        self.close_window_icon  = close_window_icon_BL
        self.time               = datetime.datetime.now().strftime("%H:%M:%S")
        self.date               = datetime.date.today()

    
        self.setWindowTitle (f"Notification {self.error_code}")
        self.setWindowIcon(QIcon(self.window_icon))
        self.setStyleSheet(f"background-color : {self.Color};")
        self.central_widget = QWidget()   
        self.setCentralWidget(self.central_widget)
                
        self.btn_closewindow = QPushButton ("",self)

        #close window
        self.close_window_pixmap = QPixmap(self.close_window_icon)
        self.icon_close_window = QIcon (self.close_window_pixmap)

        self.btn_closewindow.setFixedSize(104,104)
        self.btn_closewindow.setIconSize(self.close_window_pixmap.size())
        self.btn_closewindow.setIcon(self.icon_close_window)
        self.btn_closewindow.setStyleSheet(f"background-color : {self.Transparent}; border : none")
        self.btn_closewindow.clicked.connect(self.close_window)

        self.init_UI()


    def init_UI(self):  #layout and orgaasation of the info text`s and image 

        self.Image=QLabel("",self)
        self.Image.setFixedSize (self.ImageW,self.ImageH)
        self.Image.setStyleSheet(f"  background-image : url({self.ImagePath});  background-color : {self.Transparent};")


        self.error_type_text= QLabel(f"{self.error_type}",self)
        self.error_type_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_type_text.setFont(QFont(self.Font,self.Letter_size_XL))
        self.error_type_text.setAlignment(Qt.AlignCenter)

        self.error_code_text = QLabel(f"{self.error_code}",self)
        self.error_code_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_code_text.setFont(QFont(self.Font,self.Letter_size_M))
        self.error_code_text.setAlignment(Qt.AlignCenter)

        self.error_time= QLabel(f"{self.time} : {self.date}",self)
        self.error_time.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_time.setFont(QFont(self.Font,self.Letter_size_S))
        self.error_time.setAlignment(Qt.AlignCenter)


        self.empty=QLabel("")
        self.empty.setStyleSheet(f"background-color : {self.Transparent};")

        self.error_text=QLabel(f"{self.error_txt}",self)
        self.error_text.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
        self.error_text.setFont(QFont(self.Font,self.Letter_size_M))
        self.error_text.setAlignment(Qt.AlignCenter)




        self.organization   =   QGridLayout()
        self.error_org      =   QVBoxLayout()
        self.txt_main_grd   =   QWidget()



        self.error_org.addWidget (self.error_type_text,1)
        self.error_org.addWidget (self.empty,2)
        self.error_org.addWidget (self.error_text,3)
        self.error_org.addWidget (self.error_time,4)
        self.error_org.addWidget (self.empty,5)
        self.error_org.addWidget (self.error_code_text,5)
    

        self.txt_main_grd.setLayout(self.error_org)


        self.organization.addWidget (self.btn_closewindow,1,5)
        self.organization.addWidget (self.Image,2,1)
        self.organization.addWidget (self.txt_main_grd,2,2)
    
        self.central_widget.setLayout (self.organization)


    def close_window(self): #closes the window on buttonpress
        self.close()



class Error_MSG_handeling():
    
    """ more Info 
    # if the error Code number is within a specified range the proper error window will be caled if the error code is outside the specified erea a warning wil be called
    # it is possibile to hide the window but they log will be created anyway (viibile)

    #   error numbers and thier meaning
    #   1000 - 3000

    #   4000 - 7000 Warning
    #   7777 - unknown warning / Unknown_Warning

    #   8000 - 9990 Error
    #   9999 = unknown error / Unknown_ERROR """


    def __init__ (self, err_code :int = 9999, err_MSG :str = "Unknown_ERROR", err_sys_code :Exception = None, visible :bool = True):
        super().__init__()

        self.visible            = visible
        self.error_MSG          = err_MSG
        self.err_code           = err_code
        self.file_path          = Log_Files
        self.err_sys_code       = err_sys_code
        self.time               = datetime.datetime.now().strftime("%H:%M:%S")
        self.date               = datetime.date.today()
        self.I_range_A          = 1000
        self.I_range_B          = 3000
        self.W_range_A          = 4000
        self.W_range_B          = 7000
        self.E_range_A          = 8000
        self.E_range_B          = 9999
        self.window             = None              # if the window is generated 
        self.sucess             = 0                 # repots sucess of the Error operation      

        self.open_window()



    def open_window(self):

        if self.err_code >= self.I_range_A and self.err_code <= self.I_range_B:
            self.error_type = "Info"

            if self.visible == True:
                self.window = BlueAlert(self.error_MSG, self.err_code)
                self.window.show()


        elif self.err_code >= self.W_range_A and self.err_code <= self.W_range_B:
            self.error_type = "Warning"

            if self.visible == True:
                self.window = YellowAlert(self.error_MSG, self.err_code)  
                self.window.showFullScreen()


        elif self.err_code >= self.E_range_A and self.err_code <= self.E_range_B:
            self.error_type = "Error"

            if self.visible == True:    
                self.window = RedAlert(self.error_MSG, self.err_code)
                self.window.showFullScreen()


        else:
            self.error_type = "Unknown Warning"
            
            if self.visible == True:
                self.window = YellowAlert(self.error_MSG, self.err_code)
                self.window.showFullScreen()



        try:
            with open (self.file_path,"a")as file:
                file.write (f"\n{self.time} : {self.date},   {self.error_type:15}, Message: {self.error_MSG:5}, Code : {self.err_code:10}, is visible : {self.visible},    Python Error : {self.err_sys_code}")
                self.sucess = 2

        except Exception as err:
            print ("Log event Failure !")
            print ("Exception details:", err)
            self.sucess = 1


        return(self.sucess)



ERR = "ERR_MSG_TEST"

def main():
    
    app = QApplication(sys.argv)
    #window = Error_MSG_handeling(4200,
    #f""" JSONDecodeError Window closed {ERR}""",True)
    window1 = Error_MSG_handeling(2000,"Turret",True)
    
    window2 = Error_MSG_handeling(5000,"APATURE",True)    
    
    window3 = Error_MSG_handeling(9999,"G.L.A.D.O.S",True)


    sys.exit(app.exec_())                           # exits the window constructor


if __name__ == "__main__":
    main()
         

import sys
import os
import json
import random
import openpyxl
import Error_Handeling
import MasterSettings as MasSet
import Sub_Windows
import prefab_window_elements as prefab
import StartScreen

#from Language_module import Translation_Dictionary_File
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import QSvgWidget

CONFIG_FILE = MasSet.CONFIG_FILE
Gui_ver = MasSet.Gui_ver 
#__________________________________________________Images and icons__________________________________________________

company_logo        :str =   MasSet.img_company_logo
no_image            :str =   MasSet.no_image                #40px   X   10px
settings_icon       :str =   MasSet.settings_icon           #100px  X   100px
ligtingmode_icon    :str =   MasSet.ligtingmode_icon        #208px  X   208px
tranlation_icon     :str =   MasSet.tranlation_icon         #208px  X   208px
help_icon           :str =   MasSet.help_icon               #100px  X   100px
info_icon           :str =   MasSet.info_icon               #100px  X   100px
close_window_icon   :str =   MasSet.close_window_icon_BL    #104px  X   104px


#__________________________________________________Decorative constants__________________________________________________

DarkmodeColor       :str =    MasSet.DarkmodeColor # to be replaced by function
Transparencolor     :str =    MasSet.Transparencolor
Green_color         :str =    MasSet.Green_color
Red_color           :str =    MasSet.Red_color
Orange_color        :str =    MasSet.Orange_color
Fonttype_1          :str =    MasSet.Fonttype_1
letter_size_Big     :int =    MasSet.letter_size_Big
letter_size_Medium  :int =    MasSet.letter_size_Medium
letter_size_Smal    :int =    MasSet.letter_size_Smal
 
#__________________________________________________from functions__________________________________________________

Translation_Dict :dict = MasSet.Translate_Dictonary_Fallback

#__________________________________________________Constants for not working/missing functions__________________________________________________

darkmode = True         # does not work. no function exists 



#__________________________________________________Notes for not working/missing functions__________________________________________________
"""
Ligthigmode fuction completely missing

Translation function does not work properly and is stuck at 2 (eng) 
Translation basicly works but needs tweking so thad the calles after button press and not on activation

"""



#--------------------------------------------------------------------------------Begin of code--------------------------------------------------------------------------------
def load_current_settings():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE,"r") as f:
                return json.load(f) or {}
            
        except json.JSONDecodeError as ERR:
            Translation_GUI.close()
            Error_Handeling(4250,
f"""
JSONDecodeError 
Window closed 
{ERR}
""",True)
        return {}

def get_setting(key):
    try:
        settings = load_current_settings()
    except Exception as ERR:
        Error_Handeling(4251,f"follow Error = {ERR}",False)

    return settings.get(key,f"ERR {key}")

def animate_button_click(btn_id,color_org,color_pressed):
# Shrink animation
    color_animation = QPauseAnimation(500)
    color_animation.finished.connect(lambda: reset_button(btn_id,color_animation,color_org))  
    btn_id.setStyleSheet(f"border-radius : 50px; background-color : {color_pressed}; border: 4px solid black")
    color_animation.start()

def reset_button(btn_id,color_animation,color_org):
    QTimer.singleShot(150, lambda: btn_id.setStyleSheet(f"border-radius : 50px; background-color : {color_org}; border: 4px solid black"))
        
def round_corners_mask(label,radious=0):
    path = QPainterPath()
    path.addRoundedRect(0,0,label.width(),label.height(),radious,radious)
    region = QRegion(path.toFillPolygon().toPolygon())
    label.setMask(region)

def animate_radio_button(btn_id,checked,color_org,color_pressed):
    if checked:
        btn_id.setStyleSheet(f"border-radius : 50px; background-color : {color_pressed}; border: 4px solid black")
        
    else:
        btn_id.setStyleSheet(f"border-radius : 50px; background-color : {color_org}; border: none")
        


class Reed_the_EXcelsheet(QObject):     #opens the excel file and appends the chosen language colum to the list 
                                    #colums 1 None, 2 EN (English (US)), 3 DE (German), 4 PL (Polish), 5 RO (Romanian), 6 FR (French), 7 ES (Spanisch), 8 PT (Portugese)  
    
    def __init__(self,colum_Num: int =2):

        self.colum_Num  =   colum_Num                                                   # num of the default colum in the workbook file
        self.row_Num:               int         = MasSet.row_Num_translate_dict         # is 2 (dec.2024)       # num of the start row in the workbook file
        self.num_of_rows:           int         = MasSet.num_of_rows_translate_dict     # is 124 (dec.2024)     # the number of rows to reed in succession
        self.Translate_Dictonary:   dict        = MasSet.Translate_Dictonary
        self.tranlation_file:       str         = MasSet.tranlation_file

        #fallback dictionary in case the workbook has a problem.
        self.Translate_Dictonary_Fallback: dict = MasSet.Translate_Dictonary_Fallback
        self.Reed()
        


    def Reed (self):


        try:
            openpyxl.load_workbook
            self.OpenExcelFile()

        except MemoryError as err:
            self.ERR_winow = Error_Handeling.Error_MSG_handeling(4101,"""
Memory Error, Translation file:
Loaded backup (EN)
                                                                 """,err,True) # reports the faliure to open the file and some causes to the Error handeling file.
            Home_Window.Translation_Dict = self.Translate_Dictonary_Fallback

        except SystemError as err:
            self.ERR_winow = Error_Handeling.Error_MSG_handeling(4102,"""
#System Error, Translation file:
Loaded backup (EN)
                                                                 """,err,True)
            Home_Window.Translation_Dict = self.Translate_Dictonary_Fallback

        except TimeoutError as err:
            self.ERR_winow = Error_Handeling.Error_MSG_handeling(4103,"""
#Timeout Error, Translation file:
# Loaded backup (EN)
                                                                 """,err,True)
            Home_Window.Translation_Dict = self.Translate_Dictonary_Fallback

        except FileNotFoundError as err:
            self.ERR_winow = Error_Handeling.Error_MSG_handeling(4104,"""
File Not Found Error, Translation file:
Loaded backup (EN)
                                                                 """,err,True)
            Home_Window.Translation_Dict = self.Translate_Dictonary_Fallback

        except PermissionError as err:
            self.ERR_winow = Error_Handeling.Error_MSG_handeling(4105,"""
Permission Error, Translation file:
Loaded backup (EN)
                                                                 """,err,True)
            Home_Window.Translation_Dict = self.Translate_Dictonary_Fallback

        except Exception as err:
            print (err)
            self.ERR_winow = Error_Handeling.Error_MSG_handeling(4100,"""
Exeption Error, Translation file:
Loaded backup (EN)
                                                                """,err,True)
            Home_Window.Translation_Dict = self.Translate_Dictonary_Fallback


    def OpenExcelFile(self):
    
        wb_obj  = openpyxl.load_workbook(self.tranlation_file,True)
        sheet_obj = wb_obj.active

        key_iteration = iter(self.Translate_Dictonary)                                              # iterates over the Excel sheet one cell at a time
        while not self.row_Num == self.num_of_rows:                                                 # reeds the content of the file 

            self.key = next(key_iteration)                                                          # set next key for iteration
            self.cell_Item =     sheet_obj.cell   (row=self.row_Num,     column=self.colum_Num)     # selects the aproprate cell e.g. (row,colum) 136 D (136,4)
            if self.cell_Item.value == None:
                self.Translate_Dictonary[self.key] = self.Translate_Dictonary_Fallback.get(self.key)
            else:
                self.Translate_Dictonary[self.key] = self.cell_Item.value                               # asigns the curently accessed key/value pair the cell value 
            self.row_Num +=1                                                                        # row +1 for the while loop

        Home_Window.Translation_Dict = self.Translate_Dictonary

class Translation_GUI(QWidget):     #creates the window

    def __init__(self):
        super().__init__()

        self.Transparen_color_int   = MasSet.Transparencolor
        self.Font                   = MasSet.Fonttype_1
        self.letter_size_Large      = MasSet.letter_size_Big
        self.letter_size_Mid        = MasSet.letter_size_Medium
        self.DarkmodeColor          = MasSet.DarkmodeColor
        self.company_logo           = MasSet.img_company_logo
        self.close_window_icon      = MasSet.close_window_icon_RD
        self.Flag_Heigth_ST         = MasSet.Flag_Heigth
        self.Flag_Legth_ST          = MasSet.Flag_Legth
        
        self.init_UI()

    def init_UI(self): #Buttons, Flags, layout

        def LanguageButton(self, Language,  ImagePath, 
                           Font = self.Font, Letter_size = self.letter_size_Large, Transparent_color = self.Transparen_color_int, 
                           min_heigth_Widget = self.Flag_Heigth_ST, min_legth_widget = self.Flag_Legth_ST): # crates singular QWidget fom 3 QLabels (selected icon (Grreen Box) / Flag image / language as text)
            
            str_length              =   len(Language)
            textbox_size_W          =   (str_length*Letter_size)+10
            textbox_size_H          =   Letter_size+10


            empty = QLabel("")
            empty.setStyleSheet(f"border: 0px; background-color : {Transparent_color};")
            empty.setFixedSize(50,50)
            
            # Create flag image label
            flag_img = QLabel("",self)
            flag_pixmap = QPixmap(ImagePath)
            flag_pixmap_scaled = flag_pixmap.scaledToHeight(min_heigth_Widget)
            flag_img.setPixmap(flag_pixmap_scaled)
            flag_img.setFixedSize(min_legth_widget,min_heigth_Widget)
            flag_img.setStyleSheet(f"border-radius : 50px; border: 0px; background-color : {Transparent_color};")
            round_corners_mask(flag_img,50)

            # Create language text label
            langugage_txt = QLabel(Language,self)
            langugage_txt.setMinimumSize(textbox_size_W,textbox_size_H)
            langugage_txt.setFont(QFont(Font,Letter_size))
            langugage_txt.setStyleSheet(f"border-radius : 50px; border: 0px; background-color : {Transparent_color}; font-weight : bold; padding:{Letter_size/2}")



            layout = QHBoxLayout()
            layout.setSpacing (1)
            layout.addWidget(empty,1)
            layout.addWidget(flag_img,2)
            layout.addWidget(langugage_txt,3)

            return layout
        
        self.setWindowTitle(("Translation"))
        self.setWindowIcon(QIcon(self.company_logo))
        self.setMinimumSize(1200,1400)
        self.setStyleSheet(f"background-color :{self.DarkmodeColor};")


        # Header Button
        self.btn_window_header = QPushButton("")
        self.btn_window_header.setFixedHeight(125)
        self.btn_window_header.setStyleSheet(f"background-color : {MasSet.DarkmodeColor_header}; border: none")
        self.btn_window_header.setLayout(prefab.window_header.init_Header(MasSet.tranlation_icon,"window_title_5",MasSet.Translate_Dictonary_Fallback))
        self.btn_window_header.clicked.connect(self.close)

        self.language_btn_layout = QGridLayout()

        if get_setting("EN") == True: #english
            self.BTN_EN     =   QRadioButton("")
            self.BTN_EN.setMinimumSize(500,150)
            self.BTN_EN.setStyleSheet("border : none;")
            self.BTN_EN.setLayout(LanguageButton (self, "English", MasSet.Flag_images_dict.get(random.choice(["GB","US"]))))
            self.language_btn_layout.addWidget (self.BTN_EN, 1, 2)          # calls the LanguageButton Creator

            self.BTN_EN.toggled.connect(lambda checked:animate_radio_button(self.BTN_EN,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_EN.clicked.connect(lambda :Reed_the_EXcelsheet(2))
        
        if get_setting("DE") == True: #german
            self.BTN_DE     =   QRadioButton("")
            self.BTN_DE.setMinimumSize(500,150)
            self.BTN_DE.setStyleSheet("border : none;")
            self.BTN_DE.setLayout(LanguageButton (self, "Deutsch", MasSet.Flag_images_dict.get("DE")))
            self.language_btn_layout.addWidget (self.BTN_DE, 1, 3)

            self.BTN_DE.toggled.connect(lambda checked:animate_radio_button(self.BTN_DE,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_DE.clicked.connect(lambda :Reed_the_EXcelsheet(3))

        if get_setting("PL") == True: #polish
            self.BTN_PL     =   QRadioButton("")
            self.BTN_PL.setMinimumSize(500,150)
            self.BTN_PL.setStyleSheet("border : none;")
            self.BTN_PL.setLayout(LanguageButton (self, "Polski", MasSet.Flag_images_dict.get("PL")))
            self.language_btn_layout.addWidget (self.BTN_PL, 2, 2)

            self.BTN_PL.toggled.connect(lambda checked:animate_radio_button(self.BTN_PL,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_PL.clicked.connect(lambda :Reed_the_EXcelsheet(4))

        if get_setting("RO") == True: #romainian
            self.BTN_RO     =   QRadioButton("")
            self.BTN_RO.setMinimumSize(500,150)
            self.BTN_RO.setStyleSheet("border : none;")
            self.BTN_RO.setLayout(LanguageButton (self, "Română", MasSet.Flag_images_dict.get("RO")))
            self.language_btn_layout.addWidget (self.BTN_RO, 2, 3)

            self.BTN_RO.toggled.connect(lambda checked:animate_radio_button(self.BTN_RO,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_RO.clicked.connect(lambda :Reed_the_EXcelsheet(5))

        if get_setting("FR") == True: #french
            self.BTN_FR     =   QRadioButton("")
            self.BTN_FR.setMinimumSize(500,150)
            self.BTN_FR.setStyleSheet("border : none;")
            self.BTN_FR.setLayout(LanguageButton (self, "Français", MasSet.Flag_images_dict.get("FR")))
            self.language_btn_layout.addWidget (self.BTN_FR, 3, 2)

            self.BTN_FR.toggled.connect(lambda checked:animate_radio_button(self.BTN_FR,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_FR.clicked.connect(lambda :Reed_the_EXcelsheet(6))

        if get_setting("ES") == True: #spanish
            self.BTN_ES     =   QRadioButton("")
            self.BTN_ES.setMinimumSize(500,150)
            self.BTN_ES.setStyleSheet("border : none;")
            self.BTN_ES.setLayout(LanguageButton (self, "Español", MasSet.Flag_images_dict.get("ES")))
            self.language_btn_layout.addWidget (self.BTN_ES, 3, 3)

            self.BTN_ES.toggled.connect(lambda checked:animate_radio_button(self.BTN_ES,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_ES.clicked.connect(lambda :Reed_the_EXcelsheet(7))

        if get_setting("PT") == True: #portugese
            self.BTN_PT     =   QRadioButton("")
            self.BTN_PT.setMinimumSize(500,150)
            self.BTN_PT.setStyleSheet("border : none;")
            self.BTN_PT.setLayout(LanguageButton (self, "Portugués", MasSet.Flag_images_dict.get("PT")))
            self.language_btn_layout.addWidget (self.BTN_PT, 4, 2)

            self.BTN_PT.toggled.connect(lambda checked:animate_radio_button(self.BTN_PT,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_PT.clicked.connect(lambda :Reed_the_EXcelsheet(8))

        if get_setting("AL") == True: #albanian
            self.BTN_AL     =   QRadioButton("")
            self.BTN_AL.setMinimumSize(500,150)
            self.BTN_AL.setStyleSheet("border : none;")
            self.BTN_AL.setLayout(LanguageButton (self, "Shqip", MasSet.Flag_images_dict.get("AL")))
            self.language_btn_layout.addWidget (self.BTN_AL, 4, 3)

            self.BTN_AL.toggled.connect(lambda checked:animate_radio_button(self.BTN_AL,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_AL.clicked.connect(lambda :Reed_the_EXcelsheet(9))

        if get_setting("LV") == True: #latvian
            self.BTN_LV     =   QRadioButton("")
            self.BTN_LV.setMinimumSize(500,150)
            self.BTN_LV.setStyleSheet("border : none;")
            self.BTN_LV.setLayout(LanguageButton (self, "Latviešu", MasSet.Flag_images_dict.get("LV")))
            self.language_btn_layout.addWidget (self.BTN_LV, 5, 2)

            self.BTN_LV.toggled.connect(lambda checked:animate_radio_button(self.BTN_LV,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_LV.clicked.connect(lambda :Reed_the_EXcelsheet(10))

        if get_setting("LT") == True: #lithuanian
            self.BTN_LT     =   QRadioButton("")
            self.BTN_LT.setMinimumSize(500,150)
            self.BTN_LT.setStyleSheet("border : none;")
            self.BTN_LT.setLayout(LanguageButton (self, "Lietuvių", MasSet.Flag_images_dict.get("LT")))
            self.language_btn_layout.addWidget (self.BTN_LT, 5, 3)

            self.BTN_LT.toggled.connect(lambda checked:animate_radio_button(self.BTN_LT,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_LT.clicked.connect(lambda :Reed_the_EXcelsheet(11))

        if get_setting("UA") == True: #ukrainian
            self.BTN_UA     =   QRadioButton("")
            self.BTN_UA.setMinimumSize(500,150)
            self.BTN_UA.setStyleSheet("border : none;")
            self.BTN_UA.setLayout(LanguageButton (self, "Українська", MasSet.Flag_images_dict.get("UA")))
            self.language_btn_layout.addWidget (self.BTN_UA, 6, 2)

            self.BTN_UA.toggled.connect(lambda checked:animate_radio_button(self.BTN_UA,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_UA.clicked.connect(lambda :Reed_the_EXcelsheet(12))

        if get_setting("RU") == True: #russian
            self.BTN_RU     =   QRadioButton("")
            self.BTN_RU.setMinimumSize(500,150)
            self.BTN_RU.setStyleSheet("border : none;")
            self.BTN_RU.setLayout(LanguageButton (self, "Русский", MasSet.Flag_images_dict.get("RU")))
            self.language_btn_layout.addWidget (self.BTN_RU, 6, 3)

            self.BTN_RU.toggled.connect(lambda checked:animate_radio_button(self.BTN_RU,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_RU.clicked.connect(lambda :Reed_the_EXcelsheet(13))

        if get_setting("TR") == True: #turkish
            self.BTN_TR     =   QRadioButton("")
            self.BTN_TR.setMinimumSize(500,150)
            self.BTN_TR.setStyleSheet("border : none;")
            self.BTN_TR.setLayout(LanguageButton (self, "Türkçe", MasSet.Flag_images_dict.get("TR")))
            self.language_btn_layout.addWidget (self.BTN_TR, 7, 2)

            self.BTN_TR.toggled.connect(lambda checked:animate_radio_button(self.BTN_TR,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_TR.clicked.connect(lambda :Reed_the_EXcelsheet(14))
        
        if get_setting("SA") == True: #arabic
            self.BTN_SA     =   QRadioButton("")
            self.BTN_SA.setMinimumSize(500,150)
            self.BTN_SA.setStyleSheet("border : none;")
            self.BTN_SA.setLayout(LanguageButton (self, "العربية", MasSet.Flag_images_dict.get("SA")))
            self.language_btn_layout.addWidget (self.BTN_SA, 7, 3)

            self.BTN_SA.toggled.connect(lambda checked:animate_radio_button(self.BTN_SA,checked,MasSet.Transparencolor,MasSet.DarkmodeColor_header))
            self.BTN_SA.clicked.connect(lambda :Reed_the_EXcelsheet(15))
        
        
        self.window_main = QWidget()
        self.window_main.setStyleSheet(f"background-color : {MasSet.DarkmodeColor};")
        self.window_main.setLayout(self.language_btn_layout)


        self.organization = QVBoxLayout()

        self.organization.setContentsMargins (0,0,0,0)
        self.organization.addWidget(self.btn_window_header)
        self.organization.addWidget(self.window_main)
        self.setLayout(self.organization)


class Translation_Handeling():
    def __init__(self): 
        super().__init__()
        self.open()

    def open (self):
        
        self.window = Translation_GUI()
        self.window.show()

      
#_________________main window____________________
class Machinery_Visualization(QGraphicsView):
    def __init__(self, window_size_W :int = 2560, window_size_H :int = 1600):
        super().__init__()

        self.window_size_W = window_size_W
        self.window_size_H = window_size_H
        self.reference_W = 2560
        self.reference_H = 1600

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setStyleSheet(f"background-color : {MasSet.DarkmodeColor};border : none")
        self.part_items = {} # Dict to hold part items

        self.init_view()

    def init_view(self):
        base_pixmap = QPixmap(MasSet.img_CL_Topview_Table_outline)
        base_pixmap_scaled = QPixmap(base_pixmap).scaledToWidth(int(self.window_size_W*.8))
        base_item = QGraphicsPixmapItem(base_pixmap_scaled)
        self.scene.addItem(base_item)

        Table_Poly = self.poly_part_overlay(QPolygonF([self.scale_point(1780, 20),self.scale_point(1780, 360),self.scale_point(1880,360),self.scale_point(1905, 335),self.scale_point(1905, 20),self.scale_point (1905,45),self.scale_point(1880,20)]),"Table")      
        RB_01_poly = self.poly_part_overlay(QPolygonF([self.scale_point(1450, 65),self.scale_point(1450, 190),self.scale_point(1775, 190),self.scale_point(1775, 40)]),"RB_01")
        RB_02_poly = self.poly_part_overlay(QPolygonF([self.scale_point(1450, 190),self.scale_point(1450,345),self.scale_point(1775, 345),self.scale_point(1775, 190)]),"RB_02")
        RB_03_poly = self.poly_part_overlay(QPolygonF([self.scale_point(1130, 100),self.scale_point(1130, 190),self.scale_point(1450, 190),self.scale_point(1450, 65)]),"RB_03")
        RB_04_poly = self.poly_part_overlay(QPolygonF([self.scale_point(1130, 190),self.scale_point(1130,285),self.scale_point(1350,345),self.scale_point(1450, 345),self.scale_point(1450, 190)]),"RB_04")
        GF_05_poly = self.poly_part_overlay(QPolygonF([self.scale_point(810, 100),self.scale_point(810, 285),self.scale_point(1130, 285),self.scale_point(1130, 100)]),"RB_05")
        GF_05_movent_box_1_poly = self.poly_part_overlay(QPolygonF([self.scale_point(810, 95),self.scale_point(810, 40),self.scale_point(1130, 40),self.scale_point(1130,95)]),"RB_05_movent_box_1")
        GF_05_movent_box_2_poly = self.poly_part_overlay(QPolygonF([self.scale_point(810, 285),self.scale_point(810, 345),self.scale_point(1130, 345),self.scale_point(1130,285)]),"RB_05_movent_box_2")
        GK_06_poly = self.poly_part_overlay(QPolygonF
                                           ([self.scale_point(420, 280),self.scale_point(570, 395),self.scale_point(630, 345),self.scale_point(690, 310),self.scale_point(740, 295),                                        #lower curve
                                             self.scale_point(810, 285),self.scale_point(810, 100),self.scale_point(740, 100),self.scale_point(650, 120),self.scale_point(550, 170),self.scale_point(480, 220)]),"RB_06")   #upper curve
        GF_07_poly = self.poly_part_overlay(QPolygonF([self.scale_point(420, 285),self.scale_point(255, 500),self.scale_point(405, 615),self.scale_point(570, 400)]),"GF_07")
        GF_08_poly = self.poly_part_overlay(QPolygonF([self.scale_point(255,508),self.scale_point(80,735),self.scale_point(230,848),self.scale_point(400, 620)]),"GF_08")
        RF_09_poly = self.poly_part_overlay(QPolygonF([self.scale_point(75, 735),self.scale_point(40, 785),self.scale_point(18, 1130),self.scale_point(225, 850)]),"RF_09")

        self.part_items["Table"] = Table_Poly
        self.part_items["RB_01"] = RB_01_poly
        self.part_items["RB_02"] = RB_02_poly
        self.part_items["RB_03"] = RB_03_poly
        self.part_items["RB_04"] = RB_04_poly
        self.part_items["RB_05"] = GF_05_poly
        self.part_items["RB_05_movent_box_1"] = GF_05_movent_box_1_poly
        self.part_items["RB_05_movent_box_2"] = GF_05_movent_box_2_poly
        self.part_items["RB_06"] = GK_06_poly
        self.part_items["GF_07"] = GF_07_poly
        self.part_items["GF_08"] = GF_08_poly

    def poly_part_overlay(self, polygon, part_name):
        poly_item = self.scene.addPolygon(polygon)
        poly_item.setBrush(QBrush(QColor(128, 128, 128, 100)))  # Grey transparent
        #poly_item.setBrush(QBrush(QColor(0, 225, 0, 100))) # Green transparent
        poly_item.setPen(QPen(Qt.NoPen))  # No border
        poly_item.setZValue(-1)  # Below base image
        poly_item.setVisible(True)
        return poly_item

    def update_part_state(self, part_name, state):
        part = self.part_items.get(part_name)
        if not part:
            return
        
        if state == "ready":
            part.setBrush(QBrush(QColor(128, 128, 128, 100))) # Grey

        if state == "normal":
            part.setBrush(QBrush(QColor(0, 255, 0, 100)))  # Green
            part.setVisible(True)
        
        elif state == "error":
            part.setBrush(QBrush(QColor(255, 0, 0, 100)))  # Red
            part.setVisible(True)
        
        elif state == "warning":
            part.setBrush(QBrush(QColor(255, 255, 0, 100)))  # Yellow
            part.setVisible(True)
        
        elif state == "maintanance":
            part.setBrush(QBrush(QColor(0, 0, 255, 100))) # Blue
            part.setVisible(True)
        
        elif state == "hidden":
            part.setVisible(False)

    def scale_point(self, x, y):
        scale_x = self.window_size_W / self.reference_W
        scale_y = self.window_size_H / self.reference_H
        return QPointF(x * scale_x, y * scale_y)

class Home_Window(QMainWindow):      #the main window GUI Window / Home Window

    def __init__(self, window_size_W :int = 2560, window_size_H :int = 1600):
        super().__init__()

        self.Transparent        = Transparencolor
        self.Green_color        = Green_color
        self.Red_color          = Red_color
        self.Orange_color       = Orange_color
        self.settings_icon      = settings_icon
        self.ligtingmode_icon   = ligtingmode_icon
        self.tranlation_icon    = tranlation_icon
        self.help_icon          = help_icon
        self.info_icon          = info_icon
        self.Font               = Fonttype_1
        self.window_size_W      = window_size_W
        self.window_size_H      = window_size_H
        self.Letter_size_L      = letter_size_Big
        self.Letter_size_M      = letter_size_Medium
        self.Translation_Dict   = MasSet.Translate_Dictonary_Fallback
        Home_Window.Translation_Dict = MasSet.Translate_Dictonary_Fallback

        self.basic_btn_size_X   = MasSet.start_stop_clear_btn_size_X
        self.basic_btn_size_Y   = MasSet.start_stop_clear_btn_size_Y




        self.setWindowTitle(f"PTU GUI {Gui_ver}")                                              #window title + GUI version
        self.setGeometry(200,200,2000,1200)                                                 #windowstartsize (is launched in fullscren anyway)
        self.setWindowIcon(QIcon(company_logo))                                             #window icon
        label_background = QLabel (self)
        label_background.setGeometry(-10,-10,self.window_size_W+15,self.window_size_H+15)
        label_background.setStyleSheet("background-color :" + DarkmodeColor)          # sets the GUI to Ligthmode
        
        self.current_language = Translation_Dict.get("language_long")


        self.central_widget = QWidget()  
        self.setCentralWidget(self.central_widget)


        self.window_header          =   QLabel("",self)
        self.visualization_widget   =   QLabel("",self)
        self.empty_label            =   QLabel("",self)
        self.control_btn            =   QLabel("",self)
        self.current_language       =   QLabel(self.Translation_Dict.get("language_long"),self)
        self.Translation_icon       =   QLabel("",self)
        self.start_txt              =   QLabel(self.Translation_Dict.get("start_cl"),self)
        self.start_icon             =   QSvgWidget(MasSet.ON_Icon)
        self.stop_txt               =   QLabel(self.Translation_Dict.get("stop_cl"),self)
        self.stop_icon              =   QSvgWidget(MasSet.OFF_Icon)
        self.reset_txt              =   QLabel(self.Translation_Dict.get("clear_event"),self)
        self.reset_icon             =   QSvgWidget(MasSet.reset_Icon)

        self.btn_start_CL       =   QPushButton("",self)
        self.btn_stop_CL        =   QPushButton("",self)
        self.btn_clear_event    =   QPushButton("",self)
        self.btn_settingsmenu   =   QPushButton("",self)
        self.btn_translate_Menu =   QPushButton("",self)
        self.btn_open_Help_menu =   QPushButton("",self)
        self.btn_Info_Open      =   QPushButton("",self)

        self.initUI()


    def initUI(self): #Buttons and layout

        #Sub_Windows.Settings_window.connect_keypad()

        def Header():
        
            str_legth =   len(self.Translation_Dict.get("language_long"))*self.Letter_size_M

            #opens the tranlation menu
    
            Translation_icon_pixmap     =QPixmap(self.tranlation_icon)
            Translation_icon_scaled     =Translation_icon_pixmap.scaledToHeight(MasSet.menu_buttonsize_L)

            self.Translation_icon.setBaseSize(MasSet.menu_buttonsize_L,MasSet.menu_buttonsize_L)
            self.Translation_icon.setPixmap(Translation_icon_scaled)
            self.Translation_icon.setStyleSheet(f"""background-color : {self.Transparent};border : none""")
        
            # shows the current language
            self.current_language.setMinimumSize(str_legth,MasSet.menu_buttonsize_L)
            self.current_language.setStyleSheet(f"background-color : {self.Transparent};font-weight : bold;")
            self.current_language.setFont(QFont(self.Font,self.Letter_size_M))
            self.current_language.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)            

            language_btn_layout = QHBoxLayout()

            language_btn_layout.setContentsMargins (0,0,0,0)
            language_btn_layout.addWidget(self.Translation_icon)
            language_btn_layout.addWidget(self.current_language)

            
            #more settings menu
            settingsmenu_icon_pixmap    =QPixmap(self.settings_icon)
            settingsmenu_icon_scaled    =settingsmenu_icon_pixmap.scaledToHeight(MasSet.menu_buttonsize_L-60)
            settingsmenu_icon           =QIcon(settingsmenu_icon_scaled)
            self.btn_settingsmenu.setIcon(settingsmenu_icon)
            self.btn_settingsmenu.setIconSize(settingsmenu_icon_scaled.size())
            self.btn_settingsmenu.setStyleSheet("border : none")
            self.btn_settingsmenu.setAttribute(Qt.WA_TranslucentBackground, True)
            self.btn_settingsmenu.clicked.connect(lambda checked : self.OpenSubwindow(Sub_Windows.Handeler("Settings",Home_Window.Translation_Dict)))

            #opens the help menu
            if get_setting("user_help_enabled"): #if the user help is enabled the help button is shown
                Help_menu_icon_pixmap       =QPixmap(self.help_icon)
                Help_menu_icon_scaled       =Help_menu_icon_pixmap.scaledToHeight(MasSet.menu_buttonsize_L-60)
                Help_menu_icon              =QIcon(Help_menu_icon_scaled)
                self.btn_open_Help_menu.setIcon(Help_menu_icon)
                self.btn_open_Help_menu.setIconSize(Help_menu_icon_scaled.size())
                self.btn_open_Help_menu.setStyleSheet(f"background-color : {self.Transparent};border : none")
                self.btn_open_Help_menu.clicked.connect(lambda checked : self.OpenSubwindow(Sub_Windows.Handeler("help",Home_Window.Translation_Dict)))
                
            #opens the info menu
            Info_icon_pixmap            =QPixmap(self.info_icon)
            Info_icon_scaled            =Info_icon_pixmap.scaledToHeight(MasSet.menu_buttonsize_L-60)
            Info_icon_                  =QIcon(Info_icon_scaled)
            self.btn_Info_Open.setIcon(Info_icon_)
            self.btn_Info_Open.setIconSize(Info_icon_scaled.size())
            self.btn_Info_Open.setStyleSheet("border : none")
            self.btn_Info_Open.setAttribute(Qt.WA_TranslucentBackground, True)
            self.btn_Info_Open.clicked.connect(lambda checked: self.OpenSubwindow(Sub_Windows.Handeler("info",Home_Window.Translation_Dict)))

            if get_setting("user_language_enabled"):  #if the user language is enabled the translation button is shown, if disabled the backup language is loaded
                self.btn_translate_Menu.setLayout(language_btn_layout)
                self.btn_translate_Menu.setMinimumSize(750,MasSet.menu_buttonsize_L)
                self.btn_translate_Menu.clicked.connect(lambda checked: self.OpenSubwindow(Translation_Handeling()))
            
            
            self.empty_label.setStyleSheet("border : none;")
            self.empty_label.setAttribute(Qt.WA_TranslucentBackground, True)

            self.empty_label.setMinimumWidth(MasSet.menu_buttonsize_M)
            
            layout = QHBoxLayout()
            layout.setContentsMargins (0,0,0,0)
            
            layout.addWidget(self.btn_translate_Menu)
            layout.addWidget(self.empty_label)
            layout.addWidget(self.empty_label)
            layout.addWidget(self.empty_label)
            layout.addWidget(self.empty_label)
            layout.addWidget(self.btn_open_Help_menu)
            layout.addWidget(self.btn_Info_Open)
            layout.addWidget(self.btn_settingsmenu)

            return layout

        def Control_btn (): #creates the control buttons for the CL

            #_________________CL control btn____________________
            
            #Start CL
            self.start_icon.setFixedSize(MasSet.menu_buttonsize_M, MasSet.menu_buttonsize_M)
            self.start_icon.setStyleSheet("border: 0px solid black;")
            self.start_icon.setAttribute(Qt.WA_TranslucentBackground, True)
            
            start_icon_wrapper = QWidget()
            start_icon_wrapper.setFixedSize(MasSet.menu_buttonsize_M, MasSet.menu_buttonsize_M)
            start_icon_wrapper.setStyleSheet("border: 0px solid black;")
            start_icon_wrapper.setAttribute(Qt.WA_TranslucentBackground, True)
            
            start_icon_layout = QVBoxLayout(start_icon_wrapper)
            start_icon_layout.setContentsMargins(5,0,0,0)
            start_icon_layout.addWidget(self.start_icon, alignment=Qt.AlignCenter)

            self.start_txt.setMinimumSize(200,MasSet.menu_buttonsize_M)
            self.start_txt.setStyleSheet("font-weight : bold; border: 0px solid black")
            self.start_txt.setAttribute(Qt.WA_TranslucentBackground, True)
            self.start_txt.setFont(QFont(self.Font,self.Letter_size_L))
            self.start_txt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            btn_start_Layout = QHBoxLayout()
            btn_start_Layout.setContentsMargins (5,0,0,0)
            btn_start_Layout.addWidget(start_icon_wrapper)
            btn_start_Layout.addWidget(self.start_txt)

            self.btn_start_CL.setFixedSize(self.basic_btn_size_X,self.basic_btn_size_Y)
            self.btn_start_CL.setLayout(btn_start_Layout)
            self.btn_start_CL.setStyleSheet(f"border-radius : 50px; background-color : {MasSet.Green_color}; border: 4px solid black")
            self.btn_start_CL.clicked.connect(lambda: animate_button_click(self.btn_start_CL,self.Green_color,MasSet.Dark_green_color))

            #Stop CL
            
            self.stop_icon.setFixedSize(MasSet.menu_buttonsize_M, MasSet.menu_buttonsize_M)
            self.stop_icon.setStyleSheet("border: 0px solid black;")
            self.stop_icon.setAttribute(Qt.WA_TranslucentBackground, True)
            
            stop_icon_wrapper = QWidget()
            stop_icon_wrapper.setFixedSize(MasSet.menu_buttonsize_M, MasSet.menu_buttonsize_M)
            stop_icon_wrapper.setStyleSheet("border: 0px solid black;")
            stop_icon_wrapper.setAttribute(Qt.WA_TranslucentBackground, True)
            
            stop_icon_layout = QVBoxLayout(stop_icon_wrapper)
            stop_icon_layout.setContentsMargins(0,0,0,0)
            stop_icon_layout.addWidget(self.stop_icon, alignment=Qt.AlignCenter)

            self.stop_txt.setMinimumSize(200,MasSet.menu_buttonsize_M)
            self.stop_txt.setStyleSheet("font-weight : bold; border: 0px solid black")
            self.stop_txt.setAttribute(Qt.WA_TranslucentBackground, True)
            self.stop_txt.setFont(QFont(self.Font,self.Letter_size_L))
            self.stop_txt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            btn_stop_Layout = QHBoxLayout()
            btn_stop_Layout.setContentsMargins (5,0,0,0)
            btn_stop_Layout.addWidget(stop_icon_wrapper)
            btn_stop_Layout.addWidget(self.stop_txt)

            self.btn_stop_CL.setFixedSize(self.basic_btn_size_X,self.basic_btn_size_Y)
            self.btn_stop_CL.setLayout(btn_stop_Layout)
            self.btn_stop_CL.setStyleSheet(f"border-radius : 50px; background-color : {self.Red_color}; border: 4px solid black")
            self.btn_stop_CL.clicked.connect(lambda: animate_button_click(self.btn_stop_CL,self.Red_color,MasSet.Dark_red_color))

            #Clear Event

            
            self.reset_icon.setFixedSize(MasSet.menu_buttonsize_M, MasSet.menu_buttonsize_M)
            self.reset_icon.setStyleSheet("border: 0px solid black;")
            self.reset_icon.setAttribute(Qt.WA_TranslucentBackground, True)
            
            reset_icon_wrapper = QWidget()
            reset_icon_wrapper.setFixedSize(MasSet.menu_buttonsize_M, MasSet.menu_buttonsize_M)
            reset_icon_wrapper.setStyleSheet("border: 0px solid black;")
            reset_icon_wrapper.setAttribute(Qt.WA_TranslucentBackground, True)
            
            reset_icon_layout = QVBoxLayout(reset_icon_wrapper)
            reset_icon_layout.setContentsMargins(0,0,0,0)
            reset_icon_layout.addWidget(self.reset_icon, alignment=Qt.AlignCenter)

            self.reset_txt.setMinimumSize(200,MasSet.menu_buttonsize_M)
            self.reset_txt.setStyleSheet("font-weight : bold; border: 0px solid black")
            self.reset_txt.setAttribute(Qt.WA_TranslucentBackground, True)
            self.reset_txt.setFont(QFont(self.Font,self.Letter_size_L))
            self.reset_txt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            btn_stop_Layout = QHBoxLayout()
            btn_stop_Layout.setContentsMargins (5,0,0,0)
            btn_stop_Layout.addWidget(reset_icon_wrapper)
            btn_stop_Layout.addWidget(self.reset_txt)

            self.btn_clear_event.setFixedSize(self.basic_btn_size_X,self.basic_btn_size_Y)
            self.btn_clear_event.setLayout(btn_stop_Layout)
            self.btn_clear_event.setStyleSheet(f"border-radius : 50px; background-color : {self.Orange_color}; border: 4px solid black")
            self.btn_clear_event.clicked.connect(lambda: animate_button_click(self.btn_clear_event,self.Orange_color,MasSet.Dark_orange_color))

            #_________________CL control btn Layout____________________
            control_btn = QHBoxLayout()

            control_btn.addWidget (self.btn_stop_CL)
            control_btn.addWidget (self.btn_start_CL)
            control_btn.addWidget (self.btn_clear_event)

            return control_btn
        

        self.visualization_widget = Machinery_Visualization(window_size_W=self.window_size_W, window_size_H=self.window_size_H)
        self.visualization_widget.setMaximumWidth(int(self.window_size_W*0.8)) # sets the max width of the visualization widget to 80% of the window size
        self.visualization_widget.setMinimumWidth(int(self.window_size_W*0.8)) # sets the min width of the visualization widget to 80% of the window size
        self.visualization_widget.setMinimumHeight(int(self.window_size_H*0.75)) # sets the min height of the visualization widget to 80% of the window size
        self.visualization_widget.setMaximumHeight(int(self.window_size_H*0.75)) # sets the max height of the visualization widget to 80% of the window size
        self.visualization_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    

        self.window_header.setFixedHeight(200)
        self.window_header.setStyleSheet(f"background-color : {MasSet.DarkmodeColor_header};border : none")
        self.window_header.setLayout(Header())

        self.control_btn.setStyleSheet(f"background-color : {MasSet.DarkmodeColor_footer};border : none")
        self.control_btn.setLayout(Control_btn())

        #_________________Layouts____________________
        
        self.window_main = QVBoxLayout()     
        self.window_main.setContentsMargins (0,0,0,0)

        self.window_main.addWidget(self.visualization_widget)
        self.window_main.addWidget(self.control_btn)

        #_________________master Layout____________________

        self.language_btn_layout = QVBoxLayout()
        self.language_btn_layout.setContentsMargins (0,0,0,0)

        self.language_btn_layout.addWidget(self.window_header)
        self.language_btn_layout.addLayout(self.window_main)

        self.central_widget.setLayout(self.language_btn_layout)

        # timer to update the GUI
        self.timer = QTimer(self)
        self.timer.timeout.connect (self.update_label)
        self.timer.start(5000) # 5000ms = 5 seconds

    def update_label(self):
        self.current_language.setText(Home_Window.Translation_Dict.get("language_long")) #updates the language label
        self.start_txt.setText(Home_Window.Translation_Dict.get("start_cl"))
        self.stop_txt.setText(Home_Window.Translation_Dict.get("stop_cl"))
        self.reset_txt.setText(Home_Window.Translation_Dict.get("clear_event"))

    def OpenSubwindow (self,subwindow):
        self.start_window = subwindow
        



  




def main():
    app = QApplication(sys.argv)
    Desktop = QDesktopWidget()
    screen_geometry = Desktop.screenGeometry()
    width = screen_geometry.width()
    heith = screen_geometry.height()
    window = Home_Window(width,heith)                          # constructs the window
    window.show()                                   # opens a window
#    window.showFullScreen()                        # opens the window in fullscren
 
    sys.exit(app.exec_())                           # exits the window constructor

if __name__ == "__main__":
    main()
            
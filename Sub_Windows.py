import sys
import os
import vlc
import time
import datetime
import Error_Handeling
import Logger
import MasterSettings as MasSet
import prefab_window_elements as prefab #siple prefabs including the header or a keypad
import sqlite3 #to reed the number of parcels and calculate the number of events
import json #to write and save settings
import numpy as np #to plot data
import matplotlib.pyplot as plt #to plot data


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#__________________________________________________Decorative constants__________________________________________________

DarkmodeColor       :str =    MasSet.DarkmodeColor # to be replaced by function
Transparencolor     :str =    MasSet.Transparencolor
Fonttype_1          :str =    MasSet.Fonttype_1
letter_size_Big     :int =    MasSet.letter_size_Big
letter_size_Medium  :int =    MasSet.letter_size_Medium
letter_size_Smal    :int =    MasSet.letter_size_Smal
 
company_logo        :str =    MasSet.img_company_logo
close_window_icon   :str =    MasSet.close_window_icon_RD
GUI_main_color      :str =    MasSet.DarkmodeColor
GUI_header_color    :str =    MasSet.DarkmodeColor_header
GUI_footer_color    :str =    MasSet.DarkmodeColor_footer


help_icon           :str =   MasSet.help_icon               #100px  X   100px
info_icon           :str =   MasSet.info_icon               #100px  X   100px
settings_icon       :str =   MasSet.settings_icon           #100px  X   100px

CONFIG_FILE_PARCEL = MasSet.parlcel_dimesions.path_parcel_settings_json

#--------------------------------------------------------------------------------Begin of code--------------------------------------------------------------------------------

def load_current_settings():
    if os.path.exists(CONFIG_FILE_PARCEL):
        try:
            with open(CONFIG_FILE_PARCEL,"r") as f:
                return json.load(f) or {}
            
        except json.JSONDecodeError as ERR:
            Admin.close()
            Technic.close()
            Error_Handeling(4200,
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
        Technic.close()
        Admin.close()
        Error_Handeling(4201,f"follow Error = {ERR}",False)
    return settings.get(key,f"ERR {key}")



#_________________infomation window____________________
class info_window(QWidget):

    def __init__(self,Translation_Dict: dict):
        super().__init__()


        self.Translation_Dict       = Translation_Dict
        self.Transparent            = Transparencolor
        self.Font                   = Fonttype_1
        self.letter_size_smal       = letter_size_Smal
        self.letter_size_Medium     = letter_size_Medium
        self.letter_size_Large      = letter_size_Big
        self.DarkmodeColor          = DarkmodeColor
        self.company_logo           = company_logo
        self.close_window_icon      = close_window_icon
        self.info_icon              = info_icon
        self.GUI_header             = GUI_header_color
        self.GUI_footer             = GUI_footer_color
        self.GUI_color              = DarkmodeColor           


        self.setWindowTitle(self.Translation_Dict.get("window_title_3"))
        self.setWindowIcon(QIcon(self.company_logo))
        self.setMinimumSize(400,400)
        self.setStyleSheet(f"background-color :{self.DarkmodeColor}")
        self.central_widget = QWidget()

        #self.btn_closewindow_info = QPushButton ("",self)
        self.btn_window_header              = QPushButton ("",self)
        self.window_main                    = QWidget ()
        
        self.init_UI()



    def close_window(self):
        self.close()

    def init_UI(self): #Buttons and layout
        

        # the str value for the infoscreen (if not name)
        
        self.StandardBackground: str = f"background-color :{self.Transparent}; font-weight : bold;"

        
        self.init_INFO_UI()
    
    

    def patent_Info (self):             # shows patent related data (gov organisation and file number)
        
        
        # patent NR  US (USPO)
        self.label_US = QLabel (f"{self.Translation_Dict.get("us_patent")}: ")
        self.label_US.setStyleSheet(self.StandardBackground)
        self.label_US.setFont(QFont(self.Font,self.letter_size_smal))
        
        self.label_US_NR= QLabel (MasSet.Nr_USPO)
        self.label_US_NR.setStyleSheet(self.StandardBackground)
        self.label_US_NR.setFont(QFont(self.Font,self.letter_size_smal))
        
        # patent NR  EU (EPO)
        self.label_EU = QLabel (f"{self.Translation_Dict.get("eu_patent")}: ")
        self.label_EU.setStyleSheet(self.StandardBackground)
        self.label_EU.setFont(QFont(self.Font,self.letter_size_smal))
        
        self.label_EU_NR= QLabel (MasSet.Nr_EPO)
        self.label_EU_NR.setStyleSheet(self.StandardBackground)
        self.label_EU_NR.setFont(QFont(self.Font,self.letter_size_smal))
        
        # patent NR  DE (DPMA)
        self.label_DE = QLabel (f"{self.Translation_Dict.get("de_patent")}: ")
        self.label_DE.setStyleSheet(self.StandardBackground)
        self.label_DE.setFont(QFont(self.Font,self.letter_size_smal))
        
        self.label_DE_NR= QLabel (MasSet.Nr_DPMA)
        self.label_DE_NR.setStyleSheet(self.StandardBackground)
        self.label_DE_NR.setFont(QFont(self.Font,self.letter_size_smal))
        
        # patent NR  CH (CHIPA)
        self.label_CH = QLabel (f"{self.Translation_Dict.get("ch_patent")}: ")
        self.label_CH.setStyleSheet(self.StandardBackground)
        self.label_CH.setFont(QFont(self.Font,self.letter_size_smal))

        self.label_CH_NR= QLabel (MasSet.Nr_CNIPA)
        self.label_CH_NR.setStyleSheet(self.StandardBackground)
        self.label_CH_NR.setFont(QFont(self.Font,self.letter_size_smal))
       
       

        # _________________________ Patents layout _________________________
        self.organization_patents   = QGridLayout()

        self.organization_patents.addWidget (self.label_US,1,1)
        self.organization_patents.addWidget (self.label_EU,2,1)
        self.organization_patents.addWidget (self.label_DE,3,1)
        self.organization_patents.addWidget (self.label_CH,4,1)

        self.organization_patents.addWidget (self.label_US_NR,1,2)
        self.organization_patents.addWidget (self.label_EU_NR,2,2)
        self.organization_patents.addWidget (self.label_DE_NR,3,2)
        self.organization_patents.addWidget (self.label_CH_NR,4,2)

        return self.organization_patents

    def parcel_settings_Info (self):    # shows parcel related data (grabs those from parcel modul (icon and text))
        
        self.sensor_max_name = QLabel (f"{MasSet.sensor_1MPS_max_time_msec_name}")
        self.sensor_max_name.setStyleSheet(self.StandardBackground)
        self.sensor_max_name.setFont(QFont(self.Font,self.letter_size_smal))
        
        self.sensor_min_name = QLabel (f"{MasSet.sensor_1MPS_min_time_msec_name}")
        self.sensor_min_name.setStyleSheet(self.StandardBackground)
        self.sensor_min_name.setFont(QFont(self.Font,self.letter_size_smal))
        
        self.sensor_single_double_name = QLabel (f"{MasSet.sensor_1MPS_single_double_time_msec_name}")
        self.sensor_single_double_name.setStyleSheet(self.StandardBackground)
        self.sensor_single_double_name.setFont(QFont(self.Font,self.letter_size_smal))

        self.sensor_ERR_time_name = QLabel (f"{MasSet.sensor_1MPS_ERR_time_msec_name}")
        self.sensor_ERR_time_name.setStyleSheet(self.StandardBackground)
        self.sensor_ERR_time_name.setFont(QFont(self.Font,self.letter_size_smal))
        

        self.sensor_max = QLabel (f"{MasSet.parlcel_dimesions.sensor_1MPS_max_time_msec}")
        self.sensor_max.setStyleSheet(self.StandardBackground)
        self.sensor_max.setFont(QFont(self.Font,self.letter_size_smal))

        self.sensor_min = QLabel (f"{MasSet.parlcel_dimesions.sensor_1MPS_min_time_msec}")
        self.sensor_min.setStyleSheet(self.StandardBackground)
        self.sensor_min.setFont(QFont(self.Font,self.letter_size_smal))
        
        self.sensor_single_double = QLabel (f"{MasSet.parlcel_dimesions.sensor_1MPS_single_double_time_msec}")
        self.sensor_single_double.setStyleSheet(self.StandardBackground)
        self.sensor_single_double.setFont(QFont(self.Font,self.letter_size_smal))
        
        self.sensor_ERR_time = QLabel (f"{MasSet.parlcel_dimesions.Default_Sensor_ERR_time_in_msec}")
        self.sensor_ERR_time.setStyleSheet(self.StandardBackground)
        self.sensor_ERR_time.setFont(QFont(self.Font,self.letter_size_smal))
    


        # _________________________ Parcelsettings layout _________________________
        self.parcel_settings        = QGridLayout()

        self.parcel_settings.addWidget (self.sensor_max_name,1,1)
        self.parcel_settings.addWidget (self.sensor_min_name,2,1)
        self.parcel_settings.addWidget (self.sensor_single_double_name,3,1)
        self.parcel_settings.addWidget (self.sensor_ERR_time_name,4,1)

        self.parcel_settings.addWidget (self.sensor_max,1,2)
        self.parcel_settings.addWidget (self.sensor_min,2,2)
        self.parcel_settings.addWidget (self.sensor_single_double,3,2)
        self.parcel_settings.addWidget (self.sensor_ERR_time,4,2)

        return self.parcel_settings

    def Window_content (self):
            

        #_Project name
        self.label_1 = QLabel (self.Translation_Dict.get("project_name"))
        self.label_1.setStyleSheet(self.StandardBackground)
        self.label_1.setFont(QFont(self.Font,self.letter_size_Large))

        self.label_11 = QLabel ("PTU",self)
        self.label_11.setStyleSheet(self.StandardBackground)
        self.label_11.setFont(QFont(self.Font,self.letter_size_Large))

        # app ver
        self.label_2 = QLabel (self.Translation_Dict.get("Software_version"))
        self.label_2.setStyleSheet(self.StandardBackground)
        self.label_2.setFont(QFont(self.Font,self.letter_size_Large))
            
        self.label_22 = QLabel (MasSet.Gui_ver)
        self.label_22.setStyleSheet(self.StandardBackground)
        self.label_22.setFont(QFont(self.Font,self.letter_size_Large))


        # app dev´s
        self.label_3 = QLabel (self.Translation_Dict.get("devs"))
        self.label_3.setStyleSheet(self.StandardBackground)
        self.label_3.setFont(QFont(self.Font,self.letter_size_Large))
            
        self.label_33 = QLabel (f"{self.Translation_Dict.get("dev_1")} {self.Translation_Dict.get("dev_2")} {self.Translation_Dict.get("dev_3")} ")
        self.label_33.setStyleSheet(self.StandardBackground)
        self.label_33.setFont(QFont(self.Font,self.letter_size_Large))


        # graphics designer
        self.label_4 = QLabel (self.Translation_Dict.get("graphic_design"))
        self.label_4.setStyleSheet(self.StandardBackground)
        self.label_4.setFont(QFont(self.Font,self.letter_size_Large))

        self.label_44 = QLabel (f"{self.Translation_Dict.get("graphic_designer1")} {self.Translation_Dict.get("graphic_designer2")} {self.Translation_Dict.get("graphic_designer3")}",self)
        self.label_44.setStyleSheet(self.StandardBackground)
        self.label_44.setFont(QFont(self.Font,self.letter_size_Large))


        # icons provider
        self.label_5 = QLabel (self.Translation_Dict.get("icon_provider_1"))
        self.label_5.setStyleSheet(self.StandardBackground)
        self.label_5.setFont(QFont(self.Font,self.letter_size_Large))

        self.label_55 = QLabel (self.Translation_Dict.get("icon_provider_name_1"))
        self.label_55.setStyleSheet(self.StandardBackground)
        self.label_55.setFont(QFont(self.Font,self.letter_size_Large))
        


        self.sub_organization           = QGridLayout()

        self.sub_organization.addWidget (self.label_1, 1, 1)
        self.sub_organization.addWidget (self.label_2, 2, 1)
        self.sub_organization.addWidget (self.label_3, 3, 1)
        self.sub_organization.addWidget (self.label_4, 4, 1)
        self.sub_organization.addWidget (self.label_5, 5, 1)

        self.sub_organization.addLayout(self.patent_Info(),6,1)

        self.sub_organization.addWidget (self.label_11, 1, 2)
        self.sub_organization.addWidget (self.label_22, 2, 2)
        self.sub_organization.addWidget (self.label_33, 3, 2)
        self.sub_organization.addWidget (self.label_44, 4, 2)
        self.sub_organization.addWidget (self.label_55, 5, 2)

        self.sub_organization.addLayout(self.parcel_settings_Info(),6,2)
    
        return self.sub_organization
            

    def init_INFO_UI(self): #Buttons and remaining text + layout 
        
        self.btn_window_header.setFixedHeight(125)
        self.btn_window_header.setStyleSheet(f"background-color : {self.GUI_header};border : none")
        self.btn_window_header.setLayout(prefab.window_header.init_Header(MasSet.info_icon,"window_title_3",self.Translation_Dict))
        self.btn_window_header.clicked.connect(self.close_window)
        

        self.window_main.setStyleSheet(f"background-color : {self.GUI_color};")
        self.window_main.setLayout(info_window.Window_content(self))

       
        # _________________________ Final layout _________________________

        self.organization           = QVBoxLayout()

        self.organization.setContentsMargins (0,0,0,0)
        self.organization.addWidget (self.btn_window_header)
        self.organization.addWidget (self.window_main)
        self.setLayout(self.organization)

#_________________Help window____________________

class Guide_window (QWidget):
    def __init__(self,Translation_Dict: dict ,window_name: str ,num_of_slides: int,
                image_video_list: list, list_of_keys: list,
                window_size_W :int = 2560, window_size_H :int = 1600):
        super().__init__()
            
        self.window_size_W          = window_size_W
        self.window_size_H          = window_size_H
        self.GUI_header             = GUI_header_color
        self.GUI_footer             = GUI_footer_color
        self.GUI_color              = DarkmodeColor
        self.window_name            = window_name
        self.Translation_Dict       = Translation_Dict
        self.Transparencolor        = MasSet.Transparencolor
        self.letter_size_Massive    = MasSet.letter_size_Massive
        self.letter_size_Medium     = MasSet.letter_size_Medium
        self.Fonttype_1             = MasSet.Fonttype_1
        self.start_slide_time       = MasSet.start_slide_time
        self.next_slide_time_vid    = MasSet.next_slide_time_vid
        self.next_slide_time        = MasSet.next_slide_time
        self.index                  = 0
        self.end                    = 0
        #imports of file and text paths 
        self.num_of_slides = num_of_slides

        self.list_of_images = image_video_list

        self.list_of_keys   = list_of_keys

        #Buttons / widgets      
        self.btn_window_header              = QPushButton ("",self)
        self.window_main                    = QWidget ()

        self.setWindowTitle(f"Guide : {self.window_name}")                                                               #windowstartsize
        self.setWindowIcon(QIcon(MasSet.img_company_logo))                                             #window icon
        self.setMinimumSize(400,400)
        self.setStyleSheet(f"background-color :{self.GUI_color}")

        self.initUI()

    def close_window(self):
        self.close()

    def initUI(self):

        def Window_content ():
            btn_next        = QPushButton("❱",self)
            btn_previous    = QPushButton("❰",self)
            content_95perc  = int ((self.window_size_H)/100)*95
            
            layout      = QVBoxLayout()
            image       = QLabel("")
            video_widget = QLabel("Video")
            timer       = QTimer()
            timer_vid   = QTimer()
            VLC_player  = vlc.Instance()
            vid_player  = VLC_player.media_player_new()

         
            def indexing_posetiv (run_state):
                run         = run_state
                vid_played  = False
                
                while run == True:
                    run = False


                    if self.index == self.num_of_slides or self.index > self.num_of_slides:     # opens the next window
                        self.index = self.num_of_slides
                        self.end += 1
                        
                        if self.end > 0:                        # closes the guide window
                            Guide_window.close_window(self)

                    self.index += 1
                    text.setText(self.Translation_Dict.get(self.list_of_keys[self.index]))

                    def replay ():
                            vid_player.stop()
                            vid_player.play()
                        
                    if self.list_of_images[self.index].rfind("Video_files")>0:


                        if vid_played == True:
                            vid_played = False
                            vid_player.stop()
                            
                        vid_played = True
                        vid_player.set_mrl(self.list_of_images[self.index])
                        vid_player.set_hwnd(int(video_widget.winId()))
                        vid_player.play()
                        time.sleep(1)

                        vid_legth = vid_player.get_length()
                        print(vid_legth)

                        timer.start(self.next_slide_time_vid + vid_legth*3)
                        timer_vid.start(vid_legth)
                        timer_vid.timeout.connect(lambda: replay())

                        video_widget.show()
                        image.hide()
     
                    else:
                        pixmap = QPixmap(self.list_of_images[self.index])
                        image_scaled = pixmap.scaledToWidth(content_95perc)

                        image.setPixmap(image_scaled)
                        image.show()
                        video_widget.hide()

                        timer.start(self.next_slide_time)


            def indexing_negativ (run_state):
                
                run         = run_state
                vid_played  = False

                while run == True:
                    run = False

                    if self.index <= 0:
                        self.index = 0
                    else:
                        self.index -= 1
     
                    text.setText(self.Translation_Dict.get(self.list_of_keys[self.index]))

                    def replay ():
                            vid_player.stop()
                            vid_player.play()
                        
                    if self.list_of_images[self.index].rfind("Video_files")>0:


                        if vid_played == True:
                            vid_played = False
                            vid_player.stop()
                            
                        vid_played = True
                        vid_player.set_mrl(self.list_of_images[self.index])
                        vid_player.set_hwnd(int(video_widget.winId()))
                        vid_player.play()
                        time.sleep(1)

                        vid_legth = vid_player.get_length()
                        print(vid_legth)

                        timer.start(self.next_slide_time_vid + vid_legth*3)
                        timer_vid.start(vid_legth)
                        timer_vid.timeout.connect(lambda: replay())

                        video_widget.show()
                        image.hide()
             
                    else:
                        pixmap = QPixmap(self.list_of_images[self.index])
                        image_scaled = pixmap.scaledToWidth(content_95perc)

                        image.setPixmap(image_scaled)
                        image.show()
                        video_widget.hide()

                        timer.start(self.next_slide_time)


            pixmap = QPixmap(self.list_of_images[self.index])
            image_scaled = pixmap.scaledToWidth(content_95perc)
            
            image.setMaximumSize(image_scaled.width(),int(image_scaled.height()/100)*125)
            image.setStyleSheet(f"background-color : {self.Transparencolor};")
            image.setPixmap(image_scaled)
            image.setAlignment(Qt.AlignCenter)

            video_widget.setMinimumSize(MasSet.vid_standard_width,MasSet.vid_standard_Height)
            video_widget.setStyleSheet(f"background-color :{self.Transparencolor};")
            video_widget.setAlignment(Qt.AlignCenter)
            video_widget.hide()

            text = QLabel(self.Translation_Dict.get(self.list_of_keys[self.index]))
            text.setMinimumSize(200,200)
            text.setStyleSheet(f"background-color :{self.Transparencolor}; font-weight: bold;")
            text.setFont(QFont(self.Fonttype_1,self.letter_size_Medium))
            text.setAlignment(Qt.AlignCenter)

            layout.addWidget(text,1)
            layout.addWidget(image,2)
            layout.addWidget(video_widget,2)
            
            btn_next.setStyleSheet(f"background-color :{self.Transparencolor}; font-weight: bold;")
            btn_next.setFont(QFont(self.Fonttype_1,self.letter_size_Massive))
            btn_next.setMaximumHeight(image_scaled.height())
            btn_next.clicked.connect(lambda checked: indexing_posetiv(True))
            
            btn_previous.setStyleSheet(f"background-color :{self.Transparencolor}; font-weight: bold;")
            btn_previous.setFont(QFont(self.Fonttype_1,self.letter_size_Massive))   
            btn_previous.setMaximumHeight(image_scaled.height())         
            btn_previous.clicked.connect(lambda checked: indexing_negativ(True))

            timer.timeout.connect(lambda: indexing_posetiv(True))
            timer.start(self.start_slide_time)


            window_mainlayout      = QHBoxLayout() #QGridLayout()
            
            window_mainlayout.addWidget(btn_previous)
            window_mainlayout.addLayout(layout)
            window_mainlayout.addWidget(btn_next)

            return window_mainlayout


        self.btn_window_header.setFixedHeight(125)
        self.btn_window_header.setStyleSheet(f"background-color : {self.GUI_header};border : none")
        self.btn_window_header.setLayout(prefab.window_header.init_Header(MasSet.help_icon,self.window_name,self.Translation_Dict))

        self.btn_window_header.clicked.connect(self.close_window)
        

        self.window_main.setStyleSheet(f"background-color : {self.GUI_color};")
        self.window_main.setLayout(Window_content())

        
        #_________________Window Layout____________________
        self.organization           = QVBoxLayout()

        self.organization.setContentsMargins (0,0,0,0)
        self.organization.addWidget (self.btn_window_header)
        self.organization.addWidget (self.window_main)
        self.setLayout(self.organization)
        

class Help_window(QWidget):

    def __init__(self,Translation_Dict: dict, window_size_W :int = 2560, window_size_H :int = 1600, log_all: bool = False):
        super().__init__()

        #_________________ some imports ____________________

        self.number_of_menubuttons: int = 5
        self.log_all                = log_all
        self.Translation_Dict       = Translation_Dict
        self.Transparent            = Transparencolor
        self.Font                   = Fonttype_1
        self.letter_size_smal       = letter_size_Smal
        self.letter_size_Medium     = letter_size_Medium
        self.letter_size_Large      = letter_size_Big
        self.company_logo           = company_logo
        self.close_window_icon      = close_window_icon
        self.help_icon  	        = help_icon
        self.size_W                 = window_size_W
        self.size_H                 = window_size_H
        self.GUI_header             = GUI_header_color
        self.GUI_footer             = GUI_footer_color
        self.GUI_color              = DarkmodeColor

        # Buttons / widgets      
        self.btn_window_header              = QPushButton ("",self)
        self.window_main                    = QWidget ()


        self.setWindowTitle(self.Translation_Dict.get("window_title_2"))
        self.setWindowIcon(QIcon(self.company_logo))
        self.setMinimumSize(400,400)
        self.setStyleSheet(f"background-color :{self.GUI_color}")
        


        self.initUI()

    def close_window(self):
        self.close()


    def initUI(self):

        def show_Guide_window_Tranport_hepler():
            number_of_slides: int  = 8
            starimage   = MasSet.img_Mousetrap
            image1      = MasSet.img_Mousetrap_dmg_1
            image2      = MasSet.img_Mousetrap_dmg_2
            image3      = MasSet.img_Mousetrap_dmg_3
            image4      = MasSet.img_Mousetrap_dmg_4
            image5      = MasSet.img_Mousetrap_dmg_4_alt
            image6      = MasSet.img_Mousetrap_invalid_1
            image7      = MasSet.vid_Clear_cl
            image8      = MasSet.vid_Parcel_to_thin
            image9      = MasSet.img_CL_Topview_Table
            start_text  = ("Help_text_1")
            text1       = ("Help_text_2")
            text2       = ("Help_text_3")
            text3       = ("Help_text_4")
            text4       = ("Help_text_5")
            text5       = ("Help_text_6")
            text6       = ("Help_text_7")
            text7       = ("Help_text_8")
            text8       = ("Help_text_9")
            text9       = ("Help_text_10")
            
            image_video_list    = (starimage,   image1, image2, image3, image4, image5, image6, image7, image8, image9)
            text_list           = (start_text,  text1,  text2,  text3,  text4,  text5,  text6,  text7,  text8,  text9)

            self.window = Guide_window(self.Translation_Dict,"help_subwindow_name_1",number_of_slides,image_video_list,text_list)
            self.window.showFullScreen()
            


        def Window_content (self, Translation_Dict: dict = self.Translation_Dict, 
                                Letter_size: int = letter_size_Big, font = self.Font, window_H: int = self.size_H, num_off_buttons: int =  self.number_of_menubuttons, 
                                Transparent: str = self.Transparent,):
        
            btn_heith  = (int(window_H/num_off_buttons)+25)
            
            btn_damaged_parcels         = QPushButton ("",self)
            btn_mousetrap               = QPushButton ("",self)
            btn_no_goes                 = QPushButton ("",self)
            btn_goes                    = QPushButton ("",self)
            btn_label                   = QPushButton ("",self)

                
            def Button_designer (button_name_key: str, immage_path: str,):
                
                widget_h = int(window_H/num_off_buttons)

                pixmap = QPixmap(immage_path)
                image_scaled = pixmap.scaledToHeight(widget_h)

                image = QLabel("")
                image.setMinimumSize(image_scaled.width(),image_scaled.height())
                image.setStyleSheet(f"background-color : {Transparent};")
                image.setPixmap(image_scaled)
                image.setAlignment(Qt.AlignCenter)

                text = QLabel(Translation_Dict.get(button_name_key))
                text.setMinimumSize(200,200)
                text.setStyleSheet(f"background-color :{Transparent}; font-weight: bold;")
                text.setFont(QFont(font,Letter_size))
                text.setAlignment(Qt.AlignCenter)

                layout = QHBoxLayout()
                layout.addWidget(image,1)
                layout.addWidget(text,2)

                return layout


            btn_mousetrap.setStyleSheet("border : none; ")
            btn_mousetrap.setMinimumHeight(btn_heith)
            btn_mousetrap.setLayout(Button_designer("help_subwindow_name_1",MasSet.img_Mousetrap))
            btn_mousetrap.clicked.connect(lambda checked: show_Guide_window_Tranport_hepler())
            
            btn_label.setStyleSheet("border : none; ")
            btn_label.setMinimumHeight(btn_heith)
            btn_label.setLayout(Button_designer("help_subwindow_name_2",MasSet.img_label))

            btn_goes.setStyleSheet("border : none; ")
            btn_goes.setMinimumHeight(btn_heith)
            btn_goes.setLayout(Button_designer("help_subwindow_name_3",MasSet.img_does))

            btn_no_goes.setStyleSheet("border : none; ")
            btn_no_goes.setMinimumHeight(btn_heith)
            btn_no_goes.setLayout(Button_designer("help_subwindow_name_4",MasSet.img_donts))

            btn_damaged_parcels.setStyleSheet("border : none; ")
            btn_damaged_parcels.setMinimumHeight(btn_heith)
            btn_damaged_parcels.setLayout(Button_designer("help_subwindow_name_5",MasSet.img_Damaged_parcel))
            
            
            #_________________Layout____________________
            
            window_mainlayout      = QGridLayout()
            
            window_mainlayout.addWidget (btn_mousetrap, 1,1)
            window_mainlayout.addWidget (btn_label, 1,2)
            window_mainlayout.addWidget (btn_goes, 2,1)
            window_mainlayout.addWidget (btn_no_goes, 2,2)
            window_mainlayout.addWidget (btn_damaged_parcels, 3,1)

            return window_mainlayout

        self.btn_window_header.setFixedHeight(125)
        self.btn_window_header.setStyleSheet(f"background-color : {self.GUI_header};border : none")
        self.btn_window_header.setLayout(prefab.window_header.init_Header(MasSet.help_icon,"window_title_2",self.Translation_Dict))

        self.btn_window_header.clicked.connect(self.close_window)
        

        self.window_main.setStyleSheet(f"background-color : {self.GUI_color};")
        self.window_main.setLayout(Window_content(self))

        
        #_________________Window Layout____________________
        self.organization           = QVBoxLayout()

        self.organization.setContentsMargins (0,0,0,0)
        self.organization.addWidget (self.btn_window_header)
        self.organization.addWidget (self.window_main)
        self.setLayout(self.organization)
                    
#_________________Settings window____________________

class PlotCanvas(FigureCanvas): #creates the diagrams
    def __init__(self, Data: list, Title_label: str, X_label: str, Y_label: str, legend_label: str = "", show_Grid: bool = True):
        
        self.Data = Data    
        self.Title_label = Title_label
        self.X_label = X_label
        self.Y_label = Y_label
        self.legend_label = legend_label
        self.show_Grid = show_Grid

        fig, self.ax = plt.subplots()
        super().__init__(fig)
        self.plt(self.Data)

    def plt(self, data):
        time = np.linspace(0, 3, len(data))  # Time from 0 to 3 hours (in hours)

        self.ax.set_facecolor(MasSet.DarkmodeColor)  #funtion is stil missing
        self.figure.patch.set_facecolor(MasSet.DarkmodeColor)  

        self.ax.plot(time, data, label="Data over Time")
        self.ax.set_title(self.Title_label, fontsize=12)
        self.ax.set_xlabel(self.X_label)
        self.ax.set_ylabel(self.Y_label)

        if self.legend_label:
            self.ax.legend([self.legend_label])

        self.ax.grid(self.show_Grid)

    def __del__(self):
        plt.close(self.figure)  #to free memory

class Setting_choise_window(QWidget):

    def __init__(self,Translation_Dict: dict, window_size_W :int = 2560, window_size_H :int = 1600, log_all: bool = False):
        super().__init__()

        self.number_of_menubuttons: int = 3
        self.log_all                = log_all
        self.Translation_Dict       = Translation_Dict
        self.Transparent            = Transparencolor
        self.Font                   = Fonttype_1
        self.letter_size_smal       = letter_size_Smal
        self.letter_size_Medium     = letter_size_Medium
        self.letter_size_Large      = letter_size_Big
        self.company_logo           = company_logo
        self.close_window_icon      = close_window_icon
        self.settings_icon          = settings_icon
        self.size_W                 = window_size_W
        self.size_H                 = window_size_H
        self.GUI_header             = GUI_header_color
        self.GUI_footer             = GUI_footer_color
        self.GUI_color              = DarkmodeColor
        
        self.setWindowTitle(self.Translation_Dict.get("window_title_4"))
        self.setWindowIcon(QIcon(self.company_logo))
        self.setMinimumSize(400,400)
        self.setStyleSheet(f"background-color :{self.GUI_color}")
        self.central_widget = QWidget()   
        #self.setCentralWidget(self.central_widget)

        # Buttons / widgets      
        self.btn_window_header              = QPushButton ("")
        self.window_main                    = QWidget ()
        
        self.init_UI()


    def close_window(self):
        self.close()

    def init_UI(self):

        def Window_content (Translation_Dict: dict = self.Translation_Dict, 
                                Letter_size: int = letter_size_Big, font = self.Font, window_H: int = self.size_H, num_off_buttons: int =  self.number_of_menubuttons, 
                                Transparent: str = self.Transparent):
        
                
            def Button_designer (button_name_key: str, icon_path: str,):

                widget_h = int(window_H/(num_off_buttons+2))

                pixmap = QPixmap(icon_path)
                icon_scaled = pixmap.scaledToHeight(widget_h)

                image = QLabel("")
                image.setMinimumSize(icon_scaled.width(),icon_scaled.height())
                image.setStyleSheet(f"background-color : {Transparent};")
                image.setPixmap(icon_scaled)
                image.setAlignment(Qt.AlignCenter)

                text = QLabel(button_name_key)
                text.setMinimumSize(200,200)
                text.setStyleSheet(f"background-color :{Transparent}; font-weight: bold;")
                text.setFont(QFont(font,Letter_size))
                text.setAlignment(Qt.AlignCenter)

                layout = QHBoxLayout()
                layout.addWidget(image,1)
                layout.addWidget(text,2)

                return layout

            btn_heith  = (int(window_H/num_off_buttons)+25)

            btn_technic                    = QPushButton ("")
            btn_supervisor                 = QPushButton ("")
            btn_admin                      = QPushButton ("")
            

            btn_technic.setStyleSheet("border : none; ")
            btn_technic.setMinimumHeight(btn_heith)
            btn_technic.setLayout(Button_designer("Technic",MasSet.technic_user_icon))
            btn_technic.clicked.connect(self.open_technic)

            btn_supervisor.setStyleSheet("border : none; ")
            btn_supervisor.setMinimumHeight(btn_heith)
            btn_supervisor.setLayout(Button_designer("Supervisor",MasSet.supervisor_user_icon))
            btn_supervisor.clicked.connect(self.open_supervisor)

            btn_admin.setStyleSheet("border : none; ")
            btn_admin.setMinimumHeight(btn_heith)
            btn_admin.setLayout(Button_designer("Admin",MasSet.admin_icon))
            btn_admin.clicked.connect(self.open_admin)

            
            #_________________Layout____________________
            
            window_mainlayout      = QVBoxLayout()
            
            window_mainlayout.addWidget (btn_supervisor)
            window_mainlayout.addWidget (btn_technic)
            window_mainlayout.addWidget (btn_admin)

            return window_mainlayout



        self.btn_window_header.setFixedHeight(125)
        self.btn_window_header.setStyleSheet(f"background-color : {self.GUI_header};border : none")
        self.btn_window_header.setLayout(prefab.window_header.init_Header(MasSet.help_icon,"window_title_4",self.Translation_Dict))
        self.btn_window_header.clicked.connect(self.close_window)

        self.window_main.setStyleSheet(f"background-color : {self.GUI_color};")
        self.window_main.setLayout(Window_content(self))

        #_________________Window Layout____________________
        self.organization           = QVBoxLayout()

        self.organization.setContentsMargins (0,0,0,0)
        self.organization.addWidget (self.btn_window_header)
        self.organization.addWidget (self.window_main)
        self.setLayout(self.organization)

        
    def open_technic(self):

        if self.log_all == True:
            Logger.logger(f"opening : open_technic")

        window = prefab.Keypad_Handeler(MasSet.technic_password, self.log_all)

    def open_supervisor(self):

        if self.log_all == True:
            Logger.logger(f"opening : open_supervisor")

        window = Public_facing(2560,1600)

    def open_admin(self):
        
        if self.log_all == True:
            Logger.logger(f"opening : open_admin")

        window = prefab.Keypad_Handeler(MasSet.admin_password, self.log_all)

class Supervisor(QWidget):
    def __init__(self, window_w, window_h, Translation_Dict):
        super().__init__()
        
        
        self.Translation_Dict = Translation_Dict
        self.window_w = window_w
        self.window_h = window_h
        # Connect to DB
        conn = sqlite3.connect("PTU_test_db_now_parcels.db") #replace / intigrate (MASET)
        curser = conn.cursor()
        #get timestamps from the last 3 hours
        curser.execute("""
    SELECT timestamp, dimensions_x, dimensions_y, dimensions_z 
    FROM parcel_data
    WHERE timestamp >= DATETIME('now', '-3 hours')
""")

        rows = curser.fetchall()
        #converts timestamps

        timestamps, too_long, too_short, too_tall, too_thin, too_wide  = [],[],[],[],[],[]

        for row in rows:
            timestamp = datetime.datetime.fromisoformat(row[0])
            timestamps.append(timestamp)

            #check condtion #intrigation in to the remaining programm and maset
            #ctu if parcel to long, wide, tall, etc
            #intigrate the data to dertermain witch parcel is to long,wide,etc has to be the same witch triggers the stop function(MASET etc)
            if row[1] > 1200:
                too_long.append(timestamp)
            if row [1] < 100:
                too_short.append(timestamp)
            if row[2] > 600:
                too_wide.append(timestamp)
            if row[3] > 600:
                too_tall.append(timestamp)
            if row[3] < 100:
                too_thin.append(timestamp)

                
        # create the time intervall for looking throue the DB
        datetime_object = datetime.datetime.now() #datetime.datetime.strptime("2025-02-27T05:24:55.704472", "%Y-%m-%dT%H:%M:%S.%f")#replace w current time
        start_time = datetime_object - datetime.timedelta(hours = 3)

        #creates the 13 bins a 15 min long 
        bins = [start_time + datetime.timedelta(minutes = 15 * i) for i in range(13)]

        counts_all   = [0] * (len(bins) -1)
        counts_long  = [0] * (len(bins) -1)
        counts_short = [0] * (len(bins) -1)
        counts_wide  = [0] * (len(bins) -1)
        counts_tall  = [0] * (len(bins) -1)
        counts_thin  = [0] * (len(bins) -1)

        def count_entrys_in_bins (entry, count):
            for ts in entry:
                for i in range(len(bins)-1):
                    if bins[i]<= ts < bins[i + 1]:
                        count[i] +=1
                        break   
        
        count_entrys_in_bins(timestamps,counts_all)
        count_entrys_in_bins(too_long,counts_long)
        count_entrys_in_bins(too_short,counts_short)
        count_entrys_in_bins(too_wide,counts_wide)
        count_entrys_in_bins(too_tall,counts_tall)
        count_entrys_in_bins(too_thin,counts_thin)

        conn.close()

        data_events_30_min = ()#replace / intigrate

        parcels_3h = sum(counts_all)
        events_4h = sum(data_events_30_min)


        parcels_3h_Label = QLabel(f"Parcels in the last 3h \n{parcels_3h}")#replace / intigrate
        events_3h_Label = QLabel(f"Events in the last 3h \n{events_4h}")#replace / intigrate

        parcels_3h_plot = PlotCanvas(counts_all, "Parcels", "Time", "Parcels (30 min)")#replace / intigrate
        error_3h_plot = PlotCanvas(data_events_30_min, "Events", "Time", "Events (30 min)")#replace / intigrate

        parcels_3h_Label.setStyleSheet(f"background-color : {MasSet.Transparencolor};border : none")
        parcels_3h_Label.setAlignment(Qt.AlignCenter)
        parcels_3h_Label.setMinimumHeight(int(self.window_h/5))
        parcels_3h_Label.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))

        events_3h_Label.setStyleSheet(f"background-color : {MasSet.Transparencolor};border : none")
        events_3h_Label.setAlignment(Qt.AlignCenter)
        events_3h_Label.setMinimumHeight(int(self.window_h/5))
        events_3h_Label.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        
        self.Supervisor_layout = QGridLayout()
        self.Supervisor_layout.addWidget(parcels_3h_Label,1,1)
        self.Supervisor_layout.addWidget(parcels_3h_plot,1,2,1,5)
        self.Supervisor_layout.addWidget(events_3h_Label,2,1)
        self.Supervisor_layout.addWidget(error_3h_plot,2,2,2,5)

        self.setLayout(self.Supervisor_layout)

class Technic(QWidget):
    def __init__(self):
        super().__init__()
        self.changed_settings = []
        self.init_ui()
    
    def init_ui (self):

        class increase_decrease_num_prefab(QWidget):
            changed_values = {}

            def __init__ (self, num:int, key:str, display_name:str = "undifined",increase:bool = True, decrease:bool = True, unit:str = "mm"):
                super().__init__()

                self.max_adjust:int = MasSet.parlcel_dimesions.technician_max_adjust_parlcel_dimesions #limets the maximum percentage a number can be adjusted (100 base + 20 percentage = 120 max adjust)
                self.min_adjust:int = MasSet.parlcel_dimesions.technician_min_adjust_parlcel_dimesions #limets the minimum percentage a number can be adjusted (100 base - 20 percentage = 80 min adjust)
                self.target_num_ref = MasSet.parlcel_dimesions.path_parcel_settings_dict.get(f"Default_{key}") #caps the max and min settings, based on the preset in Maset.parlcel_dimesions

                self.target_num     = num
                self.loaded_num     = num
                self.key            = key
                self.display_name   = display_name
                self.increase_bool  = increase
                self.decrease_bool  = decrease
                self.unit           = unit

                self.display_name   = QLabel(self.display_name)
                self.text_label     = QLabel(f" {self.target_num}{self.unit} ")
                self.increse        = QPushButton("+")
                self.decrease       = QPushButton ("-")

                increase_decrease_num_prefab.changed_values[self.key] = self.target_num


                def increse_pressed():
                    if self.target_num < self.target_num_ref/100*self.max_adjust: #limets the maximum percentage a number can be adjusted
                        self.target_num += 1
                        self.text_label.setText(f" {self.target_num}{self.unit} ")
                        increase_decrease_num_prefab.changed_values[self.key] = self.target_num
                
                def decreased_pressed():
                    if self.target_num > self.target_num_ref/100*self.min_adjust: #limets the minmum percentage a number can be adjusted
                        self.target_num -= 1
                        self.text_label.setText(f" {self.target_num}{self.unit} ")
                        increase_decrease_num_prefab.changed_values[self.key] = self.target_num

            # _________________________ Design _________________________
                self.sub_layout = QGridLayout()

                self.display_name.setMinimumSize(150,150)
                self.display_name.setStyleSheet(f"border: 0px; background-color : {MasSet.Transparencolor};")
                self.display_name.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
                self.display_name.setAlignment(Qt.AlignCenter)

                self.text_label.setMinimumSize(150,150)
                self.text_label.setStyleSheet(f"border: 0px; background-color : {MasSet.Transparencolor};")
                self.text_label.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Massive))
                self.text_label.setAlignment(Qt.AlignCenter)

                if self.increase_bool == True:
                    self.increse.setMinimumSize(150,150)
                    self.increse.setStyleSheet(f"border: 0px; background-color : {MasSet.Transparencolor};")
                    self.increse.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Massive))
                    self.increse.clicked.connect(increse_pressed)
                    self.sub_layout.addWidget(self.increse,2,3)

                if self.decrease_bool == True:
                    self.decrease.setMinimumSize(150,150)
                    self.decrease.setStyleSheet(f"border: 0px; background-color : {MasSet.Transparencolor};")
                    self.decrease.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Massive))
                    self.decrease.clicked.connect(decreased_pressed)
                    self.sub_layout.addWidget(self.decrease,2,1)


                self.sub_layout.addWidget(self.display_name,1,1,1,3)
                self.sub_layout.addWidget(self.text_label,2,2)
      
                self.border_widget = QWidget()
                self.border_widget.setLayout(self.sub_layout)
                self.border_widget.setStyleSheet(f"border: 3px solid black; border-radius: 10px; background-color: {MasSet.Ligth_grey_color}; padding: 5px;")  # Apply border here

                # Main Layout
                self.main_layout = QVBoxLayout()
                self.main_layout.addWidget(self.border_widget)
                self.setLayout(self.main_layout)


            @classmethod
            def get_changed_values(cls):
                return cls.changed_values



        def save_current_settings():

            new_settings = increase_decrease_num_prefab.get_changed_values()
            settings = load_current_settings()
            Logger.logger(f"values updated {settings}")
            settings.update(new_settings)

            try:
                with open (CONFIG_FILE_PARCEL
            ,"w") as f:
                    json.dump(settings,f, indent=4)
            except Exception as ERR:
                    Admin.close()
                    Technic.close()
                    Error_Handeling(4202,
        f"""
        could not save settings
        Window closed
        {ERR}
        """,True)
        
        
        def reset_values():
            pass

        self.btn_SaveChanges            = QPushButton (" Save Changes ")
        self.btn_reset_values           = QPushButton (" Reset ")
        self.btn_reset_to_base_values   = QPushButton (" Reset to base values ")

        self.btn_SaveChanges.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Green_color}; border: 4px solid black")
        self.btn_SaveChanges.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Big))
        self.btn_SaveChanges.clicked.connect(save_current_settings)

        self.btn_reset_values.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Blue_color}; border: 4px solid black")
        self.btn_reset_values.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Medium))
        self.btn_reset_values.clicked.connect(reset_values)

        self.btn_reset_to_base_values.setStyleSheet(f"border-radius : 20px; background-color : {MasSet.Orange_color}; border: 4px solid black")
        self.btn_reset_to_base_values.setFont(QFont(MasSet.Fonttype_1,MasSet.letter_size_Medium))
        # _________________________ Final layout _________________________

        self.organization = QGridLayout()
        self.organization.addWidget (increase_decrease_num_prefab(get_setting("Parcel_Max_length_in_mm"),"Parcel_Max_length_in_mm","Parcel max length"),1,0)
        self.organization.addWidget (increase_decrease_num_prefab(get_setting("Parcel_Min_length_in_mm"),"Parcel_Min_length_in_mm","Parcel min length"),2,0)
        self.organization.addWidget (increase_decrease_num_prefab(get_setting("Parcel_max_width"),"Parcel_max_width","Parcel Max width"),1,1)
        self.organization.addWidget (increase_decrease_num_prefab(get_setting("Parcel_min_width"),"Parcel_min_width","Parcel Min width"),2,1)
        self.organization.addWidget (increase_decrease_num_prefab(get_setting("Sensor_ERR_time_in_msec"),"Sensor_ERR_time_in_msec","Light barrier blocked error time",True,True,"msec"),3,0)
        self.organization.addWidget (self.btn_SaveChanges,10,3)
        self.organization.addWidget (self.btn_reset_values,11,3)
        self.organization.addWidget (self.btn_reset_to_base_values,12,3)
        self.setLayout (self.organization)
    


class Admin(QWidget):

    def __init__(self):
        super().__init__()
        pass


class Public_facing(QWidget):
    def __init__(self, width: int, height: int, log_all: bool = False, Colormode="Dark", Translation_Dictionary=None):
        super().__init__()
        self.width = width
        self.height = height
        self.log_all = log_all
        self.Colormode = Colormode
        self.Translation_Dictionary = Translation_Dictionary or MasSet.Translate_Dictonary_Fallback

        self.Technic_ov = True
        self.Admin_OV = False

        self.setWindowTitle("Settings")
        self.setMinimumSize(800, 900)
        self.setWindowIcon(QIcon("path/to/icon.png"))

        self.init_ui()

    def init_ui(self):
        # Header Button
        self.btn_window_header = QPushButton("")
        self.btn_window_header.setFixedHeight(125)
        self.btn_window_header.setStyleSheet(f"background-color : {MasSet.DarkmodeColor_header}; border: none")
        self.btn_window_header.setLayout(prefab.window_header.init_Header(MasSet.settings_icon,"window_title_4",self.Translation_Dictionary))
        self.btn_window_header.clicked.connect(self.close)

        self.setStyleSheet(f"background-color : {MasSet.DarkmodeColor}; border: none")

        # Scroll Area
        contentWidget = QWidget()
        main_layout = QVBoxLayout(contentWidget)

        main_layout.addWidget(Supervisor(self.width, self.height, self.Translation_Dictionary))

        if self.Technic_ov:
            main_layout.addWidget(Technic())

        if self.Admin_OV:
            main_layout.addWidget(Admin())

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setStyleSheet(f"background-color : {MasSet.DarkmodeColor}; border: none;")
        scrollArea.setStyleSheet("""QScrollBar:vertical {
                border: none;
                background: #434c4d;
                width: 10px;
                margin: 0px 0px 0px 0px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #888;
                border-radius: 25px;
                min-height: 30px;
            }
            """)
        scrollArea.setWidget(contentWidget)

        #self.setStyleSheet(f"background-color : {MasSet.Transparencolor};")

        # Main Layout
        self.organization = QVBoxLayout()

        self.organization.setContentsMargins (0,0,0,0)
        self.organization.addWidget(self.btn_window_header)
        self.organization.addWidget(scrollArea)
        self.setLayout(self.organization)



#_________________Window Handeler____________________
class Handeler():

    def __init__ (self, window_name : str, Translate_Dict : dict = MasSet.Translate_Dictonary_Fallback, window_size_W :int = 2560, window_size_H :int = 1600):
        super().__init__()

        self.log_all        = MasSet.log_all
        self.window_size_W  = window_size_W
        self.window_size_H  = window_size_H
        self.window_name    = window_name
        self.Translate_Dict = Translate_Dict


        self.open()

    def open(self):
        if self.log_all == True:
            Logger.logger(f"opening : {self.window_name}")

        if self.window_name == "info":
            self.window = info_window(self.Translate_Dict)
        
        if self.window_name == "help":
            self.window = Help_window(self.Translate_Dict,self.window_size_W,self.window_size_H)

        if self.window_name == "Settings":
            self.window = Setting_choise_window(self.Translate_Dict)

        self.window.showFullScreen()


def main():

    app = QApplication(sys.argv)
    window = Public_facing(2560,1600)
    window.showFullScreen()
    #window = Handeler("Settings")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

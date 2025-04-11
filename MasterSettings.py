#this file can nor be run and is only there to provide visual data file paths and parcel/package related data.

""" used external programs/ dbs /external libarys
    28.01.2025
    
    SQLite
    VLC mediaplyer: 3.0.21 Vetinari 
    PqQt5
    numpy
    matplotlib
    openpyxl
        """
Gui_ver:                                         str    =   "0.0.085"
log_all:                                        bool    =   True     # Dev Tool # to log all relevant events, exluding closing windows and situation already heandeld by Error_Handeling 

#__________________________________________________ backend constants __________________________________________________

# placeholder paswords witch need to be replaced @ a later datr 

admin_password:                                 int     = 11 # only for testing
technic_password:                               int     = 22 # only for testing
CONFIG_FILE:                                    str     = "C:/Users/Tim_F/OneDrive/Documents/Work/PTU/APK/PTU_APP/settings.json"

# parcel/package releted

#names
sensor_1MPS_max_time_msec_name:                 str     =   "Parcel Max Legth"
sensor_1MPS_min_time_msec_name:                 str     =   "Parcel min Legth"
sensor_1MPS_single_double_time_msec_name:       str     =   "Parcel Actuator min Length"
sensor_1MPS_single_double_time_msec_name:       str     =   "Parcel Actuator max Length"
sensor_1MPS_ERR_time_msec_name:                 str     =   "Sensor Error Time"


#parcel_Actuartor_A_min_legth:                   int     = 0
#parcel_Actuartor_A_max_legth:                   int     = 0
#parcel_Actuartor_B_min_legth:                   int     = 0
#parcel_Actuartor_B_max_legth:                   int     = 0
#parcel_Actuartor_C_min_legth:                   int     = 0
#parcel_Actuartor_C_max_legth:                   int     = 0

#parcel_Actuartor_A_min_with:                    int     = 0
#parcel_Actuartor_A_max_with:                    int     = 0
#parcel_Actuartor_B_min_with:                    int     = 0
#parcel_Actuartor_B_max_with:                    int     = 0
#parcel_Actuartor_C_min_with:                    int     = 0
#parcel_Actuartor_C_max_with:                    int     = 0
 
#__________________________________________________ Parcellength and timeouts 
                                                        # in mm 
class parlcel_dimesions:

    path_parcel_settings_json:                              str     ="C:/Users/Tim_F/OneDrive/Documents/Work/PTU/APK/PTU_APP/parcel_settings.json"# "settings.json"

    Default_Parcel_Max_length_in_mm:                        int     = 1220  
    Default_Parcel_Min_length_in_mm:                        int     = 85
    Default_Parcel_sigle_double_in_mm:                      int     = 560 # the length at witch a parcel is concidert a "double sheller" (DE: "Doppelschaler")
    Default_Sensor_ERR_time_in_msec:                        int     = 3000
    Default_Parcel_max_width:                               int     = 600
    Default_Parcel_min_width:                               int     = 50

    path_parcel_settings_dict = {
        "Default_Parcel_Max_length_in_mm" : Default_Parcel_Max_length_in_mm,
        "Default_Parcel_Min_length_in_mm" : Default_Parcel_Min_length_in_mm,
        "Default_Parcel_sigle_double_in_mm" : Default_Parcel_sigle_double_in_mm,
        "Default_Sensor_ERR_time_in_msec" : Default_Sensor_ERR_time_in_msec,
        "Default_Parcel_max_width" : Default_Parcel_max_width,
        "Default_Parcel_min_width" : Default_Parcel_min_width
        }

    #__________________________________________________ Parcellength and timeout adjustment
                                                                        
    technician_max_adjust_parlcel_dimesions:        int     = 110 #limets the maximum percentage a number can be adjusted       example:(100 base + 20 percentage = 120 max adjust)
    technician_min_adjust_parlcel_dimesions:        int     = 90  #limets the minimum percentage a number can be adjusted       example:(100 base - 20 percentage = 80 min adjust)
                    
                                            # all times are in milli seconds 
                                            # DO_NOT_USE_CALCULATE_LATER_IN_SCRIPT

    # 1 Meter per second
    sensor_1MPS_devider:                            float   = 1 
    sensor_1MPS_max_time_msec                               = int (Default_Parcel_Max_length_in_mm/sensor_1MPS_devider)       # org 122.0 cm = 1220   # max length of a parcel
    sensor_1MPS_min_time_msec                               = int (Default_Parcel_Min_length_in_mm/sensor_1MPS_devider)       # org 8.5 cm = 85   # min time of a parcel
    sensor_1MPS_single_double_time_msec                     = int (Default_Parcel_sigle_double_in_mm/sensor_1MPS_devider)     # org 56.0 cm = 560   # time @ witch a single parcel becomes a double

    # 0.70 Meter per second
    sensor_070MPS_devider:                          float   = 0.7
    sensor_070MPS_max_time_msec                             = int (Default_Parcel_Max_length_in_mm/sensor_070MPS_devider)     # max length of a parcel
    sensor_070MPS_min_time_msec                             = int (Default_Parcel_Min_length_in_mm/sensor_070MPS_devider)     # min time of a parcel
    sensor_070MPS_single_double_time_msec                   = int (Default_Parcel_sigle_double_in_mm/sensor_070MPS_devider)   # time @ witch a single parcel becomes a double

    # 0.60 Meter per second
    sensor_060MPS_devider:                          float   = 0.6
    sensor_060MPS_max_time_msec                             = int (Default_Parcel_Max_length_in_mm/sensor_060MPS_devider)     # max length of a parcel
    sensor_060MPS_min_time_msec                             = int (Default_Parcel_Min_length_in_mm/sensor_060MPS_devider)     # min time of a parcel
    sensor_060MPS_single_double_time_msec                   = int (Default_Parcel_sigle_double_in_mm/sensor_060MPS_devider)   # time @ witch a single parcel becomes a double

    # 0.50 Meter per second
    sensor_050MPS_devider:                          float   = 0.5
    sensor_050MPS_max_time_msec                             = int (Default_Parcel_Max_length_in_mm/sensor_050MPS_devider)     # max length of a parcel
    sensor_050MPS_min_time_msec                             = int (Default_Parcel_Min_length_in_mm/sensor_050MPS_devider)     # min time of a parcel
    sensor_050MPS_single_double_time_msec                   = int (Default_Parcel_sigle_double_in_mm/sensor_050MPS_devider)   # time @ witch a single parcel becomes a double

# function releted

#__________________________________________________Lists, tuples, dictionarys__________________________________________________

# start scren hello txt
hello_txt:                                      list    = ("Welcome","Wilkommen","Powitanie","Bienvenue","Bienvenida","Bem-vindo","Ласкаво просимо","Добро пожаловать","स्वागत","مرحباً","вітаем") # used in start scrren

#patent data 

Nr_USPO:                                        str     =   "Waiting"
Nr_EPO:                                         str     =   "Waiting"
Nr_DPMA:                                        str     =   "Waiting"
Nr_CNIPA:                                       str     =   "Waiting"

#__________________________________________________Decorative constants__________________________________________________

# coulors

Transparencolor:                                str     =   "#00FFFFFF"
DarkmodeColor:  	                            str     =   "#434c4d"       #Dead Forest
DarkmodeColor_header:                           str     =   "#2b3030"       #Caviar
DarkmodeColor_footer:                           str     =   "#2b3030"       #Caviar
LigthmodeColor:                                 str     =   "#9bb9ba"       #Shallow Sea
Red_color:                                      str     =   "#FF4C4C"
Dark_red_color:                                 str     =   "#8c0e0e"                            
Yellow_color:                                   str     =   "#ed9a09"                            
Blue_color:                                     str     =   "#144dfa"  
Green_color:                                    str     =   "#4CAF50"
Dark_green_color:                               str     =   "#0e630e"
Orange_color:                                   str     =   "#FFA500"
Dark_orange_color:                              str     =   "#8c3d0e"
Ligth_grey_color:                               str     =   "#757373"

# text
Fonttype_1:                                     str     =   "Arial"
letter_size_Massive:                            int     =   75
letter_size_Big:                                int     =   35
letter_size_Medium:                             int     =   25
letter_size_Smal:                               int     =   12


# button constants

menu_buttonsize_L:                              int     =   200
menu_buttonsize_M:                              int     =   100
menu_buttonsize_S:                              int     =   75


start_stop_clear_btn_size_X:                    int     = 450
start_stop_clear_btn_size_Y:                    int     = 120

# slide functions

#after how many ms shoud the next slide play automaticly 1 sec = 1000 msec

start_slide_time:                               int     = 7000
next_slide_time_vid:                            int     = 200
next_slide_time:                                int     = 5000



#__________________________________________________     File Paths     __________________________________________________

# txt files

Error_Log_Files:                                str     =   "reports/Error_reports"
Log_Files:                                      str     =   "reports/reports"

# excel files

tranlation_file:                                str     =   "GUI/Recources/Language_Table.xlsx"

#__________________________________________________       images       __________________________________________________

# icons BL
no_image:                                       str     =   "GUI/Recources/icons/icons8-no-image-256"
settings_icon:                                  str     =   "GUI/Recources/icons/icons8-settings-256.png"
ligtingmode_icon:                               str     =   "GUI/Recources/icons/icons8-sun-256.png"
tranlation_icon:                                str     =   "GUI/Recources/icons/icons8-translate-256.png"
help_icon:                                      str     =   "GUI/Recources/icons/icons8-help-256.png"
info_icon:                                      str     =   "GUI/Recources/icons/icons8-info-256.png"
close_window_icon_BL:                           str     =   "GUI/Recources/icons/icons8-close-256"
keypad_icon:                                    str     =   "GUI/Recources/icons/icons8-keypad-256"
warning_triangle_icon:                          str     =   "GUI/Recources/icons/icons8-error-256"
bell_icon:                                      str     =   "GUI/Recources/images/icons8-error-256"
bell_icon_WxH:                                  int     =   640
ON_Icon:                                        str     =   "GUI/Recources/icons/icons8-power.svg"
OFF_Icon:                                       str     =   "GUI/Recources/icons/icons8-power.svg"
reset_Icon:                                     str     =   "GUI/Recources/icons/icons8-reset.svg"


icon_eye:                                       str     =   "GUI/Recources/icons/icons8-eye-256"
icon_blind:                                     str     =   "GUI/Recources/icons/icons8-eye-closed-256"
technic_user_icon:                              str     =   "GUI/Recources/icons/icons8-technician-256"
supervisor_user_icon:                           str     =   "GUI/Recources/icons/icons8-user-256"
admin_icon:                                     str     =   "GUI/Recources/icons/icons8-admin-256"

# icons WH

# icons Color
close_window_icon_RD:                           str     =   "GUI/Recources/icons/icons8-close-256"


# flags 

Flag_Heigth:                                    int     =   120                                                                         #in px
Flag_Legth :                                    int     =   160                                                                         #in px

Flag_images_dict:                               dict    = {
    "US":"GUI/Recources/every_country_flag_160x120/us.png",#english
    "GB":"GUI/Recources/every_country_flag_160x120/gb.png",#english
    "DE":"GUI/Recources/every_country_flag_160x120/de.png",#german
    "PL":"GUI/Recources/every_country_flag_160x120/pl.png",#polish
    "RO":"GUI/Recources/every_country_flag_160x120/ro.png",#romainian
    "FR":"GUI/Recources/every_country_flag_160x120/fr.png",#french
    "ES":"GUI/Recources/every_country_flag_160x120/es.png",#spanish
    "PT":"GUI/Recources/every_country_flag_160x120/pt.png",#potugise
    "AL":"GUI/Recources/every_country_flag_160x120/al.png",#albanian
    "LV":"GUI/Recources/every_country_flag_160x120/lv.png",#latvian
    "LT":"GUI/Recources/every_country_flag_160x120/lt.png",#lithuanian
    "UA":"GUI/Recources/every_country_flag_160x120/ua.png",#ukrainian
    "RU":"GUI/Recources/every_country_flag_160x120/ru.png",#russian
    "TR":"GUI/Recources/every_country_flag_160x120/tr.png",#turkish
    "SA":"GUI/Recources/every_country_flag_160x120/sa.png",#arabic
}

# other image 

img_company_logo:                               str     =   ""#"GUI/Recources/company_Logo/ghatec_logo_org"

img_Warning_Triangle_BL:                        str     =   "GUI/Recources/images/exclamation-mark-98739_960-845"
img_Warning_Triangle_H:                         int     =   845
img_Warning_Triangle_W:                         int     =   960

img_CL_Topview_Table:                           str     =   "GUI/Recources/images/CL_Topview_Table"
img_CL_Topview_TB:                              str     =   "GUI/Recources/images/CL_Topview_TB"
img_CL_Topview_Table_outline:                   str     =   "GUI/Recources/images/CL_Topview_Table_outline"

img_does:                                       int     =   "GUI/Recources/icons/icons8-thumb-up-green-256"
img_donts:                                      int     =   "GUI/Recources/icons/icons8-thumb-up-red-256"
img_Mousetrap:                                  int     =   "GUI/Recources/images/Mousetraps_io"
img_Damaged_parcel:                             int     =   "GUI/Recources/icons/icons8-no-image-512"
img_label:                                      int     =   "GUI/Recources/icons/icons8-no-image-512"

img_Parcel_Shape_invalid_1:                     str     =   "GUI/Recources/images/parcel_shape_1"                       # shows a parcel made up of two components (bag) 
img_Parcel_Shape_invalid_2:                     str     =   "GUI/Recources/images/parcel_shape_2"                       # reaches over site 1
img_Parcel_Shape_invalid_3:                     str     =   "GUI/Recources/images/parcel_shape_3"                       # reaches over site 2
img_Parcel_Shape_invalid_4:                     str     =   "GUI/Recources/images/parcel_shape_4"                       # has hole in the middle
img_Parcel_long:                                str     =   "GUI/Recources/images/parcel_long"                          # parcel to long
img_Mousetrap_invalid_1:                        str     =   "GUI/Recources/images/Mousetraps_Canon_4k"                  # Looks like a canon 
img_Mousetrap_loose_parcel_1:                   str     =   "GUI/Recources/images/Mousetraps_parcel_not_secured_1"      # parcel only lies in 
img_Mousetrap_loose_parcel_2:                   str     =   "GUI/Recources/images/Mousetraps_parcel_not_secured_2"      # parcel only lies in 
img_Mousetrap_dmg_1:                            str     =   "GUI/Recources/images/Mousetraps_dmg_1"                     # mousetrap is damaged
img_Mousetrap_dmg_2:                            str     =   "GUI/Recources/images/Mousetraps_dmg_2"                     # mousetrap is damaged
img_Mousetrap_dmg_3:                            str     =   "GUI/Recources/images/Mousetraps_dmg_3"                     # mousetrap is damaged
img_Mousetrap_dmg_4:                            str     =   "GUI/Recources/images/Mousetraps_dmg_4"                     # mousetrap is damaged 
img_Mousetrap_dmg_4_alt:                        str     =   "GUI/Recources/images/Mousetraps_dmg_41"                    # mousetrap is damaged
img_Mousetrap_loose_belt_1:                     str     =   "GUI/Recources/images/Mousetrap_belt_loose_1"               # a band is loose and dagelin of @ the end
img_Mousetrap_loose_belt_1:                     str     =   "GUI/Recources/images/Mousetrap_belt_loose_2"               # a band is loose and dagelin of @ the end
img_label_position:                             str     =   "GUI/Recources/images/Mousetraps_Label_blocked_1"           # short vid of the label position (only top IO)


vid_standard_width:                             int     =   1920
vid_standard_Height:                            int     =   1080
vid_Clear_cl:                                   str     =   "GUI/Recources/Video_files/package_removal.mp4"                 # shows vid of the cl beeing cleard   (multiple variants ? (random choise?)) 
vid_Parcel_Shape_invalid_1:                     str     =   "GUI/Recources/Video_files/package_DMG_1.mp4"
vid_Parcel_Shape_invalid_2:                     str     =   "GUI/Recources/Video_files/package_DMG_2.mp4"
vid_Parcel_to_thin:                             str     =   "GUI/Recources/Video_files/package_thin.mp4"
vid_Parcel_to_long:                             str     =   "GUI/Recources/Video_files/package_long.mp4"
vid_Mousetrap_invalid_no_belts_1:               str     =   "GUI/Recources/Video_files/Mousetraps_no_belts_on parcel_1.mp4"
vid_Mousetrap_invalid_no_belts_2:               str     =   "GUI/Recources/Video_files/Mousetraps_no_belts_on parcel_2.mp4"
vid_Mousetrap_invalid_Mousetraps_Canon:         str     =   "GUI/Recources/Video_files/Mousetraps_Canon_4k.mp4"
vid_label_position:                             str     =   ""# short vid of the label position (only top IO)



#__________________________________________________     Dictionarys    __________________________________________________

# num of the default colum in the workbook file
row_Num_translate_dict:                         int     =   2            # num of the start row in the workbook file
num_of_rows_translate_dict:                     int     =   186          # the number of rows to reed in succession

# primary dict
Translate_Dictonary:                            dict    =   {
"language_short": "",
"language_long" : "",
"language_Native": "",
"welcome":  "",
"goodbye":  "",
"empty":  "",
"no_data":  "",
"confirm":  "",
"deny":  "",
"start_cl":  "",
"stop_cl":  "",
"hardware_kill_switch_msg":  "",
"clear_event":  "",
"more_details":  "",
"more_information":  "",
"Software_version": "",
"reserve_1":  "",
"reserve_2":  "",
"reserve_3":  "",
"reserve_4":  "",
"reserve_5":  "",
"window_title_1":  "",
"window_title_2":  "",
"window_title_3":  "",
"window_title_4":  "",
"window_title_5":  "",
"window_title_6":  "",
"window_title_7":  "",
"window_title_8":  "",
"window_title_9":  "",
"window_title_10":  "",
"window_title_11":  "",
"window_title_12":  "",
"window_title_13":  "",
"window_title_14":  "",
"window_title_15":  "",
"window_title_16":  "",
"window_title_17":  "",
"window_title_18":  "",
"window_title_19":  "",
"window_title_20":  "",
"Help_text_1": "",
"Help_text_2": "",
"Help_text_3": "",
"Help_text_4": "",
"Help_text_5": "",
"Help_text_6": "",
"Help_text_7": "",
"Help_text_8": "",
"Help_text_9": "",
"Help_text_10": "",
"Help_text_11": "",
"Help_text_12": "",
"Help_text_13": "",
"Help_text_14": "",
"Help_text_15": "",
"Help_text_16": "",
"Help_text_17": "",
"Help_text_18": "",
"Help_text_19": "",
"Help_text_20": "",
"Help_text_21": "",
"Help_text_22": "",
"Help_text_23": "",
"Help_text_24": "",
"Help_text_25": "",
"Help_text_26": "",
"Help_text_27": "",
"Help_text_28": "",
"Help_text_29": "",
"Help_text_30": "",
"Help_text_31": "",
"Help_text_256": "",
"Help_text_33": "",
"Help_text_34": "",
"Help_text_35": "",
"Help_text_36": "",
"Help_text_37": "",
"Help_text_38": "",
"Help_text_39": "",
"Help_text_40": "",
"Help_text_41": "",
"Help_text_42": "",
"Help_text_43": "",
"Help_text_44": "",
"Help_text_45": "",
"Help_text_46": "",
"Help_text_47": "",
"Help_text_48": "",
"Help_text_49": "",
"Help_text_50": "",
"parcel_state_1":  "",
"parcel_state_2":  "",
"parcel_state_3":  "",
"parcel_state_4":  "",
"parcel_state_5":  "",
"parcel_state_6":  "",
"parcel_state_7":  "",
"parcel_state_8":  "",
"parcel_state_9":  "",
"parcel_state_10":  "",
"parcel_form_1":  "",
"parcel_form_2":  "",
"parcel_form_3":  "",
"parcel_form_4":  "",
"parcel_form_5":  "",
"parcel_form_6":  "",
"parcel_form_7":  "",
"parcel_form_8":  "",
"parcel_form_9":  "",
"parcel_form_10":  "",
"event_1":  "",
"event_2":  "",
"event_3":  "",
"event_4":  "",
"event_5":  "",
"event_6":  "",
"event_7":  "",
"event_8":  "",
"event_9":  "",
"event_10":  "",
"clear_event_cl 1":  "",
"clear_event_cl 2":  "",
"clear_event_cl 3":  "",
"clear_event_cl 4":  "",
"clear_event_cl 5":  "",
"clear_event_cl 6":  "",
"clear_event_cl 7":  "",
"clear_event_cl 8":  "",
"clear_event_cl 9":  "",
"clear_event_cl 10":  "",
"clear_event_cl 11":  "",
"clear_event_cl 12":  "",
"clear_event_cl 13":  "",
"clear_event_cl 14":  "",
"clear_event_cl 15":  "",
"hardware_info_1":  "",
"hardware_info_2":  "",
"hardware_info_3":  "",
"hardware_info_4":  "",
"hardware_info_5":  "",
"hardware_info_6":  "",
"hardware_info_7":  "",
"hardware_info_8":  "",
"hardware_info_9":  "",
"hardware_info_10":  "",
"hardware_info_11":  "",
"hardware_info_12":  "",
"hardware_info_13":  "",
"hardware_info_14":  "",
"hardware_info_15":  "",
"hardware_info_16":  "",
"hardware_info_17":  "",
"hardware_info_18":  "",
"hardware_info_19":  "",
"hardware_info_20":  "",
"project_name":  "",
"us_patent":  "",
"eu_patent":  "",
"de_patent":  "",
"ch_patent":  "",
"devs":  "",
"dev_1":  "",
"dev_2":  "",
"dev_3":  "",
"graphic_design":  "",
"graphic_designer1":  "",
"graphic_designer2":  "",
"graphic_designer3":  "",
"icon_provider_1":  "",
"icon_provider_2":  "",
"icon_provider_3":  "",
"icon_provider_name_1":  "",
"icon_provider_name_2":  "",
"icon_provider_name_3":  "",
"help_subwindow_name_1": "",
"help_subwindow_name_2": "",
"help_subwindow_name_3": "",
"help_subwindow_name_4": "",
"help_subwindow_name_5": "",
"help_subwindow_name_6": "",
"help_subwindow_name_7": "",
"help_subwindow_name_8": "",
"help_subwindow_name_8": "",
"help_subwindow_name_10": "",
                                                }    

#Fallback dict
Translate_Dictonary_Fallback:                   dict    =   {
"language_short": "EN_FB",
"language_long" : "English_Fallback",
"language_Native": "Fallback",
"welcome":  "Welcome",
"goodbye":  "Goodbye",
"empty":  "empty_fb",
"no_data":  "no_data_fb",
"confirm":  "confirm",
"deny":  "deny",
"start_cl":  "Start",
"stop_cl":  "Stop",
"hardware_kill_switch_msg":  "Emergency stop active",
"clear_event":  "Reset",
"more_details":  "Details",
"more_information":  "More information",
"Software_version":  "Software version",
"reserve_1":  "",
"reserve_2":  "",
"reserve_3":  "",
"reserve_4":  "",
"reserve_5":  "",
"window_title_1":  "Main menu",
"window_title_2":  "Help",
"window_title_3":  "Info",
"window_title_4":  "Settings",
"window_title_5":  "Translation",
"window_title_6":  "Keypad",
"window_title_7":  "",
"window_title_8":  "",
"window_title_9":  "",
"window_title_10":  "",
"window_title_11":  "",
"window_title_12":  "",
"window_title_13":  "",
"window_title_14":  "",
"window_title_15":  "",
"window_title_16":  "",
"window_title_17":  "",
"window_title_18":  "",
"window_title_19":  "",
"window_title_20":  "",
"Help_text_1": "A breef introduction in to Transporthelper",
"Help_text_2": "random teaching text 1",
"Help_text_3": "random teaching text 2",
"Help_text_4": "random teaching text 3",
"Help_text_5": "random teaching text 4",
"Help_text_6": "random teaching text 5",
"Help_text_7": "random teaching text 6",
"Help_text_8": "random teaching text 7",
"Help_text_9": "random teaching text 8",
"Help_text_10": "random teaching text 9",
"Help_text_11": "",
"Help_text_12": "",
"Help_text_13": "",
"Help_text_14": "",
"Help_text_15": "",
"Help_text_16": "",
"Help_text_17": "",
"Help_text_18": "",
"Help_text_19": "",
"Help_text_20": "",
"Help_text_21": "",
"Help_text_22": "",
"Help_text_23": "",
"Help_text_24": "",
"Help_text_25": "",
"Help_text_26": "",
"Help_text_27": "",
"Help_text_28": "",
"Help_text_29": "",
"Help_text_30": "",
"Help_text_31": "",
"Help_text_256": "",
"Help_text_33": "",
"Help_text_34": "",
"Help_text_35": "",
"Help_text_36": "",
"Help_text_37": "",
"Help_text_38": "",
"Help_text_39": "",
"Help_text_40": "",
"Help_text_41": "",
"Help_text_42": "",
"Help_text_43": "",
"Help_text_44": "",
"Help_text_45": "",
"Help_text_46": "",
"Help_text_47": "",
"Help_text_48": "",
"Help_text_49": "",
"Help_text_50": "",
"parcel_state_1":  "Package to long",
"parcel_state_2":  "Package to short",
"parcel_state_3":  "Package to high",
"parcel_state_4":  "Package to smal",
"parcel_state_5":  "",
"parcel_state_6":  "",
"parcel_state_7":  "",
"parcel_state_8":  "",
"parcel_state_9":  "",
"parcel_state_10":  "",
"parcel_form_1":  "Package form",
"parcel_form_2":  "Package dented",
"parcel_form_3":  "Parcel triangular",
"parcel_form_4":  "Parcel bottom dented",
"parcel_form_5":  "",
"parcel_form_6":  "",
"parcel_form_7":  "",
"parcel_form_8":  "",
"parcel_form_9":  "",
"parcel_form_10":  "",
"event_1":  "",
"event_2":  "",
"event_3":  "",
"event_4":  "",
"event_5":  "",
"event_6":  "",
"event_7":  "",
"event_8":  "",
"event_9":  "",
"event_10":  "",
"clear_event_cl 1":  "",
"clear_event_cl 2":  "",
"clear_event_cl 3":  "",
"clear_event_cl 4":  "",
"clear_event_cl 5":  "",
"clear_event_cl 6":  "",
"clear_event_cl 7":  "",
"clear_event_cl 8":  "",
"clear_event_cl 9":  "",
"clear_event_cl 10":  "",
"clear_event_cl 11":  "",
"clear_event_cl 12":  "",
"clear_event_cl 13":  "",
"clear_event_cl 14":  "",
"clear_event_cl 15":  "",
"hardware_info_1":  "Blocked light barrier",
"hardware_info_2":  "",
"hardware_info_3":  "",
"hardware_info_4":  "",
"hardware_info_5":  "",
"hardware_info_6":  "",
"hardware_info_7":  "",
"hardware_info_8":  "",
"hardware_info_9":  "",
"hardware_info_10":  "",
"hardware_info_11":  "",
"hardware_info_12":  "",
"hardware_info_13":  "",
"hardware_info_14":  "",
"hardware_info_15":  "",
"hardware_info_16":  "",
"hardware_info_17":  "",
"hardware_info_18":  "",
"hardware_info_19":  "",
"hardware_info_20":  "",
"project_name":  "Project name",
"us_patent":  "USPO",
"eu_patent":  "EPO",
"de_patent":  "DPMA",
"ch_patent":  "CNIPA",
"devs":   "Developer",
"dev_1":  "Tim Fuhrmann,",
"dev_2":  "Usama Gharz,",
"dev_3":  "",
"graphic_design":  "graphic design",
"graphic_designer1":  "Tim Fuhrmann",
"graphic_designer2":  "",
"graphic_designer3":  "",
"icon_provider_1":  "icon provider",
"icon_provider_2":  "",
"icon_provider_3":  "",
"icon_provider_name_1":  "icons8.com",
"icon_provider_name_2":  "",
"icon_provider_name_3":  "",
"help_subwindow_name_1": "Transport helper",
"help_subwindow_name_2": "Label",
"help_subwindow_name_3": "do's",
"help_subwindow_name_4": "don'ts",
"help_subwindow_name_5": "damaged package",
"help_subwindow_name_6": "",
"help_subwindow_name_7": "",
"help_subwindow_name_8": "",
"help_subwindow_name_9": "",
"help_subwindow_name_10": "",
                                                }

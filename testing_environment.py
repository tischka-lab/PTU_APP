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


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MachineryView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setStyleSheet(f"background-color : {MasSet.DarkmodeColor};border : none")
        self.part_items = {} # Dict to hold part items

        self.init_view()

    def init_view(self):
        pass

    def poly_part_overlay(self, polygon, part_name):
        poly_item = self.scene.addPolygon(polygon)
        poly_item.setBrush(QBrush(QColor(128, 128, 128, 100)))  # Grey transparent
        poly_item.setPen(QPen(Qt.NoPen))  # No border
        poly_item.setZValue(0)  # Below base image
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






class Test_window(QMainWindow):      #the main window GUI Window / Home Window

    def __init__(self, window_size_W :int = 2560, window_size_H :int = 1600):
        super().__init__()
        self.window_size_W      = window_size_W
        self.window_size_H      = window_size_H
        self.Translation_Dict   = MasSet.Translate_Dictonary_Fallback
        Test_window.Translation_Dict = MasSet.Translate_Dictonary_Fallback

        self.components_dict = {}

        self.setWindowTitle("Test Window")
        self.setGeometry(0, 0, window_size_W-100, window_size_H-100)
        self.setStyleSheet(f"background-color:{MasSet.DarkmodeColor};")
    
        self.init_UI() # constructs the main UI


    def init_UI(self):

        def main_CL_UI(self):
                
            main_layout = QVBoxLayout()
            main_layout.setContentsMargins (0,0,0,0)

            main_CL = QLabel()
            base_pixmap = QPixmap(MasSet.img_CL_Topview_Table_outline)
            base_img = base_pixmap.scaledToWidth(int(self.window_size_W*.8))
            main_CL.setPixmap(base_img)
            main_CL.setStyleSheet(f"background-color : {MasSet.Transparencolor};border :  4px solid black") # none") remove before intigration
            main_CL.setAlignment(Qt.AlignCenter)


            main_layout.addWidget(main_CL)
            main_layout.addStretch(1)
            main_layout.setAlignment(Qt.AlignCenter)

            return main_layout

    
        self.window_Cl_visualization = QWidget(self)
        self.window_Cl_visualization.setStyleSheet(f"background-color : {MasSet.DarkmodeColor};border : none")
        self.window_Cl_visualization.setMinimumWidth(int(self.window_size_W*.8))
        self.window_Cl_visualization.setMinimumHeight(int(self.window_size_H*.8))
        self.window_Cl_visualization.setLayout(main_CL_UI(self))
            

        self.window_main = QHBoxLayout()     
        self.window_main.setContentsMargins (0,0,0,0)

        self.window_main.addWidget(self.window_Cl_visualization)






def main():
    app = QApplication(sys.argv)
    Desktop = QDesktopWidget()
    screen_geometry = Desktop.screenGeometry()
    width = screen_geometry.width()
    heith = screen_geometry.height()
    window = Test_window(width,heith)                          # constructs the window
    window.show()                                   # opens a window
#    window.showFullScreen()                        # opens the window in fullscren
 
    sys.exit(app.exec_())                           # exits the window constructor

if __name__ == "__main__":
    main()

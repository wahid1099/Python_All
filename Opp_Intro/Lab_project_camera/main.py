"""" large
My Camera Application
author:'MD WAHID'



"""
import sys
from turtle import  width
from webbrowser import  get
 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QImage,QIcon
from PyQt5.Qtcore import QTimer

import cv2
import datetime


class Window(QWidget):
    """Main app window"""


    def __init__(self):
        super().__init__()


        # variable for app window
        self.window_width = 600
        self.window_height=400

         # image variables
        self.img_width = 640
        self.img_height = 400

        # other variables
        self.dt = '0-0-0'
        self.record_flag = False
        #load icon file
        self.camera_icon=QIcon(cap_icon_path)
        self.rec_icon=QIcon(rec_icon_path)
        self.stop_icon=QIcon(stop_icon_path)

        #to save vedio
        self.force=cv2.VideoWriter_fourcc(*'XVID')
       

        # set up window
        

        self.setWindowTitle("My camera App")
        self.setGeometry(100,100,self.window_width,self.window_height)
        self.setFixedSize(self.window_width,self.window_height)
        #setup timer
        self.timer=QTimer()
        self.timer.timeout.connect(self.update)

        self.ui()

        """ contains all ui things """
        # layout
       

    def ui(self):
          # """ contains all ui things """
          #layout
        grid=QGridLayout()
        self.setLayout(grid)

        #image_label
        self.image_label=QLabel(self)
        self.image_label.setGeometry(0,0,self.window_width,self.window_height)
        #capturebutton
        self.capturebutton=QPushButton(self)
        self.capturebutton.setIcon(self.camera_icon)
        self.capturebutton.setStyle("border-radius:30; border:2px solid black; border-width:3px")
        self.capturebutton.setFixedSize(60,60)
        self.capturebutton.clicked.connect(self.save_img)
        #record_button
        self.rec_btn=QPushButton(self)
        self.rec_btn.setStyleSheet("border-radius:30; border:2px solid black; border-width:3px")
        self.rec_btn.setFixedSize(60,60)
        self.rec_btn.clicked.connect(self.record)



        if not self.timer.isActive():
            self.cap=cv2.VideoCapture(0) 
            self.timer.start(20)
        

        #add thing to the setLayout
        grid.addWidget(self.capturebutton,0,0)
        grid.addWidget(self.image_label,0,1,2,3)
        grid.addWidget(self.rec_btn,1,0)


        self.show()
    def update(self):
        """ Update frames"""
        _, self.frame=self.cap.read()
        copy_frame=self.frame
        if self.record_flag==True:
            print("Recording.....")
            self.out.write(copy_frame)
            self.rec_btn.setIcon(self.stop_icon)
            self.frame=cv2.circle(self.frame,(20,70),5,(0,0,255),10)
        else:
            self.rec_btn.setIcon(self.rec_icon)



        frame=cv2.cvtColor(self.frame,cv2.COLOR_BGR2RBG)
        height,width,channel=frame.shape
        step=channel*width
        q_frame=QImage(frame.data,width,height,step,QImage.Format_RGB888)
        self.image_label.setPixmat(Qpixmap.fromImage(q_frame))

    def save_image(self):
        """"save image from camera image"""
        
        print("Saving image")
        self.get_time()
        cv2.imwrite(f"{self.dt}.jpg", self.frame)

    def record(self):
        # """ record video """
        print(self.record_flag)

        if self.record_flag == True:
            self.record_flag = False
            print("Stopping the record process")
        else:
            self.record_flag = True
            print("Starting to record")
            self.get_time()

            self.out = cv2.VideoWriter(f"{self.dt}.avi", self.fourcc, 20.0, (640, 480))
    
    def get_time(self):
        now = datetime.datetime.now()
        self.dt = now.strftime("%m-%d-%y, %H-%M-%S")
        print(self.dt)



# run
if __name__ == '__main__':
    cap_icon_path = 'Assets/camera.png'
    rec_icon_path = 'Assets/video-camera.png'
    stop_icon_path = 'Assets/stop-button.png'

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facedtwork(live1) .ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from id_faces import facebox
from facerec_from_webcam import facecode
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2,numpy as np

class Ui_Facedetection(object):
    def setupUi(self, Facedetection):
        Facedetection.setObjectName("Facedetection")
        Facedetection.setWindowModality(QtCore.Qt.ApplicationModal)
        Facedetection.resize(640, 490)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Facedetection.sizePolicy().hasHeightForWidth())
        Facedetection.setSizePolicy(sizePolicy)
        Facedetection.setMinimumSize(QtCore.QSize(640, 490))
        Facedetection.setAutoFillBackground(True)
        Facedetection.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(Facedetection)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.consolewidget = QtWidgets.QWidget(self.centralwidget)
        self.consolewidget.setEnabled(True)
        self.consolewidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.consolewidget.setObjectName("consolewidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.consolewidget)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.consolelayout = QtWidgets.QVBoxLayout()
        self.consolelayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.consolelayout.setObjectName("consolelayout")
        self.consolelabel = QtWidgets.QLabel(self.consolewidget)
        self.consolelabel.setObjectName("consolelabel")
        self.consolelayout.addWidget(self.consolelabel)
        self.listWidget = QtWidgets.QListWidget(self.consolewidget)
        self.listWidget.setObjectName("listWidget")
        self.consolelayout.addWidget(self.listWidget)
        self.verticalLayout_3.addLayout(self.consolelayout)
        self.gridLayout_3.addWidget(self.consolewidget, 0, 4, 1, 1)
        self.scanLayout_2 = QtWidgets.QVBoxLayout()
        self.scanLayout_2.setObjectName("scanLayout_2")
        self.scanbutton = QtWidgets.QPushButton(self.centralwidget)
        self.scanbutton.setObjectName("scanbutton")
        self.scanLayout_2.addWidget(self.scanbutton)
        self.gridLayout_3.addLayout(self.scanLayout_2, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 2, 1, 1)
        self.addprofileWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addprofileWidget.sizePolicy().hasHeightForWidth())
        self.addprofileWidget.setSizePolicy(sizePolicy)
        self.addprofileWidget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.addprofileWidget.setObjectName("addprofileWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.addprofileWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.addprofileWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.addprofileWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.savebutton = QtWidgets.QPushButton(self.addprofileWidget)
        self.savebutton.setObjectName("savebutton")
        self.verticalLayout.addWidget(self.savebutton)
        self.gridLayout_3.addWidget(self.addprofileWidget, 2, 0, 1, 2)
        self.Imagelabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Imagelabel.sizePolicy().hasHeightForWidth())
        self.Imagelabel.setSizePolicy(sizePolicy)
        self.Imagelabel.setFrameShape(QtWidgets.QFrame.Box)
        self.Imagelabel.setText("")
        self.Imagelabel.setObjectName("Imagelabel")
        self.gridLayout_3.addWidget(self.Imagelabel, 0, 0, 1, 4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.golivebtn = QtWidgets.QPushButton(self.centralwidget)
        self.golivebtn.setObjectName("golivebtn")
        self.verticalLayout_2.addWidget(self.golivebtn)
        self.stoplivebtn = QtWidgets.QPushButton(self.centralwidget)
        self.stoplivebtn.setObjectName("stoplivebtn")
        self.verticalLayout_2.addWidget(self.stoplivebtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 4, 1, 1)
        self.consolewidget.raise_()
        self.addprofileWidget.raise_()
        self.Imagelabel.raise_()
        Facedetection.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Facedetection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        Facedetection.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Facedetection)
        self.statusbar.setObjectName("statusbar")
        Facedetection.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(Facedetection)
        self.actionopen.setObjectName("actionopen")
        self.actionexit = QtWidgets.QAction(Facedetection)
        self.actionexit.setObjectName("actionexit")
        self.actionAbout = QtWidgets.QAction(Facedetection)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionexit)
        self.menuabout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(Facedetection)
        QtCore.QMetaObject.connectSlotsByName(Facedetection)
        #initial image
        pixmap = QtGui.QPixmap("arunimage_with_boxes.jpg")  # Setup pixmap with the provided image
        #pixmap = pixmap.scaled(640,480,
        #                       QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.Imagelabel.setPixmap(pixmap)  # Set the pixmap onto the label
        self.Imagelabel.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        #end initial

        self.savebutton.clicked.connect(self.addItem)
        self.scanbutton.clicked.connect(self.setImage)
        self.golivebtn.clicked.connect(self.go_live)
        self.stoplivebtn.clicked.connect(self.stop_live)
        self.fprocess = facecode()

    def addItem(self):
        import numpy as np
        value = self.lineEdit.text()  # Get the value of the lineEdit
        self.lineEdit.clear()  # Clear the text
        self.listWidget.addItem(value)  # Add the value we got to the list
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "",
                                                            "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
        if fileName:  # If the user gives a file
            import face_recognition
            image = face_recognition.load_image_file(fileName)
            face_encoding = face_recognition.face_encodings(image)[0]
            # print(np.shape(face_encoding))
            try:
                ldencd = np.load('known_face_encodings.npy')

                # print(np.append(ldencd,face_encoding,axis=0))
                np.save('known_face_encodings.npy', np.append(ldencd, [face_encoding], axis=0))

            except:

                np.save('known_face_encodings.npy', [face_encoding])

            try:
                with open("known_face_names.txt", 'a') as f:
                    f.write(str(value) + '\n')
            except:
                with open("known_face_names.txt", 'w') as f:
                    f.write(str(value) + '\n')

    def go_live(self):
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def update_frame(self):
        ret, self.image = self.capture.read()

        self.frame = facecode.faceplot(self.image)
        #self.frame = cv2.flip(self.frame, 1)
        self.display_image(self.frame, 1)

    def stop_live(self):
        self.timer.stop()
        self.capture.release()
        cv2.destroyAllWindows()
    def display_image(self, img, window=1):
        rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)

        if window == 1:
            self.Imagelabel.setPixmap(QPixmap.fromImage(p))
            #self.Imagelabel.setSizePolicy(self,Q)
    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "",
                                                            "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file

        if fileName:  # If the user gives a file
            fileName, recname = facebox(fileName)
            pixmap = QtGui.QPixmap(fileName)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.Imagelabel.width(), self.Imagelabel.height(),
                                   QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.Imagelabel.setPixmap(pixmap)  # Set the pixmap onto the label
            self.Imagelabel.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
            self.lineEdit.clear()  # Clear the text
            self.listWidget.addItem('Face Detected:' + recname)  # Add the value we got to the list

    def retranslateUi(self, Facedetection):
            _translate = QtCore.QCoreApplication.translate
            Facedetection.setWindowTitle(_translate("Facedetection", "Face Detection"))
            self.consolelabel.setText(_translate("Facedetection", "Console:"))
            self.scanbutton.setText(_translate("Facedetection", "ScanImage"))
            self.label.setText(_translate("Facedetection", "Name"))
            self.savebutton.setText(_translate("Facedetection", "Add New Profile"))
            self.golivebtn.setText(_translate("Facedetection", "Go Live"))
            self.stoplivebtn.setText(_translate("Facedetection", "Stop Live"))
            self.menuFile.setTitle(_translate("Facedetection", "File"))
            self.menuabout.setTitle(_translate("Facedetection", "Help"))
            self.actionopen.setText(_translate("Facedetection", "open"))
            self.actionexit.setText(_translate("Facedetection", "exit"))
            self.actionAbout.setText(_translate("Facedetection", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Facedetection = QtWidgets.QMainWindow()
    ui = Ui_Facedetection()
    ui.setupUi(Facedetection)
    Facedetection.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facedt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from id_faces import facebox


class Ui_Facedetection(object):
    def setupUi(self, Facedetection):
        Facedetection.setObjectName("Facedetection")
        Facedetection.resize(640, 481)
        self.centralwidget = QtWidgets.QWidget(Facedetection)
        self.centralwidget.setObjectName("centralwidget")
        self.Imagelabel = QtWidgets.QLabel(self.centralwidget)
        self.Imagelabel.setGeometry(QtCore.QRect(20, 20, 441, 301))
        self.Imagelabel.setFrameShape(QtWidgets.QFrame.Box)
        self.Imagelabel.setText("")
        self.Imagelabel.setObjectName("Imagelabel")
        self.scanbutton = QtWidgets.QPushButton(self.centralwidget)
        self.scanbutton.setGeometry(QtCore.QRect(480, 360, 111, 27))
        self.scanbutton.setObjectName("scanbutton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 330, 201, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.savebutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.savebutton.setObjectName("savebutton")
        self.gridLayout.addWidget(self.savebutton, 1, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 20, 171, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
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
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionexit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(Facedetection)
        QtCore.QMetaObject.connectSlotsByName(Facedetection)

        self.savebutton.clicked.connect(self.addItem)
        self.scanbutton.clicked.connect(self.setImage)


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
            face_encoding =face_recognition.face_encodings(image)[0]
            print(np.shape(face_encoding))
            try:
                ldencd = np.load('known_face_encodings.npy')

                #print(np.append(ldencd,face_encoding,axis=0))
                np.save('known_face_encodings.npy', np.append(ldencd,[face_encoding],axis=0))

            except:

                np.save('known_face_encodings.npy', [face_encoding])

            try:
                with open("known_face_names.txt", 'a') as f:
                    f.write(str(value) + '\n')
            except:
                with open("known_face_names.txt", 'w') as f:
                    f.write(str(value) + '\n')




    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "",
                                                            "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file

        if fileName:  # If the user gives a file
            fileName,recname = facebox(fileName)
            pixmap = QtGui.QPixmap(fileName)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.Imagelabel.width(), self.Imagelabel.height(),
                                   QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.Imagelabel.setPixmap(pixmap)  # Set the pixmap onto the label
            self.Imagelabel.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
            self.lineEdit.clear()  # Clear the text
            self.listWidget.addItem('Face Detected:'+recname)  # Add the value we got to the list

    def retranslateUi(self, Facedetection):
        _translate = QtCore.QCoreApplication.translate
        Facedetection.setWindowTitle(_translate("Facedetection", "Facedetection"))
        self.scanbutton.setText(_translate("Facedetection", "Scan"))
        self.label.setText(_translate("Facedetection", "Name"))
        self.savebutton.setText(_translate("Facedetection", "Save"))
        self.label_2.setText(_translate("Facedetection", "Console:"))
        self.menuFile.setTitle(_translate("Facedetection", "File"))
        self.menuabout.setTitle(_translate("Facedetection", "about"))
        self.actionopen.setText(_translate("Facedetection", "open"))
        self.actionexit.setText(_translate("Facedetection", "exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Facedetection = QtWidgets.QMainWindow()
    ui = Ui_Facedetection()
    ui.setupUi(Facedetection)
    Facedetection.show()
    sys.exit(app.exec_())


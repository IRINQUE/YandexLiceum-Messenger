# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yandex.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1000, 800))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1000, 800))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_new_user = QtWidgets.QWidget()
        self.page_new_user.setObjectName("page_new_user")
        self.B_new_user_reg = QtWidgets.QPushButton(self.page_new_user)
        self.B_new_user_reg.setGeometry(QtCore.QRect(355, 500, 310, 50))
        self.B_new_user_reg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.B_new_user_reg.setFont(font)
        self.B_new_user_reg.setObjectName("B_new_user_reg")
        self.B_new_user_log = QtWidgets.QPushButton(self.page_new_user)
        self.B_new_user_log.setGeometry(QtCore.QRect(355, 400, 310, 50))
        self.B_new_user_log.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.B_new_user_log.setFont(font)
        self.B_new_user_log.setObjectName("B_new_user_log")
        self.L_new_user_const_1 = QtWidgets.QLabel(self.page_new_user)
        self.L_new_user_const_1.setGeometry(QtCore.QRect(250, 120, 500, 380))
        self.L_new_user_const_1.setText("")
        self.L_new_user_const_1.setObjectName("L_new_user_const_1")
        self.L_new_user_const_2 = QtWidgets.QLabel(self.page_new_user)
        self.L_new_user_const_2.setGeometry(QtCore.QRect(250, 280, 500, 380))
        self.L_new_user_const_2.setText("")
        self.L_new_user_const_2.setObjectName("L_new_user_const_2")
        self.B_new_user_ic_log = QtWidgets.QPushButton(self.page_new_user)
        self.B_new_user_ic_log.setGeometry(QtCore.QRect(300, 400, 50, 50))
        self.B_new_user_ic_log.setText("")
        self.B_new_user_ic_log.setObjectName("B_new_user_ic_log")
        self.B_new_user_ic_reg = QtWidgets.QPushButton(self.page_new_user)
        self.B_new_user_ic_reg.setGeometry(QtCore.QRect(300, 500, 50, 50))
        self.B_new_user_ic_reg.setText("")
        self.B_new_user_ic_reg.setObjectName("B_new_user_ic_reg")
        self.L_new_user_const_0 = QtWidgets.QLabel(self.page_new_user)
        self.L_new_user_const_0.setGeometry(QtCore.QRect(380, 150, 300, 100))
        self.L_new_user_const_0.setObjectName("L_new_user_const_0")
        self.skip = QtWidgets.QPushButton(self.page_new_user)
        self.skip.setGeometry(QtCore.QRect(670, 590, 41, 41))
        self.skip.setText("")
        self.skip.setObjectName("skip")
        self.L_new_user_const_3 = QtWidgets.QLabel(self.page_new_user)
        self.L_new_user_const_3.setGeometry(QtCore.QRect(250, 640, 500, 45))
        self.L_new_user_const_3.setText("")
        self.L_new_user_const_3.setObjectName("L_new_user_const_3")
        self.L_new_user_const_1.raise_()
        self.L_new_user_const_2.raise_()
        self.B_new_user_log.raise_()
        self.B_new_user_reg.raise_()
        self.B_new_user_ic_log.raise_()
        self.B_new_user_ic_reg.raise_()
        self.L_new_user_const_0.raise_()
        self.skip.raise_()
        self.L_new_user_const_3.raise_()
        self.stackedWidget.addWidget(self.page_new_user)
        self.page_log = QtWidgets.QWidget()
        self.page_log.setObjectName("page_log")
        self.L_log_const_1 = QtWidgets.QLabel(self.page_log)
        self.L_log_const_1.setGeometry(QtCore.QRect(250, 120, 500, 380))
        self.L_log_const_1.setText("")
        self.L_log_const_1.setObjectName("L_log_const_1")
        self.L_log_const_2 = QtWidgets.QLabel(self.page_log)
        self.L_log_const_2.setGeometry(QtCore.QRect(250, 280, 500, 380))
        self.L_log_const_2.setText("")
        self.L_log_const_2.setObjectName("L_log_const_2")
        self.L_log_const_0 = QtWidgets.QLabel(self.page_log)
        self.L_log_const_0.setGeometry(QtCore.QRect(410, 150, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.L_log_const_0.setFont(font)
        self.L_log_const_0.setObjectName("L_log_const_0")
        self.B_log_ic_log = QtWidgets.QPushButton(self.page_log)
        self.B_log_ic_log.setGeometry(QtCore.QRect(300, 400, 50, 50))
        self.B_log_ic_log.setText("")
        self.B_log_ic_log.setObjectName("B_log_ic_log")
        self.B_log_ic_reg = QtWidgets.QPushButton(self.page_log)
        self.B_log_ic_reg.setGeometry(QtCore.QRect(300, 500, 50, 50))
        self.B_log_ic_reg.setText("")
        self.B_log_ic_reg.setObjectName("B_log_ic_reg")
        self.LE_log_login = QtWidgets.QLineEdit(self.page_log)
        self.LE_log_login.setGeometry(QtCore.QRect(355, 400, 310, 50))
        self.LE_log_login.setObjectName("LE_log_login")
        self.LE_log_password = QtWidgets.QLineEdit(self.page_log)
        self.LE_log_password.setGeometry(QtCore.QRect(355, 500, 310, 50))
        self.LE_log_password.setObjectName("LE_log_password")
        self.B_log_back = QtWidgets.QPushButton(self.page_log)
        self.B_log_back.setGeometry(QtCore.QRect(250, 120, 70, 70))
        self.B_log_back.setText("")
        self.B_log_back.setObjectName("B_log_back")
        self.B_log_save = QtWidgets.QPushButton(self.page_log)
        self.B_log_save.setGeometry(QtCore.QRect(375, 580, 250, 40))
        self.B_log_save.setObjectName("B_log_save")
        self.B_log_warning_1 = QtWidgets.QPushButton(self.page_log)
        self.B_log_warning_1.setGeometry(QtCore.QRect(680, 400, 51, 51))
        self.B_log_warning_1.setText("")
        self.B_log_warning_1.setObjectName("B_log_warning_1")
        self.B_log_warning_2 = QtWidgets.QPushButton(self.page_log)
        self.B_log_warning_2.setGeometry(QtCore.QRect(680, 500, 51, 51))
        self.B_log_warning_2.setText("")
        self.B_log_warning_2.setObjectName("B_log_warning_2")
        self.L_log_warning = QtWidgets.QLabel(self.page_log)
        self.L_log_warning.setGeometry(QtCore.QRect(360, 360, 301, 20))
        self.L_log_warning.setText("")
        self.L_log_warning.setObjectName("L_log_warning")
        self.L_log_const_3 = QtWidgets.QLabel(self.page_log)
        self.L_log_const_3.setGeometry(QtCore.QRect(250, 640, 500, 45))
        self.L_log_const_3.setText("")
        self.L_log_const_3.setObjectName("L_log_const_3")
        self.B_log_forgot_password = QtWidgets.QPushButton(self.page_log)
        self.B_log_forgot_password.setGeometry(QtCore.QRect(440, 630, 125, 23))
        self.B_log_forgot_password.setObjectName("B_log_forgot_password")
        self.L_log_const_1.raise_()
        self.L_log_const_2.raise_()
        self.L_log_const_0.raise_()
        self.B_log_ic_log.raise_()
        self.LE_log_login.raise_()
        self.LE_log_password.raise_()
        self.B_log_ic_reg.raise_()
        self.B_log_save.raise_()
        self.B_log_back.raise_()
        self.B_log_warning_1.raise_()
        self.B_log_warning_2.raise_()
        self.L_log_warning.raise_()
        self.L_log_const_3.raise_()
        self.B_log_forgot_password.raise_()
        self.stackedWidget.addWidget(self.page_log)
        self.page_reg = QtWidgets.QWidget()
        self.page_reg.setObjectName("page_reg")
        self.B_reg_back = QtWidgets.QPushButton(self.page_reg)
        self.B_reg_back.setGeometry(QtCore.QRect(250, 120, 70, 70))
        self.B_reg_back.setText("")
        self.B_reg_back.setObjectName("B_reg_back")
        self.L_reg_const_1 = QtWidgets.QLabel(self.page_reg)
        self.L_reg_const_1.setGeometry(QtCore.QRect(250, 120, 500, 380))
        self.L_reg_const_1.setText("")
        self.L_reg_const_1.setObjectName("L_reg_const_1")
        self.L_reg_const_2 = QtWidgets.QLabel(self.page_reg)
        self.L_reg_const_2.setGeometry(QtCore.QRect(250, 280, 500, 380))
        self.L_reg_const_2.setText("")
        self.L_reg_const_2.setObjectName("L_reg_const_2")
        self.L_reg_const_0 = QtWidgets.QLabel(self.page_reg)
        self.L_reg_const_0.setGeometry(QtCore.QRect(410, 150, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_reg_const_0.setFont(font)
        self.L_reg_const_0.setObjectName("L_reg_const_0")
        self.B_reg_ic_log = QtWidgets.QPushButton(self.page_reg)
        self.B_reg_ic_log.setGeometry(QtCore.QRect(300, 340, 50, 50))
        self.B_reg_ic_log.setText("")
        self.B_reg_ic_log.setObjectName("B_reg_ic_log")
        self.LE_reg_login = QtWidgets.QLineEdit(self.page_reg)
        self.LE_reg_login.setGeometry(QtCore.QRect(355, 340, 310, 50))
        self.LE_reg_login.setObjectName("LE_reg_login")
        self.LE_reg_password_2 = QtWidgets.QLineEdit(self.page_reg)
        self.LE_reg_password_2.setGeometry(QtCore.QRect(355, 500, 310, 50))
        self.LE_reg_password_2.setObjectName("LE_reg_password_2")
        self.B_reg_ic_reg_2 = QtWidgets.QPushButton(self.page_reg)
        self.B_reg_ic_reg_2.setGeometry(QtCore.QRect(300, 500, 50, 50))
        self.B_reg_ic_reg_2.setText("")
        self.B_reg_ic_reg_2.setObjectName("B_reg_ic_reg_2")
        self.B_reg_save = QtWidgets.QPushButton(self.page_reg)
        self.B_reg_save.setGeometry(QtCore.QRect(375, 580, 250, 40))
        self.B_reg_save.setObjectName("B_reg_save")
        self.LE_reg_password_1 = QtWidgets.QLineEdit(self.page_reg)
        self.LE_reg_password_1.setGeometry(QtCore.QRect(355, 420, 310, 50))
        self.LE_reg_password_1.setObjectName("LE_reg_password_1")
        self.B_reg_ic_reg_1 = QtWidgets.QPushButton(self.page_reg)
        self.B_reg_ic_reg_1.setGeometry(QtCore.QRect(300, 420, 50, 50))
        self.B_reg_ic_reg_1.setText("")
        self.B_reg_ic_reg_1.setObjectName("B_reg_ic_reg_1")
        self.B_reg_warning_2 = QtWidgets.QPushButton(self.page_reg)
        self.B_reg_warning_2.setGeometry(QtCore.QRect(680, 420, 51, 51))
        self.B_reg_warning_2.setText("")
        self.B_reg_warning_2.setObjectName("B_reg_warning_2")
        self.B_reg_warning_3 = QtWidgets.QPushButton(self.page_reg)
        self.B_reg_warning_3.setGeometry(QtCore.QRect(680, 500, 51, 51))
        self.B_reg_warning_3.setText("")
        self.B_reg_warning_3.setObjectName("B_reg_warning_3")
        self.B_reg_warning_1 = QtWidgets.QPushButton(self.page_reg)
        self.B_reg_warning_1.setGeometry(QtCore.QRect(680, 340, 51, 51))
        self.B_reg_warning_1.setText("")
        self.B_reg_warning_1.setObjectName("B_reg_warning_1")
        self.L_reg_warning_1 = QtWidgets.QLabel(self.page_reg)
        self.L_reg_warning_1.setGeometry(QtCore.QRect(360, 280, 301, 20))
        self.L_reg_warning_1.setText("")
        self.L_reg_warning_1.setObjectName("L_reg_warning_1")
        self.L_reg_warning_2 = QtWidgets.QLabel(self.page_reg)
        self.L_reg_warning_2.setGeometry(QtCore.QRect(360, 310, 301, 20))
        self.L_reg_warning_2.setText("")
        self.L_reg_warning_2.setObjectName("L_reg_warning_2")
        self.L_reg_const_3 = QtWidgets.QLabel(self.page_reg)
        self.L_reg_const_3.setGeometry(QtCore.QRect(250, 640, 500, 45))
        self.L_reg_const_3.setText("")
        self.L_reg_const_3.setObjectName("L_reg_const_3")
        self.L_reg_const_1.raise_()
        self.L_reg_const_2.raise_()
        self.L_reg_const_0.raise_()
        self.B_reg_ic_log.raise_()
        self.LE_reg_login.raise_()
        self.LE_reg_password_2.raise_()
        self.B_reg_ic_reg_2.raise_()
        self.B_reg_save.raise_()
        self.B_reg_back.raise_()
        self.LE_reg_password_1.raise_()
        self.B_reg_ic_reg_1.raise_()
        self.B_reg_warning_2.raise_()
        self.B_reg_warning_3.raise_()
        self.B_reg_warning_1.raise_()
        self.L_reg_warning_1.raise_()
        self.L_reg_warning_2.raise_()
        self.L_reg_const_3.raise_()
        self.stackedWidget.addWidget(self.page_reg)
        self.page_forgot_password = QtWidgets.QWidget()
        self.page_forgot_password.setObjectName("page_forgot_password")
        self.L_forgot_password_const_0 = QtWidgets.QLabel(self.page_forgot_password)
        self.L_forgot_password_const_0.setGeometry(QtCore.QRect(410, 150, 300, 100))
        self.L_forgot_password_const_0.setObjectName("L_forgot_password_const_0")
        self.L_forgot_password_const_1 = QtWidgets.QLabel(self.page_forgot_password)
        self.L_forgot_password_const_1.setGeometry(QtCore.QRect(250, 120, 500, 380))
        self.L_forgot_password_const_1.setText("")
        self.L_forgot_password_const_1.setObjectName("L_forgot_password_const_1")
        self.L_forgot_password_const_2 = QtWidgets.QLabel(self.page_forgot_password)
        self.L_forgot_password_const_2.setGeometry(QtCore.QRect(250, 280, 500, 380))
        self.L_forgot_password_const_2.setText("")
        self.L_forgot_password_const_2.setObjectName("L_forgot_password_const_2")
        self.L_forgot_password_const_3 = QtWidgets.QLabel(self.page_forgot_password)
        self.L_forgot_password_const_3.setGeometry(QtCore.QRect(250, 640, 500, 45))
        self.L_forgot_password_const_3.setText("")
        self.L_forgot_password_const_3.setObjectName("L_forgot_password_const_3")
        self.LE_forgot_password_login = QtWidgets.QLineEdit(self.page_forgot_password)
        self.LE_forgot_password_login.setGeometry(QtCore.QRect(355, 340, 310, 50))
        self.LE_forgot_password_login.setObjectName("LE_forgot_password_login")
        self.LE_forgot_password_email = QtWidgets.QLineEdit(self.page_forgot_password)
        self.LE_forgot_password_email.setGeometry(QtCore.QRect(355, 420, 310, 50))
        self.LE_forgot_password_email.setObjectName("LE_forgot_password_email")
        self.LE_forgot_password_code = QtWidgets.QLineEdit(self.page_forgot_password)
        self.LE_forgot_password_code.setGeometry(QtCore.QRect(355, 500, 310, 50))
        self.LE_forgot_password_code.setObjectName("LE_forgot_password_code")
        self.B_forgot_password_save = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_save.setGeometry(QtCore.QRect(375, 580, 250, 40))
        self.B_forgot_password_save.setObjectName("B_forgot_password_save")
        self.B_forgot_password_ic_log = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_ic_log.setGeometry(QtCore.QRect(300, 340, 50, 50))
        self.B_forgot_password_ic_log.setText("")
        self.B_forgot_password_ic_log.setObjectName("B_forgot_password_ic_log")
        self.B_forgot_password_ic_email = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_ic_email.setGeometry(QtCore.QRect(300, 420, 50, 50))
        self.B_forgot_password_ic_email.setText("")
        self.B_forgot_password_ic_email.setObjectName("B_forgot_password_ic_email")
        self.B_forgot_password_ic_code = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_ic_code.setGeometry(QtCore.QRect(300, 500, 50, 50))
        self.B_forgot_password_ic_code.setText("")
        self.B_forgot_password_ic_code.setObjectName("B_forgot_password_ic_code")
        self.B_forgot_password_back = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_back.setGeometry(QtCore.QRect(250, 120, 70, 70))
        self.B_forgot_password_back.setText("")
        self.B_forgot_password_back.setObjectName("B_forgot_password_back")
        self.B_forgot_password_change = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_change.setGeometry(QtCore.QRect(439, 630, 125, 23))
        self.B_forgot_password_change.setObjectName("B_forgot_password_change")
        self.B_forgot_password_warning_1 = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_warning_1.setGeometry(QtCore.QRect(680, 340, 51, 51))
        self.B_forgot_password_warning_1.setText("")
        self.B_forgot_password_warning_1.setObjectName("B_forgot_password_warning_1")
        self.B_forgot_password_warning_2 = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_warning_2.setGeometry(QtCore.QRect(680, 420, 51, 51))
        self.B_forgot_password_warning_2.setText("")
        self.B_forgot_password_warning_2.setObjectName("B_forgot_password_warning_2")
        self.B_forgot_password_warning_3 = QtWidgets.QPushButton(self.page_forgot_password)
        self.B_forgot_password_warning_3.setGeometry(QtCore.QRect(680, 500, 51, 51))
        self.B_forgot_password_warning_3.setText("")
        self.B_forgot_password_warning_3.setObjectName("B_forgot_password_warning_3")
        self.L_forgot_password_warning = QtWidgets.QLabel(self.page_forgot_password)
        self.L_forgot_password_warning.setGeometry(QtCore.QRect(360, 290, 301, 20))
        self.L_forgot_password_warning.setText("")
        self.L_forgot_password_warning.setObjectName("L_forgot_password_warning")
        self.L_forgot_password_const_3.raise_()
        self.L_forgot_password_const_1.raise_()
        self.L_forgot_password_const_2.raise_()
        self.L_forgot_password_const_0.raise_()
        self.LE_forgot_password_login.raise_()
        self.LE_forgot_password_email.raise_()
        self.LE_forgot_password_code.raise_()
        self.B_forgot_password_save.raise_()
        self.B_forgot_password_ic_log.raise_()
        self.B_forgot_password_ic_email.raise_()
        self.B_forgot_password_ic_code.raise_()
        self.B_forgot_password_back.raise_()
        self.B_forgot_password_change.raise_()
        self.B_forgot_password_warning_1.raise_()
        self.B_forgot_password_warning_2.raise_()
        self.B_forgot_password_warning_3.raise_()
        self.L_forgot_password_warning.raise_()
        self.stackedWidget.addWidget(self.page_forgot_password)
        self.page_user = QtWidgets.QWidget()
        self.page_user.setObjectName("page_user")
        self.L_user_const_1 = QtWidgets.QLabel(self.page_user)
        self.L_user_const_1.setGeometry(QtCore.QRect(250, 120, 500, 380))
        self.L_user_const_1.setText("")
        self.L_user_const_1.setObjectName("L_user_const_1")
        self.L_user_const_2 = QtWidgets.QLabel(self.page_user)
        self.L_user_const_2.setGeometry(QtCore.QRect(250, 280, 500, 380))
        self.L_user_const_2.setText("")
        self.L_user_const_2.setObjectName("L_user_const_2")
        self.B_user_setting = QtWidgets.QPushButton(self.page_user)
        self.B_user_setting.setGeometry(QtCore.QRect(250, 120, 70, 70))
        self.B_user_setting.setText("")
        self.B_user_setting.setObjectName("B_user_setting")
        self.L_user_const_0 = QtWidgets.QLabel(self.page_user)
        self.L_user_const_0.setGeometry(QtCore.QRect(360, 150, 300, 100))
        self.L_user_const_0.setObjectName("L_user_const_0")
        self.F_user_1 = QtWidgets.QFrame(self.page_user)
        self.F_user_1.setGeometry(QtCore.QRect(250, 170, 70, 111))
        self.F_user_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_user_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_user_1.setObjectName("F_user_1")
        self.B_user_frame_1 = QtWidgets.QPushButton(self.F_user_1)
        self.B_user_frame_1.setGeometry(QtCore.QRect(10, 40, 51, 51))
        self.B_user_frame_1.setText("")
        self.B_user_frame_1.setObjectName("B_user_frame_1")
        self.F_user_2 = QtWidgets.QFrame(self.page_user)
        self.F_user_2.setGeometry(QtCore.QRect(250, 280, 70, 141))
        self.F_user_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_user_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_user_2.setObjectName("F_user_2")
        self.B_user_frame_2 = QtWidgets.QPushButton(self.F_user_2)
        self.B_user_frame_2.setGeometry(QtCore.QRect(10, 0, 51, 51))
        self.B_user_frame_2.setText("")
        self.B_user_frame_2.setObjectName("B_user_frame_2")
        self.B_user_frame_3 = QtWidgets.QPushButton(self.F_user_2)
        self.B_user_frame_3.setGeometry(QtCore.QRect(10, 70, 51, 51))
        self.B_user_frame_3.setText("")
        self.B_user_frame_3.setObjectName("B_user_frame_3")
        self.L_user_const_3 = QtWidgets.QLabel(self.page_user)
        self.L_user_const_3.setGeometry(QtCore.QRect(250, 640, 500, 45))
        self.L_user_const_3.setText("")
        self.L_user_const_3.setObjectName("L_user_const_3")
        self.L_user_const_1.raise_()
        self.L_user_const_2.raise_()
        self.L_user_const_0.raise_()
        self.F_user_1.raise_()
        self.F_user_2.raise_()
        self.L_user_const_3.raise_()
        self.B_user_setting.raise_()
        self.stackedWidget.addWidget(self.page_user)
        self.page_profile = QtWidgets.QWidget()
        self.page_profile.setObjectName("page_profile")
        self.L_profile_const_1 = QtWidgets.QLabel(self.page_profile)
        self.L_profile_const_1.setGeometry(QtCore.QRect(250, 120, 500, 380))
        self.L_profile_const_1.setText("")
        self.L_profile_const_1.setObjectName("L_profile_const_1")
        self.L_profile_const_2 = QtWidgets.QLabel(self.page_profile)
        self.L_profile_const_2.setGeometry(QtCore.QRect(250, 280, 500, 380))
        self.L_profile_const_2.setText("")
        self.L_profile_const_2.setObjectName("L_profile_const_2")
        self.L_profile_const_0 = QtWidgets.QLabel(self.page_profile)
        self.L_profile_const_0.setGeometry(QtCore.QRect(410, 150, 300, 100))
        self.L_profile_const_0.setObjectName("L_profile_const_0")
        self.LE_profile_login = QtWidgets.QLineEdit(self.page_profile)
        self.LE_profile_login.setGeometry(QtCore.QRect(355, 340, 310, 50))
        self.LE_profile_login.setObjectName("LE_profile_login")
        self.L_profile_1 = QtWidgets.QLabel(self.page_profile)
        self.L_profile_1.setGeometry(QtCore.QRect(360, 320, 101, 16))
        self.L_profile_1.setObjectName("L_profile_1")
        self.LE_profile_password = QtWidgets.QLineEdit(self.page_profile)
        self.LE_profile_password.setGeometry(QtCore.QRect(355, 550, 310, 50))
        self.LE_profile_password.setObjectName("LE_profile_password")
        self.L_profile_3 = QtWidgets.QLabel(self.page_profile)
        self.L_profile_3.setGeometry(QtCore.QRect(360, 530, 101, 16))
        self.L_profile_3.setObjectName("L_profile_3")
        self.B_profile_show_password = QtWidgets.QPushButton(self.page_profile)
        self.B_profile_show_password.setGeometry(QtCore.QRect(630, 560, 31, 31))
        self.B_profile_show_password.setText("")
        self.B_profile_show_password.setObjectName("B_profile_show_password")
        self.B_profile_back = QtWidgets.QPushButton(self.page_profile)
        self.B_profile_back.setGeometry(QtCore.QRect(250, 120, 70, 70))
        self.B_profile_back.setText("")
        self.B_profile_back.setObjectName("B_profile_back")
        self.L_profile_const_3 = QtWidgets.QLabel(self.page_profile)
        self.L_profile_const_3.setGeometry(QtCore.QRect(250, 640, 500, 45))
        self.L_profile_const_3.setText("")
        self.L_profile_const_3.setObjectName("L_profile_const_3")
        self.LE_profile_email = QtWidgets.QLineEdit(self.page_profile)
        self.LE_profile_email.setGeometry(QtCore.QRect(355, 440, 310, 50))
        self.LE_profile_email.setObjectName("LE_profile_email")
        self.L_profile_2 = QtWidgets.QLabel(self.page_profile)
        self.L_profile_2.setGeometry(QtCore.QRect(360, 420, 101, 16))
        self.L_profile_2.setObjectName("L_profile_2")
        self.stackedWidget.addWidget(self.page_profile)
        self.page_edit_profile = QtWidgets.QWidget()
        self.page_edit_profile.setObjectName("page_edit_profile")
        self.L_edit_profile_const_1 = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_const_1.setGeometry(QtCore.QRect(250, 120, 500, 380))
        self.L_edit_profile_const_1.setText("")
        self.L_edit_profile_const_1.setObjectName("L_edit_profile_const_1")
        self.L_edit_profile_const_2 = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_const_2.setGeometry(QtCore.QRect(250, 280, 500, 380))
        self.L_edit_profile_const_2.setText("")
        self.L_edit_profile_const_2.setObjectName("L_edit_profile_const_2")
        self.L_edit_profile_const_0 = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_const_0.setGeometry(QtCore.QRect(380, 150, 311, 100))
        self.L_edit_profile_const_0.setObjectName("L_edit_profile_const_0")
        self.LE_edit_profile_login = QtWidgets.QLineEdit(self.page_edit_profile)
        self.LE_edit_profile_login.setGeometry(QtCore.QRect(355, 340, 310, 50))
        self.LE_edit_profile_login.setObjectName("LE_edit_profile_login")
        self.LE_edit_profile_password = QtWidgets.QLineEdit(self.page_edit_profile)
        self.LE_edit_profile_password.setGeometry(QtCore.QRect(355, 430, 310, 50))
        self.LE_edit_profile_password.setObjectName("LE_edit_profile_password")
        self.L_edit_profile_1 = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_1.setGeometry(QtCore.QRect(360, 320, 101, 16))
        self.L_edit_profile_1.setObjectName("L_edit_profile_1")
        self.L_edit_profile_2 = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_2.setGeometry(QtCore.QRect(360, 410, 101, 16))
        self.L_edit_profile_2.setObjectName("L_edit_profile_2")
        self.B_edit_profile_save_login = QtWidgets.QPushButton(self.page_edit_profile)
        self.B_edit_profile_save_login.setGeometry(QtCore.QRect(300, 340, 50, 50))
        self.B_edit_profile_save_login.setText("")
        self.B_edit_profile_save_login.setObjectName("B_edit_profile_save_login")
        self.B_edit_profile_save_password = QtWidgets.QPushButton(self.page_edit_profile)
        self.B_edit_profile_save_password.setGeometry(QtCore.QRect(300, 430, 50, 50))
        self.B_edit_profile_save_password.setText("")
        self.B_edit_profile_save_password.setObjectName("B_edit_profile_save_password")
        self.B_edit_profile_warning_1 = QtWidgets.QPushButton(self.page_edit_profile)
        self.B_edit_profile_warning_1.setGeometry(QtCore.QRect(680, 340, 50, 50))
        self.B_edit_profile_warning_1.setText("")
        self.B_edit_profile_warning_1.setObjectName("B_edit_profile_warning_1")
        self.B_edit_profile_warning_2 = QtWidgets.QPushButton(self.page_edit_profile)
        self.B_edit_profile_warning_2.setGeometry(QtCore.QRect(680, 430, 50, 50))
        self.B_edit_profile_warning_2.setText("")
        self.B_edit_profile_warning_2.setObjectName("B_edit_profile_warning_2")
        self.L_edit_profile_close_profile = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_close_profile.setGeometry(QtCore.QRect(360, 610, 181, 31))
        self.L_edit_profile_close_profile.setObjectName("L_edit_profile_close_profile")
        self.L_edit_profile_warning = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_warning.setGeometry(QtCore.QRect(360, 290, 301, 20))
        self.L_edit_profile_warning.setText("")
        self.L_edit_profile_warning.setObjectName("L_edit_profile_warning")
        self.B_edit_profile_back = QtWidgets.QPushButton(self.page_edit_profile)
        self.B_edit_profile_back.setGeometry(QtCore.QRect(250, 120, 70, 70))
        self.B_edit_profile_back.setText("")
        self.B_edit_profile_back.setObjectName("B_edit_profile_back")
        self.L_edit_profile_const_3 = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_const_3.setGeometry(QtCore.QRect(250, 640, 500, 45))
        self.L_edit_profile_const_3.setText("")
        self.L_edit_profile_const_3.setObjectName("L_edit_profile_const_3")
        self.B_edit_profile_close_profile = QtWidgets.QPushButton(self.page_edit_profile)
        self.B_edit_profile_close_profile.setGeometry(QtCore.QRect(300, 600, 50, 50))
        self.B_edit_profile_close_profile.setText("")
        self.B_edit_profile_close_profile.setObjectName("B_edit_profile_close_profile")
        self.B_edit_profile_save_email = QtWidgets.QPushButton(self.page_edit_profile)
        self.B_edit_profile_save_email.setGeometry(QtCore.QRect(300, 520, 50, 50))
        self.B_edit_profile_save_email.setText("")
        self.B_edit_profile_save_email.setObjectName("B_edit_profile_save_email")
        self.LE_edit_profile_email = QtWidgets.QLineEdit(self.page_edit_profile)
        self.LE_edit_profile_email.setGeometry(QtCore.QRect(355, 520, 310, 50))
        self.LE_edit_profile_email.setObjectName("LE_edit_profile_email")
        self.B_edit_profile_warning_3 = QtWidgets.QPushButton(self.page_edit_profile)
        self.B_edit_profile_warning_3.setGeometry(QtCore.QRect(680, 520, 50, 50))
        self.B_edit_profile_warning_3.setText("")
        self.B_edit_profile_warning_3.setObjectName("B_edit_profile_warning_3")
        self.L_edit_profile_3 = QtWidgets.QLabel(self.page_edit_profile)
        self.L_edit_profile_3.setGeometry(QtCore.QRect(360, 500, 101, 16))
        self.L_edit_profile_3.setObjectName("L_edit_profile_3")
        self.stackedWidget.addWidget(self.page_edit_profile)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.B_new_user_reg.setText(_translate("MainWindow", "REGISTRATION"))
        self.B_new_user_log.setText(_translate("MainWindow", "LOGIN"))
        self.L_new_user_const_0.setText(_translate("MainWindow", "😊 Welcome 😊"))
        self.L_log_const_0.setText(_translate("MainWindow", "🠗 LOG IN 🠗"))
        self.B_log_save.setText(_translate("MainWindow", " ✰ GET IN ✰"))
        self.B_log_forgot_password.setText(_translate("MainWindow", "📪 forgot password 📪"))
        self.L_reg_const_0.setText(_translate("MainWindow", "🠗 REG IN 🠗"))
        self.B_reg_save.setText(_translate("MainWindow", "✰ CREATE ✰"))
        self.L_forgot_password_const_0.setText(_translate("MainWindow", "FORGOT PASSWORD"))
        self.B_forgot_password_save.setText(_translate("MainWindow", "✰ SEND ✰"))
        self.B_forgot_password_change.setText(_translate("MainWindow", "change login/email"))
        self.L_user_const_0.setText(_translate("MainWindow", "😀 U\'re logged in 😀"))
        self.L_profile_const_0.setText(_translate("MainWindow", "🠗 U\'r profile 🠗"))
        self.L_profile_1.setText(_translate("MainWindow", "Ваш логин:"))
        self.L_profile_3.setText(_translate("MainWindow", "Ваш пароль:"))
        self.L_profile_2.setText(_translate("MainWindow", "Ваша почта:"))
        self.L_edit_profile_const_0.setText(_translate("MainWindow", "🠗 EDIT PROFILE 🠗"))
        self.L_edit_profile_1.setText(_translate("MainWindow", "Новый логин:"))
        self.L_edit_profile_2.setText(_translate("MainWindow", "Новый пароль:"))
        self.L_edit_profile_close_profile.setText(_translate("MainWindow", "Темная тема"))
        self.L_edit_profile_3.setText(_translate("MainWindow", "Добавить почту:"))

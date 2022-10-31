import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, \
    QPushButton, QLabel, QLineEdit, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QRect, QPropertyAnimation
from PyQt5 import QtCore, QtGui

from urllib import request

from PyQt5 import QtCore, QtWidgets
from designer.yandex import Ui_MainWindow
from switch_animation import AnimatedToggle
from style import *

import threading


class MyWindow(QMainWindow, Ui_MainWindow):  # Главный класс

    def clear_field(self):  # Очистка всех полей

        # ======== PAGE_LOG ========

        self.LE_log_login.setText('')
        self.LE_log_password.setText('')
        self.B_log_warning_1.hide()
        self.B_log_warning_2.hide()
        self.L_log_warning.setText('')

        # ======== PAGE_LOG ========

        # ======== PAGE_RES ========

        self.LE_reg_login.setText('')
        self.LE_reg_password_1.setText('')
        self.LE_reg_password_2.setText('')
        self.B_reg_warning_1.hide()
        self.B_reg_warning_2.hide()
        self.B_reg_warning_3.hide()
        self.L_reg_warning_1.setText('')
        self.L_reg_warning_2.setText('')

        # ======== PAGE_RES ========

        # ======== PAGE_EDIT_PROFILE========
        self.LE_edit_profile_login.setText('')
        self.LE_edit_profile_password.setText('')
        self.B_edit_profile_warning_1.hide()
        self.B_edit_profile_warning_2.hide()
        self.L_edit_profile_warning.setText('')
        # ======== PAGE_EDIT_PROFILE========

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Вызываем ui файл
        self.style_new_user()  # Вызываем style_new_user
        self.stackedWidget.setCurrentWidget(
            self.page_new_user)  # Ставим страничку <page_new_user>,
        # то есть самую первую>

        # =================== BUTTON EVENT ===================

        # login:
        self.B_new_user_log.clicked.connect(
            self.log)  # Если нажата кнопка <Залогиниться>,
        # то вызываем функцию <log>

        # registration:
        self.B_new_user_reg.clicked.connect(
            self.reg)  # Если нажата кнопка <Залогиниться>,
        # то вызываем функцию <log>

        self.B_new_user_to_user.clicked.connect(self.user)

        # =================== BUTTON EVENT ===================

    def style_new_user(self):  # Стили new_user

        # ========= BACKGROUND =========

        # main name:
        self.L_new_user_name.setStyleSheet(
            "color:white; font-size: 60px; background-color:purple;")

        # purple:
        self.L_new_user_purple.setStyleSheet(
            'background-color: purple;border:1px; solid:white;')

        # white:
        self.L_new_user_white.setStyleSheet(
            'background-color: white;border:1px; solid:white;')

        # ========= BACKGROUND =========

        # ========= LOGIN =========

        # login icon:
        self.B_new_user_ic_log.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/login.png"))

        self.B_new_user_ic_log.setStyleSheet("border:0px;")

        # login:
        self.B_new_user_log.setStyleSheet(
            'color: black; font-size: 25px')

        # ========= LOGIN =========

        # ========= REGISTRATION =========

        # registration icon:
        self.B_new_user_ic_reg.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/password.png"))
        self.B_new_user_ic_reg.setStyleSheet("border:0px;")

        # registration:
        self.B_new_user_reg.setStyleSheet(
            'color: black; font-size: 25px')

        # ========= REGISTRATION =========

    # =========================== PAGE LOG ===========================

    def style_log(self):  # Стили log

        # ========= back =========
        self.B_log_back.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/main.png"))
        self.B_log_back.setStyleSheet(
            "border:0px; border-radius:35px; background-color: rgb(248, 206, 255);")
        # ========= back =========

        # ========= BACKGROUND =========

        # ========= GET IN =========
        self.B_log_save.setStyleSheet('border-radius:20px; font-size:25px;')
        # ========= GET IN =========

        # main name:
        self.L_log_name.setStyleSheet(
            "color:white; font-size: 60px; background-color:purple;")

        # purple:
        self.L_log_purple.setStyleSheet(
            'background-color: purple;border:1px; solid:white;')

        # white:
        self.L_log_white.setStyleSheet(
            'background-color: white;border:1px; solid:white;')

        # ========= BACKGROUND =========

        # ========= LOGIN =========

        # login icon:

        self.B_log_ic_log.setIcon(QIcon(
            "images/login.png"))

        self.B_log_ic_log.setStyleSheet("border:0px;")

        # login:
        self.LE_log_login.setPlaceholderText('Login')
        self.LE_log_login.setStyleSheet('font-size:25px;')

        # ========= LOGIN =========

        # ========= REGISTRATION =========

        # registration icon:
        self.B_log_ic_reg.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/password.png"))
        self.B_log_ic_reg.setStyleSheet("border:0px;")

        # registration:
        self.LE_log_password.setPlaceholderText('Password')
        self.LE_log_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_log_password.setStyleSheet('font-size:25px;')

        # ========= WARNING =========

        # L_log_warning:

        self.L_log_warning.setStyleSheet(
            'font-size:14px; background-color: white;')

        # warning_1:

        self.B_log_warning_1.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/warning.png"))
        self.B_log_warning_1.setStyleSheet(
            "border:0px; background-color: white;")
        self.B_log_warning_1.hide()

        # warning_2:

        self.B_log_warning_2.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/warning.png"))
        self.B_log_warning_2.setStyleSheet(
            "border:0px; background-color: white;")
        self.B_log_warning_2.hide()

        # ========= WARNING =========

        # ========= REGISTRATION =========

    def log(self):  # Страничка log

        self.style_log()  # стили log
        self.stackedWidget.setCurrentWidget(
            self.page_log)  # Переключаем страничку

        # =================== BUTTON EVENT ===================

        self.B_log_back.clicked.connect(
            self.log_back)  # Если нажать кнопку назад
        self.B_log_save.clicked.connect(
            self.log_save)  # Если нажать кнопку войти

        # =================== BUTTON EVENT ===================

    def log_back(self):  # Функция переключения назад

        # === CLEAR LE ===
        self.clear_field()
        # === CLEAR LE ===

        self.stackedWidget.setCurrentWidget(
            self.page_new_user)  # Переключаем страничку

    def log_save(self):  # Функция сохранения
        class Error(Exception):
            pass

        BD = []  # К примеру
        result = False
        self.login = self.LE_log_login.text()  # Вывод логина
        self.password = self.LE_log_password.text()  # Вывод пароля
        try:
            if self.login in BD and self.password in BD:
                result = True
            else:
                raise Error()
        except Error:
            self.L_log_warning.setText(
                '✖ В логине или пароле допущена ошибка ✖')
            self.B_log_warning_1.show()
            self.B_log_warning_2.show()
        if result:
            self.user()

    # =========================== PAGE LOG ===========================

    # =========================== PAGE REGISTRATION ===========================
    def style_reg(self):  # Стили reg

        # ========= ВЕРНУТЬСЯ НА ГЛАВНЫЙ ЭКРАН =========

        self.B_reg_back.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/main.png"))
        self.B_reg_back.setStyleSheet(
            "border:0px; border-radius:35px; background-color: rgb(248, 206, 255);")

        # ========= ВЕРНУТЬСЯ НА ГЛАВНЫЙ ЭКРАН =========

        # ========= CREATE =========

        self.B_reg_save.setStyleSheet('border-radius:20px; font-size:25px;')

        # ========= CREATE =========

        # ========= BACKGROUND =========

        # main name:
        self.L_reg_name.setStyleSheet(
            "color:white; font-size: 60px; background-color:purple;")

        # purple:
        self.L_reg_purple.setStyleSheet(
            'background-color: purple;border:1px; solid:white;')

        # white:
        self.L_reg_white.setStyleSheet(
            'background-color: white;border:1px; solid:white;')

        # ========= BACKGROUND =========
        # ====================================================================
        # ========= LOGIN =========

        # login icon:
        self.B_reg_ic_log.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/login.png"))

        self.B_reg_ic_log.setStyleSheet("border:0px;")

        # login:
        self.LE_reg_login.setPlaceholderText('Login')
        self.LE_reg_login.setStyleSheet('font-size:25px;')

        # ========= LOGIN =========
        # ====================================================================
        # ========= REGISTRATION =========

        # Поле 1:

        # registration icon:
        self.B_reg_ic_reg_1.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/password.png"))
        self.B_reg_ic_reg_1.setStyleSheet("border:0px;")

        # registration:
        self.LE_reg_password_1.setPlaceholderText('Password')
        self.LE_reg_password_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_reg_password_1.setStyleSheet('font-size:25px;')

        # Поле 2:

        # registration icon:
        self.B_reg_ic_reg_2.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/password.png"))
        self.B_reg_ic_reg_2.setStyleSheet("border:0px;")

        # registration:
        self.LE_reg_password_2.setPlaceholderText('Confirm Password')
        self.LE_reg_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_reg_password_2.setStyleSheet('font-size:25px;')

        # ========= REGISTRATION =========
        # ====================================================================
        # ========= WARNING =========

        # L_reg_warning:

        self.L_reg_warning_1.setStyleSheet(
            'font-size:14px; background-color: white;')
        self.L_reg_warning_2.setStyleSheet(
            'font-size:14px; background-color: white;')

        # warning_1:

        self.B_reg_warning_1.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/warning.png"))
        self.B_reg_warning_1.setStyleSheet(
            "border:0px; background-color: white;")
        self.B_reg_warning_1.hide()

        # warning_2:

        self.B_reg_warning_2.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/warning.png"))
        self.B_reg_warning_2.setStyleSheet(
            "border:0px; background-color: white;")
        self.B_reg_warning_2.hide()

        # warning_3:

        self.B_reg_warning_3.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/warning.png"))
        self.B_reg_warning_3.setStyleSheet(
            "border:0px; background-color: white;")
        self.B_reg_warning_3.hide()

        # ========= WARNING =========

    def reg(self):  # Страничка reg
        self.style_reg()
        self.stackedWidget.setCurrentWidget(
            self.page_reg)  # Переключаем страничку

        # self.password = PasswordEdit()
        # self.setCentralWidget(self.password)

        self.B_reg_back.clicked.connect(
            self.reg_back)  # Если нажать кнопку назад
        self.B_reg_save.clicked.connect(
            self.reg_save)  # Если нажать кнопку войти

    def reg_back(self):  # Функция переключения назад

        # === CLEAR LE ===
        self.clear_field()
        # === CLEAR LE ===

        self.stackedWidget.setCurrentWidget(
            self.page_new_user)  # Переключаем страничку

    def reg_save(self):  # Функция сохранения
        class PasswordLenghtError(Exception):  # Ошибка длины пароля
            pass

        class PasswordSymbolError(Exception):  # Ошибка символом
            pass

        class PasswordSimilarityError(Exception):  # Ошибка схожести
            pass

        class LoginSymbolError(Exception):  # Ошибка символом
            pass

        class LoginBusy(Exception):  # Ошибка индивидуальности логина
            pass

        BD = []  # База Данных логинов
        result_login, result_password = False, False  # Ресультат проверки
        self.login = self.LE_reg_login.text()  # Вывод логина
        self.password_1 = self.LE_reg_password_1.text()  # Вывод пароля
        self.password_2 = self.LE_reg_password_2.text()  # Вывод пароля
        try:
            if re.fullmatch(r'[a-zA-Z0-9]+', self.login):
                if self.login not in BD:
                    result_login = True
                else:
                    raise LoginBusy()
            else:
                raise LoginSymbolError()
        except LoginSymbolError:
            self.L_reg_warning_1.setText(
                '✖ В логине есть недопустимые символы! ✖')
            self.B_reg_warning_1.show()
        except LoginBusy:
            self.L_reg_warning_1.setText('       ✖ Такой логин уже занят! ✖')
            self.B_reg_warning_1.show()

        try:
            if self.password_1 == self.password_2:
                if re.fullmatch(r'[a-zA-Z0-9]+', self.password_1):
                    if len(self.password_1) >= 8:
                        result_password = True
                    else:
                        raise PasswordLenghtError()
                else:
                    raise PasswordSymbolError()
            else:
                raise PasswordSimilarityError()
        except PasswordSimilarityError:
            self.L_reg_warning_2.setText('           ✖ Пароли не совпадают ✖')
            self.B_reg_warning_2.show()
            self.B_reg_warning_3.show()
        except PasswordSymbolError:
            self.L_reg_warning_2.setText(
                '✖ В паролях есть недопустимые символы! ✖')
            self.B_reg_warning_2.show()
            self.B_reg_warning_3.show()
        except PasswordLenghtError:
            self.L_reg_warning_2.setText('      ✖ Пароль короче 8 символов ✖')
            self.B_reg_warning_2.show()
            self.B_reg_warning_3.show()
        if result_login and result_password:
            self.user()

    # =========================== PAGE REGISTRATION ===========================

    # =========================== PAGE USER ===========================
    def style_user(self):  # Стили user

        # ========= SETTING =========

        # setting_1:
        self.B_user_setting.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/setting.png"))
        self.B_user_setting.setStyleSheet(
            "border:0px; background-color: rgb(248, 206, 255);")
        # ========= SETTING =========

        # ==================== FRAME ====================

        # F_user_1
        self.F_user_1.setStyleSheet('background-color: rgb(247, 179, 255);')

        # F_user_2
        self.F_user_2.setStyleSheet('background-color: rgb(247, 179, 255);')

        # B_user_frame_1:
        self.B_user_frame_1.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/login.png"))
        self.B_user_frame_1.setStyleSheet(
            "border-radius: 30px; background-color: orange;")

        # B_user_frame_2:
        self.B_user_frame_2.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/redact.png"))
        self.B_user_frame_2.setStyleSheet(
            "border-radius: 30px; background-color: orange;")

        # B_user_frame_3:
        self.B_user_frame_3.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/door.png"))
        self.B_user_frame_3.setStyleSheet(
            "border-radius: 30px; background-color: orange;")

        # ==================== FRAME ====================
        # ========= BACKGROUND =========

        # main name:
        self.L_user_name.setStyleSheet(
            "color:white; font-size: 60px; background-color:purple;")

        # purple:
        self.L_user_purple.setStyleSheet(
            'background-color: purple;border:1px; solid:white;')

        # white:
        self.L_user_white.setStyleSheet(
            'background-color: white;border:1px; solid:white;')

        # ========= BACKGROUND =========

    def user(self):
        self.frame = False
        self.style_user()  # стили user
        self.stackedWidget.setCurrentWidget(
            self.page_user)  # Переключаем страничку
        self.F_user_1.hide()
        self.F_user_2.hide()

        # =================== BUTTON EVENT ===================

        self.B_user_setting.clicked.connect(self.set)
        self.B_user_frame_1.clicked.connect(self.profile)
        self.B_user_frame_2.clicked.connect(self.edit_profile)
        self.B_user_frame_3.clicked.connect(self.user_back)

        # =================== BUTTON EVENT ===================

    def set(self):
        if not self.frame:
            self.open_settings()
        else:
            self.close_settings()
        self.frame = not self.frame


    def open_settings(self):
        self.F_user_1.show()
        self.F_user_2.show()

    def close_settings(self):
        self.F_user_1.hide()
        self.F_user_2.hide()

    def user_back(self):
        self.stackedWidget.setCurrentWidget(
            self.page_new_user)  # Переключаем страничку
        self.clear_field()

    # =========================== PAGE USER ===========================

    # =========================== PAGE PROFILE ===========================
    def style_profile(self):  # Стили profile

        # ========= back =========
        self.B_profile_back.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/main.png"))
        self.B_profile_back.setStyleSheet(
            "border:0px; border-radius:35px; background-color: rgb(248, 206, 255);")
        # ========= back =========

        # ========= LOGIN =========

        self.L_profile_1.setStyleSheet('background-color:white;')

        self.LE_profile_login.setEnabled(False)
        login = self.login
        self.LE_profile_login.setText(login)
        self.LE_profile_login.setStyleSheet('font-size:20px')
        # ========= LOGIN =========

        # ========= PASSWORD =========

        self.L_profile_2.setStyleSheet('background-color:white;')

        self.LE_profile_password.setEnabled(False)
        try:
            self.close_password = len(self.password) * '*'
        except Exception as e:
            print(e)
        self.LE_profile_password.setText(str(self.close_password))
        self.LE_profile_password.setStyleSheet('font-size:20px')

        self.B_profile_show_password.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/close_password.png"))
        self.B_profile_show_password.setStyleSheet(
            'border-radius:15px; background-color:white;')

        # ========= BACKGROUND =========

        # main name:
        self.L_profile_name.setStyleSheet(
            "color:white; font-size: 60px; background-color:purple;")

        # purple:
        self.L_profile_purple.setStyleSheet(
            'background-color: purple;border:1px; solid:white;')

        # white:
        self.L_profile_white.setStyleSheet(
            'background-color: white;border:1px; solid:white;')

        # ========= BACKGROUND =========

    def profile(self):
        print(self.frame)
        self.login = 'NaFo61'  # Пример
        self.password = 'Mirosha61'  # Пример
        self.see_password = False
        self.style_profile()  # стили user
        self.stackedWidget.setCurrentWidget(
            self.page_profile)  # Переключаем страничку

        # =================== BUTTON EVENT ===================
        self.B_profile_show_password.clicked.connect(self.check_password)
        self.B_profile_back.clicked.connect(self.profile_back)
        # =================== BUTTON EVENT ===================

    def profile_back(self):
        # === CLEAR LE ===
        self.clear_field()
        # === CLEAR LE ===

        self.stackedWidget.setCurrentWidget(
            self.page_user)  # Переключаем страничку

    def check_password(self):
        if not self.see_password:
            self.see_password = True
            self.o_password()
        else:
            self.see_password = False
            self.c_password()

    def o_password(self):
        self.LE_profile_password.setText(self.password)
        self.B_profile_show_password.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/open_password.png"))

    def c_password(self):
        self.LE_profile_password.setText(len(self.password) * '*')
        self.B_profile_show_password.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/close_password.png"))


    # =========================== PAGE PROFILE ===========================

    # =========================== PAGE EDIT PROFILE ===========================
    def style_edit_profile(self):  # Стили edit_profile

        # ========= back =========
        self.B_edit_profile_back.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/main.png"))
        self.B_edit_profile_back.setStyleSheet(
            "border:0px; border-radius:35px; background-color: rgb(248, 206, 255);")
        # ========= back =========

        # ========= LOGIN =========

        self.B_edit_profile_save_login.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/save.png"))

        self.L_edit_profile_1.setStyleSheet('background-color:white;')

        self.LE_edit_profile_login.setStyleSheet('font-size:20px')
        # ========= LOGIN =========

        # ========= PASSWORD =========

        self.B_edit_profile_save_password.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/save.png"))

        self.L_edit_profile_2.setStyleSheet('background-color:white;')

        self.LE_edit_profile_password.setStyleSheet('font-size:20px')

        # ================= WARNING ================

        # warning:

        self.L_edit_profile_warning.setStyleSheet(
            'background-color:white; font-size:14px;')

        # warning_1:

        self.B_edit_profile_warning_1.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/warning.png"))
        self.B_edit_profile_warning_1.setStyleSheet(
            "border:0px; background-color: white;")
        self.B_edit_profile_warning_1.hide()

        # warning_2:

        self.B_edit_profile_warning_2.setIcon(QIcon(
            "C:/Users/NAFO/PycharmProjects/pythonProject/Yandex/images/warning.png"))
        self.B_edit_profile_warning_2.setStyleSheet(
            "border:0px; background-color: white;")
        self.B_edit_profile_warning_2.hide()

        # ================= WARNING =================

        # ================ SETTING ================

        self.L_edit_profile_3.setStyleSheet(
            'background-color:white; font-size:14px;')

        # ================ SETTING ================

        # ========= BACKGROUND =========

        # main name:
        self.L_edit_profile_name.setStyleSheet(
            "color:white; font-size: 60px; background-color:purple;")

        # purple:
        self.L_edit_profile_purple.setStyleSheet(
            'background-color: purple;border:1px; solid:white;')

        # white:
        self.L_edit_profile_white.setStyleSheet(
            'background-color: white;border:1px; solid:white;')

        # ========= BACKGROUND =========

    def edit_profile(self):
        self.on_off_switch = False
        self.style_edit_profile()  # стили user
        self.stackedWidget.setCurrentWidget(
            self.page_edit_profile)  # Переключаем страничку

        self.mainToggle = AnimatedToggle()
        self.mainToggle.setFixedSize(self.mainToggle.sizeHint())

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.mainToggle)
        self.mainToggle.move(450, 530)

        # mainToggle.stateChanged.connect(secondaryToggle.setChecked)
        self.mainToggle.stateChanged.connect(self.switch)


        # =================== BUTTON EVENT ===================

        self.B_edit_profile_back.clicked.connect(self.edit_profile_back)
        self.B_edit_profile_save_login.clicked.connect(self.save_login)
        self.B_edit_profile_save_password.clicked.connect(self.save_password)

        # =================== BUTTON EVENT ===================
    def switch(self):
        result = self.mainToggle.isChecked()
        print(result)
        print('Переключил')

    def edit_profile_back(self):
        # === CLEAR LE ===
        self.clear_field()
        # === CLEAR LE ===
        self.mainToggle.hide()
        self.stackedWidget.setCurrentWidget(
            self.page_user)  # Переключаем страничку

    def save_login(self):
        class LoginSymbolError(Exception):  # Ошибка символом
            pass

        class LoginBusy(Exception):  # Ошибка индивидуальности логина
            pass

        login = self.LE_edit_profile_login.text()  # Вывод логина
        result = False  # Ресультат проверки
        BD = []  # База Данных логинов
        try:
            if re.fullmatch(r'[a-zA-Z0-9]+', login):
                if login not in BD:
                    result = True
                else:
                    raise LoginBusy()
            else:
                raise LoginSymbolError()
        except LoginSymbolError:
            self.L_edit_profile_warning.setText(
                '✖ В логине есть недопустимые символы! ✖')
            self.B_edit_profile_warning_1.show()
        except LoginBusy:
            self.L_edit_profile_warning.setText('       ✖ Такой логин уже занят! ✖')
            self.B_edit_profile_warning_1.show()
        if result:
            self.L_edit_profile_warning.setText('✔ Логин успешно изменен ✔')
            self.B_edit_profile_warning_1.hide()
            self.login = login

    def save_password(self):
        class PasswordLenghtError(Exception):  # Ошибка длины пароля
            pass

        class PasswordSymbolError(Exception):  # Ошибка символом
            pass

        password = self.LE_edit_profile_password.text()  # Вывод логина
        result = False  # Ресультат проверки
        try:
            if re.fullmatch(r'[a-zA-Z0-9]+', password):
                if len(password) >= 8:
                    result = True
                else:
                    raise PasswordLenghtError()
            else:
                raise PasswordSymbolError()
        except PasswordSymbolError:
            self.L_edit_profile_warning.setText('✖ В паролях есть недопустимые символы! ✖')
            self.B_edit_profile_warning_2.show()
        except PasswordLenghtError:
            self.L_edit_profile_warning.setText('      ✖ Пароль короче 8 символов ✖')
            self.B_edit_profile_warning_2.show()
        if result:
            self.L_edit_profile_warning.setText('✔ Пароль успешно изменен ✔')
            self.B_edit_profile_warning_2.hide()
            self.password = password
    # =========================== PAGE EDIT PROFILE ===========================

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.setStyleSheet('background-color: rgb(36,213,159)')
    mywindow.show()
    sys.exit(app.exec())

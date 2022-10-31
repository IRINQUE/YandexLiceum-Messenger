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


class MyWindow(QMainWindow, Ui_MainWindow):  # Главный класс

    def clear_field(self):  # Очистка всех полей

        # /======== PAGE_LOG ========\

        self.LE_log_login.setText('')
        self.LE_log_password.setText('')
        self.B_log_warning_1.hide()
        self.B_log_warning_2.hide()
        self.L_log_warning.setText('')

        # \======== PAGE_LOG ========/

        # /======== PAGE_RES ========\

        self.LE_reg_login.setText('')
        self.LE_reg_password_1.setText('')
        self.LE_reg_password_2.setText('')
        self.B_reg_warning_1.hide()
        self.B_reg_warning_2.hide()
        self.B_reg_warning_3.hide()
        self.L_reg_warning_1.setText('')
        self.L_reg_warning_2.setText('')

        # \======== PAGE_RES ========/

        # /======== PAGE_EDIT_PROFILE========\

        self.LE_edit_profile_login.setText('')
        self.LE_edit_profile_password.setText('')
        self.B_edit_profile_warning_1.hide()
        self.B_edit_profile_warning_2.hide()
        self.L_edit_profile_warning.setText('')

        # \======== PAGE_EDIT_PROFILE========/

    def __init__(self):
        super().__init__()
        self.result = True  # Взять значения из BD
        self.mainToggle = None
        self.see_password = None
        self.frame = None
        self.login = None
        self.password_1 = None
        self.password_2 = None
        self.password = None
        self.setupUi(self)  # Вызываем ui файл
        self.style_new_user()  # Вызываем style_new_user
        self.stackedWidget.setCurrentWidget(
            self.page_new_user)  # Ставим страничку <page_new_user>,
        # то есть самую первую>

        # /=================== BUTTON EVENT ===================\

        # login:
        self.B_new_user_log.clicked.connect(
            self.log)  # Если нажата кнопка <Залогиниться>,
        # то вызываем функцию <log>

        # registration:
        self.B_new_user_reg.clicked.connect(
            self.reg)  # Если нажата кнопка <Залогиниться>,
        # то вызываем функцию <log>

        self.skip.clicked.connect(self.user)

        # \=================== BUTTON EVENT ===================/

    def style_new_user(self):  # Стили new_user

        # /========= BACKGROUND =========\

        # const_0:
        self.L_new_user_const_0.setStyleSheet(const_0)

        # const_1
        self.L_new_user_const_1.setStyleSheet(const_1)

        # const_2:
        self.L_new_user_const_2.setStyleSheet(const_2)

        # const_3:
        self.L_new_user_const_3.setStyleSheet(const_3)

        # \========= BACKGROUND =========/

        # /========= LOGIN =========\

        # login icon:
        self.B_new_user_ic_log.setIcon(QIcon(img_log))
        self.B_new_user_ic_log.setStyleSheet(icon_log_pas)

        # login:
        self.B_new_user_log.setStyleSheet(B_login)

        # \========= LOGIN =========/

        # /========= REGISTRATION =========\

        # registration icon:
        self.B_new_user_ic_reg.setIcon(QIcon(img_pas))
        self.B_new_user_ic_reg.setStyleSheet(icon_log_pas)

        # registration:
        self.B_new_user_reg.setStyleSheet(B_password)

        # \========= REGISTRATION =========/

    # =========================== PAGE LOG ===========================

    def style_log(self):  # Стили log

        # /========= BACK =========\

        self.B_log_back.setIcon(QIcon(img_main))
        self.B_log_back.setStyleSheet(B_back)

        # \========= BACK =========/

        # /========= GET IN =========\

        self.B_log_save.setStyleSheet(B_save)

        # \========= GET IN =========/

        # /========= BACKGROUND =========\

        # const_0:
        self.L_log_const_0.setStyleSheet(const_0)

        # const_1
        self.L_log_const_1.setStyleSheet(const_1)

        # const_2:
        self.L_log_const_2.setStyleSheet(const_2)

        # const_3:
        self.L_log_const_3.setStyleSheet(const_3)

        # \========= BACKGROUND =========/

        # /========= LOGIN =========\

        # login icon:

        self.B_log_ic_log.setIcon(QIcon(img_log))
        self.B_log_ic_log.setStyleSheet(icon_log_pas)

        # login:
        self.LE_log_login.setPlaceholderText('Login')
        self.LE_log_login.setStyleSheet(LE_login_pas)

        # \========= LOGIN =========/

        # /========= REGISTRATION =========\

        # registration icon:
        self.B_log_ic_reg.setIcon(QIcon(img_pas))
        self.B_log_ic_reg.setStyleSheet(icon_log_pas)

        # registration:
        self.LE_log_password.setPlaceholderText('Password')
        self.LE_log_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_log_password.setStyleSheet(LE_login_pas)

        # L_log_warning:
        self.L_log_warning.setStyleSheet(L_warning)

        # warning_1:
        self.B_log_warning_1.setIcon(QIcon(img_war))
        self.B_log_warning_1.setStyleSheet(icon_warning)
        self.B_log_warning_1.hide()

        # warning_2:
        self.B_log_warning_2.setIcon(QIcon(img_war))
        self.B_log_warning_2.setStyleSheet(icon_warning)
        self.B_log_warning_2.hide()

        # \========= REGISTRATION =========/

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

        # /========= BACK =========\

        self.B_reg_back.setIcon(QIcon(img_main))
        self.B_reg_back.setStyleSheet(B_back)

        # \========= BACK =========/

        # /========= CREATE =========\

        self.B_reg_save.setStyleSheet(B_save)

        # \========= CREATE =========/

        # /========= BACKGROUND =========\

        # const_0:
        self.L_reg_const_0.setStyleSheet(const_0)

        # const_1
        self.L_reg_const_1.setStyleSheet(const_1)

        # const_2:
        self.L_reg_const_2.setStyleSheet(const_2)

        # const_3:
        self.L_reg_const_3.setStyleSheet(const_3)

        # \========= BACKGROUND =========/

        # /========= LOGIN =========\

        # login icon:
        self.B_reg_ic_log.setIcon(QIcon(img_log))
        self.B_reg_ic_log.setStyleSheet(icon_log_pas)

        # login:
        self.LE_reg_login.setPlaceholderText('Login')
        self.LE_reg_login.setStyleSheet(LE_login_pas)

        # \========= LOGIN =========/

        # /========= REGISTRATION =========\

        # Поле 1:

        # registration icon:
        self.B_reg_ic_reg_1.setIcon(QIcon(img_pas))
        self.B_reg_ic_reg_1.setStyleSheet(icon_log_pas)

        # registration:
        self.LE_reg_password_1.setPlaceholderText('Password')
        self.LE_reg_password_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_reg_password_1.setStyleSheet(LE_login_pas)

        # Поле 2:

        # registration icon:
        self.B_reg_ic_reg_2.setIcon(QIcon(img_pas))
        self.B_reg_ic_reg_2.setStyleSheet(icon_log_pas)

        # registration:
        self.LE_reg_password_2.setPlaceholderText('Confirm Password')
        self.LE_reg_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_reg_password_2.setStyleSheet(LE_login_pas)

        # \========= REGISTRATION =========/

        # /========= WARNING =========\

        # L_reg_warning:
        self.L_reg_warning_1.setStyleSheet(L_warning)
        self.L_reg_warning_2.setStyleSheet(L_warning)

        # warning_1:
        self.B_reg_warning_1.setIcon(QIcon(img_war))
        self.B_reg_warning_1.setStyleSheet(icon_warning)
        self.B_reg_warning_1.hide()

        # warning_2:
        self.B_reg_warning_2.setIcon(QIcon(img_war))
        self.B_reg_warning_2.setStyleSheet(icon_warning)
        self.B_reg_warning_2.hide()

        # warning_3:
        self.B_reg_warning_3.setIcon(QIcon(img_war))
        self.B_reg_warning_3.setStyleSheet(icon_warning)
        self.B_reg_warning_3.hide()

        # \========= WARNING =========/

    def reg(self):  # Страничка reg

        self.style_reg()
        self.stackedWidget.setCurrentWidget(
            self.page_reg)  # Переключаем страничку

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
            if re.fullmatch(r"[a-zA-Z0-9]+", self.login):
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

        # /========= SETTING =========\

        # setting_1:
        self.B_user_setting.setIcon(QIcon(img_set))
        self.B_user_setting.setStyleSheet(icon_setting)
        # \========= SETTING =========/

        # /==================== FRAME ====================\

        # F_user_1
        self.F_user_1.setStyleSheet(Frame)

        # F_user_2
        self.F_user_2.setStyleSheet(Frame)

        # B_user_frame_1:
        self.B_user_frame_1.setIcon(QIcon(img_log))
        self.B_user_frame_1.setStyleSheet(B_frame)

        # B_user_frame_2:
        self.B_user_frame_2.setIcon(QIcon(img_edit))
        self.B_user_frame_2.setStyleSheet(B_frame)

        # B_user_frame_3:
        self.B_user_frame_3.setIcon(QIcon(img_door))
        self.B_user_frame_3.setStyleSheet(B_frame)

        # \==================== FRAME ====================/

        # /========= BACKGROUND =========\

        # const_0:
        self.L_user_const_0.setStyleSheet(const_0)

        # const_1
        self.L_user_const_1.setStyleSheet(const_1)

        # const_2:
        self.L_user_const_2.setStyleSheet(const_2)

        # const_3:
        self.L_user_const_3.setStyleSheet(const_3)

        # \========= BACKGROUND =========/

    def user(self):
        self.frame = False
        self.style_user()  # стили user
        self.stackedWidget.setCurrentWidget(
            self.page_user)  # Переключаем страничку
        self.F_user_1.hide()
        self.F_user_2.hide()

        # /=================== BUTTON EVENT ===================\

        self.B_user_setting.clicked.connect(self.set)
        self.B_user_frame_1.clicked.connect(self.profile)
        self.B_user_frame_2.clicked.connect(self.edit_profile)
        self.B_user_frame_3.clicked.connect(self.user_back)

        # \=================== BUTTON EVENT ===================/

    def set(self):
        self.frame = not self.frame
        if not self.frame:
            self.open_settings()
        else:
            self.close_settings()

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

        # /========= BACK =========\
        self.B_profile_back.setIcon(QIcon(img_main))
        self.B_profile_back.setStyleSheet(B_back)
        # \========= BACK =========/

        # /========= LOGIN =========\

        self.L_profile_1.setStyleSheet(L_default)

        self.LE_profile_login.setEnabled(False)
        login = self.login
        self.LE_profile_login.setText(login)
        self.LE_profile_login.setStyleSheet(LE_login_pas)
        # \========= LOGIN =========/

        # /========= PASSWORD =========\

        self.L_profile_2.setStyleSheet(L_default)

        self.LE_profile_password.setEnabled(False)

        self.LE_profile_password.setText(str(len(self.password) * '*'))
        self.LE_profile_password.setStyleSheet(LE_login_pas)

        self.B_profile_show_password.setIcon(QIcon(img_close_pas))
        self.B_profile_show_password.setStyleSheet(icon_show_password)

        # \========= PASSWORD =========/

        # /========= BACKGROUND =========\

        # const_0:
        self.L_profile_const_0.setStyleSheet(const_0)

        # const_1
        self.L_profile_const_1.setStyleSheet(const_1)

        # const_2:
        self.L_profile_const_2.setStyleSheet(const_2)

        # const_3:
        self.L_profile_const_3.setStyleSheet(const_3)

        # \========= BACKGROUND =========/

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
        self.B_profile_show_password.setIcon(QIcon(img_open_pas))

    def c_password(self):
        self.LE_profile_password.setText(len(self.password) * '*')
        self.B_profile_show_password.setIcon(QIcon(img_close_pas))

    # =========================== PAGE PROFILE ===========================

    # =========================== PAGE EDIT PROFILE ===========================

    def style_edit_profile(self):  # Стили edit_profile
        try:

            # /========= BACK =========\

            self.B_edit_profile_back.setIcon(QIcon(img_main))
            self.B_edit_profile_back.setStyleSheet(B_back)

            # \========= BACK =========/

            # /========= LOGIN =========\

            self.B_edit_profile_save_login.setIcon(QIcon(img_save))
            self.B_edit_profile_save_login.setStyleSheet(icon_save)

            self.L_edit_profile_1.setStyleSheet(L_default)

            self.LE_edit_profile_login.setStyleSheet(LE_login_pas)
            # \========= LOGIN =========/

            # /========= PASSWORD =========\

            self.B_edit_profile_save_password.setIcon(QIcon(img_save))
            self.B_edit_profile_save_password.setStyleSheet(icon_save)

            self.L_edit_profile_2.setStyleSheet(L_default)

            self.LE_edit_profile_password.setStyleSheet(LE_login_pas)

            # \========= PASSWORD =========/

            # /================= WARNING ================\

            # warning:
            self.L_edit_profile_warning.setStyleSheet(L_warning)

            # warning_1:
            self.B_edit_profile_warning_1.setIcon(QIcon(img_war))
            self.B_edit_profile_warning_1.setStyleSheet(icon_warning)
            self.B_edit_profile_warning_1.hide()

            # warning_2:

            self.B_edit_profile_warning_2.setIcon(QIcon(img_war))
            self.B_edit_profile_warning_2.setStyleSheet(icon_warning)
            self.B_edit_profile_warning_2.hide()

            # \================= WARNING =================/

            # /================ SETTING ================\

            self.B_edit_profile_close_profile.setIcon(QIcon(img_close_profile))
            self.B_edit_profile_close_profile.setStyleSheet(icon_close_profile)
            self.L_edit_profile_close_profile.setStyleSheet(L_close_profile)

            # \================ SETTING ================/

            # /========= BACKGROUND =========\

            # const_0:
            self.L_edit_profile_const_0.setStyleSheet(const_0)

            # const_1
            self.L_edit_profile_const_1.setStyleSheet(const_1)

            # const_2:
            self.L_edit_profile_const_2.setStyleSheet(const_2)

            # const_3:
            self.L_edit_profile_const_3.setStyleSheet(const_3)

            # \========= BACKGROUND =========/
        except Exception as e:
            print(e)

    def edit_profile(self):
        self.style_edit_profile()  # стили user
        self.stackedWidget.setCurrentWidget(
            self.page_edit_profile)  # Переключаем страничку

        # /=========== Toggle ===========\
        if not self.mainToggle:
            self.mainToggle = AnimatedToggle()
            self.mainToggle.setFixedSize(self.mainToggle.sizeHint())

            self.setLayout(QVBoxLayout())
            self.layout().addWidget(self.mainToggle)
            self.mainToggle.move(555, 540)
        self.mainToggle.show()

        # mainToggle.stateChanged.connect(secondaryToggle.setChecked)
        self.mainToggle.stateChanged.connect(self.switch)

        # \=========== Toggle ===========/

        # /=================== BUTTON EVENT ===================\

        self.B_edit_profile_back.clicked.connect(self.edit_profile_back)
        self.B_edit_profile_save_login.clicked.connect(self.save_login)
        self.B_edit_profile_save_password.clicked.connect(self.save_password)

        # \=================== BUTTON EVENT ===================/

    def switch(self):
        self.result = self.mainToggle.isChecked()

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
            if re.fullmatch(r"[a-zA-Z0-9]+", login):
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
            self.L_edit_profile_warning.setText(
                '       ✖ Такой логин уже занят! ✖')
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
            self.L_edit_profile_warning.setText(
                '✖ В паролях есть недопустимые символы! ✖')
            self.B_edit_profile_warning_2.show()
        except PasswordLenghtError:
            self.L_edit_profile_warning.setText(
                '      ✖ Пароль короче 8 символов ✖')
            self.B_edit_profile_warning_2.show()
        if result:
            self.L_edit_profile_warning.setText('✔ Пароль успешно изменен ✔')
            self.B_edit_profile_warning_2.hide()
            self.password = password

    # =========================== PAGE EDIT PROFILE ===========================


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.setStyleSheet('background-color: rgb(51, 51, 51); border-radius: 10px')
    mywindow.show()
    sys.exit(app.exec())

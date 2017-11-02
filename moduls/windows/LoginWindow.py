#!/usr/bin/python3
#-*- coding: utf-8 -*-

from .MainWindow import MainWindow
from .GuestWindow import GuestWindow
from moduls.ErrorMessage import ErrorMessage

from PyQt4 import QtGui, QtCore, uic

# StudentData = StudentData()

    
class LoginWindow(QtGui.QDialog):
    """docstring for LoginWindow"""
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = uic.loadUi("ui\LoginWidget.ui", self)
        self.connect( self.LoginButton, QtCore.SIGNAL('clicked()'), self.login )
        self.connect( self.GuestButton, QtCore.SIGNAL('clicked()'), self.guest )

    def login( self ):
        if self.line1.text() == 'admin' and self.line2.text() == 'admin':
            self.MainWindow = MainWindow()
            self.MainWindow.show()
            self.close()
        else :
            ErrorMessage('Неверный логин\пароль').show()

    def guest( self ):
        self.GuestWindow = GuestWindow()
        self.GuestWindow.show()
        self.close()

#!/usr/bun/python3
#-*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore, uic

class ErrorMessage(QtGui.QDialog):
    """docstring for FacultyData"""
    def __init__(self, text):
        super(ErrorMessage, self).__init__()
        self.ui = uic.loadUi("ui\ErrorMessageDialog.ui", self) 
        self.label = QtGui.QLabel(text)
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.label)

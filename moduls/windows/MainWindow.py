#!/usr/bin/python3
#-*- coding: utf-8 -*-

from moduls.data import *

from PyQt4 import QtGui, QtCore, uic

# StudentData = StudentData()

    
class MainWindow(QtGui.QMainWindow):
    """docstring for MainWindow"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("ui\MainWindow.ui", self)

        self.FormData = FormData()
        self.FormLayout.addWidget( self.FormData )

        self.Faculty = FacultyData()
        self.FacLayout.addWidget( self.Faculty )
        
        self.Speciality = SpecialityData()
        self.SpecLayout.addWidget( self.Speciality)

        self.Students = StudentData( self.Faculty.data[0], self.Speciality.data[0], self.FormData.data[0] ) 
        self.StudLayout.addWidget( self.Students )

        self.Contract = ContractData( self.Students.data )
        self.ContrLayout.addWidget( self.Contract )

        self.connect( self.tabWidget, QtCore.SIGNAL('currentChanged(int)'), self.Contract.update )
        self.connect( self.tabWidget, QtCore.SIGNAL('currentChanged(int)'), self.Students.update )
      

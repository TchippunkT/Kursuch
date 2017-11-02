#!/usr/bun/python3
#-*- coding: utf-8 -*-

from .Data import Data
from PyQt4 import QtGui, QtCore, uic

class FacultyData(Data, QtGui.QWidget):
    """docstring for FacultyData"""
    def __init__(self):
        super(FacultyData, self).__init__()
        self.ui = uic.loadUi("ui\FacultyWidget.ui", self) 
        self.load()
        self.table = self.FacTable
        self.updateTable()
        self.connect( self.AppendFaculty, QtCore.SIGNAL('clicked()'), self.appFacInfo )
        self.connect( self.DeleteButton, QtCore.SIGNAL('clicked()'), self.deleteInfo )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.enableDelButton  )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.setText  )
        self.connect( self.Change, QtCore.SIGNAL('clicked()'), self.change )


    def change( self ):
        self.deleteInfo()
        self.appFacInfo()

    def setText(self):
        row = self.table.currentRow()
        self.line.setText( str(self.data[0][row]) )
        self.line2.setText( self.data[1][row] )
        self.line3.setText( self.data[2][row] )
        

    def appFacInfo( self ):
        # if int( self.line.text() ) in self.data[0]:
        #     self.errorMessage('Факультет с таким кодом уже был добавлен!')
        #     raise ValueError
        self.appendInfo( int(self.line.text()),
                            self.line2.text(),
                            self.line3.text() )
        self.updateTable()
        self.save()
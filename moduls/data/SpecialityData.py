#!/usr/bun/python3
#-*- coding: utf-8 -*-

from .Data import Data
from PyQt4 import QtGui, QtCore, uic

class SpecialityData(Data, QtGui.QWidget):
    """docstring for SpecialityData"""
    def __init__(self):
        super(SpecialityData, self).__init__()
        self.ui = uic.loadUi("ui\SpecialityWidget.ui", self) 
        self.load()
        self.table = self.SpecTable
        self.updateTable()
        self.connect( self.AppendSpeciality, QtCore.SIGNAL('clicked()'), self.appSpecInfo )
        self.connect( self.DeleteButton, QtCore.SIGNAL('clicked()'), self.deleteInfo )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.enableDelButton  )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.setText  )
        self.connect( self.Change, QtCore.SIGNAL('clicked()'), self.change )


    def change( self ):
        self.deleteInfo()
        self.appSpecInfo()

    def setText(self):
        row = self.table.currentRow()
        self.line.setText( str(self.data[0][row]) )
        self.line2.setText( self.data[1][row] )
        self.line3.setText( self.data[2][row] )
        
    def appSpecInfo( self ):
        
        # if int( self.line.text() ) in self.data[0]:
        #     self.errorMessage('Специальность с таким кодом уже была добавлена!')
        #     raise ValueError
        print(int(self.line.text()),
                             self.line2.text(),
                             self.line3.text())
        self.appendInfo( int(self.line.text()),
                             self.line2.text(),
                             self.line3.text() )
        self.updateTable()
        self.save()
      
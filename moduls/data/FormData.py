#!/usr/bin/python3
#-*- coding: utf-8 -*-

from .Data import Data
from PyQt4 import QtGui, QtCore, uic

class FormData(Data, QtGui.QWidget):
    """docstring for FormData"""
    def __init__(self):
        super(FormData, self).__init__()
        self.ui = uic.loadUi("ui\FormWidget.ui", self) 
        self.load()
        self.table = self.FormTable
        self.updateTable()
        self.connect( self.Append, QtCore.SIGNAL('clicked()'), self.appFormInfo )
        self.connect( self.DeleteButton, QtCore.SIGNAL('clicked()'), self.deleteInfo )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.enableDelButton  )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.setText  )
        self.connect( self.Change, QtCore.SIGNAL('clicked()'), self.change )
    


    def change( self ):
        self.deleteInfo()
        self.appFormInfo()

    def setText(self):
        row = self.table.currentRow()
        self.line.setText( str(self.data[0][row]) )
        self.line2.setText( self.data[1][row] )
        
       

    def appFormInfo( self ):
        # if not int( self.GroupNumber.currentText() ) in self.groupId:
        #     self.errorMessage('Группы с таким кодом не существует')
        #     raise ValueError
        # if int( self.line.text() ) in self.data[0]:
        #     self.errorMessage('Студент с таким кодом уже был добавлен')
        #     raise ValueError

        self.appendInfo(int( self.line.text() ),
                      self.line2.text() )
        self.updateTable()
        self.save()

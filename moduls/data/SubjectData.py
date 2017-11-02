#!/usr/bun/python3
#-*- coding: utf-8 -*-

from .Data import Data
from PyQt4 import QtGui, QtCore, uic

class SubjectData(Data, QtGui.QWidget):
    """docstring for SubjectData"""
    def __init__(self):
        super(SubjectData, self).__init__()
        self.ui = uic.loadUi("ui\SubjectWidget.ui", self) 
        self.load()
        self.table = self.SubjTable
        self.updateTable()
        self.connect( self.AppendSubject, QtCore.SIGNAL('clicked()'), self.appSubjInfo )
        self.connect( self.DeleteButton, QtCore.SIGNAL('clicked()'), self.deleteInfo )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.enableDelButton  )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.setText  )
        self.connect( self.Change, QtCore.SIGNAL('clicked()'), self.change )


    def change( self ):
        self.deleteInfo()
        self.appSubjInfo()

    def setText(self):
        row = self.table.currentRow()
        self.line.setText( str(self.data[0][row]) )
        self.line2.setText( self.data[1][row] )
        
       
    def appSubjInfo( self ):
        if int( self.line.text() ) in self.data[0]:
            self.errorMessage('Предмет с таким кодом уже был добавлен!')
            raise ValueError
        self.appendInfo( int(self.line.text()),
                            self.line2.text() )
        self.updateTable()
        self.save()
       
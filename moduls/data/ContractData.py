#!/usr/bin/python3
#-*- coding: utf-8 -*-

from .Data import Data
from PyQt4 import QtGui, QtCore, uic

class ContractData(Data, QtGui.QWidget):
    """docstring for StudentData"""
    def __init__(self, abData):
        super(ContractData, self).__init__()
        self.ui = uic.loadUi("ui\ContractWidget.ui", self) 
        self.abData = abData
        self.abId = abData[0] 
        
        self.load()
        self.addItems( self.combo1, self.abId )
        self.updateTable()
        self.connect( self.Append, QtCore.SIGNAL('clicked()'), self.appStudInfo )
        self.connect( self.DeleteButton, QtCore.SIGNAL('clicked()'), self.deleteInfo )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.enableDelButton  )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.setText  )
        self.connect( self.Change, QtCore.SIGNAL('clicked()'), self.change )
        # self.connect( self.combo1, QtCore.SIGNAL('highlighted(QString)'), self.update )
        self.connect( self.combo1, QtCore.SIGNAL('activated(int)'), self.fill )

    def fill( self ):
        
        text = int(self.combo1.currentText())
        index = self.abData[0].index(text)
        self.line2.setText( str(self.abData[4][index] ) )
        self.line3.setText( str(self.abData[5][index] ) )
        self.line4.setText( str(self.abData[6][index] ) )   

    def update(self):
        self.combo1.clear()
        self.addItems( self.combo1, self.abId )
        



    def change( self ):
        self.deleteInfo()
        self.appStudInfo()

    def setText(self):
        row = self.table.currentRow()
        self.line.setText( str(self.data[0][row]) )
        self.line2.setText( self.data[1][row] )
        self.line3.setText( self.data[2][row] )
        self.line4.setText( self.data[3][row] )
        self.combo1.setCurrentIndex( self.combo1.findText( str(self.data[4][row]) ) )
        self.combo2.setCurrentIndex( self.combo2.findText( str( self.data[5][row]) ) )
        self.combo3.setCurrentIndex( self.combo3.findText( str( self.data[6][row]) ) )
        self.line5.setText( self.data[7][row] )
       

    def appStudInfo( self ):
        # if not int( self.GroupNumber.currentText() ) in self.groupId:
        #     self.errorMessage('Группы с таким кодом не существует')
        #     raise ValueError
        # if int( self.line.text() ) in self.data[0]:
        #     self.errorMessage('Студент с таким кодом уже был добавлен')
        #     raise ValueError

        self.appendInfo(int( self.line.text() ),
                      int(self.combo1.currentText()),
                      self.line2.text(),
                      self.line3.text(),
                      self.line4.text(),
                      self.line5.text(),
                      self.line6.text(),
                      self.date.date().toString('dd.MM.yyyy')  )
        self.updateTable()
        self.save()

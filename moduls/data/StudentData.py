#!/usr/bin/python3
#-*- coding: utf-8 -*-

from .Data import Data
from PyQt4 import QtGui, QtCore, uic

class StudentData(Data, QtGui.QWidget):
    """docstring for StudentData"""
    def __init__(self, facId, specId, formId):
        super(StudentData, self).__init__()
        self.ui = uic.loadUi("ui\StudentWidget.ui", self) 
        self.facId = facId 
        self.SpecId = specId
        self.formId = formId
        self.load()
        self.table = self.StudTable
        self.updateTable()
        self.connect( self.StudAppend, QtCore.SIGNAL('clicked()'), self.appStudInfo )
        self.connect( self.DeleteButton, QtCore.SIGNAL('clicked()'), self.deleteInfo )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.enableDelButton  )
        self.connect( self.table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.setText  )
        self.connect( self.Change, QtCore.SIGNAL('clicked()'), self.change )
        # self.connect( self.combo1, QtCore.SIGNAL('highlighted(QString)'), self.update )
        # self.connect( self.combo2, QtCore.SIGNAL('highlighted(QString)'), self.update )
        # self.connect( self.combo3, QtCore.SIGNAL('highlighted(QString)'), self.update )

    def update(self):
        self.combo1.clear()
        self.combo2.clear()
        self.combo3.clear()
        self.addItems( self.combo1, self.facId )
        self.addItems( self.combo2, self.SpecId )
        self.addItems( self.combo3, self.formId )


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
                      self.line2.text(),
                      self.line3.text(),
                      self.line4.text(),
                      int(self.combo1.currentText()),
                      int(self.combo2.currentText()),
                      int(self.combo3.currentText()),
                      self.line5.text() )
        self.updateTable()
        self.save()

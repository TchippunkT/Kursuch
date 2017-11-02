#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore, uic
from moduls.data import *
from moduls.search import search


class GuestWindow(QtGui.QMainWindow):
    """docstring for GuestWindow"""
    def __init__(self):
        super(GuestWindow, self).__init__()
        self.ui = uic.loadUi("ui\GuestWindow.ui", self)
        
        self.connect( self.line1, QtCore.SIGNAL(' textChanged(QString)'), self.searchStudent )
        self.connect( self.line2, QtCore.SIGNAL(' textChanged(QString)'), self.searchStudent )
        self.connect( self.line3, QtCore.SIGNAL(' textChanged(QString)'), self.searchStudent )
        self.connect( self.SearchStudent, QtCore.SIGNAL(' clicked() '), self.searchStudent )

        self.connect( self.line5, QtCore.SIGNAL(' textChanged(QString)'), self.searchTeacher )        
        self.connect( self.line6, QtCore.SIGNAL(' textChanged(QString)'), self.searchTeacher )
        self.connect( self.SearchTeacher, QtCore.SIGNAL(' clicked() '), self.searchTeacher )


    def searchStudent( self ):
        self.data = StudentData(None,None,None)
        self.TableLayout.removeWidget(self.Table)
        try:
            line1 = int(self.line1.text() )
        except ValueError:
            line1 = ''

        fields = ( line1 ,
                    self.line2.text(),
                    self.line3.text())
        self.data.data = search( self.data.data, fields, (0,1,2) )
            
        self.data.updateTable()
        self.Table = self.data.table
        self.TableLayout.addWidget( self.Table )


    def searchTeacher( self ):
        self.data = ContractData( StudentData(None,None,None).data )
        self.TableLayout.removeWidget(self.Table)
        try:
            line5 = int(self.line5.text() )
        except ValueError:
            line5 = ''
        
        fields = ( line5 ,
                    self.line6.text() )
        print(fields)
        self.data.data = search( self.data.data, fields, (0,6) )
            
        self.data.updateTable()
        self.Table = self.data.table
        self.TableLayout.addWidget( self.Table )


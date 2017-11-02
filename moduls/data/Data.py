#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, pickle
from PyQt4 import QtGui
from moduls.sortArray import sortArray
from moduls.ErrorMessage import ErrorMessage

class Data(object):
    """docstring for Data"""
    def __init__( self ):
        super(Data, self).__init__()
        self.__Data = None



    def addItems(self, box, items):
        if items:
            for item in items:
                box.addItem( str(item) )

    def enableDelButton(self):
        self.DeleteButton.setEnabled(True)

    def updateTable( self ):
        if self.__Data :
            self.table.setRowCount( len(self.__Data[0]) )
            column = 0
            row = 0
            for array in self.__Data :
                row = 0
                for element in array :
                    self.table.setItem( row, column, QtGui.QTableWidgetItem( str(element) ) )
                    row += 1
                column += 1

    def appendInfo( self, *args ):
        array = self.__Data
        if not array:
            array = []
            for i in range( len(args) ):
                array.append([])
        try:
            if args[0] in self.__Data[0]:
                ErrorMessage('Запись с таким ключем уже была добавлена!').show()
                raise ValueError
        except  TypeError:
            pass       
        for i in range(len(array)):
            array[i].append(args[i])
        array = sortArray( array )
        self.__Data = array

    def errorMessage( self, text ):
        a = ErrorMessage( text )
        a.textError = text
        a.show()
    def deleteALL( self ):
        self.__Data = None
    def deleteInfo( self ):
        row = self.table.currentRow()

        key =  int(self.table.item(row,0).text()) 
        index = self.__Data[0].index( key )
        for i in range( len(self.__Data) ) :
            del self.__Data[i][index]
        self.updateTable()
        self.save()
    
    @property
    def data( self ):
        return self.__Data
    @data.setter
    def data( self, value ):
        self.__Data = value
    

    

    def save( self, fileName = None ):

        if fileName:
            fileName = os.path.abspath( 'data\\'+fileName )
        else:
            fileName = os.path.abspath( 'data\\'+self.__class__.__name__+'.db' )

        file = open(fileName+'1', 'wb')
        try:
            pickle.dump(self.data, file)
            print('save')
        finally:
            file.close()
            
        try:
            os.remove( fileName )
        except FileNotFoundError :
            pass
        os.rename(fileName+'1',  fileName )
        return self

    def load( self, fileName = None ):
        
        if fileName:
            fileName = os.path.abspath( 'data\\'+fileName )
        else:
            fileName = os.path.abspath( 'data\\'+self.__class__.__name__+'.db' )

        try:
            file = open(fileName, 'rb')
            self.data = pickle.load( file )
            print(self)
            print('load')
        except FileNotFoundError:
            print('FAIL!')
            pass
        except Exception as ex:
            file.close()
            raise ex

        return self





























        
        
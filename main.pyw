#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt4 import QtCore,QtGui
from moduls.windows.LoginWindow import LoginWindow

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    a = LoginWindow()
    a.show()
    sys.exit(app.exec_())

import sys
import serial   
from PyQt4 import QtCore, QtGui, uic

class StartQT4(QtGui.QMainWindow):
    
    def setSerial(self, s):
        self.serial = s;
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        FormClass = uic.loadUi('servoControl.ui', self)
        self.ui = FormClass
        
        '''Signal connections'''
        QtCore.QObject.connect(self.ui.verticalSlider, QtCore.SIGNAL("valueChanged(int)"), self.slider1)        
        QtCore.QObject.connect(self.ui.verticalSlider_2, QtCore.SIGNAL("valueChanged(int)"), self.slider2)
    
    def slider1(self, value):
        self.serial.write(chr(1))
        self.serial.write(chr(value))
        
    def slider2(self, value):
        self.serial.write(chr(2))
        self.serial.write(chr(value))
        

if __name__ == '__main__':
    
        s = serial.Serial('/dev/ttyACM1', 9600, timeout=1, stopbits=1)       
        
        #Working with user interface
        app = QtGui.QApplication(sys.argv)
        myapp = StartQT4()
        myapp.setSerial(s)
        myapp.show()
        s.close()
        sys.exit(app.exec_())
        
        
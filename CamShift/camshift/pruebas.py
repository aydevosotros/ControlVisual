'''
Created on 06/04/2012

@author: antonio
'''
import cv2.cv as cv

if __name__ == '__main__':
    capture = cv.CaptureFromCAM(0)
    cv.NamedWindow( "CamShiftDemo", 1 )
    
    while True:
        frame = cv.QueryFrame(capture)
        cv.ShowImage("CamShiftDemo", frame)
        
        c = cv.WaitKey(7) % 0x100
        if c == 27:
            break #Salimos con la tecla ESC
    
    cv.DestroyAllWindows()
    pass
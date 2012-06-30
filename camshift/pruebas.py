'''
Created on 06/04/2012

@author: antonio
'''
import cv2.cv as cv

if __name__ == '__main__':
    capture = cv.CaptureFromCAM(0)
    cv.NamedWindow( "CamShiftDemo", 1 )
    cv.NamedWindow("hsv", 1)
    
    while True:
        frame = cv.QueryFrame(capture)
        cv.ShowImage("CamShiftDemo", frame)
        
        hsv = cv.CreateImage(cv.GetSize(frame), 8, 3)
        cv.CvtColor(frame, hsv, cv.CV_BGR2HSV)
        
        hue = cv.CreateImage(cv.GetSize(frame), 8, 1)
        cv.Split(hsv, hue, None, None, None)
        
        hist = cv.CreateHist([180], cv.CV_HIST_ARRAY, [(0,255)], 1 )
        crit = ( cv.CV_TERMCRIT_EPS | cv.CV_TERMCRIT_ITER, 10, 1)
        
        backproject = cv.CreateImage(cv.GetSize(frame), 8, 1)
        cv.CalcArrBackProject( [hue], backproject, hist )
        
        track_window = (0, 0, cv.GetSize(frame)[0], cv.GetSize(frame)[1])
        print cv.GetSize(frame)[0], cv.GetSize(frame)[1]
        
        (iters, (area, value, rect), track_box) = cv.CamShift(backproject, track_window, crit)
        print track_box
#        cv.EllipseBox( frame, track_box, cv.CV_RGB(255,0,0), 3, cv.CV_AA, 0 )
        
        cv.ShowImage("hsv", backproject)
        
        
        c = cv.WaitKey(7) % 0x100
        if c == 27:
            break #Salimos con la tecla ESC
    
    cv.DestroyAllWindows()
    pass
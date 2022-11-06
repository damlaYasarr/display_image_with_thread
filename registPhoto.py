import cv2 as cv
import threading
def capture():
        
    cap=cv.VideoCapture(0)
    cap.set(3,640) #width=640
    cap.set(4,480) #height=480

    img_counter=0
    while True:
        img_counter=img_counter+1
        rest,frame=cap.read()
        cv.imshow('Video', frame)
        key=cv.waitKey(1)
        print(img_counter)
        cv.imwrite('/home/damlayasarr/threadExample/images/bisi.png',frame)
        if  key== ord('s'): 
            rest,frame=cap.read()
            cv.imshow("capturing", frame)
            print(f"foto thread ile kaydedildi {threading.get_native_id}")

            break
            
       
     
    cap.release()  
    cv.destroyAllWindows()

capture()
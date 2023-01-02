import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

while True:

    _,frame = cap.read()
  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5) 
    bodies = body_cascade.detectMultiScale(gray,1.1,5)


   

    #1.1 - 1.5 (niższy daje nam lepsza jakosc ale czas jest długi) 5-6 (trzeba sie pobawic)
  
    for (x,y,width,height) in faces:
        cv2.rectangle(frame,(x,y),(x+width,y+height),(255,0,0),3) # niebieski prostokąt 3 pixel szerokosc
    
    cv2.imshow("Camera",frame)
    


    if cv2.waitKey(1) == ord('q'): ### q jako quit
        break



### release wymagane bo inaczej żaden inny program nie może korzystać z naszego device

cap.release()
cv2.destroyAllWindows()


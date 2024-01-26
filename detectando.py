import cv2 

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

bottleClassif = cv2.CascadeClassifier('cascade.xml')#Se leera el modelo ya entrenado en un archivo xml

while True:
    
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    bot = bottleClassif.detectMultiScale(gray,scaleFactor = 5, minNeighbors = 91, minSize = (70,78)) #Todo lo que detecte se almacena en la variable "object" y se ha establecido un valor de  scaleFactor de 5, miniNeigbors 91, minSize de (70,78) para realizar pruebas
    
    for (x,y,w,h) in bot:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        cv2.putText(frame, 'Botella Buen Estado', (x,y-10), 2, 0.7, (0,255,0), 2, cv2.LINE_AA)#De la linea 14 a 16 se desempaqueta la informacion contenida en "object" por lo que cada deteccion tendremos las coordenadas, x, y, ancho y alto para dibujar un rectangulo
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()
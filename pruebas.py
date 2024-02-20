import pykinect
import cv2

# Inicializar Kinect
kinect = pykinect.Kinect()

# Abrir la camara RGB
kinect.start()
color_frame = kinect.get_color()

# Convertir la imagen a formato OpenCV
color_image = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)

# Mostrar la imagen
cv2.imshow('Camara Kinect', color_image)

# Cerrar la camara
kinect.stop()

# Esperar a que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()

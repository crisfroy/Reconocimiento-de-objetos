import cv2
from pykinect2 import PyKinectV2
import easygui

def initialize_kinect():
    kinect = PyKinectV2.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)
    return kinect

def capture_kinect_frame(kinect):
    if kinect.has_new_color_frame():
        frame = kinect.get_last_color_frame()
        frame = frame.reshape((1080, 1920, 4))
        frame = frame[:, :, :3]
        return frame
    return None

def show_message(frame, message):
    cv2.putText(frame, message, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Inicializar la cámara Kinect
kinect = initialize_kinect()

if kinect is None:
    easygui.msgbox("No se pudo detectar el Kinect. Asegúrate de que esté conectado y funcione correctamente.")
else:
    # Configurar la ventana de visualización
    cv2.namedWindow("Kinect Camera", cv2.WINDOW_NORMAL)

    while True:
        # Obtener el cuadro de color de la cámara Kinect
        frame = capture_kinect_frame(kinect)

        if frame is not None:
            # Mostrar la imagen en una ventana
            show_message(frame, 'Mensaje a mostrar')
            cv2.imshow("Kinect Camera", frame)

        # Salir del bucle si se presiona la tecla 'Esc'
        key = cv2.waitKey(1)
        if key == 27:
            break

    # Liberar la instancia de la cámara Kinect y cerrar la ventana
    kinect.close()
    cv2.destroyAllWindows()

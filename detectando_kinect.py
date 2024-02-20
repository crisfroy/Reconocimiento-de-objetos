import cv2
from pykinect import nui

def is_kinect_connected():
    try:
        kinect = nui.Runtime()
        return True
    except WindowsError as e:
        if "Failed to open Kinect sensor" in str(e):
            return False
        else:
            raise

# Verificar si el Kinect esta conectado
if is_kinect_connected():
    print("Kinect esta conectado.")
else:
    print("Kinect no esta conectado.")
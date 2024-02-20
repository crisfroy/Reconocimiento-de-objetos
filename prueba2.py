import cv2
from openni import Device, SensorType, ImageStream, DepthGenerator

def translate_coordinates(openni_point):
    opencv_point = depth.to_projective([openni_point])
    return (int(opencv_point[0][0]), int(opencv_point[0][1]))

def update_video_with(image):
    cv2.imshow('Video', image)
    cv2.imshow('Depth', depth.to_image_map())

########################### MAIN ##################################

cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.moveWindow('Video', 0, 0)
cv2.namedWindow('Depth', cv2.WINDOW_NORMAL)
cv2.moveWindow('Depth', 720, 0)

ni = Device()
ni.initialize()
ni.run_xml_script("OpenniConfig.xml")

depth_stream = ni.create_depth_stream()
image_stream = ImageStream(ni, SensorType.COLOR)
depth_stream.start()
image_stream.start()

key = -1
while key < 0:
    depth_frame = depth_stream.read_frame()
    image_frame = image_stream.read_frame()

    depth_data = depth_frame.get_buffer_as_uint16()
    depth_array = depth_data.reshape((1, depth_frame.height, depth_frame.width))

    depth = DepthGenerator()
    depth.create_map(SensorType.DEPTH, depth_array)

    image = image_frame.get_buffer_as_uint8()
    image_array = image.reshape((image_frame.height, image_frame.width, 3))

    update_video_with(image_array)

    key = cv2.waitKey(1)

cv2.destroyAllWindows()

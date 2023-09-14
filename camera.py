# Python program to capture a single image
# using pygame library

# importing the pygame library
import pygame
import pygame.camera
from time import sleep

# initializing the camera
pygame.camera.init()

# make the list of all available cameras
camlist = pygame.camera.list_cameras()
path = "C:/RIKI/images/"

# if camera is detected or not
if camlist:
	# initializing the cam variable with default camera
	cam = pygame.camera.Camera(camlist[0], (640, 480))
    # sleep(3) 
	# opening the camera
	cam.start()  

	# capturing the single image
	image = cam.get_image()

	# saving the image
	pygame.image.save(image, f"{path}filename.jpg")

# if camera is not detected the moving to else part
else:
	print("No camera on current device")

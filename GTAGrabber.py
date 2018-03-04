##
# GTAGrabber.py
#
# This file contains useful functions to work with GTA V

# Some useful imports
import numpy as np
from PIL import ImageGrab
import cv2

class GTAGrabber:

    # Class constructor
    def __init__(self):
        None

    # Grab an image
    def grab_game_image(self):
        return np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))

    # Set high beams
    def high_beams_on(self):
        None

    # Remove high beams
    def high_beams_off(self):
        None

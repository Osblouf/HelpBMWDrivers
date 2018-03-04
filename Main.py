##
# Main.py
#
# As this original name states, this is the main file for this project.

# Some useful imports
from GTAGrabber import *
from NightDetector import *
from VehicleDetector import *

# Load the models
is_vehicle_in_line_model = IsVehicleInLine()
is_vehicle_in_line_model.load_trained_model("is_vehicle_in_line_trained_model")
is_at_night_model = IsNightModel()
is_at_night_model.load_trained_model("is_at_night_trained_model")
game_grabber = GTAGrabber()

# Loop
while 1:

    # Grab image from GTA V
    image_to_use = game_grabber.grab_game_image()

    # Make night prediction on grabbed image
    is_at_night = is_at_night_model.make_prediction(image_to_use)

    if is_at_night:

        # Make prediction on grabbed image
        is_vehicle_in_line_of_sight = is_at_night_model.make_prediction(image_to_use)

        if is_vehicle_in_line_of_sight:
            # Set in normal beam mode
            game_grabber.high_beams_off()

        else:
            # Set in high beam mode
            game_grabber.high_beams_on()

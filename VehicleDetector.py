##
# VehicleDetector.py
#
# This file contains the model used to detect if a vehicle is in the line of sight


class IsVehicleInLine:

    # Class constructor
    def __init__(self):
        None

    # Method used to train the model
    def train_model(self):
        None

    # Method used to save the current model
    def save_model(self):
        None

    # Method used to load a trained model
    def load_trained_model(self, model_file_name):
        None

    # Method used to make a prediction
    def make_prediction(self, X):
        None


if __name__ == "__main__":
    print('This will train the model IsVehicleInLine.')
    model = IsVehicleInLine()
    model.train_model()
    model.save_model()

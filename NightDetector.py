##
# NightDetector.py
#
# This file contains the model used to detect if the car is in a night environment or not


class IsNightModel:

    # The model constructor
    def __init__(self):
        None

    # Train the model
    def train_model(self):
        None

    # Load a trained model
    #
    # model_file is the file name string from which the model has to be loaded
    def load_trained_model(self, model_file):
        None

    # Make a prediction
    #
    # X is the input image used to make the prediction
    # Outputs a boolean true if night is detected false otherwise
    def make_prediction(self, X):
        None


if __name__ == "__main__":
    print('This will train the model IsVehicleInLine.')
    model = IsNightModel()
    model.train_model()
    model.save_model()

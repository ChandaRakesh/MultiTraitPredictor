import pickle
import numpy as np
from seqToNum import convert_to_npArray
import tensorflow as tf
# Load the random forest model from the pickle file
# with open('FFNN.pkl', 'rb') as file:
#     ffnn= pickle.load(file)

ffnn = tf.keras.models.load_model("FFNN.h5")
with open('scaler_y.pkl', 'rb') as file:
    scaler_y= pickle.load(file)
with open('scaler_x.pkl', 'rb') as file:
    scaler_x= pickle.load(file)

# Example usage
def predictFNN(sequence):
    seqarr= convert_to_npArray(sequence)
    scaled_new_sequence = scaler_x.transform(seqarr)
    predictions_scaler= ffnn.predict(scaled_new_sequence)
    predictions = scaler_y.inverse_transform(predictions_scaler)
    predictions=predictions.tolist()
    predictions=predictions[0]
    return predictions
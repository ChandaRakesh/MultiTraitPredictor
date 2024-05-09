import pickle
import numpy as np
from seqToNum import map_sequence_to_numbers
# Load the random forest model from the pickle file
with open('random_forest_model2.pkl', 'rb') as file:
    random_forest_model2 = pickle.load(file)
# Example usage
def predict(sequence):
    mapped_numbers = map_sequence_to_numbers(sequence)
    # print(mapped_numbers)
    new_sequence_1 = np.array(mapped_numbers).reshape(1, -1)  # Reshape to match input shape
    # print(new_sequence_1)
    predictions = random_forest_model2.predict(new_sequence_1)
    predictions=predictions.tolist()
    predictions=predictions[0]
    return predictions
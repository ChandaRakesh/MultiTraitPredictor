import streamlit as st
from streamlit_lottie import st_lottie
import json
from rf import predict
from ann import predictFNN
# Set page configuration
st.set_page_config(page_title="Multi Trait Predictor", page_icon="🌾", layout="wide", initial_sidebar_state="expanded")

def load_lottieurl(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load assets
lottie_dna = load_lottieurl("image/mdna.json")
predictions=[]
predictionsFnn=[]
#to check whether dna has 24 pairs of genomic data

def analyze_dna_sequence(dna_sequence):
    # dna_sequence=dna_sequence.strip()
    if len(dna_sequence)==48:
        return True
    return False

# Header title
st.title("MULTI TRAIT PREDICTOR FOR WHEAT")

# DNA sequence input and analysis section
with st.container():
    st.write("---")
    left_column, right_column = st.columns([3,2]) 

    # Left column for DNA sequence input and prediction values table
    with left_column:
        dna_sequence = st.text_area("Enter DNA Sequence","     ")
        dna_sequence=dna_sequence.strip()
        print(len(dna_sequence))
        print(dna_sequence)
        if st.button("Predict"):
            if not dna_sequence:
                st.warning("Please enter a DNA sequence.")
            if analyze_dna_sequence(dna_sequence)==False:
                st.warning("Please enter a dna sequence with 24 pairs")
            else:
                # Display the results
                st.success(f"DNA Sequence Length: 24 base pairs")
                x=predict(dna_sequence)
                xfnn=predictFNN(dna_sequence)
                predictions=x
                predictionsFnn=xfnn
                # print(predictions)

        # Subheader for prediction values
        st.subheader("Random Forest Predictions")

        # Table data
        table_data = {
            'DH_Pooled': [predictions[0]if predictions else ''],
            'GFD_Pooled': [predictions[1]if predictions else ''],
            'GNPS_Pooled': [predictions[2]if predictions else ''],
            'GWPS_Pooled': [predictions[3]if predictions else ''],
            'PH_Pooled': [predictions[4]if predictions else ''],
            'GY_Pooled': [predictions[5]if predictions else '']
        }

        # Display the table
        st.table(table_data)
        # Subheader for prediction values
        st.subheader("Feed Forward Neural Network Predctions")

        # Table data
        table_data2 = {
            'DH_Pooled': [predictionsFnn[0]if predictions else ''],
            'GFD_Pooled': [predictionsFnn[1]if predictions else ''],
            'GNPS_Pooled': [predictionsFnn[2]if predictions else ''],
            'GWPS_Pooled': [predictionsFnn[3]if predictions else ''],
            'PH_Pooled': [predictionsFnn[4]if predictions else ''],
            'GY_Pooled': [predictionsFnn[5]if predictions else '']
        }

        # Display the table
        st.table(table_data2)

    # Right column for animation
    with right_column:
        st_lottie(lottie_dna, speed=2)

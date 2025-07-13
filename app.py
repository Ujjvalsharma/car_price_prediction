import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('car_price_model.pkl')

# App title
st.title("🚗 Car Price Prediction App")

st.write("Fill the car specifications below and click **Predict** to estimate the price.")

# User inputs
symboling = st.slider("Symboling", -2, 3, 0)
wheelbase = st.number_input("Wheelbase", step=0.1)
carlength = st.number_input("Car Length", step=0.1)
carwidth = st.number_input("Car Width", step=0.1)
carheight = st.number_input("Car Height", step=0.1)
curbweight = st.number_input("Curb Weight")
enginesize = st.number_input("Engine Size")
boreratio = st.number_input("Bore Ratio", step=0.01)
stroke = st.number_input("Stroke", step=0.01)
compressionratio = st.number_input("Compression Ratio", step=0.1)
horsepower = st.number_input("Horsepower")
peakrpm = st.number_input("Peak RPM")
citympg = st.number_input("City MPG")
highwaympg = st.number_input("Highway MPG")

# Categorical features (convert to dummy manually)
fueltype = st.selectbox("Fuel Type", ['gas', 'diesel'])
aspiration = st.selectbox("Aspiration", ['std', 'turbo'])
doornumber = st.selectbox("Door Number", ['two', 'four'])
carbody = st.selectbox("Car Body", ['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'])
drivewheel = st.selectbox("Drive Wheel", ['fwd', 'rwd', '4wd'])
enginelocation = st.selectbox("Engine Location", ['front', 'rear'])
fuelsystem = st.selectbox("Fuel System", ['mpfi', '2bbl', 'idi', '1bbl', 'spdi', '4bbl', 'mfi', 'spfi'])

# Create a dictionary of inputs
input_dict = {
    'symboling': symboling,
    'wheelbase': wheelbase,
    'carlength': carlength,
    'carwidth': carwidth,
    'carheight': carheight,
    'curbweight': curbweight,
    'enginesize': enginesize,
    'boreratio': boreratio,
    'stroke': stroke,
    'compressionratio': compressionratio,
    'horsepower': horsepower,
    'peakrpm': peakrpm,
    'citympg': citympg,
    'highwaympg': highwaympg,
    # Manually encoded dummy variables
    'fueltype_diesel': 1 if fueltype == 'diesel' else 0,
    'aspiration_turbo': 1 if aspiration == 'turbo' else 0,
    'doornumber_two': 1 if doornumber == 'two' else 0,
    'carbody_hardtop': 1 if carbody == 'hardtop' else 0,
    'carbody_hatchback': 1 if carbody == 'hatchback' else 0,
    'carbody_sedan': 1 if carbody == 'sedan' else 0,
    'carbody_wagon': 1 if carbody == 'wagon' else 0,
    'drivewheel_fwd': 1 if drivewheel == 'fwd' else 0,
    'drivewheel_rwd': 1 if drivewheel == 'rwd' else 0,
    'enginelocation_rear': 1 if enginelocation == 'rear' else 0,
    'fuelsystem_2bbl': 1 if fuelsystem == '2bbl' else 0,
    'fuelsystem_4bbl': 1 if fuelsystem == '4bbl' else 0,
    'fuelsystem_idi': 1 if fuelsystem == 'idi' else 0,
    'fuelsystem_mfi': 1 if fuelsystem == 'mfi' else 0,
    'fuelsystem_spdi': 1 if fuelsystem == 'spdi' else 0,
    'fuelsystem_spfi': 1 if fuelsystem == 'spfi' else 0
}

# Prepare the final input data as per model
model_columns = model.feature_names_in_  # sklearn >=1.0
input_data = [input_dict.get(col, 0) for col in model_columns]

# Predict button
if st.button("Predict Price"):
    predicted_price = model.predict([input_data])[0]
    st.success(f"Estimated Car Selling Price: ₹{int(predicted_price):,}")


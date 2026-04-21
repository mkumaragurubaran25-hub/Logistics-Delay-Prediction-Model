import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("logistics_model.pkl", "rb"))

st.title("🚚 Logistics Delay Prediction App")

# Inputs
distance = st.number_input("Distance (km)")
weight = st.number_input("Weight (kg)")
traffic = st.number_input("Traffic Volume")
hour = st.slider("Delivery Hour", 0, 23)
system_load = st.number_input("System Load")

vehicle = st.selectbox("Vehicle Type", ["Bike", "Truck", "Van"])

weather = st.selectbox("Weather", ["Clear", "Cloudy", "Rain", "Storm"])

# Convert inputs
weather_map = {"Clear":0,"Cloudy":1,"Rain":2,"Storm":3}
weather_score = weather_map[weather]

# Create input dataframe
input_data = pd.DataFrame({
    "distance_km":[distance],
    "weight_kg":[weight],
    "traffic_volume":[traffic],
    "delivery_hour":[hour],
    "system_load":[system_load],
    "weather_score":[weather_score],
    "vehicle_type_Truck":[1 if vehicle=="Truck" else 0],
    "vehicle_type_Van":[1 if vehicle=="Van" else 0]
})

# Prediction
if st.button("Predict Delay"):
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("⚠️ High Chance of Delay")
    else:
        st.success("✅ On-Time Delivery Expected")

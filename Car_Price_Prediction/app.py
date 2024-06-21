#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import pickle


# In[2]:


with open('desktop/Project/Car_Price_Prediction/car_price_prediction.pkl', 'rb')as file:
    model = pickle.load(file)


# In[3]:


st.title('Car Price Prediction App')
st.markdown(
    'Enter the fields below to get an estimate of the price of your car...')


# In[4]:

year_input = st.number_input('Year of purchase')

km_driven_input = st.number_input('The number of km driven')

fuel_options = ['Diesel', 'Petrol', 'CNG', 'LPG']
fuel_input = st.selectbox('Select the fuel type', fuel_options)

seller_type_options = ['Individual', 'Dealer', 'Trustmark Dealer']
seller_type_input = st.selectbox('Select the fuel type', seller_type_options)

transmission_options = ['Automatic', 'Manual']
transmission_input = st.selectbox(
    'Select the transmission type', transmission_options)

owner_options = ['First Owner', 'Second Owner',
                 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car']
owner_input = st.selectbox('Select the owner type', owner_options)

mileage_input = st.number_input('Mileage in kmpl', format='%2f')

engine_input = st.number_input('Engine in CC')

max_power_input = st.number_input('Max Power in bhp', format='%2f')

torque_rpm_input = st.number_input('Enter the torque rpm')

seat_input = st.number_input('Enter the number of seats in the car')

predict = st.button('Predict')


# In[5]:


if predict:
    if fuel_input == 'Petrol':
        fuel = 1
    elif fuel_input == 'Diesel':
        fuel = 0
    else:
        fuel = -1

    if seller_type_input == 'Individual':
        seller_type = 1
    elif seller_type_input == 'Dealer':
        seller_type = 0
    else:
        seller_type = -1

    if transmission_input == 'Manual':
        transmission = 1
    else:
        transmission = 0

    first_owner = 0
    second_owner = 0
    third_owner = 0
    fourth_and_above_owner = 0
    test_drive_car = 0

    if owner_input == 'First Owner':
        first_owner = 1
    elif owner_input == 'Second Owner':
        second_owner = 1
    elif owner_input == 'Third Owner':
        third_owner = 1
    elif owner_input == 'Fourth & Above Owner':
        fourth_and_above_owner = 1
    else:
        test_drive_car = 1

    columns = ['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'seats', 'torque_rpm', 'mil_kmpl', 'engine_cc',
               'max_power_bhp', 'First Owner', 'Fourth & Above Owner', 'Second Owner', 'Test Drive Car', 'Third Owner']
    data = [[year_input, km_driven_input, fuel, seller_type, transmission, seat_input, torque_rpm_input, mileage_input,
             engine_input, max_power_input, first_owner, fourth_and_above_owner, second_owner, test_drive_car, third_owner]]
    X = pd.DataFrame(data, columns)
    st.write('The Predicted Price of the car is:')
    st.write(model.predict(X)[0])


# In[ ]:

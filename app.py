import streamlit as st
import datetime
import requests

#Remember that there are several ways to output content into your web page...
#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
'''Taxi Fare Prediction'''
st.markdown('''Please enter the following parameters:
''')
#date and time
#today = datetime.date.today()
pickup_date = st.date_input(
    "Which day would you like to be picked up?")

#now = datetime.datetime.now()
pickup_time = st.time_input(
    "What time would you like to be picked up?")

pickup_datetime = str(pickup_date) + ' '+str(pickup_time) +' UTC'

#pickup and drop off on map

# @st.cache
# def get_map_data():
#     #print('get_map_data called')
#     return st.map(df)
pickup_latitude = st.text_input('Pickup Latitude',40.747)
pickup_longitude = st.text_input('Pickup Longiude',-73.989)
dropoff_latitude = st.text_input('Dropoff Latitude',40.802)
dropoff_longitude = st.text_input('Dropoff Longitude', -73.956)

# passenger count
passengers = st.slider('How many passengers?',1,8,2)

#API call using requests

url = 'http://taxifare.lewagon.ai/predict_fare/'

#Let's build a dictionary containing the parameters for our API...
params = {
    'key': '2012-10-06 12:10:20.0000001', 
    'pickup_latitude': float(pickup_latitude), 
    'pickup_longitude': float(pickup_longitude),
    'dropoff_latitude': float(dropoff_latitude),
    'dropoff_longitude': float(dropoff_longitude),
    'passenger_count': int(passengers),
    'pickup_datetime': pickup_datetime
    }

# Let's call our API using the `requests` package...
response = requests.get(url, params = params).json()

# # Let's retrieve the prediction from the **JSON** returned by the API...
pred = response['prediction']

# ## Finally, we can display the prediction to the user
pred
# #st.markdown(f"Your fare will cost around {pred}")

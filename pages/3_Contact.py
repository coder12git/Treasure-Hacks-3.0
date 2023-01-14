import streamlit as st
import pandas as pd

import requests

st.set_page_config(
    page_title="Alzheimer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Google Maps API key
api_key = st.secrets["YOUR_API_KEY"]

# Create a function to search for nearby doctors based on city name


def search_doctors(city, api_key):
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query=doctors+specializing+in+Alzheimer+in+{city}&key={api_key}'
    results = requests.get(url).json()
    return results['results']


# Input city name
city = st.text_input("Enter city name: ")

if city:
    # Search for nearby doctors
    doctors = search_doctors(city, api_key)

    # Display the results to the user
    st.write("Results for Alzheimer doctors in: ", city)
    lat_long = [(doc['geometry']['location']['lat'], doc['geometry']
                 ['location']['lng']) for doc in doctors]
    df = pd.DataFrame(lat_long, columns=["latitude", "longitude"])
    st.map(df)

    for i, doctor in enumerate(doctors):
        st.write(f"{i+1}. Name: ", doctor['name'])
        st.write("Address: ", doctor['formatted_address'])

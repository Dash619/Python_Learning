import streamlit as st
import requests
api_key = "FfN6C997vS3gXXPY6R1PwYrQoY6LZlD5M0YfeMQf"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
content = response.json()

st.title(content["title"])
st.image(content["hdurl"])
st.write(content["explanation"])


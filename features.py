from cgitb import reset
from distutils.command.install_egg_info import to_filename
import imp
from sqlite3 import Time
from time import sleep, time
from unittest import result
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt



# title/header/sub_header
st.title("Welcome to Streamlit :smile:")
st.header("This will be fun")

#text
st.text("Helo data science")


#info Colours and Errors
st.success("Great :thumbsup:")
st.info("Information")
st.warning(" Red Alert :warning:")
st.error("This is an error")


# image
from PIL import Image
img = Image.open("Logo.jpg")
st.image(img,width =250, caption="My Logo")

# checkbox
st.checkbox("I am Human")

# Radio
status = st.radio("What is your status",("Single","Married","Divorsed","Not Sure"))

# SelectBox
occupation = st.selectbox("Your Occupation",['Programmer','Data Scientist','Machine Learning Engineer'])
age =st.slider("What is your age",1,100)

# UserInput
name = st.text_input('Enter your name: ')
if st.button("Submit"):
    result = name.title()
    st.success(result)
    

#data Input
import datetime
today = st.date_input('Today is',datetime.datetime.now())


#camera_inpuut
camera_photo = st.camera_input("Take a photo")
progress_bar =st.progress(0)

for perc_completed in range (100):
    sleep(0.05)
    progress_bar.progress(perc_completed +1)
    
st.success("Photo uploaded successfully!")

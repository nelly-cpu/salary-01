import calendar
from datetime import datetime


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Title

st.set_page_config(page_title="NGZ Analytics", page_icon=":tada:", layout="wide")

# --- HEADER SECTION
with st.container():
    st.header("I am Nelson :wave:")
 # Subheader
    st.subheader("Data Analyst from SA")
# Text
    st.text("I am passionate about finding ways of using python and VBA to be more efficient and effective analyst")
    st.write("[learn more >](https://www.anodot.com/blog/top-10-analytics-websites/)")

# Markdown
st.markdown("### This is a markdown heading.")
# Displaying data

data = [1, 2, 3, 4, 5]

st.write("Data:", data)
# Dataframe

import pandas as pd

df = pd.DataFrame({"col1": [1.1, 2.2, 3.3], "col2": [4.4, 5.5, 6.6]})

st.write("DataFrame:", df)

# Plotting

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y,color='blue', linestyle='-', linewidth=2, marker='o', markersize=4)

st.pyplot(plt)
# Interactive widgets

name = st.text_input("Enter your name:")

st.write("Hello,", name)
age = st.slider("Select your age:", 0, 100, 25)

st.write("Age:", age)
color = st.selectbox("Select a color:", ["Red", "Green", "Blue"])

st.write("Color:", color)

# Button

if st.button("Click me"):

    st.write("Button clicked!")

# Checkbox

checkbox = st.checkbox("Check me")

if checkbox:

    st.write("Checkbox checked!")

    # Sidebar
st.sidebar.title("Sidebar")

st.sidebar.text("This is a sidebar.")
#Number Input

age = st.number_input("Enter your age:", min_value=0, max_value=100, value=25)

st.write("Age:", age)

#Slider

temperature = st.slider("Select temperature:", min_value=-10.0, max_value=40.0, value=20.0, step=0.1)

st.write("Temperature:", temperature)

#Checkbox

option = st.checkbox("Enable Feature")

if option:

    st.write("Feature is enabled!")

else:

    st.write("Feature is disabled!")

# Date Input

selected_date = st.date_input("Select a date:")
#years = [datetime.today().year, datetime.today().year + 1]
#months = list(calendar.month_name[1:])
st.write("Selected date:", selected_date)

#Time Input
selected_time = st.time_input("Select a time:")
st.write("Selected time:", selected_time)

#with st.form("entry_form", clear_on_submit=True):
    #col1, col2 = st.columns(2)
    #col1.selectbox("Select Month:", months,key="month")
    #col2.selectbox("Select Year:", years, key="year")

 #   "---"
    #with st.expander("")


#Colour

st.color_picker("choose your fav. color")

#File Upload

st.file_uploader('upload a file')
st.write("Hello")




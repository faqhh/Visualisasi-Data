

import streamlit as st

st.title('Creating a Button')

# Defining a Button
button = st.button('Click Here')

if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

import streamlit as st

st.title('Creating Radio Buttons')

# Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

import streamlit as st

st.title('Creating Checkboxes')
st.write('Select your Hobbies:')

# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

import streamlit as st

st.title('Creating Dropdown')

# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))


import streamlit as st

st.title('Multi-Select')

# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)


import streamlit as st

st.title("Download Button")

# Creating Download Button
down_btn = st.download_button(
    label="Download Image",
    data=open("images/image1.jpeg", "rb"),
    file_name="tiger.jpg",
    mime="image/jpg"
)
import streamlit as st
import time

st.title('Progress Bar')

# Defining Progress Bar
download = st.progress(0)

for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)

st.write('Download Complete')
import streamlit as st
import time

st.title('Spinner')

# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)

st.write('Hello Data Scientists')

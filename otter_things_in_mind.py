import streamlit as st
import pandas as  pd
import numpy as np

import os
import random



st.set_page_config(layout="wide")
st.title("I Had Otter Things In Mind...")


selector = st.sidebar.selectbox('Pick One!', ['Otter Pictures', 'Otter DNA', 'Phone a Friend'])


if selector == 'Otter Pictures':

    #pic_button = st.button('Press for Otters!')
    dir = '.\\otters'
    path = random.choice(os.listdir(".\\"))
    #path = "C:\\Users\\Matthew\\streamlit_apps\\otter_pics\\" + path
    path = path.strip()
    st.write(path)
    st.image(path, width=500, output_format='PNG')

elif selector == 'Otter DNA':
    st.header('A little piece of otter DNA!')

    st.subheader('Otter DNA art with Lissajous Curves')

    st.image(".\\lissajous_dna_plot.png")

elif selector == 'Phone a Friend':

    st.subheader("Call an *OTTER!*")
    audio_file = open('.\\Otter Whistle Short - QuickSounds.com.mp3', 'rb')
    audio_file = audio_file
    audio_bytes = audio_file.read()
    st.audio(audio_bytes,format='audio/ogg')

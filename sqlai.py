import openai

import numpy as np
import streamlit as st


# load api key from secrets file
openai.api_key = st.secrets['pass']

# config app
st.sidebar.header('Test Header')


# Integerate our code OpenAI API
import os
from constants import openai_key
from langchain_community.llms import OpenAI

# OpenAI Key initialisation
os.environ["OPENAI_API_KEY"]=openai_key

import streamlit as st

# Streamlit Framework
st.title("Langhcain Demo with OpenAI API")
input_text=st.text_input("Input the topic you want : ")

# OPENAI LLMS
llm=OpenAI(temperature=0.8)
# temperature suggest how much control the agent has while providing the result

if input_text:
    st.write(llm(input_text))
    
# Q&A Chatbot
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv() # take environment variables from .env

import streamlit as st

import os

## Function to load openai model and get response

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),temperature=0.5)
    response=llm(question)
    return response

#Load streamlit for creating  UI.

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

question = st.text_input("Please enter the input", key=input)
response = get_openai_response(question)

submit = st.button("Ask the question")
## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
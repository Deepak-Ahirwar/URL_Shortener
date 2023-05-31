import streamlit as st
import pyshorteners
import pyperclip

st.title("URL Shortner")

url = st.text_area("Enter the URL")

s = pyshorteners.Shortener()

if st.button('Convert'):

    st.header(s.tinyurl.short(url))

if st.button("Copy"):

    pyperclip.copy(s.tinyurl.short(url))





import streamlit as st
st.title("tumhara personal AI")

naam = st.text_input("naam likh")
if naam:
         st.write(f"hii {naam}! mai tumhara ai hu")

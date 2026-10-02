import streamlit as st
st.title("tumhara personal AI")

naam = st.text_input("naam likh")
if naam:
         st.write(f"hii {naam}! mai tumhara ai hu")
from openai import OpenAI 

st.divider()
st.write("mera chat wala dimaag hai")
client = OpenAI(
    base_ur1="https://api.groq.com/openai/v1",
     api_key=st.secrets["GROQ_API_KEY"]
)
sawal = st.text_input("mujhse kuch bhi pucho:")

if sawal:
          response = client.chat.completions.create(model="11ama-3.3-70b-versatile",messages=[{"role": "user", "content":sama1}])
          st.success(response.choices[0].message.content)
                   

import streamlit as st
import pandas as pd

st.write("Hello, Azaam Ahmed!")

st.header("Musical Event Registration Form")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
instrument = st.selectbox("Instrument", ["None", "Guitar", "Piano", "Violin", "Drums", "Vocals", "Other"])
experience = st.slider("Years of Experience", 0, 30, 0)
submit_button = st.button("Register")

if submit_button:
    if name and email and phone:
        st.success(f"Thank you for registering, {name}!")
        st.write("Registration Details:")
        st.write(f"- Email: {email}")
        st.write(f"- Phone: {phone}")
        st.write(f"- Instrument: {instrument}")
        st.write(f"- Experience: {experience} years")
    else:
        st.error("Please fill in all required fields.")

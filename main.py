import streamlit as st
import pandas as pd

st.write("Hello, Azaam Ahmed!")
# Create a simple DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
})

# Display the DataFrame in Streamlit
st.write("Sample DataFrame:")
st.dataframe(df)

# Create some data elements
number = 42
text = "Streamlit is awesome!"
st.write("Number:", number)
st.write("Text:", text)
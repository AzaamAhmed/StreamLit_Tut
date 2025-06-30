import pandas as pd

import streamlit as st

def get_clean_data():
    # Load your data
    data = pd.read_csv("data/data.csv")
    print(data.head())
    
    data = data.drop(['Unnamed: 32', 'id'], axis=1)

    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})



    return data




def main():
    data = get_clean_data()
    print(data.head())


if __name__ == "__main__":
    main()

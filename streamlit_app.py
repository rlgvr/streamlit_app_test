#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import time

# Function to perform some action based on the selected value
def perform_action(selected_value):
    # Replace this with your custom logic
    if selected_value < 50:
        return "Low Value"
    else:
        return "High Value"

def main():
    st.title("CSV Data Analyzer")

    # Upload a CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(data)

        st.subheader("Select a Row to Analyze")

        # Create a slider to select a row to display
        row_selector = st.slider("Row", 0, len(data) - 1, 0)

        # Display the selected row
        selected_row = data.iloc[row_selector]
        st.write("Selected Row:")
        st.write(selected_row)

        # Perform an action based on the selected value
        selected_value = selected_row['Value']  # Change 'Value' to the actual column name
        output = perform_action(selected_value)
        st.write("Output based on the selected value:")
        st.write(output)

    else:
        st.warning("Please upload a CSV file.")

if __name__ == '__main__':
    main()


# In[1]:


#pip install streamlit


import streamlit as st
import pandas as pd
import time
from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, JsCode

# Function to perform some action based on the selected values
def perform_action(selected_values):
    # Replace this with your custom logic
    if selected_values.mean() < 50:
        return "Low Values"
    else:
        return "High Values"

st.title("CSV Data Analyzer")

# Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(data)

    st.subheader("Select a Column to Analyze")

    # Create radio buttons to choose a column name
    column_selector = st.radio("Select Column", data.columns)

    if column_selector in data.columns:  # Check if the selected column exists
        # Display the selected column
        selected_column = data[column_selector]

        grid = AgGrid(
            selected_column,
            gridOptions=GridOptionsBuilder.from_dataframe(selected_column).build(),
            update_mode=DataReturnMode.NO_UPDATE,
            theme='streamlit'
        )

        if st.button("Start Viewing Rows"):
            for i in range(len(selected_column)):
                grid.update_table(selected_column.iloc[i:i+1])
                time.sleep(2)  # Sleep for 2 seconds between rows

            st.write("Viewing completed.")
    else:
        st.warning("Selected column does not exist in the DataFrame.")

else:
    st.warning("Please upload a CSV file.")

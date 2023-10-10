import streamlit as st
import pandas as pd
import time

st.title("CSV Data Analyzer")

# Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, index_col=0)

    st.subheader("Data Preview")
    st.write(data, index=False)

    st.subheader("Select a Column to Analyze")

    # Create radio buttons to choose a column name
    column_selector = st.radio("Select Column", data.columns)

    if column_selector in data.columns:  # Check if the selected column exists
        # Display the selected column
        selected_column = data[column_selector]

        max_value = None
        min_value = None
        max_min_table = st.empty()
        table_component = st.empty()
        output_table = st.empty()  # New table for additional information

        if st.button("Start Viewing Rows"):
            for i in range(len(selected_column)):
                table_component.table(selected_column.iloc[i:i+1])
                time.sleep(2)  # Sleep for 2 seconds between rows

                # Update max and min values
                current_value = selected_column.iloc[i]
                if max_value is None or current_value > max_value:
                    max_value = current_value
                if min_value is None or current_value < min_value:
                    min_value = current_value

                # Display the max and min values in a separate table
                max_min_table.table(pd.DataFrame({'Max Value': [max_value], 'Min Value': [min_value]}))

            st.write("Viewing completed.")

            # Additional information after viewing
            output_table.table(pd.DataFrame({'Max Value': [max_value], 'Min Value': [min_value]}))
    else:
        st.warning("Selected column does not exist in the DataFrame.")

else:
    st.warning("Please upload a CSV file.")

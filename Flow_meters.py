import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title('Upload a file and convert to DataFrame')

# File Uploader widget
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Check the file's extension and load into a DataFrame accordingly
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)

    # Apply your filters
    df_filtered = df[df['Name'].str.contains('FIT', case=True)]
    df_filtered = df_filtered[~df_filtered['Description'].str.contains('Forecast|Budget|Target|Adjusted|Uncertainty', case=True)]

    # Display the filtered DataFrame in the app
    st.write(df_filtered)

    # Convert DataFrame to CSV
    csv = df_filtered.to_csv(index=False).encode('utf-8')

    # Create a download button for the CSV file
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )
else:
    st.write("Please upload a file to display its contents here.")

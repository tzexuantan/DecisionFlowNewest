import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Distribution of Certificates in the Data File")

# Fixed file path
file_path = r"D:\SCHOOL\UNI\Year 1\Trimester 1\INF1102 - Programming Fundamentals\Project\Data sets\merged.csv"

# Check if the file exists
import os
if not os.path.isfile(file_path):
    st.error(f"File not found: {file_path}")
else:
    # Read the CSV file with the correct encoding
    df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip')

    # Check if 'certification_text' column exists
    if 'certification_text' in df.columns:
        # Count occurrences of each certificate
        certificate_counts = df['certification_text'].value_counts().sort_index()

        # Multi-select to filter certificates
        selected_certificates = st.multiselect(
            'Select certificates to visualize',
            options=certificate_counts.index.tolist(),  # Provide the list of options
            default=[]  # Default to show none
        )

        # Filter the data based on selected certificates
        filtered_counts = certificate_counts[selected_certificates]

        # Generate a plot for distribution
        plt.figure(figsize=(10, 5))
        plt.step(filtered_counts.index, filtered_counts.values, where='mid', color='b', linestyle='-', linewidth=2, marker='o')
        plt.title('Distribution of Certificates')
        plt.xlabel('Certificate')
        plt.ylabel('No. of people with the certificate')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.grid(True)

        # Adjust layout to ensure everything fits without overlap
        plt.tight_layout()

        # Display the step line chart
        st.pyplot(plt)

import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title of the app
st.title("Distribution of Certificates in Singapore")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the file path to Final.xlsx
file_path = os.path.join(current_dir, "../dataset/Certificate.xlsx")

# Read the excel file
df = pd.read_excel(file_path)

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
    if selected_certificates:
        filtered_counts6 = certificate_counts[selected_certificates]

        if st.button('Generate Line Chart'):
            plt.figure(figsize=(10, 5))
            plt.plot(filtered_counts6.index, filtered_counts6.values, marker='o', linestyle='-', color='b')
            plt.title('Distribution of Certificates in Singapore')
            plt.xlabel('Certificate')
            plt.ylabel('No. of people with the certificate')
            plt.xticks(rotation=90)
            plt.grid(True)
            st.pyplot(plt)

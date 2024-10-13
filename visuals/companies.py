import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title of the app
st.title("Companies that are hiring the IT roles")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the file path to Final.xlsx
file_path = os.path.join(current_dir, "../dataset/Final.xlsx")

# Read the excel file
df = pd.read_excel(file_path)

# Column to plot
column_to_plot3 = "Company/Candidate Name"

if df[column_to_plot3].dtype == 'object':
    # Count occurrences of each category
    category_counts3 = df[column_to_plot3].value_counts()

    # Check if category_counts is not empty
    if not category_counts3.empty:
        # Multi-select to choose specific data
        selected_companies = st.multiselect(
            label='Select companies to visualize',
            options=category_counts3.index.tolist(),  # Provide the list of options
            default=[]  # Default to show none
        )

        # Filter the data based on selected companies
        if selected_companies:
            filtered_data = df[df[column_to_plot3].isin(selected_companies)]
            filtered_counts = filtered_data[column_to_plot3].value_counts().reset_index()
            filtered_counts.columns = ['Company', 'No. of roles']  # Ensure the columns match correctly

            # Add a button to generate the chart
            if st.button('Generate Bar Chart'):
                # Create a Bar Chart
                plt.figure(figsize=(10, 6))
                plt.bar(filtered_counts['Company'], filtered_counts['No. of roles'], color='skyblue')
                plt.xlabel('Company')
                plt.ylabel('No. of roles')
                plt.title('Companies Hiring IT Roles')
                plt.xticks(rotation=90)
                plt.tight_layout()

                # Display the plot in Streamlit
                st.pyplot(plt)

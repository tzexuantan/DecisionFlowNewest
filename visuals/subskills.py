import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title of the app
st.title("IT Competencies in the Industry")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the file path to Final.xlsx
file_path = os.path.join(current_dir, "../dataset/Final.xlsx")

# Read the excel file
df = pd.read_excel(file_path)
column = 'Sub-skill'

# Handle missing values
df[column].fillna('Unknown', inplace=True)

# Initialize filtered_df5
filtered_df5 = df.copy()  # Start with a copy of the full dataset

# Get unique sub-skills for the multiselect box
sub_skills = df[column].unique()
selected_sub_skills = st.multiselect('Select Sub-skills', sub_skills, default=[])

# Filter the DataFrame based on selected sub-skills
if selected_sub_skills:  # Check if any sub-skills are selected
    filtered_df5 = filtered_df5[filtered_df5[column].isin(selected_sub_skills)]

# Add a button to generate the chart
if st.button('Generate Histogram'):
    if not filtered_df5.empty:
        # Count occurrences of each sub-skill
        sub_skill_counts = filtered_df5[column].value_counts()

        # Create a bar chart for the filtered sub-skills
        plt.figure(figsize=(10, 6))
        plt.bar(sub_skill_counts.index, sub_skill_counts.values, edgecolor='k', alpha=0.7)
        plt.xlabel('Sub-skill')
        plt.ylabel('No. of people')
        plt.title('IT Competencies in the Industry')
        plt.xticks(rotation=90)
        plt.tight_layout()

        # Display the plot in Streamlit
        st.pyplot(plt)
    else:
        st.warning("No data available for the selected sub-skills.")

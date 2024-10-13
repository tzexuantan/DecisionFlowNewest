import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title of the app
st.title("Salary ranges for IT jobs")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the file path to Final.xlsx
file_path = os.path.join(current_dir, "../dataset/Salary_Data_Based_country_and_race.xlsx")

# Read the excel file
df = pd.read_excel(file_path)

column1 = 'Job Title'
column2 = 'Salary'

df[column2] = pd.to_numeric(df[column2], errors='coerce')

# Handle missing values
df[column1] = df[column1].fillna('')
df[column2] = df[column2].fillna(0)

# Add number inputs for filtering salary range
min_salary = df[column2].min()
max_salary = df[column2].max()
min_value = st.number_input('Min Salary', min_value=min_salary, max_value=max_salary, value=min_salary)
max_value = st.number_input('Max Salary', min_value=min_salary, max_value=max_salary, value=max_salary)

# Filter the DataFrame based on the salary range
filtered_df4 = df[(df[column2] >= min_value) & (df[column2] <= max_value)]

# Update job titles based on the filtered DataFrame
job_titles = filtered_df4[column1].unique()

# Allow users to select job titles, defaulting to all options if none are selected
selected_job_titles = st.multiselect('Select Job Titles', job_titles, default=[])

# Display the filtered dataframe
if selected_job_titles:
    filtered_df4 = filtered_df4[filtered_df4[column1].isin(selected_job_titles)]

# Add a button to generate the chart
if st.button('Generate Horizontal Bar Chart'):
    # Create a horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(filtered_df4[column1], filtered_df4[column2], label=column2)
    # Add labels and title
    plt.xlabel('Salary')
    plt.ylabel('Job Title')
    plt.title('Salary ranges for IT jobs')
    plt.legend()
    # Display the plot in Streamlit
    st.pyplot(plt)
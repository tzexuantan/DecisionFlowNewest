# main.py
import streamlit as st
import pandas as pd
import os
import plotly.express as px
import matplotlib.pyplot as plt


def initialize_indeed_dataset():
    #Obtain current directory file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # File path to the dataset
    indeed_data_file_path = os.path.join(current_dir, "../dataset/Final.xlsx")
    indeed_df = pd.read_excel(indeed_data_file_path)
    return indeed_df

def initialize_ITJobs_dataset():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the file path to Final.xlsx
    file_path = os.path.join(current_dir, "../Pre-Processing/IT Jobs.xlsx")
    ITJobs_df = pd.read_excel(file_path)
    return ITJobs_df

def initialize_itjob_headerfinal_dataset(): 
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the file path to Final.xlsx
    file_path = os.path.join(current_dir, "../Pre-Processing/itjob_headerfinal.xlsx")
    itjob_headerfinal_df = pd.read_excel(file_path)
    return itjob_headerfinal_df

def plot_bar_graph(data, x_col, y_col, title):
    plt.figure(figsize=(10, 5))
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    
    data.plot(kind='bar', color='skyblue')

def plot_pie_chart(size, label, title):
    plt.figure(figsize=(8,8))
    plt.pie(values=size, names=label)
    plt.title(title)
    plt.axis('equal')
    plt.plot()

def visualizations():
    # Initialize dataset
    indeed_df = initialize_indeed_dataset()

    # Bar Graph
    st.title("Distributions of Skills and Job Titles")

    # Specify columns for skills and job titles
    skill_column = "Skill"  # Set this to the column name for skills in your Excel file
    job_title_column = "Job Title"  # Set this to the column name for job titles in your Excel file

    # Check if columns exist
    if skill_column not in indeed_df.columns:
        st.error(f"Column '{skill_column}' not found in the Excel file.")
        return

    if job_title_column not in indeed_df.columns:
        st.error(f"Column '{job_title_column}' not found in the Excel file.")
        return

    # Predefined keywords to filter job titles
    predefined_keywords = ["Scientist", "IT", "Analyst", "DevOps", "Developer", "Computer Science", "Technology"]

    # Multi-select for job title filtering
    selected_keywords = st.multiselect(
        'Select job title keywords to filter:',
        options=predefined_keywords,
        default=predefined_keywords  # Default to show all
    )

    # Create a regex pattern to include any job title containing the selected keywords
    pattern = '|'.join(selected_keywords)

    # Filter the DataFrame based on selected job titles
    filtered_df = indeed_df[
        (indeed_df[job_title_column].str.contains(pattern, case=False, na=False))
    ]

    # Count occurrences of each skill after filtering by job titles
    if skill_column in filtered_df.columns and filtered_df[skill_column].dtype == 'object':
        category_counts = filtered_df[skill_column].value_counts()

        if not category_counts.empty:
            # Multi-select filter for sub-skills
            selected_skills = st.multiselect(
                'Select specific skills to visualize',
                options=category_counts.index.tolist(),
                default=category_counts.index.tolist()  # Default to show all skills
            )

            # Create a filtered data series based on selected skills
            filtered_counts = category_counts[selected_skills]

            # Create a bar chart for the filtered sub-skills
            if not filtered_counts.empty:
                plt.figure(figsize=(10, 6))
                plt.bar(filtered_counts.index, filtered_counts.values, color='skyblue')
                plt.xlabel('Skills')
                plt.ylabel('No. of Position Require These Skills')
                plt.title(f'Distribution of Skills')
                plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
                st.pyplot(plt)
            else:
                st.warning("No data available for the selected skills.")
        else:
            st.warning("No skills found in the filtered job titles.")
    else:
        st.warning("No skills found in the dataset or the selected job titles.")

def visualisations():
    #Initialize Dataset
    ITJobs_df = initialize_ITJobs_dataset()

    category_column = 'job_title' 
    sizes = ITJobs_df[category_column].value_counts()  # Counts the occurrences of each category
    job = sizes.index  # The unique category 
    sizes = sizes.values  # The corresponding sizes

    # Create the pie chart
    fig = px.pie(values=sizes, names=job, title="IT Entry Level Jobs")

    # Display pie chart 
    st.plotly_chart(fig)

def visualisations():
    #Initialize Dataset
    itjob_df = initialize_itjob_headerfinal_dataset()

    category_column = 'education_level' 
    sizes = itjob_df[category_column].value_counts()  # Counts the occurrences of each category
    labels = sizes.index  # The unique category labels
    sizes = sizes.values  # The corresponding sizes

    # Create the pie chart
    fig = px.pie(values=sizes, names=labels, title="Education for IT Jobs")

    # Display pie chart 
    st.plotly_chart(fig)


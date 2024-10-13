import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title of the app
st.title("Distributions of Skills")

# Define the path to your Excel file 
# file_path = "../Pre-Processing/Final.xlsx"

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the file path to Final.xlsx
file_path = os.path.join(current_dir, "../Pre-Processing/Final.xlsx")

# Read the Excel file
df = pd.read_excel(file_path)

column_to_plot = "Skill"  # Set this to the column name for skills in your Excel file
job_title_column = "Job Title" 

# Check if columns exist
if column_to_plot not in df.columns:
    st.error(f"Column '{column_to_plot}' not found in the dataset.")
else:
    if job_title_column not in df.columns:
        st.error(f"Column '{job_title_column}' not found in the dataset.")
    else:
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
        filtered_df = df[df[job_title_column].str.contains(pattern, case=False, na=False)]

        # Count occurrences of each skill after filtering by job titles
        if column_to_plot in filtered_df.columns and filtered_df[column_to_plot].dtype == 'object':
            category_counts = filtered_df[column_to_plot].value_counts()

            # Check if category_counts is not empty
            if not category_counts.empty:
                # Multi-select filter for sub-skills
                selected_skills = st.multiselect(
                    'Select specific skills to visualize:',
                    options=category_counts.index.tolist(),
                    default=category_counts.index.tolist()  # Default to show all
                )

                # Create a filtered data series based on selected skills
                filtered_counts = category_counts[selected_skills]

                # Define a range for filtering based on some criteria (add this feature if needed)
                # selected_range = st.slider("Select the range of skill counts:", 0, max(filtered_counts), (0, max(filtered_counts)))
                # filtered_counts = filtered_counts[(filtered_counts >= selected_range[0]) & (filtered_counts <= selected_range[1])]

                # Function to plot the graph
                def plot_graph(data):
                    plt.figure(figsize=(10, 5))
                    data.plot(kind='bar', color='skyblue')
                    plt.xlabel(column_to_plot)
                    plt.ylabel('No. of Positions Requiring These Skills')

                # Function to add title
                def add_title(title):
                    plt.title(title)

                # Create a bar chart for the filtered sub-skills
                if not filtered_counts.empty:
                    plot_graph(filtered_counts)
                    add_title(f'Distribution of Skills in {column_to_plot}')
                    st.pyplot(plt)
                else:
                    st.warning("No skills selected or found.")
            else:
                st.warning("Please select at least one skill to visualize.")
        else:
            st.warning("Please select a non-numeric column for plotting.")

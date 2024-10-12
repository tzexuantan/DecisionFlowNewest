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

def initialize_salary_dataset():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # File path to the dataset
    file_path = os.path.join(current_dir, "../dataset/Salary_Data_Based_country_and_race.xlsx")
    itjob_salary_df = pd.read_excel(file_path)
    return itjob_salary_df

def initialize_certificate_dataset():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # File path to the dataset
    file_path = os.path.join(current_dir, "../dataset/Certificate.xlsx")
    itjob_Certificate_df = pd.read_excel(file_path)
    return itjob_Certificate_df

def plot_bar_graph(data, company_x_col, company_y_col, title):
    x_col = company_x_col
    y_col = company_y_col
    plt.figure(figsize=(10, 5))
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)

    data.plot(kind='bar', x=x_col, y=y_col, color='skyblue')
    plt.tight_layout()  
    st.pyplot(plt)      

def plot_pie_chart(size, label, title):
    plt.figure(figsize=(8,8))
    plt.pie(values=size, names=label)
    plt.title(title)
    plt.axis('equal')
    plt.plot()

def plot_horizontal_graph(data, col1, col2, title):
    plt.figure(figsize=(10, 6))
    plt.barh(data[col1], data[col2], label=col2)
    plt.xlabel('Salary')
    plt.ylabel('Job Title')
    plt.title(title)
    plt.legend()
    plt.savefig('plot.png')
    st.pyplot(plt)

def plot_histogram(data,col,chosen, title):
    num_bins = len(chosen) if len(chosen) > 0 else 1
    plt.figure(figsize=(10, 6))
    plt.hist(data[col], bins=num_bins, edgecolor='k', alpha=0.7)
    plt.xlabel('Sub-skill')
    plt.ylabel('Frequency')
    plt.title(title)
    st.pyplot(plt)

def plot_line_chart(data, title):
        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data.values, color='b', linestyle='-', linewidth=2, marker='o')
        plt.title(title)
        plt.xlabel('Certificate')
        plt.ylabel('No. of people with the certificate')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.grid(True)
        st.pyplot(plt)

def visualizations():
    # Initialize dataset
    indeed_df = initialize_indeed_dataset()

    # Bar Graph
    st.title("Distributions of Skills")

    #Column to plot
    column_to_plot4 = "Skill"
    skill_y_col = "No. of Position Require These Skills"
    skill_x_col = "Skills"
    job_title_column = "Job Title"

    # Check if columns exist
    if column_to_plot4 not in indeed_df.columns:
        st.error(f"Column '{column_to_plot4}' not found in the Excel file.")
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
    if column_to_plot4 in filtered_df.columns and filtered_df[column_to_plot4].dtype == 'object':
        category_counts = filtered_df[column_to_plot4].value_counts()

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
                # Create a bar chart
                st.bar_chart(filtered_counts)

            else:
                st.warning("No data available for the selected skills.")
        else:
            st.warning("No skills found in the filtered job titles.")
    else:
        st.warning("No skills found in the dataset or the selected job titles.")

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

    # Initialize the dataset
    indeed_df = initialize_indeed_dataset()

    # Title of the app
    st.title("Companies that are hiring the IT roles")

    # Column to plot
    column_to_plot3 = "Company/Candidate Name"
    company_x_col = "Company"
    company_y_col = "No. of roles"

    if indeed_df[column_to_plot3].dtype == 'object':
        # Count occurrences of each category
        category_counts3 = indeed_df[column_to_plot3].value_counts()

        # Display the top 3 companies hiring the most IT roles for the entire dataset
        top3_companies = category_counts3.nlargest(3)
        st.write("**Top 3 companies that are hiring the most IT roles:**")
        for company, count in top3_companies.items():
            st.write(f"{company}: {count} roles")

        # Display the company with the highest and lowest number of roles
        highest_company = category_counts3.idxmax()
        highest_count = category_counts3.max()
        lowest_company = category_counts3.idxmin()
        lowest_count = category_counts3.min()

        st.write(f"**Company with the highest number of roles:** {highest_company} ({highest_count} roles)")
        st.write(f"**Company with the lowest number of roles:** {lowest_company} ({lowest_count} role)")

        # Check if category_counts is not empty
        if not category_counts3.empty:
            # Multi-select to choose specific data
            selected_companies = st.multiselect(
                'Select companies to visualize',
                options=category_counts3.index.tolist(),  # Provide the list of options
                default=[]  # Default to show none
            )

            # Filter the data based on selected companies
            if selected_companies:
                filtered_data = indeed_df[indeed_df[column_to_plot3].isin(selected_companies)]
                filtered_counts = filtered_data[column_to_plot3].value_counts().reset_index()
                filtered_counts.columns = [company_x_col, company_y_col]  # Ensure the columns match correctly

                # Plot the bar graph for selected companies
                plot_bar_graph(filtered_counts, company_x_col, company_y_col, 'Companies that are hiring the IT roles')

    # Assume 'initialize_salary_dataset' is a function that loads the dataset
    itjob_salary_df = initialize_salary_dataset()

    st.title("Salary ranges for IT jobs")
    column1 = 'Job Title'
    column2 = 'Salary'

    # Convert Salary column to numeric
    itjob_salary_df[column2] = pd.to_numeric(itjob_salary_df[column2], errors='coerce')

    # Handle missing values
    itjob_salary_df[column1].fillna('', inplace=True)
    itjob_salary_df[column2].fillna(0, inplace=True)

    # Add number inputs for filtering salary range
    min_salary = itjob_salary_df[column2].min()
    max_salary = itjob_salary_df[column2].max()
    min_value = st.number_input('Min Salary', min_value=min_salary, max_value=max_salary, value=min_salary)
    max_value = st.number_input('Max Salary', min_value=min_salary, max_value=max_salary, value=max_salary)

    # Assume 'initialize_salary_dataset' is a function that loads the dataset
    itjob_salary_df = initialize_salary_dataset()

    st.title("Salary ranges for IT jobs")
    column1 = 'Job Title'
    column2 = 'Salary'

    # Convert Salary column to numeric
    itjob_salary_df[column2] = pd.to_numeric(itjob_salary_df[column2], errors='coerce')

    # Handle missing values
    itjob_salary_df[column1].fillna('', inplace=True)
    itjob_salary_df[column2].fillna(0, inplace=True)

    # Add number inputs for filtering salary range
    min_salary = itjob_salary_df[column2].min()
    max_salary = itjob_salary_df[column2].max()
    min_value = st.number_input('Min Salary', min_value=min_salary, max_value=max_salary, value=min_salary)
    max_value = st.number_input('Max Salary', min_value=min_salary, max_value=max_salary, value=max_salary)

    # Filter the DataFrame based on the salary range
    filtered_df4 = itjob_salary_df[(itjob_salary_df[column2] >= min_value) & (itjob_salary_df[column2] <= max_value)]

    # Update job titles based on the filtered DataFrame
    job_titles = filtered_df4[column1].unique()

    # Allow users to select job titles, defaulting to none
    selected_job_titles = st.multiselect('Select Job Titles', job_titles, default=[])

    # Further filter the DataFrame based on selected job titles
    filtered_df4 = filtered_df4[filtered_df4[column1].isin(selected_job_titles)]

    # Display a message if no jobs match the selected criteria, else show visualization
    plot_horizontal_graph(filtered_df4, column1, column2, 'Salary ranges for IT jobs')

    # Initialize the dataset
    indeed_df = initialize_indeed_dataset()
    st.title('Most Commonly Required IT Competencies in the Industry')
    column = 'Sub-skill'
    # Handle missing values
    indeed_df[column].fillna('Unknown', inplace=True)
    # Initialize filtered_df5
    filtered_df5 = indeed_df.copy()  # Start with a copy of the full dataset
    # Get unique sub-skills for the multiselect box
    sub_skills = indeed_df[column].unique()
    selected_sub_skills = st.multiselect('Select Sub-skills', sub_skills, default=[])
    # Filter the DataFrame based on selected sub-skills
    if selected_sub_skills:  # Check if any sub-skills are selected
        filtered_df5 = filtered_df5[filtered_df5[column].isin(selected_sub_skills)]
        plot_histogram(filtered_df5, column, selected_sub_skills, 'Most Commonly Required IT Competencies in the Industry')

    # Initialize the dataset
    itjob_Certificate_df = initialize_certificate_dataset

    st.title("Distribution of Certificates in the Data File")
    if 'certification_text' in itjob_Certificate_df.columns:
    # Count occurrences of each certificate
        certificate_counts = itjob_Certificate_df['certification_text'].value_counts().sort_index()

    # Display the top 3 most common certificates
    top3_certificates = certificate_counts.nlargest(3)
    st.write("**Top 3 Most Common Certificates:**")
    for certificate, count in top3_certificates.items():
        st.write(f"{certificate}: {count} people")

    # Multi-select to filter certificates
    selected_certificates = st.multiselect(
        'Select certificates to visualize',
        options6=certificate_counts.index.tolist(),  # Provide the list of options
        default=[]  # Default to show none
    )

    # Filter the data based on selected certificates
    filtered_counts = certificate_counts[selected_certificates]
    if selected_certificates:
        filtered_counts6 = certificate_counts[selected_certificates]
        plot_line_chart(filtered_counts6, 'Distribution of Certificates in the Data File')
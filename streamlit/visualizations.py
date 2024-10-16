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
    # File path to the dataset
    file_path = os.path.join(current_dir, "../dataset/IT Jobs.xlsx")
    ITJobs_df = pd.read_excel(file_path)
    return ITJobs_df

def initialize_itjob_headerfinal_dataset(): 
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # File path to the dataset
    file_path = os.path.join(current_dir, "../dataset/itjob_headerfinal.xlsx")
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
        plt.xticks(rotation=90)
        plt.grid(True)
        st.pyplot(plt)

def visualizations():
   # Initialize dataset
    indeed_df = initialize_indeed_dataset()

    # Title of the app
    st.title("Distribution of Skills")

    # Column to plot
    column_to_plot4 = "Skill"
    skill_y_col = "No. of Positions Requiring These Skills"
    skill_x_col = "Skills"
    job_title_column = "Job Title"

    # Check if columns exist
    if column_to_plot4 not in indeed_df.columns:
        st.error(f"Column '{column_to_plot4}' not found in the dataset.")
    else:
        if job_title_column not in indeed_df.columns:
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
        filtered_df = indeed_df[
            (indeed_df[job_title_column].str.contains(pattern, case=False, na=False))
        ]

        # Count occurrences of each skill after filtering by job titles
        if column_to_plot4 in filtered_df.columns and filtered_df[column_to_plot4].dtype == 'object':
            category_counts = filtered_df[column_to_plot4].value_counts()

            if not category_counts.empty:
                # Multi-select filter for sub-skills
                selected_skills = st.multiselect(
                    'Select specific skills to visualize:',
                    options=category_counts.index.tolist(),
                    default=category_counts.index.tolist()  # Default to show all skills
                )

                # Create a filtered data series based on selected skills
                filtered_counts = category_counts[selected_skills]

                # Display Analysis
                st.title("💪 Distribution of Skills")
                st.write("""
                        # Visual Description 📊
                        **Top IT skills needed for company positions:**
                        - **Web Development (WebD)**, **Coding**, and **DevOps** are among the most in-demand technical skills.
                        - Soft skills like **communication**, **teamwork**, and **problem-solving** are crucial across industries.

                        **Importance of These Skills ✅:**
                        - **Web Development (WebD)** ensures a functional, user-friendly online presence, essential for customer engagement and e-commerce.
                        - **Coding** serves as the foundation for software development, enabling IT professionals to create, test, and maintain applications while automating processes for efficiency.
                        - **DevOps** facilitates efficient software delivery, promoting collaboration between development and operations teams for faster, more reliable updates and scalable solutions.
                        - **Soft skills** like communication, teamwork, and problem-solving enhance collaboration and productivity in any workplace.

                        **Unlock your potential by mastering these skills!These are the building blocks for success in today’s job market. Stay focused—your dream job is within reach! 🙌**
                        """)

                # Create a bar chart for the filtered sub-skills
                if not filtered_counts.empty:
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

    # Combined analysis using st.write
    st.title("📈Entry Level")
    st.write("""
            # 📊 Visual Description
            - The most popular entry-level IT job for tech freshers is **Data Analyst**, accounting for **76.1%** of applications.
            - The least popular positions include **Data Reporting Analyst**, **Data Quality Analyst**, and **BI Analyst**, each at **0.718%**.

            # 🔍 Analysis of Key Insights
            - **Data Analyst**: Focuses on developing foundational skills in data manipulation, analysis, and reporting, helping businesses gain insights from data.
            - **Business Intelligence (BI) Analyst**: Gathers and manages data using SQL, ensures data quality through cleansing techniques, and applies analytics to identify trends.
            - **Research Analyst**: Collects data from various sources, uses statistical tools like Excel, R, or Python for analysis, and creates detailed reports summarizing findings.
            - **Data Management Analyst**: Gathers and cleans data from various sources, uses database management systems like SQL to store and manipulate data, and monitors data quality with governance practices.
            - **Data Operations Analyst**: Manages data transfers, implements quality control measures to ensure data accuracy, and analyzes operations using tools like SQL and Excel.
            - **Business Intelligence**: Gathers, prepares, and analyzes data to identify trends, and creates interactive dashboards and reports using BI tools.
            - **Data Reporting Analyst**: Gathers and prepares data, cleans and manipulates it, and creates comprehensive reports tailored to stakeholder needs.
            - **Data Quality Analyst**: Assesses data quality to identify inaccuracies, implements processes for data cleaning and validation, and develops metrics for quality monitoring.
            - **BI Analyst**: Prepares and cleans data, analyzes it using SQL and Excel, and creates interactive dashboards and reports.

            As you embark on your journey in the tech industry, remember that **every challenge is an opportunity to learn and grow**. 🌱 Starting with an entry-level job will serve as a stepping stone to greater success. **Good luck in your endeavors!** 🎉✨
            """)

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

    # Analysis
    st.title("🎓Education for IT Jobs in Singapore")
    st.write("""
            # 📊 Visual Description
            - The most required education for IT jobs is a **Bachelor's Degree**, accounting for **65.7%** of roles.
            - **Diploma holders** also make up a significant portion, with **22%** of IT job positions.
            - **Certificates** contribute a minimal **0.0343%**, indicating a much lower acceptance rate for IT-related certifications.

            # 💡 Importance of Education in IT Jobs
            - IT is a highly competitive field, and many companies **prefer candidates with Bachelor's Degrees**.
             - **Degree programs** provide a comprehensive skill set and foster critical thinking and problem-solving abilities, which are crucial in IT roles.
            - **Diplomas** focus on specific skills, but they may not cover the broad knowledge required for career advancement in many IT roles.
            - **Certifications**, while helpful for learning specific technologies, may leave gaps in broader IT concepts, limiting long-term career growth.

            Pursuing a **Bachelor's Degree** can unlock new opportunities in IT, but remember, your **Diploma** and **Certifications** are valuable too. Each step builds your skill set and prepares you for success in the IT industry. 🌟
            """)

    # Display pie chart 
    st.plotly_chart(fig)

    # Initialize the dataset
    indeed_df = initialize_indeed_dataset()

    st.title("🏢 Companies Hiring IT Roles")
    # Column to plot
    column_to_plot3 = "Company/Candidate Name"
    company_x_col = "Company"
    company_y_col = "No. of roles"

    sizes = indeed_df[column_to_plot3].value_counts()  # Counts the occurrences of each category
    labels = sizes.index  # The unique category labels
    sizes = sizes.values  # The corresponding sizes

    if indeed_df[column_to_plot3].dtype == 'object':
        # Count occurrences of each category
        category_counts3 = indeed_df[column_to_plot3].value_counts()

        # Check if category_counts is not empty
        if not category_counts3.empty:
            # Multi-select to choose specific data
            selected_companies = st.multiselect(
                label='Select companies to visualize',
                options=category_counts3.index.tolist(),  # Provide the list of options
                default=[]# Default to show none
            )

        # Analysis
        st.write("""
                # **Visual Description 📊**  
                The top 3 companies that are hiring the most IT roles are **Deloitte** (1,297 roles), **Accenture** (576 roles), and **Amazon Web Services, Inc** (551 roles) respectively.

                # **Company Background 💻**  
                **Deloitte** is expanding its IT workforce to support emerging technologies like AI, cloud computing, and cybersecurity, which are in high demand globally. This hiring spree aligns with the firm's global strategy to meet the growing need for digital transformation solutions and enhanced cybersecurity services.

                **Accenture** is actively hiring for IT roles due to its expansive focus on digital transformation, consulting, and technology-driven services across numerous industries. The company leverages cutting-edge technologies like AI, cloud computing, and automation to support its clients in navigating complex business challenges and driving innovation.

                **Amazon Web Services (AWS)** is hiring extensively due to its rapid growth in the cloud computing sector. AWS has been focusing on areas like artificial intelligence, machine learning, generative AI, and expanding its global cloud infrastructure.

                These companies offer innovative environments that encourage personal growth, skill development, and the opportunity to make a real impact in the fast-evolving digital landscape. Don’t hold back—take that step forward and build the career you’ve always dreamed of! 💭
                """)

        # Filter the data based on selected companies
        if selected_companies:
            filtered_data = indeed_df[indeed_df[column_to_plot3].isin(selected_companies)]
            filtered_counts = filtered_data[column_to_plot3].value_counts().reset_index()
            filtered_counts.columns = [company_x_col, company_y_col]

            # Plot the bar graph for selected companies
            plot_bar_graph(filtered_counts, company_x_col, company_y_col, 'Companies that are hiring the IT roles')

    itjob_salary_df = initialize_salary_dataset()
    st.title("💵Salary ranges for IT jobs")

    column1 = 'Job Title'
    column2 = 'Salary'

    itjob_salary_df[column2] = pd.to_numeric(itjob_salary_df[column2], errors='coerce')

    # Handle missing values
    itjob_salary_df[column1] = itjob_salary_df[column1].fillna('')
    itjob_salary_df[column2] = itjob_salary_df[column2].fillna(0)

    # Add number inputs for filtering salary range
    min_salary = itjob_salary_df[column2].min()
    max_salary = itjob_salary_df[column2].max()
    min_value = st.number_input('Min Salary', min_value=min_salary, max_value=max_salary, value=min_salary)
    max_value = st.number_input('Max Salary', min_value=min_salary, max_value=max_salary, value=max_salary)

    # Filter the DataFrame based on the salary range
    filtered_df4 = itjob_salary_df[(itjob_salary_df[column2] >= min_value) & (itjob_salary_df[column2] <= max_value)]

    # Update job titles based on the filtered DataFrame
    job_titles = filtered_df4[column1].unique()

    st.write("""
            **Let's look into the salary range of different IT Jobs! Select the job you are interested in 🎀**

            Explore the different jobs and make your decision wisely! Ps. You can explore other jobs too
            """)
    
    # Allow users to select job titles, defaulting to all options if none are selected
    selected_job_titles = st.multiselect('Select Job Titles', job_titles, default=[])
    # Display the filtered dataframe
    if selected_job_titles:
        filtered_df4 = filtered_df4[filtered_df4[column1].isin(selected_job_titles)]
        plot_horizontal_graph(filtered_df4, column1, column2, 'Salary ranges for IT jobs')

    # Initialize the dataset
    indeed_df = initialize_indeed_dataset()
    column = 'Sub-skill'

    # Handle missing values
    indeed_df[column].fillna('Unknown', inplace=True)

    # Initialize filtered_df5
    filtered_df5 = indeed_df.copy()  # Start with a copy of the full dataset

    st.write("### **IT Competencies in the Industry**")

    # Get unique sub-skills for the multiselect box
    sub_skills = indeed_df[column].unique()
    selected_sub_skills = st.multiselect('Select Sub-skills', sub_skills, default=[])
    st.write("""
    ### Visual Description 📊
    The top 3 most commonly required IT competencies are Excel - 6322 people, PowerPoint - 2600 people and Flexible - 2162 people.

    ### Insights 💡
    **Excel Skills Lead the Demand:** With 57.04% of positions requiring Excel, it is clear that proficiency in data management, analysis, and reporting is highly valued in the IT industry. This could reflect the need for data-driven decision-making and managing large datasets.

    **PowerPoint as a Communication Tool:** PowerPoint skills are required in 23.45% of the positions, indicating the importance of presenting information effectively. This might be related to roles that require creating presentations, reports, and visualizations for stakeholders.

    **Flexibility in Work Style:** Around 19.51% of the positions emphasize flexibility, which could suggest a demand for adaptability in work environments or roles that require shifting between different projects or tools.

    ### Recommendations 🔍
    **Prioritize Excel Proficiency:**
    Since over 57% of the positions require Excel skills, it is crucial for candidates to master this tool. This includes functions like data analysis, pivot tables, charts, and macros. Investing in advanced Excel training can give a competitive edge and may open doors to a wider range of roles, especially those involving data-heavy tasks or financial analysis.

    **Develop Effective Presentation Skills:**
    With PowerPoint required for 23.45% of positions, being able to create clear, visually appealing presentations is important. This skill is valuable not only for communication but also for pitching ideas, reporting results, and training others. Candidates should focus on learning how to design slides that are concise, engaging, and easy to understand, possibly incorporating data visualizations and storytelling techniques.

    **Embrace a Flexible Work Approach:**
    Flexibility, desired in 19.51% of the positions, suggests that employers value adaptability. Being able to shift between tasks, learn new tools quickly, and adjust to different work environments can be a major asset. For candidates, developing a growth mindset and learning agile or adaptable work methodologies could be beneficial in meeting the demands of dynamic work environments.

    By sharpening your Excel expertise, mastering the art of presenting ideas through PowerPoint, and being open to change, you’re not just meeting industry needs—you’re setting yourself up for success. Remember, every skill you acquire is an investment in your future. Keep learning, stay adaptable, and the right opportunity will come your way! 🚀
    """)
    # Filter the DataFrame based on selected sub-skills
    if selected_sub_skills:  # Check if any sub-skills are selected
        filtered_df5 = filtered_df5[filtered_df5[column].isin(selected_sub_skills)]
        plot_histogram(filtered_df5, column, selected_sub_skills, 'IT Competencies in the Industry')

    # Initialize the dataset
    itjob_Certificate_df = initialize_certificate_dataset()

    st.title("Distribution of Certificates in Singapore")
    if 'certification_text' in itjob_Certificate_df.columns:
    # Count occurrences of each certificate
        certificate_counts = itjob_Certificate_df['certification_text'].value_counts().sort_index()

    # Multi-select to filter certificates
    selected_certificates = st.multiselect(
    'Select certificates to visualize',
    options=certificate_counts.index.tolist(),  # Provide the list of options
    default=[]  # Default to show none
)

    # Section for IT Certificates
    st.title("📜 IT Certificates")

    # Combined Certificates Description and Purpose
    st.write("""
            ## **Visual Description 📊**  
            The top 3 certificates in the IT industry are **Cisco (CCNA/CCNP/CCIE)** - 263 People, **Project Management Professional (PMP)** - 155 People and **Information Technology Infrastructure Library (ITIL)** - 153 People

            ## **Purpose 📎**  
            - **Cisco (CCNA/CCNP/CCIE)**: These are essential credentials for IT professionals aiming to advance their careers in networking and IT infrastructure. Employers greatly value these certificates as they demonstrate a thorough proficiency in network fundamentals, security protocols, and sophisticated troubleshooting procedures.

            - **PMP (Project Management Professional)**: This certification denotes the knowledge and expertise needed to handle projects successfully. Acquiring the PMP certification can boost prospects for professional growth, as numerous establishments value this qualification and frequently require it for project management positions.

            - **ITIL (Information Technology Infrastructure Library)**: ITIL is a widely used framework for IT service management (ITSM) that offers best practices to assist businesses in planning, implementing, and enhancing their IT services. It is structured around a lifecycle that includes service strategy, design, transition, operation, and continual improvement.

            - Overall, these IT Certifications deepen your knowledge and demonstrate your commitment to excellence in your field. They will help enhance employability and boost earning potential.

            **Upgrade yourself** and position yourself as a leader in your industry, ready to tackle complex challenges and drive innovation. Don’t just wait for opportunities—create them! 🌈
            """)

    
    # Filter the data based on selected certificates
    filtered_counts = certificate_counts[selected_certificates]
    if selected_certificates:
        filtered_counts6 = certificate_counts[selected_certificates]
        plot_line_chart(filtered_counts6, 'Distribution of Certificates in Singapore')
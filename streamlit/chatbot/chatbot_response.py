import streamlit as st

menu_list = [
    "Recruitment-related Questions",
    "Visualizations?",
    "Just wanna have a chat?"
]

recruitment_qns_list = [
    "Recommend degrees or skills for a job position",
    "Jobs I can apply for with my qualifications",
    "Find a job quickly after graduation",
    "Does my school affect my employment rate?",
    "Industries in high demand"
]

visualizations_list = [
    "What is the distribution of skills that are highly sought by companies?",
    "What are the top 3 aspects of employer branding that are most important to new graduates?",
    "What are the entry level jobs for new graduates in AI?"
]

# Function to display options
def display_options(options_list, add):
    st.write("Please select an option:")
    for idx, option in enumerate(options_list):
        if st.button(option, key=f"option_{idx+add}"):
            st.session_state.selected_option = option
            st.session_state.option_clicked = True  # Set flag to indicate an option was clicked
            st.rerun()  # Force rerun after option is clicked

    # Add a back button to return to the main menu
    if st.session_state.current_menu != None and st.button("Back to Main Menu"):
        st.session_state.current_menu = None  # Reset the current menu
        st.rerun()  # Trigger a rerun to refresh the options

def handle_option(option):
    if option:
        st.session_state.messages.append({"user": "user", "message": option})

        # Display next set of options based on previous selection
        if option == menu_list[0]:
            st.session_state.current_menu = 'recruitment'
        elif option == menu_list[1]:
            st.session_state.current_menu = 'visualization'
        elif option == menu_list[2]:
            st.session_state.current_menu = 'chat'
            bot_response = "I'm here to chat!"
            st.session_state.messages.append({"user": "bot", "message": bot_response})

        # Handle the specific recruitment or visualization options if chosen
        elif option in recruitment_qns_list:
            handle_recruitment_option(option)
        elif option in visualizations_list:
            handle_visualization_option(option)

        # If a menu item is selected, reset option_clicked and rerun once
        st.session_state.option_clicked = False
        st.rerun()

# Function to handle recruitment options
def handle_recruitment_option(option):
    if option == recruitment_qns_list[0]:
        bot_response = "To excel in a job position, degrees in relevant fields, alongside skills like critical thinking and communication, are essential."
    elif option == recruitment_qns_list[1]:
        bot_response = "Based on your qualifications, you can apply for jobs such as Data Analyst, Software Developer, or Marketing Specialist."
    elif option == recruitment_qns_list[2]:
        bot_response = "To find a job quickly, consider internships, networking events, and job fairs as they can provide valuable opportunities."
    elif option == recruitment_qns_list[3]:
        bot_response = "Yes, the reputation and resources of your school can influence your employment opportunities."
    elif option == recruitment_qns_list[4]:
        bot_response = "Currently, industries such as Technology, Healthcare, and Renewable Energy are in high demand."
    else:
        bot_response = "I'm sorry, I didn't understand that option."
    
    st.session_state.messages.append({"user": "bot", "message": bot_response})

# Function to handle visualization options
def handle_visualization_option(option):
    bot_response = "Feature currently not available"
    st.session_state.messages.append({"user": "bot", "message": bot_response})

# Function to display chat messages
def display_messages():
    for msg in st.session_state.messages:
        if msg['user'] == "user":
            st.write(f"<div style='text-align: right; margin: 5px;'><b>You:</b> {msg['message']}</div>", unsafe_allow_html=True)
        else:
            st.write(f"<div style='text-align: left; margin: 5px;'><b>Bot:</b> {msg['message']}</div>", unsafe_allow_html=True)

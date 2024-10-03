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
        # Use a unique key for each button by combining a string with the index
        if st.button(option, key=f"option_{idx+add}"):
            st.session_state.selected_option = option
            handle_option(st.session_state.selected_option, idx+add)


def handle_option(option, selected_option_key):
    st.session_state.messages.append({"user": "user", "message": option})
    # delete_other_options(f"option_{selected_option_key}")
    if option == menu_list[0]:
        display_options(recruitment_qns_list,10)
    elif option == menu_list[1]:
        display_options(visualizations_list, 20)
    # elif option == menu_list[2]:
    #     chatbot_talk()
    elif option in recruitment_qns_list:
        handle_recruitment_option(st.session_state.selected_option)
    elif option in visualizations_list:
        handle_visualization_option(st.session_state.selected_option)

# Function to handle the selected option
def handle_recruitment_option(option):
    # Append the selected option to chat history
    st.session_state.messages.append({"user": "user", "message": option})

    # Generate bot's response based on the selected option
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
    
    # Append the bot's response to chat history
    st.session_state.messages.append({"user": "bot", "message": bot_response})

def handle_visualization_option(option):
    # Append the selected option to chat history
    st.session_state.messages.append({"user": "user", "message": option})

    bot_response = "Feature currently not available"

    st.session_state.messages.append({"user": "bot", "message": bot_response})

#Function to delete other option buttons
def delete_other_options(selected_option_key):
    for key in list(st.session_state.keys()):
        if key.startswith("option_") and key != selected_option_key:
            del st.session_state[key]

# Function to display messages
def display_messages():
    for msg in st.session_state.messages:
        if msg['user'] == "user":
            st.write(f"<div style='text-align: right; margin: 5px;'><b>You:</b> {msg['message']}</div>", unsafe_allow_html=True)
        else:
            st.write(f"<div style='text-align: left; margin: 5px;'><b>Bot:</b> {msg['message']}</div>", unsafe_allow_html=True)

import streamlit as st
from chatbot.chatbot_response import *

def chatbot():

    # Initialize session state for chat history and selected option
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "selected_option" not in st.session_state:
        st.session_state.selected_option = None  # Initialize selected_option

    # Display chat messages
    display_messages()

    # Display chatbot options (buttons will always remain visible)
    display_options(menu_list,0)
    

    # No need to reset selected_option to None here anymore

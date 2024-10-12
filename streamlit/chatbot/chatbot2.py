from openai import OpenAI
import streamlit as st

def chatbot2():

    def handleUserInput(userInput):
        #if userInput:
        st.session_state.messagesList.append({"role": "user", "content": userInput})
        with st.chat_message("user"):
            st.markdown(userInput)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {
                        "role": message["role"], 
                        "content": message["content"]
                    }
                    for message in st.session_state.messagesList
                ],
                stream=True,
            )
            response = st.write_stream(stream)

        st.session_state.messagesList.append({"role": "assistant", "content": response})


    def initializeSessionStateVariables():
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = OPENAI_MODEL_TYPE

        if "messagesList" not in st.session_state:
            st.session_state.messagesList = []
            st.session_state.messagesList.append({"role": "system", "content": SYSTEM_ROLE})


    def displayMessageHistory():
        for message in st.session_state.messagesList:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
            

    def createExpanderElementAndGetSelectedQuestionIndex():
        with st.expander("Recruitment-related Questions"):
            print("triggered or not - shld be triggered on every refresh")
            # question = "Recommend degrees or skills for a job position."
            # if st.button(question):
            #     print("triggered3")
            #     return question

            selectedQuestionIndex = -1

            for i in range(len(questionsAndAnswersData)):
                questionInput = questionsAndAnswersData[i]['question']
                if st.button(questionInput):
                    print("triggered with index: ", i)
                    selectedQuestionIndex = i
            return selectedQuestionIndex


    OPENAI_MODEL_TYPE = "gpt-4o-mini"
    SYSTEM_ROLE = "You are a helpful assistant that answers recruitment-related questions to students \
                planning for their professional future in the field of tech in the context of Singapore. VAR_A is 3"

    questionsAndAnswersData = [
        {
            "question": "Recommend degrees or skills for a job position",
            "answer": ""
        },
        {
            "question": "Jobs I can apply for with my qualifications",
            "answer": "Based on your qualifications, you can apply for jobs such as Data Analyst, Software Developer, or Marketing Specialist."
        },
        {
            "question": "Find a job quickly after graduation",
            "answer": "To find a job quickly, consider internships, networking events, and job fairs as they can provide valuable opportunities."
        },
        {
            "question": "Does my school affect my employment rate?",
            "answer": "Yes, the reputation and resources of your school can influence your employment opportunities."
        },
        {
            "question": "Industries in high demand",
            "answer": "Currently, industries such as Technology, Healthcare, and Renewable Energy are in high demand."
        }
    ]

    # Example of printing the questions and answers
    # for qa in qa_data:
    #     print(f"Q: {qa['question']}\nA: {qa['answer']}\n")


    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    initializeSessionStateVariables()

    st.title("Chatbot2")
    st.write("Select from a pre-determined list of questions from either button category shown below or ask the chatbot directly!")

    selectedQuestionIndex = createExpanderElementAndGetSelectedQuestionIndex()
    print("sqi: ", selectedQuestionIndex)

    # with st.expander("Visualization-type Questions"):
    #     if st.button("Recommend degrees or skills for a job position.2"):
    #         print("how does this work?2")

    displayMessageHistory()

    userInputElement = st.chat_input("Message Chatbot")

    if selectedQuestionIndex != -1:
        print("triggered5")
        handleUserInput(questionsAndAnswersData[selectedQuestionIndex]['question'])

    if userInputElement:
        print("triggered4")
        handleUserInput(userInputElement)

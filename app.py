import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os

# Set page config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("🤖 AI Chatbot")
st.markdown("Chat with an AI assistant powered by LangChain and OpenAI")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize session state for API key
if "api_key" not in st.session_state:
    st.session_state.api_key = os.getenv("OPENAI_API_KEY", "")

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # API Key input
    api_key_input = st.text_input(
        "OpenAI API Key",
        value=st.session_state.api_key,
        type="password",
        help="Enter your OpenAI API key. Get one at https://platform.openai.com/api-keys"
    )
    
    if api_key_input:
        st.session_state.api_key = api_key_input
    
    # Model selection
    model_name = st.selectbox(
        "Model",
        ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"],
        index=0
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Higher values make output more random, lower values more deterministic"
    )
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.markdown("### About")
    st.markdown("This chatbot uses LangChain and OpenAI's GPT models to provide intelligent responses.")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Check if API key is provided
    if not st.session_state.api_key:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar to start chatting.")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            try:
                # Initialize LangChain ChatOpenAI
                llm = ChatOpenAI(
                    model=model_name,
                    temperature=temperature,
                    openai_api_key=st.session_state.api_key,
                    streaming=True
                )
                
                # Convert session messages to LangChain format
                langchain_messages = []
                for msg in st.session_state.messages:
                    if msg["role"] == "user":
                        langchain_messages.append(HumanMessage(content=msg["content"]))
                    elif msg["role"] == "assistant":
                        langchain_messages.append(AIMessage(content=msg["content"]))
                
                # Stream the response
                full_response = ""
                for chunk in llm.stream(langchain_messages):
                    full_response += chunk.content
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("Please check your API key and try again.")

# Footer
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
        Made with ❤️ using Streamlit and LangChain
    </div>
    """,
    unsafe_allow_html=True
)

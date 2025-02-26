import streamlit as st
import requests
import time
import os  # Import the 'os' module

# Ensure the RAG server is running and accessible
RAG_SERVER_URL = os.environ.get("RAG_SERVER_URL", "http://localhost:8000")  # Default URL

# Set page configuration
st.set_page_config(
    page_title="AI Assistant with RAG",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"  # Keep sidebar expanded for better UX
)

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thinking" not in st.session_state:
    st.session_state.thinking = False
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# Function to get response from API
def get_answer(question):
    try:
        st.session_state.thinking = True
        url = f"{RAG_SERVER_URL}/query/"
        response = requests.post(url, json={"question": question})
        response.raise_for_status()
        time.sleep(0.5)  # Small delay to show the thinking animation
        return response.json()["answer"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
    finally:
        st.session_state.thinking = False

def upload_file(file):
    try:
        url = f"{RAG_SERVER_URL}/upload/"
        files = {"file": file}
        response = requests.post(url, files=files)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Custom CSS for improved design
st.markdown("""
<style>
    /* Global styles */
    * {
        font-family: 'Söhne', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Ubuntu, Cantarell, 'Noto Sans', sans-serif;
    }

    /* Hide Streamlit elements */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    .main .block-container {
        padding: 0 !important;
        max-width: 100%;
    }

    .stApp {
        background-color: #F0F2F6;  /* Light gray background */
    }

    /* Chat container */
    .chat-container {
        display: flex;
        flex-direction: column;
        height: calc(100vh - 150px); /* Adjusted height */
        overflow-y: auto;
        padding-bottom: 100px; /* Increased padding for fixed input */
    }

    /* Message styling */
    .message-row {
        display: flex;
        padding: 12px;  /* Slightly reduced padding */
        margin: 0;
        border-radius: 8px;
        margin-bottom: 8px; /* Space between messages */
    }

    .user-row {
        background-color: #DCF8C6; /* Light green for user messages */
        justify-content: flex-end;
        margin-left: 50px;
    }

    .bot-row {
        background-color: #FFFFFF; /* White for bot messages */
        justify-content: flex-start;
        margin-right: 50px;
    }

    .message-container {
        max-width: 80%; /* Adjusted max-width */
    }

    .avatar {
        width: 36px; /* Slightly larger avatars */
        height: 36px; /* Slightly larger avatars */
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 10px;
        flex-shrink: 0;
        font-size: 14px; /* Adjusted font size */
        color: white;
    }

    .user-avatar {
        background-color: #4CAF50; /* Green user avatar */
    }

    .bot-avatar {
        background-color: #2196F3; /* Blue bot avatar */
    }

    .message-content {
        flex-grow: 1;
        word-break: break-word;  /* Prevent long words from overflowing */
        color: #333333;         /* Dark gray text for better readability */
    }

    /* Input area at bottom - FIXED */
    .input-area {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 12px;
        background-color: #FFFFFF; /* White input area */
        border-top: 1px solid #E6E6E6; /* Light gray border */
        z-index: 100;
        box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.05); /* Subtle shadow */
    }

    .input-container {
        max-width: 800px;
        margin: 0 auto;
        display: flex; /* Use flexbox for alignment */
        align-items: center; /* Vertically center the input and button */
    }

    .input-field {
        width: 100%;
        border: 1px solid #CCCCCC; /* Light gray border */
        border-radius: 8px;
        padding: 10px 15px; /* Reduced right padding */
        font-size: 16px;
        line-height: 1.5;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        resize: none;
        height: 45px;
        max-height: 150px;
        overflow-y: auto;
        margin-right: 10px; /* Space between input and button */
    }

    .send-button {
        background-color: #2196F3; /* Blue send button */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 15px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.2s ease;
        flex-shrink: 0; /* Prevent button from shrinking */
    }

    .send-button:hover {
        background-color: #0B7FD5; /* Darker blue on hover */
    }

    .send-button:disabled {
        background-color: #B0BEC5; /* Gray when disabled */
        color: #FFFFFF;
        cursor: not-allowed;
    }

    /* Typing indicator */
    .typing-indicator {
        display: flex;
        align-items: center;
        margin-top: 10px;
    }

    .typing-dot {
        width: 8px;
        height: 8px;
        background-color: #2196F3; /* Blue typing dots */
        border-radius: 50%;
        margin-right: 5px;
        animation: typing-animation 1.4s infinite ease-in-out;
    }

    .typing-dot:nth-child(1) {
        animation-delay: 0s;
    }

    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }

    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }

    @keyframes typing-animation {
        0%, 60%, 100% { transform: translateY(0); }
        30% { transform: translateY(-5px); }
    }

    /* Welcome message styling */
    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: calc(100vh - 250px);
        padding: 0 20px;
        text-align: center;
        color: #555555; /* Medium gray text */
    }

    .welcome-title {
        font-size: 32px;
        margin-bottom: 20px;
        font-weight: bold;
        color: #333333; /* Dark gray title */
    }

    .welcome-subtitle {
        font-size: 18px;
        color: #777777; /* Medium-light gray subtitle */
        margin-bottom: 30px;
    }

    /* Fix Streamlit button margins */
    .stButton {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }

    /* Upload area styling */
    .upload-area {
        margin-bottom: 20px;
        padding: 15px;
        border: 1px dashed #CCCCCC;
        border-radius: 8px;
        text-align: center;
        background-color: #F9F9F9;
    }

    .upload-area:hover {
        border-color: #2196F3; /* Blue hover color */
        background-color: #E8F5FF; /* Lighter blue hover */
    }

    .upload-text {
        color: #777777;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for RAG control
with st.sidebar:
    st.title("Document Management")
    st.markdown("Upload and manage documents for context.")

    uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"], key="file_uploader")
    
    if uploaded_file is not None:
        if "upload_processed" not in st.session_state or st.session_state.upload_processed != uploaded_file.name:
            # Upload the file to the RAG server
            upload_response = upload_file(uploaded_file)

            if "error" in upload_response:
                st.error(f"File upload failed: {upload_response['error']}")
            else:
                st.success(f"File '{uploaded_file.name}' uploaded successfully!")
                st.session_state.uploaded_file = uploaded_file.name
                st.session_state.messages = []  # Clear messages when a new file is uploaded
                st.session_state.upload_processed = uploaded_file.name # set state
                st.rerun() #important add rerun to fresh
        else:
            st.info("Document already uploaded and processed.")
            st.session_state.uploaded_file = uploaded_file.name

    # Display the name of the currently uploaded file
    if st.session_state.uploaded_file:
        st.write(f"Current document: {st.session_state.uploaded_file}")
    else:
        st.write("No document loaded.")

    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.uploaded_file = None #also clear the uploaded file
        st.session_state.upload_processed = None
        st.rerun() #rerun to update the UI

# Main Chat Interface
chat_container = st.container()

with chat_container:
    if len(st.session_state.messages) == 0:
        # Display welcome message if no conversation
        st.markdown("""
        <div class="welcome-container">
            <div class="welcome-title">Hi, I'm your AI Assistant!</div>
            <div class="welcome-subtitle">Upload a document in the sidebar to get started.  I can answer questions based on the document's content.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Display chat messages
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        for i, (role, content) in enumerate(st.session_state.messages):
            align = "right" if role == "user" else "left"
            st.markdown(f"""
            <div class="message-row {'user-row' if role == 'user' else 'bot-row'}">
                <div class="message-container">
                    <div style="display: flex; align-items: flex-start; justify-content: {align};">
                        <div class="avatar {'user-avatar' if role == 'user' else 'bot-avatar'}">{ 'U' if role == 'user' else 'AI'}</div>
                        <div class="message-content">{content}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)


        # Display typing indicator if the bot is "thinking"
        if st.session_state.thinking:
            st.markdown("""
            <div class="message-row bot-row">
                <div class="message-container">
                    <div style="display: flex;">
                        <div class="avatar bot-avatar">AI</div>
                        <div class="typing-indicator">
                            <div class="typing-dot"></div>
                            <div class="typing-dot"></div>
                            <div class="typing-dot"></div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
# Input area at the bottom
st.markdown("""
<div class="input-area">
    <div class="input-container">
        <div id="input-placeholder"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Place the input widget in the fixed bottom area
with st.container():
    # Create columns for input and button
    cols = st.columns([10, 1])

    # Input field
    with cols[0]:
        user_input = st.text_input(
            "Ask me anything!", # Non-empty label
            key="user_input",
            placeholder="Enter your question...",
            label_visibility="collapsed" # Hiding the label
        )

    # Send button
    with cols[1]:
        send_pressed = st.button("Send", key="send")

# Handle user input
if send_pressed and user_input.strip():
    # Add user message to chat
    st.session_state.messages.append(("user", user_input))

    # Get bot response
    response = get_answer(user_input)

    # Add bot response to chat
    st.session_state.messages.append(("assistant", response))

    # Clear input -  DO NOT clear st.session_state.user_input HERE

    # Rerun to update UI
    st.rerun()

# JavaScript for auto-scroll and textarea resizing
st.markdown("""
<script>
    // This script would handle auto-scrolling and textarea resizing
    // Note: In Streamlit, custom JavaScript has limitations
    // This is a placeholder for the concept
</script>
""", unsafe_allow_html=True)
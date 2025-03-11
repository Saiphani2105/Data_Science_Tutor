import streamlit as st
import uuid
import sqlite3
import hashlib
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import SQLChatMessageHistory
from langchain_core.output_parsers import StrOutputParser

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyAmj1vdjdeO1qWijf5ch6ZjrKuXufz-j2A"
model = ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp", google_api_key=GEMINI_API_KEY)
output_parser = StrOutputParser()

# Database setup
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    user_id TEXT
)
""")
conn.commit()

# Hash function for passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User authentication functions
def register_user(username, password):
    user_id = str(uuid.uuid4())
    hashed_password = hash_password(password)
    try:
        c.execute("INSERT INTO users (username, password, user_id) VALUES (?, ?, ?)", (username, hashed_password, user_id))
        conn.commit()
        return user_id
    except sqlite3.IntegrityError:
        return None  # Username already exists

def authenticate_user(username, password):
    hashed_password = hash_password(password)
    c.execute("SELECT user_id FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = c.fetchone()
    return user[0] if user else None

# Function to create a chat history store for each user
def get_history_store(user_id):
    return SQLChatMessageHistory(connection_string="sqlite:///chat_history.db", session_id=user_id)

# Retrieve past chat history
def get_chat_history(history_store):
    return history_store.messages

# Save chat history
def save_chat(history_store, message, response):
    history_store.add_message(HumanMessage(content=message))
    history_store.add_message(AIMessage(content=response))

# Delete chat history
def clear_chat_history(user_id):
    history_store = get_history_store(user_id)
    history_store.clear()
    st.session_state.messages = []

# Delete selected message
def delete_chat_message(user_id, message_content):
    history_store = get_history_store(user_id)
    messages = history_store.messages
    history_store.clear()
    for msg in messages:
        if msg.content != message_content:
            history_store.add_message(msg)

def chat_with_ai(user_id, message):
    history_store = get_history_store(user_id)
    history = get_chat_history(history_store)
    memory = ConversationBufferMemory()
    for msg in history:
        memory.chat_memory.add_message(msg)
    memory.chat_memory.add_message(HumanMessage(content=message))
    
    response = model.invoke([SystemMessage(content="You are a Data Science Tutor. Answer only data science-related questions. introduce your self as a data science tutor only and give answer less then 500 words")] + memory.chat_memory.messages)
    parsed_response = output_parser.parse(response.content.strip())
    save_chat(history_store, message, parsed_response)
    return parsed_response

# Streamlit UI
st.title("Conversational Data Sience Tutor AI Chatbot")

# User authentication
if "user_id" not in st.session_state:
    login_tab, register_tab = st.tabs(["Login", "Register"])
    
    with login_tab:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            user_id = authenticate_user(username, password)
            if user_id:
                st.session_state.user_id = user_id
                st.session_state.username = username
            else:
                st.error("Invalid username or password.")
    
    with register_tab:
        new_username = st.text_input("New Username", key="reg_user")
        new_password = st.text_input("New Password", type="password", key="reg_pass")
        if st.button("Register"):
            user_id = register_user(new_username, new_password)
            if user_id:
                st.success("Registration successful! Please log in.")
            else:
                st.error("Username already exists.")
else:
    st.write(f"Logged in as: {st.session_state.username}")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Logout"):
            st.session_state.clear()  # Clears session data
            st.rerun()  # Redirects to login
    
    with col2:
        if st.button("Clear Chat"):
            clear_chat_history(st.session_state.user_id)
    
    # Display chat history with delete buttons
    history_store = get_history_store(st.session_state.user_id)
    past_chats = get_chat_history(history_store)
    for chat in past_chats:
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            if isinstance(chat, HumanMessage):
                st.chat_message("user").write(chat.content)
            elif isinstance(chat, AIMessage):
                st.chat_message("assistant").write(chat.content)
        with col2:
            if st.button("🗑️", key=chat.content[:20]):
                delete_chat_message(st.session_state.user_id, chat.content)
    
    # Chat input
    user_input = st.chat_input("Type your message...")
    if user_input:
        st.chat_message("user").write(user_input)
        ai_response = chat_with_ai(st.session_state.user_id, user_input)
        st.chat_message("assistant").write(ai_response)
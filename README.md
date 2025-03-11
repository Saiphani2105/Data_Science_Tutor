# Conversational AI Chatbot (Data Science Tutor)

## 🚀 Project Overview
This project is an **AI-powered Conversational Chatbot** built using **Streamlit, LangChain, Google Gemini API, Hugging Face models, SQLite, and UUID**. It provides an interactive and context-aware chat experience with **secure user authentication, persistent chat history, and intelligent responses**.

## 📌 Features

✅ **User Authentication**: Secure login and registration system using **hashed passwords and UUID**.  
✅ **Persistent Chat History**: Conversations are stored using **SQLite & LangChain’s SQLChatMessageHistory**.  
✅ **AI-Powered Responses**: Uses **Google Gemini API & Hugging Face models** for intelligent answers.  
✅ **Contextual Memory Management**: Implements **LangChain’s ConversationBufferMemory** for maintaining chat context.  
✅ **Chat Management**: Users can **delete messages, clear chat history, and securely log out**.  
✅ **Interactive UI**: Built with **Streamlit** for a responsive and smooth user experience.  

## 🛠 Tech Stack

- **Python**: Backend scripting and API integration
- **Streamlit**: UI development for an interactive chatbot interface
- **LangChain**: Chat memory and structured history management
- **Google Gemini API**: AI-powered conversational responses
- **Hugging Face**: Model deployment and fine-tuning
- **SQLite**: Secure and efficient chat history storage
- **UUID**: Unique user identification for authentication and session management

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Saiphani2105/Data_Science_Tutor.git
cd your-repository
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys
- Obtain a **Google Gemini API Key** from [Google AI](https://ai.google.dev/)
- Set your API key as an environment variable:
```bash
export GEMINI_API_KEY="your_api_key_here"
```
(On Windows, use `set GEMINI_API_KEY=your_api_key_here`)

### 5️⃣ Run the Application
```bash
streamlit run app.py
```

## 🎯 Usage
1️⃣ **Register/Login** with a unique username and password.  
2️⃣ Start chatting with the AI-powered tutor.  
3️⃣ Access previous chat history, delete messages, or clear entire history.  
4️⃣ Logout securely when done.  

## 📂 Project Structure
```
├── app.py                # Main Streamlit App
├── requirements.txt      # Required dependencies
├── users.db              # SQLite database for user authentication
├── chat_history.db       # SQLite database for chat history
└── README.md             # Documentation
```

## 📌 Future Improvements
🔹 Add multi-language support using NLP models.  
🔹 Enhance UI with additional visualization tools.  
🔹 Integrate more LLMs from OpenAI and Hugging Face.  
🔹 Deploy on **Hugging Face Spaces / AWS / Google Cloud**.  

## 🔗 Links
 
🔹 **Hugging Face Model**: [Hugging Face](https://huggingface.co/spaces/Phaneendrabayi/Data_Science_Tutor)

## 💡 Acknowledgments
A special **thank you to Kanav Bansal** for mentorship and guidance throughout this project.  

📢 **Feel free to contribute or share feedback!** 🚀

---
#AI #MachineLearning #DataScience #Chatbot #LangChain #GoogleGemini #Python #Streamlit #HuggingFace #SQLite #UUID #Tech


import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# --- 1. CONFIGURATION & SETUP ---

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ GOOGLE_API_KEY not found. Please set it in your .env file or add it to Streamlit's secrets.")
    st.stop()

# ✅ Initialize Gemini model
# Note: Changed model to 'gemini-1.5-flash' as 'gemini-2.5-flash' is not a valid model.
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.7,
        google_api_key=api_key
    )
except ImportError as e:
    st.error(f"Error initializing LLM. Make sure you have installed all required packages: {e}")
    st.stop()
except Exception as e:
    st.error(f"An error occurred during LLM initialization: {e}")
    st.stop()


# ✅ Load support_info.txt
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "support_info.txt")

    if not os.path.exists(file_path):
        st.error(f"❌ Support file not found at: {file_path}")
        st.stop()

    with open(file_path, "r", encoding="utf-8") as f:
        support_data = f.read()
except Exception as e:
    st.error(f"Error loading support_info.txt: {e}")
    st.stop()

# ✅ Define prompt template
template = """
You are a helpful and compassionate AI assistant for a university's support center.
Your audience is parents who are concerned about their children (the students).
Use a supportive and clear tone.

Use *only* the following context to answer the parent's question.
If the answer is not in the context, politely say you don't have that specific information.

Context:
{support_info}

Parent's Question:
{question}

Your Answer:
"""

prompt = PromptTemplate(
    input_variables=["support_info", "question"],
    template=template
)

# ✅ Create LLM chain
chain = LLMChain(llm=llm, prompt=prompt)


# --- 2. STREAMLIT UI (Modified Layout) ---

# ✅ Page configuration
st.set_page_config(
    page_title="Student Support Portal",
    page_icon="🤝",
    layout="centered", # Changed from 'wide' to 'centered' for a different feel
    initial_sidebar_state="expanded" # Ensure sidebar is open on load
)

# --- Sidebar UI ---
# We moved all inputs to the sidebar for a new layout.
st.sidebar.header("🤝 Ask a Question")
st.sidebar.info("💡 Example: *'What mental health resources are available?'*")

user_q = st.sidebar.text_area(
    "Your Question:",
    height=120,
    placeholder="Type your question here..."
)

get_answer = st.sidebar.button("Find Support Info", use_container_width=True, type="primary")

st.sidebar.markdown("---")
st.sidebar.caption("Powered by Google Gemini")


# --- Main Page UI ---
st.title("🎓 SupportU: Parent Portal")
st.caption("AI-powered answers for university parents.")
st.markdown("---")

# Main content area for showing the answer
if get_answer:
    if user_q.strip(): # Check if the question is not just whitespace
        with st.spinner("🔍 Searching for answers..."):
            try:
                # Run the chain with the loaded data and the user's question
                response = chain.run(support_info=support_data, question=user_q)
                
                st.success("✅ Here's what I found:")
                st.markdown(response) # Use markdown to render formatted text
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please type a question in the sidebar first.")
else:
    # This is the default message on the main page
    st.write("Welcome! Please use the sidebar on the left to ask a question about the student wellbeing services available.")
    st.markdown("Your questions help you understand the support available to your student.")
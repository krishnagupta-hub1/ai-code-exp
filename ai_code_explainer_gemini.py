import streamlit as st
import google.generativeai as genai
import base64

genai.configure(api_key="AIzaSyBP3_R5mYhJJyBgSmTKWzmUYwoyV2LLmeI")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="GenAI Code Assistant", page_icon="💻")

st.markdown("""
    <style>
        .nav-tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .nav-tabs a {
            margin: 0 15px;
            padding: 10px 25px;
            text-decoration: none;
            color: white;
            background-color: #4B8BBE;
            border-radius: 10px;
            font-weight: bold;
        }
        .nav-tabs a.selected {
            background-color: #306998;
        }
    </style>
""", unsafe_allow_html=True)

tab = st.radio("Choose Tool:", ["🧠 Code Explainer", "🛠️ Code Debugger"], horizontal=True, label_visibility="collapsed")

st.markdown(f"""
    <h1 style='text-align: center; color: #4B8BBE;'>{"🧠 GenAI Code Explainer" if tab == "🧠 Code Explainer" else "🛠️ GenAI Code Debugger"}</h1>
    <p style='text-align: center;'>Powered by Gemini · Supports Python, JavaScript, C++, and Java</p>
    <hr style="border: 1px solid #ccc;" />
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("📌 About")
    st.markdown("""
        **This GenAI App Helps You:**
        - 🔍 Understand code in plain English
        - 🛠️ Debug and fix programming errors

        **Languages Supported:**
        - Python
        - JavaScript
        - C++
        - Java

        **Made by:** Krishna Gupta  
        [🌐 GitHub](https://github.com/krishnagupta-hub1/ai-code-exp)
    """)

language = st.selectbox("🔤 Select Programming Language:", ["Python", "JavaScript", "C++", "Java"])
code_input = st.text_area(f"💻 Paste your {language} code here:", height=200)

def get_download_link(text):
    b64 = base64.b64encode(text.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="output.txt">📥 Download Result</a>'

if tab == "🧠 Code Explainer":
    if st.button("✨ Explain Code"):
        if not code_input.strip():
            st.warning("Please paste some code first.")
        else:
            with st.spinner("🧠 Analyzing your code..."):
                prompt = f"Explain the following {language} code in beginner-friendly English:\n\n{code_input}"
                try:
                    response = model.generate_content(prompt)
                    explanation = response.text
                    st.markdown("### 📝 Explanation:")
                    st.success(explanation)
                    st.markdown("### 📄 Your Code:")
                    st.code(code_input, language=language.lower())
                    st.markdown(get_download_link(explanation), unsafe_allow_html=True)
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Error: {e}")

elif tab == "🛠️ Code Debugger":
    if st.button("🛠️ Debug Code"):
        if not code_input.strip():
            st.warning("Please paste some code first.")
        else:
            with st.spinner("🕵️‍♂️ Debugging your code..."):
                prompt = f"Find and explain any possible errors in the following {language} code. Suggest corrections:\n\n{code_input}"
                try:
                    response = model.generate_content(prompt)
                    debug_output = response.text
                    st.markdown("### 🧪 Debugging Report:")
                    st.error(debug_output)
                    st.markdown("### 📄 Your Code:")
                    st.code(code_input, language=language.lower())
                    st.markdown(get_download_link(debug_output), unsafe_allow_html=True)
                    st.snow()
                except Exception as e:
                    st.error(f"❌ Error: {e}")

st.markdown("<hr><center>Made with ❤️ by Krishna Gupta · Powered by Gemini 1.5 · Deployed on Streamlit</center>", unsafe_allow_html=True)

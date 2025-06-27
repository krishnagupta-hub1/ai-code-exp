import streamlit as st
import google.generativeai as genai
import base64

# ===================== CONFIG =====================
genai.configure(api_key="AIzaSyBP3_R5mYhJJyBgSmTKWzmUYwoyV2LLmeI")  # Replace with your actual Gemini API key
model = genai.GenerativeModel("gemini-1.5-flash")

# ===================== CUSTOM STYLING =====================
st.set_page_config(page_title="AI Code Explainer", page_icon="🧠")

st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>🧠 AI Code Explainer</h1>
    <p style='text-align: center;'>Explains Python, JavaScript, C++, and Java using Google's Gemini</p>
    <hr style="border: 1px solid #ccc;" />
""", unsafe_allow_html=True)

# ===================== SIDEBAR =====================
with st.sidebar:
    st.title("📌 About")
    st.markdown("""
        This GenAI project explains code in plain English for beginners.
        
        **Languages Supported:**
        - Python
        - JavaScript
        - C++
        - Java

        **Made by:** Krishna Gupta  
        [🌐 GitHub](https://github.com/krishnagupta-hub1/ai-code-exp)
    """)

# ===================== LANGUAGE & CODE INPUT =====================
language = st.selectbox("🔤 Select Programming Language:", ["Python", "JavaScript", "C++", "Java"])
code_input = st.text_area(f"💻 Paste your {language} code here:", height=200)

# ===================== FUNCTION TO GET DOWNLOAD LINK =====================
def get_download_link(text):
    b64 = base64.b64encode(text.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="explanation.txt">📥 Download Explanation</a>'

# ===================== GENERATE EXPLANATION =====================
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
                # Show highlighted code
                st.markdown("### 📄 Your Code:")
                st.code(code_input, language=language.lower())
                # Show download link
                st.markdown(get_download_link(explanation), unsafe_allow_html=True)
                st.balloons()
            except Exception as e:
                st.error(f"❌ Error: {e}")

# ===================== FOOTER =====================
st.markdown("<hr><center>Made with ❤️ by Krishna Gupta · Powered by Gemini 1.5 · Deployed on Streamlit</center>", unsafe_allow_html=True)

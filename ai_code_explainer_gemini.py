import streamlit as st
import google.generativeai as genai

# 🔐 Set your Gemini API key
genai.configure(api_key="AIzaSyBP3_R5mYhJJyBgSmTKWzmUYwoyV2LLmeI")

# ✅ Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")  # Or "gemini-1.5-pro" if you prefer

# 🎨 Streamlit App UI
st.title("🧠 AI Code Explainer (Multi-Language - Gemini)")
st.markdown("Explain your code in plain English using AI.")

# 🔽 Language selector
language = st.selectbox(
    "Select Programming Language:",
    ["Python", "JavaScript", "C++", "Java"]
)

# 🧾 Code input
code_input = st.text_area(f"Paste your {language} code here:", height=200)

# 🚀 Generate explanation
if st.button("Explain Code"):
    with st.spinner("Analyzing your code..."):
        # 🔥 Custom prompt using selected language
        prompt = f"Explain the following {language} code in beginner-friendly English:\n\n{code_input}"

        try:
            response = model.generate_content(prompt)
            explanation = response.text
            st.markdown("### 📝 Explanation:")
            st.success(explanation)
        except Exception as e:
            st.error(f"❌ Error: {e}")

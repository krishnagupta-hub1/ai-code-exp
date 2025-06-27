import streamlit as st
import google.generativeai as genai

# Set Gemini API key
genai.configure(api_key="AIzaSyBP3_R5mYhJJyBgSmTKWzmUYwoyV2LLmeI")

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title("🧠 AI Code Explainer (with Gemini)")
st.markdown("Explain Python or JavaScript code in plain English.")

# Text area for code input
code_input = st.text_area("Paste your Python or JavaScript code here:", height=200)

# Button to generate explanation
if st.button("Explain Code"):
    with st.spinner("Thinking..."):
        prompt = f"Explain the following code in simple English for a beginner:\n\n{code_input}"

        try:
            response = model.generate_content(prompt)
            explanation = response.text
            st.markdown("### 📝 Explanation:")
            st.success(explanation)
        except Exception as e:
            st.error(f"Error: {e}")

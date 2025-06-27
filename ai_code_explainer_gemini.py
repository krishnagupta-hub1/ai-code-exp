import streamlit as st
import google.generativeai as genai
import base64

# ===================== CONFIG =====================
genai.configure(api_key="AIzaSyBP3_R5mYhJJyBgSmTKWzmUYwoyV2LLmeI")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="GenAI Code Assistant", page_icon="💻")

# ===================== NAVIGATION =====================
tab = st.radio("Choose Tool:", ["🧠 Code Explainer", "🛠️ Code Debugger"], horizontal=True, label_visibility="collapsed")

st.markdown(f"""
    <h1 style='text-align: center; color: #4B8BBE;'>
        {'🧠 GenAI Code Explainer' if tab == '🧠 Code Explainer' else '🛠️ GenAI Code Debugger'}
    </h1>
    <p style='text-align: center;'>Powered by Gemini · Supports Python, JavaScript, C++, and Java</p>
    <hr style="border: 1px solid #ccc;" />
""", unsafe_allow_html=True)

# ===================== SIDEBAR =====================
with st.sidebar:
    st.title("📌 About")
    st.markdown("""
        **Features:**
        - Explain code in plain English
        - Debug and Auto-Fix Code
        - Generate Unit Tests
        - Show Time/Space Complexity
        - Ask AI Assistant Coding Doubts

        **Languages:** Python, JavaScript, C++, Java
        **By:** Krishna Gupta  
        [GitHub](https://github.com/krishnagupta-hub1/ai-code-exp)
    """)

# ===================== INPUTS =====================
language = st.selectbox("🔤 Select Programming Language:", ["Python", "JavaScript", "C++", "Java"])
code_input = st.text_area(f"💻 Paste your {language} code here:", height=200)

def get_download_link(text):
    b64 = base64.b64encode(text.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="output.txt">📥 Download Result</a>'

# ===================== CODE EXPLAINER =====================
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

# ===================== DEBUGGER =====================
elif tab == "🛠️ Code Debugger":
    if st.button("🛠️ Debug Code"):
        if not code_input.strip():
            st.warning("Please paste some code first.")
        else:
            with st.spinner("🕵️‍♂️ Debugging your code..."):
                debug_prompt = f"Find and explain any possible errors in the following {language} code. Suggest corrections:\n\n{code_input}"
                try:
                    response = model.generate_content(debug_prompt)
                    debug_output = response.text
                    st.markdown("### 🧪 Debugging Report:")
                    st.error(debug_output)
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    if st.button("🟢 Auto-Fix Code"):
        with st.spinner("🛠️ Fixing your code..."):
            fix_prompt = f"Fix and return the corrected {language} code. Provide a short explanation of the changes:\n\n{code_input}"
            try:
                response = model.generate_content(fix_prompt)
                fixed_code = response.text
                st.markdown("### ✅ Fixed Code:")
                st.code(fixed_code, language=language.lower())
                st.markdown(get_download_link(fixed_code), unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {e}")

    if st.button("🧪 Generate Unit Tests"):
        with st.spinner("🧪 Generating unit tests..."):
            test_prompt = f"Write unit test cases for the following {language} code:\n\n{code_input}"
            try:
                response = model.generate_content(test_prompt)
                test_code = response.text
                st.markdown("### 🧾 Unit Test Cases:")
                st.code(test_code, language=language.lower())
            except Exception as e:
                st.error(f"❌ Error: {e}")

# ===================== FLOATING COMPLEXITY BAR =====================
st.markdown("""
    <style>
        #complexity-bar {
            position: fixed;
            bottom: 10px;
            right: 10px;
            background-color: #f5f5f5;
            padding: 10px 15px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            font-size: 14px;
        }
    </style>
    <div id="complexity-bar">
        <b>Complexity Info</b><br>
        ⏱ Time: analyzing...<br>
        💾 Space: analyzing...
    </div>
""", unsafe_allow_html=True)

if code_input.strip():
    complexity_prompt = f"Analyze the time and space complexity of the following {language} code:\n\n{code_input}"
    try:
        response = model.generate_content(complexity_prompt)
        complexity_info = response.text.replace("\n", "<br>")
        st.markdown(f"""
            <script>
                document.getElementById('complexity-bar').innerHTML = `<b>Complexity Info</b><br>{complexity_info}`;
            </script>
        """, unsafe_allow_html=True)
    except:
        pass

# ===================== PERSONAL AI ASSISTANT =====================
with st.expander("🤖 Ask Personal AI Assistant"):
    assistant_query = st.text_input("Type your coding doubt or question below:")
    if st.button("Ask AI"):
        if assistant_query.strip():
            try:
                with st.spinner("🤖 Thinking..."):
                    answer = model.generate_content(assistant_query)
                    st.markdown("### 💬 Assistant's Response:")
                    st.info(answer.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")

st.markdown("<hr><center>Made with ❤️ by Krishna Gupta · Powered by Gemini 1.5 · Deployed on Streamlit</center>", unsafe_allow_html=True)

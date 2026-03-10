import streamlit as st
from main import run_crew

# 🎨 Streamlit UI Configuration
st.set_page_config(page_title="Cuda Content Architect", page_icon="🏎️", layout="wide")

st.title("🏎️ Cuda Content Architect")
st.markdown("### Fully Local AI Content Factory Powered by RTX 4050")
st.divider()

# 📝 Input Section
url = st.text_input("🔗 Paste YouTube URL here:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("🚀 Generate Viral Content"):
    if url:
        with st.spinner("🤖 The Agent Squad is thinking... (Check your GPU Task Manager!)"):
            try:
                # Call the function from your main script
                result = run_crew(url)
                
                st.success("✅ Content Generated Successfully!")
                
                # 📊 Display Results
                st.markdown("## 📝 Final Output")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please enter a valid YouTube URL first.")

# 🛠️ Sidebar Info
st.sidebar.title("System Specs")
st.sidebar.info("""
- **LLM:** Llama 3.2 (3B)
- **Engine:** Ollama
- **Hardware:** NVIDIA CUDA
- **Privacy:** 100% Offline
""")
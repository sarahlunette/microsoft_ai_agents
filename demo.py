import streamlit as st
import requests

# FastAPI endpoint URL (replace with your actual URL or ngrok URL if on Colab)
API_URL = "http://localhost:9000/handle_emergency"

st.set_page_config(page_title="Guardian Agent Chatbot", page_icon="🛟")
st.title("🛟 Guardian Agent Chatbot")

with st.form("emergency_form"):
    user_description = st.text_area("📝 Describe your emergency:", height=150)
    perceived_severity = st.selectbox("🚨 How severe is it?", ["", "Level 1", "Level 2", "Level 3", "Critical"])

    submitted = st.form_submit_button("🧠 Ask Guardian Agent")
    if submitted and user_description:
        with st.spinner("Contacting the Guardian Agent..."):
            payload = {
                "user_description": user_description,
                "perceived_severity": perceived_severity
            }
            try:
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()
                data = response.json()

                st.success(f"✅ Category: {data['category']}")
                st.info(f"🧠 LLM Suggestion:\n\n{data['llm_response']}")

                st.markdown("### 🛠️ Proposed Actions")
                for action in data["proposed_actions"]:
                    st.write(f"🔹 {action}")

                st.markdown("### ✅ Executed Actions")
                for result in data["executed"]:
                    st.write(f"✅ {result}")

            except requests.exceptions.RequestException as e:
                st.error(f"❌ Failed to reach the backend: {e}")
    elif submitted:
        st.warning("Please provide a description of the emergency.")

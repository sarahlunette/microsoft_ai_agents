import json
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import yaml

from actions_android import (
    call_911, create_transcript, call_caretaker, activate_video, ask_for_details,
    call_taxi, call_ambulance, request_pharma_uber, call_sos_medecin, locate_pharmacy
)

# Load emergency protocol
with open('home_emergency_protocol_with_agent_actions.json') as f:
    EMERGENCY_PROTOCOL = json.load(f)

# Load API key config (optional)
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)
OPENAI_API_KEY = config.get('api_key')

# Use FastAPI
app = FastAPI(title="Guardian Agent Chatbot (Colab LLM only)")

# Endpoint Input
class EmergencyReport(BaseModel):
    user_description: str
    perceived_severity: str

# Update with your cloudflare Colab URL
COLAB_URL = "https://bridge-furnishings-of-holdings.trycloudflare.com/generate"

@app.post("/handle_emergency")
async def handle_emergency(report: EmergencyReport):
    matched_category = match_emergency_category(report.user_description, report.perceived_severity)
    llm_response = generate_llm_prompt_response(matched_category, report.user_description)
    actions = matched_category.get("agent_actions", [])

    executed_actions = [execute_action(action, report.user_description) for action in actions]

    return {
        "category": matched_category["category"],
        "llm_response": llm_response,
        "proposed_actions": actions,
        "executed": executed_actions
    }

# Category matcher
def match_emergency_category(description: str, severity_hint: str = None) -> dict:
    for category in EMERGENCY_PROTOCOL["categories"]:
        if severity_hint and severity_hint in category["severity"]:
            return category
        if any(example.lower() in description.lower() for example in category["examples"]):
            return category
    return EMERGENCY_PROTOCOL["categories"][0]

# Call the remote Colab model
def generate_llm_prompt_response(category: dict, user_input: str) -> str:
    prompt = f"You are an emergency assistant. Category: {category['category']}. Description: {user_input}. Suggested action?"

    try:
        response = requests.post(COLAB_URL, json={"prompt": prompt})
        if response.status_code == 200:
            return response.json().get("response", "")
        return f"Error from Colab LLM: {response.status_code}"
    except Exception as e:
        return f"Exception while contacting Colab LLM: {str(e)}"

# Execute each predefined action
def execute_action(action: str, description: str) -> str:
    if action == "call_911": return call_911(description)
    if action == "create_transcript_for_911": return create_transcript(description, "911")
    if action == "call_caretaker": return call_caretaker(description)
    if action == "create_transcript_for_caretaker": return create_transcript(description, "caretaker")
    if action == "activate_video": return activate_video()
    if action == "ask_details": return ask_for_details()
    if action == "ask_for_photo_input": return ask_for_details(input_type="photo")
    if action == "call_taxi": return call_taxi()
    if action == "call_ambulance": return call_ambulance()
    if action == "request_pharma_uber": return request_pharma_uber(description)
    if action == "call_sos_medecin": return call_sos_medecin()
    if action == "locate_open_pharmacy": return locate_pharmacy()
    return f"Action '{action}' not recognized."

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("llm_app:app", host="0.0.0.0", port=8000, reload=True)

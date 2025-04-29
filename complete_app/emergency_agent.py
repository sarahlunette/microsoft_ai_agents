import json
import requests

# Load emergency protocol
with open('home_emergency_protocol_with_agent_actions.json') as f:
    EMERGENCY_PROTOCOL = json.load(f)

# Update with your Colab / Cloudflare endpoint
COLAB_URL = "https://recipe-strings-grave-processing.trycloudflare.com/generate"

def match_emergency_category(description: str, severity_hint: str = None) -> dict:
    for category in EMERGENCY_PROTOCOL["categories"]:
        if severity_hint and severity_hint in category["severity"]:
            return category
        if any(example.lower() in description.lower() for example in category["examples"]):
            return category
    return EMERGENCY_PROTOCOL["categories"][0]  # Default fallback

def generate_llm_prompt_response(category: dict, user_input: str) -> str:
    prompt = (
        f"You are an emergency assistant.\n"
        f"Category: {category['category']}\n"
        f"Severity: {category['severity']}\n"
        f"User description: {user_input}\n"
        f"Prompt type: {category.get('llm_prompt_type', '')}\n"
        f"Your task: Decide whether a predefined system action should be executed, or if a chatbot response is more appropriate.\n\n"
        f"If a predefined action is needed, respond in this format:\n"
        f"Action: <one of ['call_911', 'create_transcript', 'create_transcript_for_911', 'create_transcript_for_caretaker', 'call_caretaker', 'activate_video', 'ask_details', 'ask_for_photo_input', 'call_taxi', 'call_ambulance', 'request_pharma_uber', 'call_sos_medecin', 'locate_open_pharmacy', 'sound_alarm', 'unlock_doors', 'notify_emergency_contact']>\n"
        f"Description: <short explanation of why this action is necessary>\n\n"
        f"If no action is needed, respond instead with:\n"
        f"Chatbot Response: <natural language helpful response>\n\n"
        f"Suggested system action?"
    )
    try:
        response = requests.post(COLAB_URL, json={"prompt": prompt})
        if response.status_code == 200:
            return response.json().get("response", "")
        return f"Error from Colab LLM: {response.status_code}"
    except Exception as e:
        return f"Exception while contacting Colab LLM: {str(e)}"

def execute_action(action: str, description: str) -> str:
    try:
        from actions_android import (
            call_911, create_transcript, call_caretaker, activate_video, ask_for_details,
            call_taxi, call_ambulance, request_pharma_uber, call_sos_medecin, locate_pharmacy,
            cancel_action, schedule_followup, send_email_alert, track_delivery,
            alert_nearby_helper, share_location, send_sms
        )
        if action == "call_911": return call_911(description)
        if action == "create_transcript": return create_transcript(description, "general")
        if action == "create_transcript_for_911": return create_transcript(description, "911")
        if action == "create_transcript_for_caretaker": return create_transcript(description, "caretaker")
        if action == "call_caretaker": return call_caretaker(description)
        if action == "activate_video": return activate_video()
        if action == "ask_details": return ask_for_details()
        if action == "ask_for_photo_input": return ask_for_details(input_type="photo")
        if action == "call_taxi": return call_taxi()
        if action == "call_ambulance": return call_ambulance()
        if action == "request_pharma_uber": return request_pharma_uber(description
::contentReference[oaicite:1]{index=1}
 

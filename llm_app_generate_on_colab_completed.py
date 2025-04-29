import json
import whisper
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import requests
import yaml

from actions_android import (
    call_911, create_transcript, call_caretaker, activate_video, ask_for_details,
    call_taxi, call_ambulance, request_pharma_uber, call_sos_medecin, locate_pharmacy,
    sound_alarm, unlock_doors, notify_emergency_contact, lock_doors, call_number
)

# Load emergency protocol
with open('home_emergency_protocol_with_agent_actions.json') as f:
    EMERGENCY_PROTOCOL = json.load(f)

# Load API key config (optional)
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)
OPENAI_API_KEY = config.get('api_key')

# Load Whisper model
whisper_model = whisper.load_model("base")

# Use FastAPI
app = FastAPI(title="Guardian Agent Chatbot (Colab LLM only)")

# Endpoint Input
class EmergencyReport(BaseModel):
    user_description: str
    perceived_severity: str

# Update with your Colab / Cloudflare endpoint
COLAB_URL = "https://recipe-strings-grave-processing.trycloudflare.com/generate"

@app.post("/handle_emergency")
async def handle_emergency(report: EmergencyReport):
    matched_category = match_emergency_category(report.user_description, report.perceived_severity)
    llm_response = generate_llm_prompt_response(matched_category, report.user_description)
    actions = matched_category.get("agent_actions", [])

    executed_actions = [execute_action(action, report.user_description) for action in actions]

    return {
        "category": matched_category["category"],
        "severity": matched_category["severity"],
        "agent_behavior": matched_category.get("agent_behavior", "Calm"),
        "llm_prompt_type": matched_category.get("llm_prompt_type", "Give assistance"),
        "llm_response": llm_response,
        "proposed_actions": actions,
        "executed": executed_actions,
        "escalation": matched_category.get("escalation", ""),
        "response_time": matched_category.get("response_time", "Unknown")
    }

# New endpoint for handling voice input (audio transcription)
@app.post("/handle_voice_input")
async def handle_voice_input(file: UploadFile = File(...)):
    # Save the uploaded audio file
    with open("temp_audio.wav", "wb") as f:
        f.write(await file.read())

    # Transcribe the audio using Whisper
    transcription = transcribe_audio("temp_audio.wav")
    
    # Process the transcription through the existing emergency handler
    return await handle_emergency(EmergencyReport(user_description=transcription, perceived_severity="Unknown"))

# Function to transcribe audio using Whisper
def transcribe_audio(audio_path: str) -> str:
    result = whisper_model.transcribe(audio_path)
    return result["text"]

# Category matcher
def match_emergency_category(description: str, severity_hint: str = None) -> dict:
    for category in EMERGENCY_PROTOCOL["categories"]:
        if severity_hint and severity_hint in category["severity"]:
            return category
        if any(example.lower() in description.lower() for example in category["examples"]):
            return category
    return EMERGENCY_PROTOCOL["categories"][0]  # Default fallback

# Call the remote Colab model
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

# Execute each predefined action
def execute_action(action: str, description: str) -> str:
    try:
        if action == "call_911": return call_911(description)
        if action == "create_transcript": return create_transcript(description)
        if action == "create_transcript_for_911": return create_transcript(description, "911")
        if action == "create_transcript_for_caretaker": return create_transcript(description, "caretaker")
        if action == "call_caretaker": return call_caretaker(description)
        if action == "activate_video": return activate_video()
        if action == "ask_details": return ask_for_details()
        if action == "ask_for_photo_input": return ask_for_details(input_type="photo")
        if action == "call_taxi": return call_taxi()
        if action == "call_ambulance": return call_ambulance()
        if action == "request_pharma_uber": return request_pharma_uber(description)
        if action == "call_sos_medecin": return call_sos_medecin()
        if action == "locate_open_pharmacy": return locate_pharmacy()
        if action == "sound_alarm": return sound_alarm()
        if action == "unlock_doors": return unlock_doors()
        if action == "notify_emergency_contact": return

    except Exception as e:
        return f"Error executing action {action}: {str(e)}"

#TODO: make sure action triggers work
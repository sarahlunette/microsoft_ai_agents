from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import whisper
import json
import yaml
import requests
from emergency_agent import (
    match_emergency_category,
    generate_llm_prompt_response,
    execute_action
)

app = FastAPI(title="Guardian Agent Chatbot (Colab LLM only)")

# Load emergency protocol
with open('home_emergency_protocol_with_agent_actions.json') as f:
    EMERGENCY_PROTOCOL = json.load(f)

# Load API key config (optional)
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)
OPENAI_API_KEY = config.get('api_key')

# Load Whisper model
whisper_model = whisper.load_model("base")

class EmergencyReport(BaseModel):
    user_description: str
    perceived_severity: str

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

@app.post("/handle_voice_input")
async def handle_voice_input(file: UploadFile = File(...)):
    with open("temp_audio.wav", "wb") as f:
        f.write(await file.read())
    transcription = transcribe_audio("temp_audio.wav")
    return await handle_emergency(EmergencyReport(user_description=transcription, perceived_severity="Unknown"))

def transcribe_audio(audio_path: str) -> str:
    result = whisper_model.transcribe(audio_path)
    return result["text"]

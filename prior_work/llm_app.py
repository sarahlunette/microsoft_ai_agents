import json
from typing import List
from fastapi import FastAPI, Request
from pydantic import BaseModel
import random
import uvicorn
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import os
from dotenv import load_dotenv
from actions import (
    call_911, create_transcript, call_caretaker, activate_video, ask_for_details,
    call_taxi, call_ambulance, request_pharma_uber, call_sos_medecin,
    locate_pharmacy
)
#import sys
#sys.path.append('/content/drive/MyDrive/Emergency_hackaton/home_emergency_protocol_with_agent_actions.json')

import yaml

# Load the .yml file
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Extract the variables
OPENAI_API_KEY = config['api_key']

load_dotenv()

USE_LOCAL_LLM = os.getenv("USE_LOCAL_LLM", "false").lower() == "true"

'''
if USE_LOCAL_LLM:
    LOCAL_MODEL_PATH = "/Volumes/TOSHIBA EXT/MLOPS/Emergency/zephyr"
    tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL_PATH, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(LOCAL_MODEL_PATH, device_map="auto", local_files_only=True)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
else:
    import openai
    openai.api_key = OPENAI_API_KEY # os.getenv("OPENAI_API_KEY")'''

LOCAL_MODEL_PATH = "/Volumes/TOSHIBA EXT/MLOPS/Emergency/zephyr"
tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL_PATH, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(LOCAL_MODEL_PATH, device_map="auto", local_files_only=True)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

with open('home_emergency_protocol_with_agent_actions.json') as f:
    EMERGENCY_PROTOCOL = json.load(f)

app = FastAPI(title="Guardian Agent Chatbot")

class EmergencyReport(BaseModel):
    user_description: str
    perceived_severity: str

@app.post("/handle_emergency")
async def handle_emergency(report: EmergencyReport):
    matched_category = match_emergency_category(report.user_description, report.perceived_severity)
    llm_response = generate_llm_prompt_response(matched_category, report.user_description)
    actions = matched_category.get("agent_actions", [])

    executed_actions = []
    for action in actions:
        executed = execute_action(action, report.user_description)
        executed_actions.append(executed)

    return {
        "category": matched_category["category"],
        "llm_response": llm_response,
        "proposed_actions": actions,
        "executed": executed_actions
    }

def match_emergency_category(description: str, severity_hint: str = None) -> dict:
    for category in EMERGENCY_PROTOCOL["categories"]:
        if severity_hint and severity_hint in category["severity"]:
            return category
        if any(example.lower() in description.lower() for example in category["examples"]):
            return category
    return EMERGENCY_PROTOCOL["categories"][0]

def generate_llm_prompt_response(category: dict, user_input: str) -> str:
    prompt = f"You are an emergency assistant. Category: {category['category']}. Description: {user_input}. Suggested action?"
    response = generator(prompt, max_length=100, do_sample=True, temperature=0.7)[0]["generated_text"]
    '''if USE_LOCAL_LLM:
        response = generator(prompt, max_length=100, do_sample=True, temperature=0.7)[0]["generated_text"]
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an emergency support agent."},
                {"role": "user", "content": prompt}
            ]
        )["choices"][0]["message"]["content"]'''
    return response

# TODO: modify when changing to actions_android
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
    uvicorn.run("llm_app:app", host="0.0.0.0", port=8000, reload=True)

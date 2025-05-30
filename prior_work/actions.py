# Add mock or real implementations for your agent actions
def call_911(desc): return f"📞 Called 911 with: {desc}"
def create_transcript(desc, recipient): return f"📝 Transcript for {recipient}: {desc}"
def call_caretaker(desc): return f"📞 Caretaker called with: {desc}"
def activate_video(): return "📹 Video activated."
def ask_for_details(input_type="text"): return f"🗣️ Asking for more {input_type} input."
def call_taxi(): return "🚕 Taxi requested."
def call_ambulance(): return "🚑 Ambulance requested."
def request_pharma_uber(desc): return f"💊 Uber requested to get medicine: {desc}"
def call_sos_medecin(): return "👨‍⚕️ SOS Médecin called."
def locate_pharmacy(): return "📍 Located nearby open pharmacy."

# actions.py

from jnius import autoclass, cast
from android.permissions import request_permissions, Permission

# Request needed permissions
request_permissions([Permission.CALL_PHONE, Permission.INTERNET])

# Android Intent setup
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')


# 🚨 Call emergency number
def call_number(phone_number):
    uri = Uri.parse(f"tel:{phone_number}")
    intent = Intent(Intent.ACTION_CALL, uri)
    current_activity = cast('android.app.Activity', PythonActivity.mActivity)
    current_activity.startActivity(intent)
    return f"📞 Calling {phone_number}..."


def call_911(desc="Emergency"):
    return call_number("911")


def call_caretaker(desc="Assistance needed"):
    caretaker_number = "+1234567890"  # Replace with actual number
    return call_number(caretaker_number)


# 📹 Activate video (placeholder)
def activate_video():
    # Real camera integration would need Android camera API or Kivy Camera widget
    return "📹 Video activated (mock)."


# 🗣️ Ask for more input
def ask_for_details(input_type="text"):
    return f"🗣️ Asking for more {input_type} input."


# 🚕 Request a taxi (mock)
def call_taxi():
    return "🚕 Taxi requested (mock)."


# 🚑 Ambulance request (use real emergency number if needed)
def call_ambulance():
    return call_number("112")  # Europe or change to 911


# 💊 Open Uber for pharmacy delivery
def request_pharma_uber(desc="Get medicine"):
    url = "https://m.uber.com/ul/?action=setPickup&pickup=my_location"
    uri = Uri.parse(url)
    intent = Intent(Intent.ACTION_VIEW, uri)
    current_activity = cast('android.app.Activity', PythonActivity.mActivity)
    current_activity.startActivity(intent)
    return f"💊 Uber ride for pharmacy requested: {desc}"


# 👨‍⚕️ SOS Médecin (France-specific)
def call_sos_medecin():
    return call_number("3624")  # SOS Médecin France


# 📍 Locate pharmacy (mock)
def locate_pharmacy():
    return "📍 Located nearby open pharmacy (mock)."


# 📝 Transcript creation (mock)
def create_transcript(desc, recipient):
    return f"📝 Transcript for {recipient}: {desc}"

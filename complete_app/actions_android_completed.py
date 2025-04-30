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
    return call_number("3624")


# 📍 Locate pharmacy (mock)
def locate_pharmacy():
    return "📍 Located nearby open pharmacy (mock)."


# 📝 Transcript creation (mock)
def create_transcript(desc, recipient):
    return f"📝 Transcript for {recipient}: {desc}"


# 🛑 Cancel operation
def cancel_action(reason="No longer needed"):
    return f"🛑 Action cancelled: {reason}"


# ⏱️ Schedule follow-up
def schedule_followup(desc="Follow-up", time="tomorrow 9am"):
    return f"📅 Follow-up scheduled for {time}: {desc}"


# ✉️ Send email alert (mock)
def send_email_alert(recipient="doctor@example.com", subject="Emergency Alert", body="Need help"):
    return f"✉️ Email alert sent to {recipient}: {subject}"


# 📦 Track medical delivery (mock)
def track_delivery(tracking_number="XYZ123"):
    return f"📦 Tracking delivery: {tracking_number} (mock result)"


# 🔔 Alert nearby helper (mock)
def alert_nearby_helper(helper_name="Neighbor"):
    return f"🔔 Alert sent to nearby helper: {helper_name}"


# 📡 Share live location (mock)
def share_location():
    return "📡 Live location shared (mock)."


# 📲 Send SMS to emergency contact (mock)
def send_sms(contact="+1234567890", message="Help needed!"):
    return f"📲 SMS sent to {contact}: {message}"

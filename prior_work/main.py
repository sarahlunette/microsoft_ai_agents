# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import actions  # Import from actions.py

class EmergencyInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.add_widget(Button(
            text="📞 Call 911",
            font_size=24,
            on_press=lambda instance: print(actions.call_911("Emergency reported"))
        ))

        self.add_widget(Button(
            text="👨‍⚕️ Call SOS Médecin",
            font_size=24,
            on_press=lambda instance: print(actions.call_sos_medecin())
        ))

        self.add_widget(Button(
            text="📞 Call Caretaker",
            font_size=24,
            on_press=lambda instance: print(actions.call_caretaker("Need help"))
        ))

        self.add_widget(Button(
            text="💊 Request Uber for Medicine",
            font_size=24,
            on_press=lambda instance: print(actions.request_pharma_uber("Pharmacy delivery"))
        ))

        self.add_widget(Button(
            text="📹 Activate Video (mock)",
            font_size=24,
            on_press=lambda instance: print(actions.activate_video())
        ))

        self.add_widget(Button(
            text="📍 Locate Pharmacy (mock)",
            font_size=24,
            on_press=lambda instance: print(actions.locate_pharmacy())
        ))


class EmergencyApp(App):
    def build(self):
        return EmergencyInterface()

if __name__ == '__main__':
    EmergencyApp().run()

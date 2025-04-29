from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from threading import Thread
import uvicorn
from api_handler import app as fastapi_app

def run_fastapi():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

class GuardianUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Button(text="🆘 Trigger Emergency (Test)", on_press=self.test_emergency))

    def test_emergency(self, instance):
        from actions_android import call_911
        result = call_911("Test emergency")
        print(result)

class GuardianApp(App):
    def build(self):
        Thread(target=run_fastapi, daemon=True).start()
        return GuardianUI()

if __name__ == "__main__":
    GuardianApp().run()

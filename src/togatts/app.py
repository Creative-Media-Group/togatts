import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import tr
import locale
from gtts import gTTS

platform = toga.platform.current_platform

if platform != "android" and platform != "ios":
    import playsound
    from pathlib import Path
else:
    from android.media import MediaPlayer
    from os.path import dirname, join


class TogaTTS(toga.App):
    def startup(self):
        languages = [
            "english",
            "german",
            "french",
            "spanish",
            "italian",
            "portuguese",
            "dutch",
            "russian",
            "chinese",
            "japanese",
            "korean",
            "arabic",
            "hindi",
            "bengali",
            "turkish",
            "hebrew",
            "polish",
            "swedish",
            "danish",
            "finnish",
            "norwegian",
            "greek",
            "czech",
            "hungarian",
            "romanian",
            "bulgarian",
            "vietnamese",
            "thai",
            "indonesian",
            "malay",
            "swahili",
            "afrikaans",
        ]
        self.lang = locale.getlocale()[0]
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        main_box = toga.Box()
        self.text = toga.MultilineTextInput(
            placeholder=tr(
                csv_file=self.file, target_key="TEXTPLACEHOLDER", langcode=self.lang
            ),
            style=Pack(padding=10, flex=1),
        )
        self.select_lang = toga.Selection(
            items=languages, style=Pack(padding=10, flex=1)
        )
        speak_button = toga.Button(
            text=tr(csv_file=self.file, target_key="SPEAKBUTTON", langcode=self.lang),
            style=Pack(padding=10, flex=1),
            on_press=lambda _: self.speak(text=self.text.value),
        )
        save_button = toga.Button(
            text=tr(csv_file=self.file, target_key="SAVEBUTTON", langcode=self.lang),
            style=Pack(padding=10, flex=1),
            on_press=lambda _: self.save(text=self.text.value),
        )
        main_box.add(self.text)
        main_box.add(self.select_lang)
        main_box.add(speak_button)
        main_box.add(save_button)
        main_box.style.direction = "column"
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def speak(self, text):
        path = f"{self.paths.app.absolute()}/resources/"
        if platform != "android" and platform != "ios":
            sound = path
            playsound.playsound(sound=sound)
        else:
            player = MediaPlayer()
            sound = path  # "resources/happy-birthday-whistled.wav"
            player.setDataSource(sound)
            player.prepare()
            player.start()

    def save(self, text):
        engine = pyttsx3.init()
        engine.save_to_file(text=text, filename=f"{self.text.value}.mp3")
        engine.runAndWait()


def main():
    return TogaTTS()

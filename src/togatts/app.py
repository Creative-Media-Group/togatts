import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import tr
import locale
import pyttsx3

lang = locale.getlocale()[0]
engine = pyttsx3.init()
voicelanglist = engine.getProperty("voices")
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
# print(voicelanglist)
# for voice in voicelanglist:
#    for language in languages:
#        if language in voice.name.lower():
#            print(language)
#            engine.setProperty("voice", voice.id)
#            print(voice.id)
#            break


class TogaTTS(toga.App):
    def startup(self):
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        main_box = toga.Box()
        self.text = toga.TextInput(
            placeholder=tr(
                csv_file=self.file, target_key="TEXTPLACEHOLDER", langcode=lang
            ),
            style=Pack(padding=10, flex=1),
        )
        self.select_lang = toga.Selection(
            items=languages, style=Pack(padding=10, flex=1)
        )
        speak_button = toga.Button(
            text=tr(csv_file=self.file, target_key="SPEAKBUTTON", langcode=lang),
            style=Pack(padding=10, flex=1),
            on_press=self.speak,
        )
        main_box.add(self.text)
        main_box.add(self.select_lang)
        main_box.add(speak_button)
        main_box.style.direction = "column"
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def speak(self, widget):
        for voice in voicelanglist:
            if self.select_lang.value in voice.name.lower():
                engine.setProperty("voice", voice.id)
                print(voice.id)
        engine.say(self.text.value)
        engine.runAndWait()


def main():
    return TogaTTS()

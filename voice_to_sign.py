import speech_recognition as sr
import tkinter as tk
from PIL import Image, ImageTk
import os
import string
import threading
from easygui import buttonbox

# ---------------- PATH BASE ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# phrases that have GIFs
isl_gif = [
    'address','ahmedabad','all','any questions','are you angry','are you busy','are you hungry','assam','august', 'banana',
    'banaras','banglore','be careful','bridge','cat','christmas','church','clinic', 'dasara','december','did you finish homework',
    'do you have money','do you want something to drink', 'do you watch TV','dont worry','flower is beautiful','good afternoon',
    'good morning','good question', 'grapes','hello','hindu','hyderabad','i am a clerk','i am fine','i am sorry','i am thinking',
    'i am tired', 'i go to a theatre','i had to say something but i forgot','i like pink colour','i love to shop', 'job','july',
    'june','karnataka','kerala','krishna', 'lets go for lunch','mango','may','mile','mumbai','nagpur','nice to meet you', 'open the door',
    'pakistan','please call me later','please wait for sometime', 'police station','post office','pune','punjab','saturday','shall I help you',
    'shall we go together tommorow','shop','sign language interpreter','sit down','stand up', 'take care','temple','there was traffic jam',
    'thursday','toilet', 'tomato','tuesday','usa','village','wednesday', 'what are you doing','what is the problem',"what is today's date", 
    'what is your father do','what is your mobile number','what is your name','whats up', 'where is the bathroom','where is the police station','you are wrong' 
]

letters = list(string.ascii_lowercase)


# ---------------- MAIN UI CLASS ----------------
class VoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice to Sign")

        # window size
        self.root.geometry("600x600")
        self.root.minsize(500, 500)

        self.label = tk.Label(root, text="Click Start and Speak", font=("Arial", 16))
        self.label.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(expand=True)

        self.start_btn = tk.Button(root, text="Start Listening", command=self.start_thread)
        self.start_btn.pack(pady=10)

        self.frames = []
        self.running = False

    # ---------------- THREAD START ----------------
    def start_thread(self):
        thread = threading.Thread(target=self.listen)
        thread.daemon = True
        thread.start()

    # ---------------- SAFE UI UPDATE ----------------
    def update_label(self, text):
        self.root.after(0, lambda: self.label.config(text=text))

    # ---------------- SHOW IMAGE ----------------
    def show_image(self, path):
        try:
            img = Image.open(path)
            img = img.resize((400, 400))
            photo = ImageTk.PhotoImage(img)

            self.image_label.config(image=photo)
            self.image_label.image = photo  # keep reference
        except Exception as e:
            print("Image error:", e)

    # ---------------- PLAY GIF ----------------
    def play_gif(self, path):
        try:
            im = Image.open(path)
            self.frames = []

            while True:
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(len(self.frames))
        except EOFError:
            pass
        except Exception as e:
            print("GIF error:", e)
            return

        self.running = True
        self.update_gif(0)

    def update_gif(self, ind):
        if not self.running or not self.frames:
            return

        frame = self.frames[ind]
        self.image_label.config(image=frame)
        self.image_label.image = frame

        self.root.after(100, self.update_gif, (ind + 1) % len(self.frames))

    # ---------------- LISTEN ----------------
    def listen(self):
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                self.update_label("Listening...")
                audio = r.listen(source)

            text = r.recognize_google(audio).lower()

            for c in string.punctuation:
                text = text.replace(c, "")

            self.update_label(f"You said: {text}")

            self.running = False  # stop previous gif

            # GIF case
            if text in isl_gif:
                path = os.path.join(BASE_DIR, 'assets', 'Gifs', f'{text}.gif')
                if os.path.exists(path):
                    self.root.after(0, lambda: self.play_gif(path))
                else:
                    print("GIF not found:", path)

            # Alphabet fallback
            else:
                self.show_alphabets(text)

        except sr.UnknownValueError:
            self.update_label("Could not understand")
        except Exception as e:
            print("Error:", e)
            self.update_label("Error occurred")

    # ---------------- SHOW LETTERS ----------------
    def show_alphabets(self, text):
        chars = [c for c in text if c in letters]

        def show_next(index):
            if index >= len(chars):
                return

            ch = chars[index]
            path = os.path.join(BASE_DIR, 'assets', 'asl_alphabets', f'{ch}.jpeg')

            if os.path.exists(path):
                self.show_image(path)

            self.root.after(700, show_next, index + 1)

        self.root.after(0, show_next, 0)


# ---------------- FUNCTION CALLED FROM app.py ----------------
def voice_to_sign():
    while True:
        image = "assets/voicetosign.png"
        msg = "Voice to Gesture"
        choices = ["Start", "Back"]

        reply = buttonbox(msg, image=image, choices=choices)

        if reply == "Start":
            root = tk.Tk()
            app = VoiceApp(root)
            root.mainloop()
        else:
            break
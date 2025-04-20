import queue, json, pyttsx3, datetime
from vosk import Model, KaldiRecognizer
import sounddevice as sd
model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)
audio = queue.Queue()
engine = pyttsx3.init()

def callback(indata, frames, time, status):
    if status: print(status)
    audio.put(bytes(indata))

def proccessQuery(query):
    query = query.lower()
    if "time" in query:
        now = datetime.datetime.now().strftime("%H,%M")
        response = "The current time is", now
    elif "date" in query:
        day = datetime.datetime.now().strftime("%B, %d, %Y")
    else:
        response = "I'm sorry, I didn't understand that."
    return response

with sd.RawInputStream(samplerate=16000):
    print("uh oh")
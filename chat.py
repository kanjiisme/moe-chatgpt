import openai
import os
from dotenv import load_dotenv
from googletrans import Translator
import pyaudio
import speaker
import utils

traslator = Translator()

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

def get_messages(input):    
  openai.api_key = os.getenv("OPENAI_API_KEY")

  output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "assistant", "content": input}
      ]
  )

  message : str = output["choices"][0]["message"]["content"]

  return message

def run_audio(rate, data):
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, output=True)
  stream.write(data)
  stream.stop_stream()
  stream.close()
  p.terminate()

def to_speak(message):
  audio_line = []
  for sentence in utils.clean_text(message):
    rate, data = speaker.to_speak(traslator.translate(sentence, "ja").text, 1)
    audio_line.append((rate, data))
  return audio_line
while True:
  used_input = input("You: ")

  messages = get_messages(used_input)

  audio_line = to_speak(messages)

  print("=========ChatGPT==========")
  print(messages)
  print("==========================")

  for rate, data in audio_line:
    run_audio(rate, data)





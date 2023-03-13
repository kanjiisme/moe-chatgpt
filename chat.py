import time
import openai
import os
from dotenv import load_dotenv
from googletrans import Translator
import pyaudio
import speaker
import utils
from src.moettsapi import MoeTTSAPI
from argparse import ArgumentParser
from modules.models import SynthesizerTrn
traslator = Translator()



def get_messages(input):    
  

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

def to_speak(model : SynthesizerTrn, message : str):
  audio_line = []
  for sentence in utils.clean_text(message):
    rate, data = speaker.to_speak(model, traslator.translate(sentence, "ja").text, 1)
    audio_line.append((rate, data))
  return audio_line

def api_to_speak(api : MoeTTSAPI, message : str):
  audio_line = []
  for sentence in utils.clean_text(message):
    rate, data = api.text_to_speech(traslator.translate(sentence, "ja").text, 1)
    audio_line.append((rate, data))
  return audio_line

def argument_parse():
    parser = ArgumentParser()
    # parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument('--apiurl', type=str, default=None, help="The path to the server moe-tts.") 
    parser.add_argument('--openaikey', type=str, default=None, help="You OpenAI API key.") 
    args = parser.parse_args()

    return args

def main():
  
  args = argument_parse()

  if args.apiurl == "" or args.apiurl is None:
    model = SynthesizerTrn.from_pre_trained("model")
  else:
    print(f"Using api: {args.apiurl}")
    api = MoeTTSAPI(args.apiurl)

  if args.openaikey == "" or args.openaikey is None:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    openai.api_key = os.getenv("OPENAI_API_KEY")
  else:
    openai.api_key = args.openaikey

  while True:
    used_input = input("You: ")

    messages = get_messages(used_input)

    if args.apiurl == "" or args.apiurl is None:
      audio_line = to_speak(model, messages)
    else:
      audio_line = api_to_speak(api, messages)

    print("=========ChatGPT==========")
    print(messages)
    print("==========================")

    for rate, data in audio_line:
      run_audio(rate, data)
      time.sleep(0.1)

if __name__ == "__main__":
  main()





# A Command line application Chat GPT version for weebs :v.
## Download TTS model:
Origin:

- VITS : [Francis-Komizu](https://github.com/Francis-Komizu/VITS)

or in Huggingface 🤗 for Google Colab:
```bash
!wget "https://huggingface.co/Ojimi/moe-tts-model/resolve/main/model1.zip" -O "/content/model1.zip"
!unzip "/content/model1.zip" -d "/content/moe-chatgpt/"
```

## Used:
- Let's create a .env file in your directory. It is used to store your API key from https://platform.openai.com/.
- Install requirements:
```bash
pip install -r requirements.txt
```
- Run:
```bash
python chat.py
```
- Enjoy =)))

## Model structure:

+ model/
- - model.pth
- - config.json (.yaml)
- - info.json (.yaml) (Options)
- - cover.jpg (Options)

## Credits:
- VITS : [Francis-Komizu](https://github.com/Francis-Komizu/VITS)
- OpenAI: ChatGPT.
- You 🫵.
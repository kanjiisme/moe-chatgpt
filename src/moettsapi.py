import requests
import base64

class MoeTTSAPI:
    def __init__(self, url) -> None:
        self.url = url

    def text_to_speech(self, text : str, speed : float = 1, speaker_id : int = 0, using_symbols : bool = False):
        response = requests.post(f"{self.url}/run/generation", json={
        "data": [
            text,
            speed,
            speaker_id,
            using_symbols,
        ]
        }).json()

        data = response["data"]

        audio_data_base64 = data[1]
        audio_data_base64 = audio_data_base64.split(",")[1]
        audio_data = base64.decodebytes(audio_data_base64.encode())

        return int(data[0]), audio_data

    def load_model(self, model_name : str):
        response = requests.post(f"{self.url}/run/load_model", json={
            "data": [
                model_name,
            ]
        }).json()
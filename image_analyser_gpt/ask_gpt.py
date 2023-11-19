import requests

from image_analyser_gpt.utils import compose_payload

def simple_prompt(image, prompt: str, api_key: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        payload = compose_payload(image=image, prompt=prompt)
        response = requests.post("https://api.openai.com/v1/chat/completions",
                                 headers=headers, json=payload).json()

        gpt_answer=response['choices'][0]['message']['content']
        return gpt_answer
# import cv2
import base64
import numpy as np
from io import BytesIO
buffered = BytesIO()

def encode_image_to_base64(image) -> str:
    """
     @brief Encodes an image to a base64 encoded string. This is a convenience function for the use of : func : ` ~scikit - learn. image. Image. save ` and : func : ` ~scikit - learn. image. Image. read ` to decode the image to a base64 encoded string.
     @param image A PIL image representing the image to be encoded.
     @return A base64 - encoded string representing the image in JPEG format. Example usage. code - block ::
    """
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    # img_str = base64.b64encode(image).decode('utf-8')
    return img_str


def compose_payload(image, prompt: str) -> dict:
    """
     @brief Composes a payload dictionary for the GPT - 4 Vision model including a base64 encoded image and a text prompt for the GPT - 4 Vision model.
     @param image The image to be used as the payload.
     @param prompt The prompt text to accompany the image in the payload.
     @return A dictionary structured as a payload for the GPT - 4 Vision model including a base64 encoded image
    """
    base64_image = encode_image_to_base64(image)
    return {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }
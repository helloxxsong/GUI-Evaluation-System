import base64
import requests

# OpenAI API Key
api_key = "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"


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def single_image(image_path):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image?"
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

    for count in range(5):
        try:
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=40)
            return response.json()
        except requests.exceptions.Timeout:
            print(f"请求超时，正在重试...（{count + 1} / {5}）")
            continue
        except requests.exceptions.RequestException as e:
            print(f"请求遇到错误：{e}")
            break
    return None

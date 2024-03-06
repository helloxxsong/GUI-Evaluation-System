from openai import OpenAI

client = OpenAI(
    api_key=""
)


def get_vision_completion(user_prompt, image_url):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{user_prompt}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"{image_url}",
                        },
                    },
                ],
            }
        ],
        max_tokens=1000,
    )

    return response.choices[0].message.content


def get_visions_completion(user_prompt, image_url1, image_url2):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{user_prompt}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"{image_url1}",
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"{image_url2}",
                        },
                    },
                ],
            }
        ],
        max_tokens=1000,
    )

    return response.choices[0].message.content

from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key=""
)


def get_vision_completion(user_prompt, image_url):
    response = client.chat.completions.create(
        model="glm-4v",  # 填写需要调用的模型名称
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
                            "url": f"{image_url}"
                        }
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content


def get_visions_completion(user_prompt, image_url1, image_url2):
    response = client.chat.completions.create(
        model="glm-4v",  # 填写需要调用的模型名称
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
                            "url": f"{image_url1}"
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"{image_url2}"
                        }
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content

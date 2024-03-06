import GPT4V
import GLM4V
import GPT4V_local

with open('./system_prompt.txt', 'r', encoding='utf-8') as file:
    prompt = file.read()

easy_prompt = "Play the role of a test user of a mobile phone GUI interface. Describe the GUI elements in the given interface and briefly evaluate usability"

url_1 = 'https://img2.imgtp.com/2024/03/05/SJlGo5tx.png'  # 原图
url_2 = ''  # 预测
url_3 = 'https://img2.imgtp.com/2024/03/05/bjQw2bnh.png'  # 真人
image_path1 = './image/cropped_ui_screenshots/apple_1.png'
image_path2 = ''
image_path3 = './image/merged/apple_1.png'

if __name__ == "__main__":
    # print(GPT4V.get_vision_completion(user_prompt=easy_prompt, image_url=url_1))
    # print(GLM4V.get_vision_completion(user_prompt=easy_prompt, image_url=url_1))
    # print(GPT4V_local.single_image(prompt=easy_prompt, image_path="./image/cropped_ui_screenshots/apple_1.png"))
    # print(GPT4V.get_visions_completion(user_prompt=prompt, image_url1=url_1, image_url2=url_3))
    # print(GLM4V.get_visions_completion(user_prompt=prompt, image_url1=url_1, image_url2=url_3))
    print(GPT4V_local.double_images(prompt=prompt, image_path1=image_path1, image_path2=image_path3))

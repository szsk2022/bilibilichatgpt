import requests
import openai
import time
import urllib3
import warnings
warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)

openai.api_key = "YOUR OPENAI KEY"

def get_comments(room_id):
    url = f"https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid={room_id}"
    response = requests.get(url)
    data = response.json()
    comments = data["data"]["room"]
    return comments

def reply_comment(comment):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"User: {comment}\nAI:",
        max_tokens=50,
        temperature=0.9,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None
    )
    reply = response.choices[0].text.strip()
    return reply

room_id = YOUR ROOM ID
history_file = "1.txt"
processed_comments = set()

# 加载历史弹幕
with open(history_file, "r", encoding="utf-8") as f:
    for line in f:
        processed_comments.add(line.strip())

while True:
    try:
        comments = get_comments(room_id)
        new_comments = [comment for comment in comments if comment["text"] not in processed_comments]

        with open(history_file, "a", encoding="utf-8") as f:
            for comment in new_comments:
                content = comment["text"]
                f.write(f"{content}\n")
                processed_comments.add(content)

                reply = reply_comment(content)
                print(f"观众: {content}")
                if "ai" in content.lower():
                    print(f"ChatGPT3.5: {reply}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    time.sleep(3)

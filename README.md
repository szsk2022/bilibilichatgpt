# 哔哩哔哩GPT直播助手
> 一个可以让您在bilibili直播中对接ChatGPT3的一个项目

## 一、开始
> 请确保您已经安装Python3

1. 请访问[OpenAI密钥](https://platform.openai.com/acc "OpenAI密钥")获取页面，新建一个Key
2. 打开源码，找到”openai.api_key = "YOUR OPENAI KEY"“，将”YOUR OPENAI KEY“替换为您的刚刚新建的Key；注意，双引号请不要删除！
3. 在源码中找到”room_id = YOUR ROOM ID“，”YOUR ROOM ID“替换为您的[哔哩哔哩房间号](https://link.bilibili.com/#/my-room/start-live "哔哩哔哩房间号")
4. 在项目根目录下新建一个名为”1.txt“的一个记事本文件；注意：您每次直播结束后需要清空文件里的内容，否则已保存的弹幕信息将不会打印和提问GPT！
5. 打开终端，安装相关库，这里就不写了。
6. 打开终端，进入项目根目录，执行python chatgpt直播.py，即可运行！注意要配置代理！

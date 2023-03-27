# OpenAI-Discord-ChatBot
A simple Discord chat bot uses OpenAI's GPT-3.5-turbo API instead of web crawling

# Installation
**Python 3.8 or higher is required for this bot**\
\
Install Discord python package
```bash
pip install discord
```
Install OpenAI python package
```bash
pip install openai
```

# Setup
Paste your Discordtoken in main.py file
```py
#CONFIG'
TOKEN = 'YOUR-DISCORD-TOKEN-HERE'  ####TYPE YOUR DISCORD TOKEN HERE####
intents = discord.Intents.all()```
```
Paste your OpenAI token in openai_response.py
```py
openai.api_key = 'YOUR-OPENAI-TOKEN-HERE'  ####TYPE YOUR OPENAI TOKEN HERE####
```

# Features
* This bot is using OpenAI's API instead of web crawling ChatGPT website. Which has higher availability and faster response time
* You can set a system message for AI. The picture below is using the system message to make bot acting like a neko
![image](https://user-images.githubusercontent.com/44529370/227820994-4c3cac70-592b-4634-a82f-65fe27ec7ded.png)

# Todo List :white_check_mark:
* Add support for serverless hosting solution
* Increase the continuity of conversations

import os
import openai
import json

openai.api_key = ''  ####TYPE YOUR OPENAI TOKEN HERE####

SYS_response = "You're a AI assistance. The assistant is friendly and helpful" #Default instructions
AI_response = ["",""]
U_response = ["",""]

def response(user_response):
    startup=int(os.environ["STARTUP"])
    U_response.insert(0, user_response)
    if startup == 0:
        reply = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYS_response},
                {"role": "user", "content": U_response[0]},
            ]
        )
        os.environ["STARTUP"] = "1"
    if startup == 1:
        reply = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYS_response},
                {"role": "assistant", "content": AI_response[1]},
                {"role": "user", "content": U_response[1]},
                {"role": "assistant", "content": AI_response[0]},
                {"role": "user", "content": U_response[0]}
            ]
        )
    json_obj = json.loads(json.dumps(reply))
    reply = json_obj['choices'][0]['message']['content']
    print(reply)
    AI_response.insert(0,reply)
    return reply

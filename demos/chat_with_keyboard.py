import openai

"""
have chats with stright from your PC
"""


CHAT =  [{"role": "system", "content": "You are a helpful assistant. You can make question to make the conversation entertaining."}]

# Set your openai api key
openai.api_key = ''

while True:
    try:
        question = input('[user]: ')
        CHAT.append({"role":"user","content":f"{str(question)}"})
        API_response = openai.ChatCompletion.create(
                    model='gpt-3.5-turbo',
                    messages=CHAT)
                
        answer = API_response['choices'][0]['message']['content']
        print(f"[assistant]: {answer}")

        CHAT.append({"role":"assistant","content":f"{answer}"})
    except Exception as e:
        print(e)
        quit()
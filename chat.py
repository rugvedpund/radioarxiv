import os
import openai

openai.my_api_key = os.getenv('OPENAI_API_KEY')

import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

class PhY:
    '''
    PhY is a intelligent assistant.
    
    init: self.messages (list)
    add_user_message: message (str)
    get_reply: return reply (str)
    
    '''
    def __init__(self):
        self.messages = [{"role": "system", "content": "You are an intelligent assistant."}]
        self.reply = ""
    
    def add_user_message(self, message):
        self.messages.append({"role": "user", "content": message})
    
    def get_reply(self):
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.reply = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": self.reply})
        return self.reply

if __name__ == '__main__':
    phy = PhY()
    
    while True:
        user_message = input("User: ")
        if user_message:
            phy.add_user_message(user_message)
            reply = phy.get_reply()
            print(f"ChatGPT: {reply}")

        more_questions = input("Do you have questions? (yes/no): ")
        if more_questions.lower() != "yes":
            break

import os
import openai

openai.my_api_key = os.getenv('OPENAI_API_KEY')

class PhY:
    '''
    PhY is a intelligent assistant.
    
    init: message (str)
    get_reply: return reply (str)
    
    '''
    def __init__(self, message):
        self.message = message
        self.messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
        self.messages.append(
            {"role": "user", "content": self.message},)
        self.chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages)
        self.reply = self.chat.choices[0].message.content    
        self.messages.append({"role": "assistant", "content": self.reply})

    def get_reply(self):
        return self.reply

if __name__ == '__main__':
    message = input("User : ")
    if message:
        chat = PhY(message)
        reply = chat.get_reply()
        print(f"ChatGPT: {reply}")
        
        
   
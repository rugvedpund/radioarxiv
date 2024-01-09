## I want to pass the message from rss.py to chat.py and get the reply from chat.py printed in the terminal.

from chat import PhY
from rss_test import ArxivFeed

# model = PhY("What is the sine of pi/2.")
# print(model.get_reply())

papers = ArxivFeed().items
question = "Summarize the following:"
model = PhY()
for paper in papers:
    title = paper.title.text 
    description = paper.description.text
    model.add_user_message(question+title)
    print(model.get_reply())
    
    

# print("Title: ", papers[0].title.text)
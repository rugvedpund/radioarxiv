import openai
import os
from rss import ArxivFeed

items=ArxivFeed().get_items()
print(items)
openai.api_key = os.getenv("OPENAI_API_KEY")

for item in items[:3]:
	print(item.description.text)
	# response = openai.ChatCompletion.create(
	#   model="gpt-3.5-turbo",
	#   messages=[
	#     {
	#       "role": "system",
	#       "content": "You are an expert physicist assistant"
	#     },
	#     {
	#       "role": "user",
	#       "content": f"Summarize this paper: {item.description.text}"
	#     }
	#   ],
	#   temperature=1,
	#   max_tokens=256,
	#   top_p=1,
	#   frequency_penalty=0,
	#   presence_penalty=0
	# )

	# print(response)

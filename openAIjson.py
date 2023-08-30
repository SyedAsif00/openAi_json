import openai
from config import API_KEY
from query import query


api_key = API_KEY

query = query
openai.api_key = api_key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"extract info from this in the form of json:\n{query}"}
    ]
)

extracted_info = response['choices'][0]['message']['content'].strip()

print(extracted_info)

import openai

api_key = "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"
openai.api_key = api_key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "hey gpt what was the reason for the ottoman empire decline"}
    ]
)

extracted_info = response['choices'][0]['message']['content'].strip()

print(extracted_info)

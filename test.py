from google import genai

client = genai.Client(api_key = "AIzaSyBSvOZV14MKSH1RMabGgHaiNBsVT9uD8j0") #AIzaSyBSvOZV14MKSH1RMabGgHaiNBsVT9uD8j0 = api key

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "Illia vs Islam give me ur opinion with percentages"
        )
print(response.text)
















'''from ai21 import AI21Client
from ai21.models.chat import ChatMessage

messages = [
    ChatMessage(role="user", content="Hello how are you?"),
]

#0b8015db-eda7-4568-9083-ae44e05308e3 = api key lil bro
client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-large",
    max_tokens=1024,
)
print(response[0]) '''
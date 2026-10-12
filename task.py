from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chat = client.chats.create(
    model="gemini-3.8-flash"
)

print("Gemini Chatbot Started!")
print("Type 'end' to stop.\n")

# Chatbot loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "end":
        print("Chatbot stopped!")
        break

    response = chat.send_message(user_input)

    print(f"Gemini:, {response.text}\n")
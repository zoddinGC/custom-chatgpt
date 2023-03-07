from dotenv import load_dotenv
import openai
import os
import pandas as pd


load_dotenv()
openai.api_key = os.getenv("API_KEY")

class ChatBot():
    def __init__(self) -> None:
        self.messages = []
    

    def load_knowledge(self, *dropdown_choice):
        self.messages = []

        dropdown_choice = "".join(dropdown_choice)

        knowledge_data = pd.read_excel(dropdown_choice, usecols="A:B")

        if knowledge_data.shape[0] > 0:
            for row in range(knowledge_data.shape[0]):
                self.messages.append({
                    "role":knowledge_data["role"][row],
                    "content":knowledge_data["content"][row]
                })


    def __generate_response(self, user_input:str):
        # Set up OpenAI API credentials from .env file
        self.messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0.2
        )

        message = response.choices[0].message.content.strip()
        self.messages.append({"role":"assistant", "content": message})

        return message


    def chatbot(self, user_input:str) -> str:
        response = self.__generate_response(user_input)

        while True:
            try:
                isinstance(response, str)
                break
            except:
                continue

        return response

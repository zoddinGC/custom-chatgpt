from os import getenv
from dotenv import load_dotenv
import openai
import pandas as pd


load_dotenv()
openai.api_key = getenv("API_KEY")

class ChatBot():
    def __init__(self) -> None:
        self.messages = []


    def load_knowledge(self, dropdown_choice:str):
        self.messages = []

        knowledge_data = pd.read_excel(dropdown_choice, usecols="A:B")

        if knowledge_data.shape[0] > 0:
            for row in range(knowledge_data.shape[0]):
                if knowledge_data["role"][row] not in ["user", "assistant", "system"]:
                    self.messages = "Error 007"
                    break

                self.messages.append({
                    "role":knowledge_data["role"][row],
                    "content":knowledge_data["content"][row]
                })


    def __generate_response(self, user_input:str):
        if self.messages == "Error 007":
            return self.messages
        
        # Set up OpenAI API credentials from .env file
        self.messages.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                temperature=0.2
            )

            message = response.choices[0].message.content.strip()
            self.messages.append({"role":"assistant", "content": message})
        except:
            message = "ATENÇÃO: Esta NÃO é uma mensagem do ChatGPT. Ocorreu um erro."

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

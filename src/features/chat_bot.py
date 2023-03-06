from dotenv import load_dotenv
import openai
import os


load_dotenv()
openai.api_key = os.getenv("API_KEY")

class ChatBot():
    def __init__(self) -> None:
        self.messages = [
            {"role": "system",
            "content": "You are a helpful assistant."}, 
        ]
        

    # Define a function to generate a response from the model
    def __generate_response(self, prompt):
        # Set up OpenAI API credentials from .env file

        self.messages.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0.2
        )

        message = response.choices[0].message.content
        self.messages.append({"role":"assistant", "content": message})

        return message


    # Define a function to run the chatbot
    def chatbot(self, user_input):
        response = self.__generate_response(user_input)

        while True:
            try:
                isinstance(response, str)
                break
            except:
                continue

        return response

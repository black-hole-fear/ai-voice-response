from openai import OpenAI
import os
from dotenv import load_dotenv
from openai._types import NotGiven


class DialogueManagement:
    def __init__(self):
        load_dotenv()
        self.language = os.environ.get("LANGUAGE")
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.dialogue =[]

    def add_dialogue(self, role, text):
        if role == 'system':
            text += f' You must reply in **{self.language}**'

        self.dialogue.append({"role": role, "content": text})

    def add_function(self, role, content, tool_call_id, name):
        self.dialogue.append({"role": role, "content": content, "name": name, "tool_call_id": tool_call_id})

    def clear(self):
        self.dialogue = []

    def chat_completion(self, function=NotGiven(), tool_choice=NotGiven()):
        return self.client.chat.completions.create(
            messages=self.dialogue,
            model="gpt-3.5-turbo",
            tools=function,
            tool_choice=tool_choice
        )

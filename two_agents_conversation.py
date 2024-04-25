# Initalization of the OpenAI API
from dotenv import load_dotenv
import os


load_dotenv()

from autogen import ConversableAgent

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config={
        "config_list": [
            {
                "model": "gpt-3.5-turbo",
                "temperature": 0.9,
                "api_key": os.environ.get("api_key"),
            }
        ]
    },
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={
        "config_list": [
            {
                "model": "gpt-3.5-turbo",
                "temperature": 0.7,
                "api_key": os.environ.get("api_key"),
            }
        ]
    },
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=2)
# print(result)

#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/9 14:29
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   c_intent_openai.py
# @Desc     :

from data import INTENTS_CATEGORIES, INTENTS_QUESTIONS
from pandas import DataFrame
from streamlit import (write, title, data_editor, selectbox, button,
                       spinner, empty, sidebar, subheader, slider,
                       text_input, caption)

from utils.helper import intent_recognizer, Timer
from utils.models import OpenAICompleter

title("Intent Recognition with OpenAI")
content: str = "You are a professional and advanced intent classifier!"

empty_messages: empty = empty()
empty_questions: empty = empty()
data_editor(DataFrame(INTENTS_CATEGORIES), hide_index=True, disabled=True, use_container_width=True)
question: str = selectbox(
    "Select a question", ["无"] + INTENTS_QUESTIONS, index=0,
    help="Select a question in the list of intent categories.",
)
caption("After selecting a question, click the button below to classify its intent using OpenAI.")
empty_responses: empty = empty()

with sidebar:
    subheader("OpenAI Parameters")
    temperature: float = slider(
        "Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1, disabled=True,
        help="Controls the randomness of the model's output. Lower values make it more deterministic.",
    )
    Top_p: float = slider(
        "Top-p", min_value=0.0, max_value=1.0, value=0.9, step=0.1, disabled=True,
        help="Controls the diversity of the model's output by sampling from the top p% of the probability distribution.",
    )
    model: str = selectbox(
        "OpenAi Model", ["gpt-3.5-turbo"], index=0, disabled=True,
        help="Select the OpenAI model to use.",
    )
    aip_key: str = text_input(
        "OpenAI API Key",
        max_chars=164, type="password",
        help="OpenAI API key for authentication",
    )
    caption(f"The length of API key you entered is {len(aip_key)} characters.")
    if not aip_key:
        empty_messages.error("Please enter your OpenAI API key.")
    elif aip_key and not aip_key.startswith("sk-"):
        empty_messages.error("Please enter a **VALID** OpenAI API key.")
    elif aip_key and aip_key.startswith("sk-") and len(aip_key) != 164:
        empty_messages.warning("The length of OpenAI API key should be 164 characters.")
    elif aip_key and aip_key.startswith("sk-") and len(aip_key) == 164:
        empty_messages.success("The OpenAI API key is valid.")
        if question == "无":
            empty_messages.error("Please select a question from the list.")
        else:
            empty_messages.success("Now you can click the button to classify your intent using OpenAI.")
            if button(
                    "Classify Intent", type="primary",
                    use_container_width=True,
                    help="Click to classify the intent of the selected question."
            ):
                empty_messages.info("The intent of the question is classifying, please wait...")
                with Timer("Classify Intent", precision=3) as timer:
                    with spinner(text="Classifying intent of the selected question."):
                        prompt: str = intent_recognizer(question, INTENTS_CATEGORIES, content)
                        opener = OpenAICompleter(api_key=aip_key, temperature=temperature, top_p=Top_p)
                        response: str = opener.client(content=content, prompt=prompt, model=model)
                        empty_responses.data_editor(
                            DataFrame([response], columns=["Intent Classification", ]),
                            hide_index=True, disabled=True,
                            use_container_width=True,
                        )
                empty_messages.success(f"{timer}")

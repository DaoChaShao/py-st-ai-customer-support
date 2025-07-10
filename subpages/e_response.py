#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/9 14:30
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   e_response.py
# @Desc     :   

from data import PERSONALISED_QUESTIONS
from streamlit import (title, columns, selectbox, number_input, multiselect,
                       button, write, expander, caption, sidebar,
                       empty, subheader, slider, text_input, chat_message)

from utils.helper import personalised_response, Timer
from utils.models import OpenAICompleter

title("Personalised Response")
content: str = "You are a friendly and polite customer service representative!"
empty_messages: empty = empty()

question: str = selectbox(
    "Customer Question",
    PERSONALISED_QUESTIONS,
    index=0,
    help="Please select a question from the list."
)
caption("Please select a question from the list to test personised response.")
with expander("Customer Features", expanded=True):
    caption("Select your features initially to get personalised responses.")
    col_left, col_right = columns(2, gap="large", vertical_alignment="center")
empty_responses_human: empty = empty()
empty_responses_robot: empty = empty()

with col_left:
    gender: str = selectbox(
        "Gender", ["Male", "Female"], index=1,
        help="Please select your gender."
    )
    status: str = selectbox(
        "Status", ["Regular", "Silver", "Gold", "VIP"],
        index=0,
        help="Please select your customer level."
    )
with col_right:
    age: int = number_input(
        "Age", min_value=12, max_value=70, value=25, step=1,
        help="Please enter your age."
    )
    products: list[str] = multiselect(
        "Products",
        ["Clothing", "Electronics", "Books", "Food", "Sports Equipment"],
        help="Please select the types of productions you are interested in."
    )

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
    api_key: str = text_input(
        "OpenAI API Key",
        max_chars=164, type="password",
        help="OpenAI API key for authentication",
    )
    caption(f"The length of API key you entered is {len(api_key)} characters.")
    if not api_key:
        empty_messages.error("Please enter your OpenAI API key.")
    elif api_key and not api_key.startswith("sk-"):
        empty_messages.error("Please enter a **VALID** OpenAI API key.")
    elif api_key and api_key.startswith("sk-") and len(api_key) != 164:
        empty_messages.warning("The length of OpenAI API key should be 164 characters.")
    elif api_key and api_key.startswith("sk-") and len(api_key) == 164:
        empty_messages.success("The OpenAI API key is valid.")
        if question == "无":
            empty_messages.error("Please select a question from the list.")
        else:
            empty_messages.success("Now you can click the button to generate a personalised response for the customer.")

            if products:
                if button("Submit", type="primary", use_container_width=True):
                    with Timer("Personalised Response Generation") as timer:
                        prompt: str = personalised_response(gender, age, status, products, content, question)
                        opener = OpenAICompleter(api_key=api_key)
                        response: str = opener.client(content, prompt, model=model)
                        # empty_responses.write(response)
                        with empty_responses_human.chat_message(name="human", avatar="user"):
                            write(question)
                        with empty_responses_robot.chat_message(name="ai", avatar="assistant"):
                            write(response)
                    empty_messages.success(f"{timer}")
            else:
                empty_messages.error("Please select at least one product type to get a personalised response.")

#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/9 15:08
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :   

from openai import OpenAI


class OpenAIEmbedder(object):
    """OpenAI Embeddings API Wrapper"""

    def __init__(self, api_key: str) -> None:
        """ Initialise the OpenAI Embeddings API

        :param api_key: str: The API key for the OpenAI API
        """
        self._api_key = api_key

    def client(self, prompt: list, model: str, dimensions: int = 1536) -> list:
        """ Initialise the OpenAI Embeddings API
                - dimensions: 256、512、1024、1536

        :param dimensions: int: The number of dimensions for the embedding
        :param model: str: The model to use for the embedding
        :param prompt: list: The input text to be embedded
        :return: list: The embedded text as a list of floats
        """
        client = OpenAI(api_key=self._api_key, base_url="https://api.openai.com/v1")

        response = client.embeddings.create(
            input=prompt,
            model=model,
            dimensions=dimensions,
            encoding_format="float",
            timeout=3,
        )

        return [item.embedding for item in response.data]


class OpenAICompleter(object):
    """ OpenAI Completer API Wrapper """

    def __init__(self, api_key: str, temperature: float = 0.7, top_p: float = 0.9) -> None:
        """ Initialize the OpenAI Hyperparameter Tuning API
        :param api_key: str: The API key for the OpenAI API
        :param temperature: float: The temperature for the completion
        :param top_p: float: The top-p for the completion
        """
        self._api_key = api_key
        self._temperature = temperature
        self._top_p = top_p

    def client(self, content: str, prompt: str, model: str) -> str:
        """ Initialise the OpenAI Completion API
        :param content: str: The input text to be completed
        :param prompt: str: The prompt to complete the input text
        :param model: str: The model to use for the completion
        :return: str: The completed text
        """
        client = OpenAI(api_key=self._api_key, base_url="https://api.openai.com/v1")

        messages = [
            {"role": "system", "content": content},
            {"role": "user", "content": prompt},
        ]
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
            temperature=self._temperature,
            top_p=self._top_p,
        )

        return completion.choices[0].message.content

def deepseek_api_model(params: dict, prompt: str) -> str:
    """ Load Language Model """
    api_key: str = params["api_key"]
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    messages = [
        {"role": "system", "content": params["sys_content"]},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=params["model"],
        messages=messages,
        temperature=params["temperature"],
        stream=False)

    return response.choices[0].message.content
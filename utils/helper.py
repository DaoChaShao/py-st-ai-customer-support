#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/7 23:41
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :   

from numpy import array
from pandas import DataFrame
from plotly.express import scatter_3d
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
from time import perf_counter


class Timer(object):
    """A function for timing code blocks using a context manager.
    :param description: the description of the timer
    :param precision: the number of decimal places to round the elapsed time
    """

    def __init__(self, description: str = None, precision: int = 5):
        self._description: str = description
        self._precision: int = precision
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        self._start = perf_counter()
        print()
        print("-" * 50)
        print(f"{self._description} has been started.")
        return self

    def __exit__(self, *args):
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        if self._elapsed != 0.0:
            print("-" * 50)
            return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
        return f"{self._description} has NOT been started."


def dimensions_reductor_with_tsne(data, target_dimensions: int = 3, random_seed: int = 9527, perplexity: int = 3):
    """A function to reduce the dimensions of the data using t-SNE.
    :param data: The input data to be reduced, can be a list or a numpy array.
    :param target_dimensions: The number of dimensions to reduce the data to (default is 3).
    :param random_seed: The random seed for reproducibility (default is 9527).
    :param perplexity: The perplexity parameter for t-SNE (default is 3).
    :return: numpy.ndarray: The reduced data as a numpy array.
    """
    # Check if the input data is a list or numpy array, and convert it to a numpy array if necessary
    data = array(data)

    # Ensure the data is in the correct shape for t-SNE
    tsne = TSNE(
        n_components=target_dimensions,
        random_state=random_seed,
        perplexity=perplexity,
    )
    # Fit and transform the data using t-SNE
    reduced_data = tsne.fit_transform(data)

    print("Original shape:", data.shape)
    print("Reduced shape:", reduced_data.shape)

    return reduced_data


def plotly_scatter_3d(data_3d, contents: list[str], category: str = "t-SNE"):
    """A function to plot the reduced data in 3D using Plotly.
    :param data_3d: numpy.ndarray: The reduced data as a numpy array.
    :param contents: list[str]: The contents of the data points.
    :param category: str: The type of visualisation (default is "t-SNE").
    :return: plotly.graph_objects.Figure: The 3D scatter plot figure.
    """
    # Check if the input data is a numpy array, and convert it to a DataFrame
    df = DataFrame(data_3d, columns=["x", "y", "z"])
    # Ensure the contents are a list of strings and match the number of data points, like labels
    df["contents"] = contents
    # Add a new column for categories, with the first entry as "Test Sentence" and the rest as "Baseline Sentences"
    df["categories"] = ["Test Sentence"] + ["Baseline Sentences"] * (len(contents) - 1)

    fig = scatter_3d(
        df,
        x="x",
        y="y",
        z="z",
        title=f"{category} Visualization",
        color="categories",
        text="contents",
    )
    fig.update_layout(height=700)

    return fig


def similarities_getter(embeddings, sentences, target_index: int = 0, top_n: int = 3) -> list[tuple[str, float]]:
    """Calculate cosine similarities between a target sentence and a list of sentences.
    :param embeddings: list: The list of sentence embeddings.
    :param sentences: list[str]: The list of sentences corresponding to the embeddings.
    :param target_index: int: The index of the target sentence in the embeddings list (default is 0).
    :param top_n: int: The number of most similar sentences to return (default is 3).
    :return: list[tuple[str, float]]: A list of tuples containing the most similar sentences and their cosine similarity scores.
    """
    # Convert the embeddings to a numpy array
    whole = array(embeddings)
    # Ensure the target index is within the range of the embeddings list
    target = whole[target_index].reshape(1, -1)

    # Calculate cosine similarities
    similarities = cosine_similarity(target, whole)[0]
    # Set the similarity of the target sentence to itself to -1 to exclude it from the results
    similarities[target_index] = -1

    # Get indices of the top N most similar sentences
    top_n_indices = similarities.argsort()[::-1][:top_n]

    return [(sentences[i], similarities[i]) for i in top_n_indices]


def intent_recognizer(question: str, categories: dict[str, list], content: str) -> str:
    """Analyse and classify the intent of the questions customers ask.
    :param question: str: The question text.
    :param categories: dict[str, list]: A dictionary where keys are intent categories and values are lists of example questions.
    :param content: str: The content of the question text.
    """
    context: str = (f"{content}"
                    f"You are an advanced assistant that classifies user questions into intent categories.")

    few_shots: str = ""
    for intent, examples in categories.items():
        few_shots += f"\n### Category: {intent}\n"
        for example in examples:
            few_shots += f"- {example}\n"

    instruction: str = (f"Now, please classify the following customer question into ONE of the above categories"
                        f"{question}"
                        f"Respond only with the category name.")

    constraints: str = f"Your evaluation should be clear, accurate and positive."

    prompt: str = (
        f"{context}"
        f"{few_shots}"
        f"{instruction}"
        f"{constraints}"
    )

    return prompt


def personalised_response(gender: str, age: int, status: str, products: list[str], content: str, question: str) -> str:
    """A function to generate a personalised response based on user input.
    :param gender: str: The gender of the person.
    :param age: int: The age of the person.
    :param status: str: The status of the person.
    :param products: str: The products the person is interested in.
    :param content: str: The content of the OpenAI system content.
    :param question: str: The question the person has.
    """
    persona = (
        f"There is a {gender} customer."
        f"If there is a female, call him with 女士."
        f"If there is a male, call him with 男士."
        f"And, his/her age is {age}."
        f"And, his/her status is {status}."
        f"He/She brought {', '.join(products)}"
    )

    context: str = (
        f"{content}"
        f"Please generate a natural, warm, and professional customer service reply based on the following information:"
    )

    instruction: str = (
        f"Now, please give a suitable and proper response to the customer's question — {question} based on {persona}."
    )

    constraints: str = (
        f"Your response should be professional and positive."
        f"And, you should use first-person to speak to the customer."
        f"And, you should respect the customer's identity, and display his/her status."
        f"And, you should limit the response to within 80 words."
        f"And, you should use Chinese, simple and clear language."
        f"Do not include any closing words, such as '祝好' or '您的名字'. Only respond with the main message body."
    )

    prompt: str = (f"{context}"
                   f"{instruction}"
                   f"{constraints}")

    return prompt

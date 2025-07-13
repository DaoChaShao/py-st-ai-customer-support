#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/9 14:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   b_understand.py
# @Desc     :   

from data import CUSTOMER_QUESTION, CUSTOMER_QUESTIONS
from pandas import DataFrame
from streamlit import (title, sidebar, subheader, caption, text_input,
                       selectbox, empty, button, spinner,
                       data_editor, plotly_chart, write, )

from utils.models import OpenAIEmbedder
from utils.helper import (Timer,
                          dimensions_reductor_with_tsne,
                          plotly_scatter_3d,
                          similarities_getter, )

title("Semantic Understanding")
empty_messages: empty = empty()

data_editor(DataFrame(CUSTOMER_QUESTION, columns=["Test Question"]),
            hide_index=True, disabled=True,
            use_container_width=True)
data_editor(DataFrame(CUSTOMER_QUESTIONS, columns=["Baseline Questions"]),
            hide_index=True, disabled=True,
            use_container_width=True)
CUSTOMER_DATA: list[str] = CUSTOMER_QUESTION + CUSTOMER_QUESTIONS

empty_chart: empty = empty()
empty_similarities: empty = empty()

with (sidebar):
    subheader("OpenAI Parameters")
    options_box = ["text-embedding-3-small", "text-embedding-3-large", ]
    model: str = selectbox(
        "Embedding Model",
        options=options_box, index=0,
        help="Select the model for embedding"
    )
    if model == "text-embedding-3-small":
        size: str = "Small"
        dimensions: int = 1536
    elif model == "text-embedding-3-large":
        size: str = "Large"
        dimensions: int = 3072
    caption(f"{size} model has {dimensions} dimensions.")

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
        if button("Run Embedding", type="primary", use_container_width=True, help="Click to run the embedding process"):
            with Timer("Embedding Process", precision=3) as timer:
                empty_messages.info("Running the embedding process, please wait...")
                with spinner("Embedding in progress..."):
                    if aip_key:
                        embedder = OpenAIEmbedder(api_key=aip_key)
                        embeddings: list = embedder.client(prompt=CUSTOMER_DATA, model=model)
                        caption(f"The number of all questions is {len(embeddings)}.")

                        reduced_data = dimensions_reductor_with_tsne(embeddings)

                        fig = plotly_scatter_3d(reduced_data, CUSTOMER_DATA)
                        empty_chart.plotly_chart(fig, use_container_width=True)

                        top_similarities = similarities_getter(embeddings, CUSTOMER_DATA)
                        empty_similarities.data_editor(
                            DataFrame(top_similarities, columns=["Similarity Questions", "Similarity Score"]),
                            hide_index=True, disabled=True,
                            use_container_width=True,
                        )
            empty_messages.success(f"Done! {timer}")

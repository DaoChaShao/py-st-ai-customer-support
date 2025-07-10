#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/9 14:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   z_about.py
# @Desc     :   

from streamlit import title, divider, expander, caption

title("Application Information")
divider()
with expander("About this application", expanded=True):
    caption("This app demonstrates how to build an intelligent customer service system based on modern natural language processing. It includes the following core modules:")
    caption("1. **Semantic Understanding**")
    caption("Uses OpenAI embeddings to analyze the semantic similarity between customer questions and known queries, enabling accurate content matching and clustering.")
    caption("2. **Intent Recognition**")
    caption("Identifies the intent behind customer questions (e.g., shipping inquiry, after-sales request, product consultation) using prompt-based classification with predefined categories.")
    caption("3. **Personalized Response Generation**")
    caption("Generates customized replies by incorporating user personas (e.g., gender, age, membership level, products) into the prompt to simulate human-like, context-aware support.")
    caption("4. **Interactive Visualization**")
    caption("Presents semantic relationships in 3D space using t-SNE and Plotly, supporting deeper analysis of question distribution and similarity.")
    caption("5. **Prompt Engineering Showcase**")
    caption("Demonstrates how few-shot and structured prompt design can be leveraged to guide large language models in handling real-world customer service scenarios.")



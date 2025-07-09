#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/9 14:16
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   a_home.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("Smart Chat Lab")
divider()
with expander("INTRODUCTION", expanded=True):
    caption("1. SmartChatLab: Python-based intelligent customer service demos")
    caption("2. Modules Overview：Semantic Understanding, Intent Recognition, Personalized Response")
    caption("3. Implementation Language：Python 3.12, lightweight dependencies")
    caption("4. Key Techniques：API calling (OpenAI), prompt engineering, basic text processing")
    caption("5. Application Scenario：Customer service simulation in e-commerce and education")

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

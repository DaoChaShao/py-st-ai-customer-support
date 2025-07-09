#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/7 17:19
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :   

from utils.layout import page_config, pages_setter


def main() -> None:
    """ streamlit run main.py """
    # Set the page configuration
    page_config()

    # Set the sidebar pages
    pages_setter()


if __name__ == "__main__":
    main()

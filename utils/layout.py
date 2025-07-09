#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/7 23:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :   

from streamlit import set_page_config, Page, navigation


def page_config() -> None:
    """ Set the window

    :return: None
    """
    set_page_config(
        page_title="AI Customer Support",
        page_icon=":material/concierge:",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def pages_setter() -> None:
    """ Set the subpages on the sidebar

    :return: None
    """
    pages: dict = {
        "page": [
            "subpages/a_home.py",
            "subpages/b_understand.py",
            "subpages/c_intent.py",
            "subpages/d_response.py",
            "subpages/z_about.py",
        ],
        "title": [
            "Home",
            "Semantic Understanding",
            "Intent Recognition",
            "Personalized Response",
            "About",
        ],
        "icon": [
            ":material/home:",
            ":material/psychology_alt:",
            ":material/arrows_input:",
            ":material/chat_bubble:",
            ":material/info:",
        ],
    }

    structure: dict = {
        "Introduction": [
            Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        ],
        "Manipulation": [
            Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2]),
            Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3]),
        ],
        "About": [
            Page(page=pages["page"][4], title=pages["title"][4], icon=pages["icon"][4]),
        ],
    }
    pg = navigation(structure, position="sidebar", expanded=True)
    pg.run()

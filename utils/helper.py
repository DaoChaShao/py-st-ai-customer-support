#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/7 23:41
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :   

from time import perf_counter


class Timer(object):
    """ A simple timer class to measure the elapsed time.

    :param precision: the number of decimal places to round the elapsed time
    :type precision: integer
    :param description: the description of the timer
    :type description: str
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

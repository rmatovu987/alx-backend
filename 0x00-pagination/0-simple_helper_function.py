#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments page and page_size.
"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple"""

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return start_size, final_size

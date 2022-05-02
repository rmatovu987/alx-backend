#!/usr/bin/env python3
""" Write a function named index_range that takes two
integer arguments page and page_size. """
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Implement a method named get_page that takes two integer
            arguments page with default value 1 and page_size with default value 10.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        new_range: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return pagination[new_range[0]:new_range[1]]


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple"""

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return start_size, final_size

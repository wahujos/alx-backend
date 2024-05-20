#!/usr/bin/env python3
"""
documentation of the overal code
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    function named index_range that takes two
    integer arguments page and page_size.
    return a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    tup = (start_index, end_index)
    return tup


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        initialization function of the class
        """
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
        get_page that takes two integer arguments page with default
        value 1 and page_size with default value 10.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        s_index, e_index = index_range(page, page_size)
        return self.data[s_index:e_index] if s_index < len(self.data) else []

#!/usr/bin/env python3
"""
Implement a get_hyper method
"""

import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


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
        """get a list of data to pagination"""
        assert(type(page) == int and page > 0)
        assert(type(page_size) == int and page_size > 0)
        indexes = index_range(page, page_size)
        data = self.dataset()
        if (indexes[0] > len(data)):
            return []
        return data[indexes[0]:indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """returns a dictionary containing the following key-value"""
        dataset = self.get_page(page, page_size)

        next_page = page + 1
        if (page > len(dataset)):
            next_page = None

        prev_page = page - 1
        if (page <= 1):
            prev_page = None

        total_pages = math.ceil(len(self.__dataset) / page_size)
        print(type(total_pages))

        return {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

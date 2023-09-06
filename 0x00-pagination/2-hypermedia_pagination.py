#!/usr/bin/env python3
""" Hypermedia pagination """

import csv
import math
from typing import List, Dict, Any, Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """ Server class to paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialize instance. """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Property decorator to return the dataset. """
        return self.__dataset

    def get_dataset(self) -> List[List]:
        """ Get the dataset. """
        with open(self.DATA_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)
            dataset = []
            for row in reader:
                dataset.append(row)
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ Return a dictionary containing the following key-value pairs:
                    - page_size: the length of the returned dataset page
                    - page: the current page number
                    - data: the dataset page (equivalent to return from previous task)
                    - next_page: number of the next page, None if no next page
                    - prev_page: number of the previous page, None if no previous page
                    - total_pages: the total number of pages in the dataset as an integer
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        self.get_dataset()
        if self.__dataset is None:
         return {}
            
        start, end = index_range(page, page_size)
        data = self.__dataset[start:end]
        total_pages = math.ceil(len(self.__dataset) / page_size)
     
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
            
        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
        }
     
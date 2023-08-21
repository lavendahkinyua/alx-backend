#!/usr/bin/env python3
""" Simple pagination """

import csv
import math
from typing import List, Tuple


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
    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """ Return list of rows from dataset. """
            assert isinstance(page, int) and isinstance(page_size, int)
            assert page > 0 and page_size > 0
    
            self.get_dataset()
            if self.__dataset is None:
             return []
            
            start, end = index_range(page, page_size)
            return self.__dataset[start:end]
    
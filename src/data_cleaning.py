import logging
from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from src.helpers import (
    extract_names_to_list,
    extract_three_names_to_list,
    extract_director_names_to_list,
    remove_spaces,
)



class DataStrategy(ABC):
    """
    Abstract class defining strategy for handling data
    """

    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass

class DataProcessingStrategy(DataStrategy):
    """
    Strategy for preprocessing data
    """

    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess data
        """
        try:
            data = data[['movie_id','title','overview','genres','keywords','cast','crew']]
            data.dropna(inplace=True)

            data['genres'] = data['genres'].apply(extract_names_to_list)
            data['keywords'] = data['keywords'].apply(extract_names_to_list)
            data['cast'] = data['cast'].apply(extract_three_names_to_list)
            # movies['cast'] = movies['cast'].apply(lambda x:x[0:3])
            data['crew'] = data['crew'].apply(extract_director_names_to_list)

            data['cast'] = data['cast'].apply(remove_spaces)
            data['crew'] = data['crew'].apply(remove_spaces)
            data['genres'] = data['genres'].apply(remove_spaces)
            data['keywords'] = data['keywords'].apply(remove_spaces)

            data['overview'] = data['overview'].apply(lambda x:x.split())

            data['tags'] = data['overview'] + data['genres'] + data['keywords'] + data['cast'] + data['crew']

            new_data = data.drop(columns=['overview','genres','keywords','cast','crew'])
            new_data['tags'] = new_data['tags'].apply(lambda x: " ".join(x))

            return new_data

        except Exception as e:
            logging.error(e)
            raise e
        
class DataCleaning:
    """
    class for cleaning data which process the data
    """

    def __init__(self, data: pd.DataFrame, strategy: DataStrategy):
        self.data = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """ handle data """
        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error("Error handling data: {}".format(e))
            raise e


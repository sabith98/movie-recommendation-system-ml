import logging
from abc import ABC, abstractmethod

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Model(ABC):
    """ Abstract class for all models """

    @abstractmethod
    def train(self, data: pd.DataFrame):
        """
        Trains the model
        Args:
            data: Cleaned data
        Returns:
            None
        """

class CosineSimilarity(Model):
    """Cosine similarity"""

    def train(self, data: pd.DataFrame, **kwargs):
        """
        search for similar vectors
        Args:
            data: processed data
        Returns:
            None
        """
        try:
            vectorizer = TfidfVectorizer(max_features=5000,stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(data['tags']).toarray()
            similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
            logging.info("Model training completed")
            return similarity
        except Exception as e:
            logging.error("Error in similarity search: {}".format(e))
            raise e
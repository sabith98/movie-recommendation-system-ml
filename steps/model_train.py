import logging
import pandas as pd
from zenml import step

from src.model_dev import CosineSimilarity
from .config import ModelNameConfig


@step()
def train_model(
    similarity,
    config: ModelNameConfig,
) -> None:
    """
    Trains the model on the ingested data

    Args:
        similarity: Vectors
    """
    try:
        model = None
        if config.model_name == "cosine_similarity":
            model = CosineSimilarity()
            trained_model = model.train(similarity)
            return trained_model
        else:
            raise ValueError("Model {} not supported".format(config.model_name))
    except Exception as e:
        logging.error("Error in training model: {}".format(e))
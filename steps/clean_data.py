import logging
import pandas as pd
from zenml import step

from src.data_cleaning import DataProcessingStrategy, DataCleaning


@step
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the data

    Args:
        df: raw data
    Returns:
        X_train: Training data
    """
    try:
        process_strategy = DataProcessingStrategy()
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()
        logging.info("Data cleaning completed")
        return processed_data
    except Exception as e:
        logging.error("Error occurred during data cleaning: {}".format(e))
        raise e
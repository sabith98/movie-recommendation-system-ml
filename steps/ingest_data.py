import logging
import pandas as pd
from zenml import step

class IngestData:
    """
    Data ingestion class which ingests data from the source and 
    returns a DataFrame.
    """

    def __init__(self, data_paths: list[str]):
        """Initialize the data ingestion class."""
        self.data_paths = data_paths

    def get_data(self):
        dfs = []
        for data_path in self.data_paths:
            logging.info(f"Ingesting data from {data_path}")
            df = pd.read_csv(data_path)
            dfs.append(df)

        return pd.merge(left=dfs[0], right=dfs[1], on='title')


@step
def ingest_df(data_paths: list[str]) -> pd.DataFrame:
    """
    Ingesting the data from the data_path

    Args:
        data_paths: paths to the data
    Returns:
        pd.DataFrame: the ingested data
    """

    try:
        ingest_data = IngestData(data_paths)
        df =ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e

from pipelines.training_pipeline import train_pipeline
from pathlib import Path

if __name__ == "__main__":
    # Run the pipeline
    data_path = "D:\\Data Science\\Projects practice\\ML portfolio projects\\movie-recommendation-system-ml\\tmdb_5000_credits.csv"
    train_pipeline(data_path=data_path)
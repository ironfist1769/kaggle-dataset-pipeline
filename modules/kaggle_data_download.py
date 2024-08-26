# fetch the data from kaggle api
# connection building using api key then downloading it
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset():
    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()
    
    # Download the dataset
    dataset = "berkayalan/paris-2024-olympics-medals"
    download_path = "data/"
    api.dataset_download_files(dataset, download_path, unzip=True)
    print(f"Dataset '{dataset}' downloaded successfully.")
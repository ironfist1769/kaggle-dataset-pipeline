from google.cloud import storage
import os

def upload_to_gcs():
    # Initialize the GCS client
    storage_client = storage.Client()
    
    # Set bucket and file details
    bucket_name = "watch-bucket"
    bucket = storage_client.bucket(bucket_name)
    
    # Upload files from the downloaded directory
    local_folder = "data/"
    for filename in os.listdir(local_folder):
        if filename.endswith(".csv"):  # Adjust if you have different file types
            local_file_path = os.path.join(local_folder, filename)
            blob = bucket.blob(filename)
            blob.upload_from_filename(local_file_path)
            print(f"Uploaded {filename} to GCS bucket {bucket_name}.")
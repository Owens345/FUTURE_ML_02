import gdown
import os

# Google Drive file ID
file_id = "1LpmEiT__Zj4LQXmbPnmYIU-AxP8eQcuV"
output_path = "data/tmdb_movies.csv"

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

# Download the file
if not os.path.exists(output_path):
    print("Downloading dataset...")
    gdown.download(id=file_id, output=output_path, quiet=False)
    print("Download complete.")
else:
    print("File already exists.")
 

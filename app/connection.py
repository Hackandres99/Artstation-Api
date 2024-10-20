import os
from dotenv import load_dotenv
from pymongo import MongoClient


class ArtstationRepository:
    def __init__(self) -> None:
        load_dotenv()

        username = os.getenv('MONGODB_USERNAME')
        password = os.getenv('MONGODB_PASSWORD')
        host = os.getenv('MONGODB_HOST')
        port = int(os.getenv('MONGODB_PORT', 27017))
        database = os.getenv('MONGODB_DATABASE')

        connection_string = f"mongodb+srv://{username}:{password}@{host}/"

        self.client = MongoClient(connection_string, port=port)
        self.db = self.client[database]
        self.artwork_collection = self.db.artwork
        self.artist_collection = self.db.artist
        self.preview_collection = self.db.preview
    
    def get_artist(self, id: str):
        artist = self.artist_collection.find_one(
            {'base_info.artist_id': id}
        )
        return artist

    def get_artwork(self, id: str):
        artwork = self.artwork_collection.find_one({'artwork_id': id})
        return artwork

    def get_previews(self):
        previews = list(self.preview_collection.find({}))
        return previews

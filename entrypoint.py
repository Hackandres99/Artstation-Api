import os
from dotenv import load_dotenv
from app.routes import app

load_dotenv()
app.config.from_object(os.getenv('CONFIG_ENV'))

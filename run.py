import os
from dotenv import load_dotenv
from app.routes import app
from waitress import serve

load_dotenv()
app.config.from_object(os.getenv('CONFIG_ENV'))
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))

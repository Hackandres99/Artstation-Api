import os
from dotenv import load_dotenv
from app.routes import app

load_dotenv()
app.config.from_object(os.getenv('CONFIG_ENV'))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)  

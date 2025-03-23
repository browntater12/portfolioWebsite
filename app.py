from flask import Flask
import os
from dotenv import load_dotenv
from application import create_app

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure production settings
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # 1 year
app.config['TEMPLATES_AUTO_RELOAD'] = False

# ... rest of your app code ...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
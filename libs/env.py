import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
SSH_KEY_NAME = os.getenv('SSH_KEY_NAME')

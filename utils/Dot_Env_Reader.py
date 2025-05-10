
from dotenv import load_dotenv
import os

load_dotenv("config/config.env")

BASE_URL = os.getenv('BASE_URL')
BROWSER = os.getenv('BROWSER')


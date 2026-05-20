from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API", "http://localhost:1350")
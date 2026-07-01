import os
from dotenv import load_dotenv

load_dotenv('./.env')
token = os.getenv("BOT_TOKEN")  
tokenApex = os.getenv("API_APEXLEGENDS")
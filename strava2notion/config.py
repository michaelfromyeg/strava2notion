import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env_file_path = os.path.join(parent_dir, '.env')

load_dotenv(env_file_path)

# StravaIO
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Notion
TOKEN_V3 = os.getenv("TOKEN_V3")
DATABASE_ID = os.getenv("DATABASE_ID")

# get all data (true) or data after last sync (false)
ALL_DATA = True

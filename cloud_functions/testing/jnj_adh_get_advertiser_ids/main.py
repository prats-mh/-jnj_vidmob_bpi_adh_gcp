import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='env/.env')
print(os.environ.get('FOO'))
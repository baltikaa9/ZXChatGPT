import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
OPENAI_API_TOKEN = os.getenv('OPENAI_API_KEY')
CONTEXT_DB = 'context.json'

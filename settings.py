import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())


PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")



WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "👋")
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "REPLY_TO_THIS")
WRONG_REPLY = os.getenv("WRONG_REPLY", "WRONG_REPLY")

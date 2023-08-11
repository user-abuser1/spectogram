"""Collects objects, functions, variables and methods."""


import os
from dotenv import load_dotenv


load_dotenv() # Function for detect and load enviroment file

APP_TOKEN = os.getenv('TOKEN') # Application Token should be in .env

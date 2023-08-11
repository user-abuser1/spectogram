"""
Сбирает в себе объкты, функции, переменные и методы.
"""

import os

from dotenv import load_dotenv

load_dotenv()

APP_TOKEN = os.getenv('TOKEN')

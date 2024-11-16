# settings.py

import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")  # Set default if not in .env
    DATABASE_URL = os.getenv("DATABASE_URL", "postgres://postgres:123@localhost:5432/chatbot")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY", "4WHd4Cdqfudx8HlvAexgN2hHnT65rlATlvBxDJmS ")
    CORS_ORIGINS = ["http://localhost:3000"]

# You can extend the Config class for different environments (e.g., development, production)
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Add more production-specific settings here

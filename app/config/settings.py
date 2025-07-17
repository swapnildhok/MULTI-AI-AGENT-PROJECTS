from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    TRAVILY_API_KEY=os.getenv("TRAVILY_API_KEY")

    ALLOWED_MODEL_NAMES =[
        "llama3-70b-8192",
        "llama-3.3-70b-versatile"
    ]
settings=Settings()
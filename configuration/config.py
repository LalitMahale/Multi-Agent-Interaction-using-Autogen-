import os
from dotenv import load_dotenv
load_dotenv()

CONFIG_LIST= [
        {
        "model":"gemini-1.5-flash",
        'api_key':os.getenv("GOOGLE_GEMINI_API"),
        "api_type":"google"
        },

        {
        "model":"gemini-pro",
        "api_key":os.getenv("GOOGLE_GEMINI_API"),
        "api_type":"google"
        }
        
        ]


print(CONFIG_LIST)
from dotenv import load_dotenv
import os

load_dotenv()

app_name = os.getenv('APP_NAME')
print(f'Type: {type(app_name)}')    # str

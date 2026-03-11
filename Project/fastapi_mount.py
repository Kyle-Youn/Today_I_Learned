import uvicorn
from main import app
from fastapi.staticfiles import StaticFiles

app.mount('/assets', StaticFiles(directory=str(dist / 'assets')), name='static')

from fastapi import FastAPI
from routes import product_routes

app = FastAPI()
# attach files to main
app.include_router(product_routes)
from fastapi import FastAPI
# from routes import country_routes
from app.routes import country_routes

app = FastAPI()

# Include routes from country_routes
app.include_router(country_routes.router)

# Entry endpoint 
@app.get("/")
def root():
    return {"message": "Welcome to the REST Countries API using FastAPI"}

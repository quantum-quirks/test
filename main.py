from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mangum import Mangum  # Allows FastAPI to run on AWS Lambda

app = FastAPI()

# Define a request model for POST requests
class Item(BaseModel):
    name: str
    price: float

# ✅ GET request: Retrieve data
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on AWS Lambda!"}

# ✅ POST request: Create new data
@app.post("/items/")
def create_item(item: Item):
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be greater than 0")
    return {"message": "Item created", "item": item}

# ✅ Required for AWS Lambda compatibility
handler = Mangum(app)

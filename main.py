from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
        
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return {"items": ["apple", "banana", "cherry"]}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"item_{item_id}"}

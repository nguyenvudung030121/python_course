from fastapi import FastAPI
app = FastAPI()
@app.get("/example/")
def hello():
    return {"Hello": "World"}

    

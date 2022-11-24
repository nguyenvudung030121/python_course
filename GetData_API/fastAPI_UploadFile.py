from fastapi import FastAPI, File, UploadFile
app = FastAPI()
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    return {"Filename": file.filename, "Content": file.content_type}
    # return {"Filename": file.filename}
from fastapi import FastAPI, File, UploadFile
app = FastAPI()
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    return {"Filename": file.filename, "Content": file.content_type}
    # return {"Filename": file.filename}

@app.post("/upload&save")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"files/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}

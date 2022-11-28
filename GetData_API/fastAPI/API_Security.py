from fastapi import FastAPI, File, UploadFile
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI()
security = HTTPBasic()
AUTH_USERNAME = "python"
AUTH_PASSWORD = "abc123"

def verify_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, AUTH_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, AUTH_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
@app.post("/upload")
async def upload(file: UploadFile = File(...), auth=Depends(verify_user)):
    contents = await file.read()
    return {"Filename": file.filename, "Content": contents}
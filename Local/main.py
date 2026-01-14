from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 1. JS anuppum data-vukku oru structure (Schema)
class LoginRequest(BaseModel):
    email: str
    password: str

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 2. Login endpoint (POST method)
@app.post("/login")
async def login(data: LoginRequest):
    # Inga thaan neenga database check pannanum
    # For example:
    if data.email == "test@gmail.com" and data.password == "12345":
        return {"status": "success", "message": f"Welcome {data.email}!"}
    else:
        raise HTTPException(status_code=401, detail="Invalid Email or Password")
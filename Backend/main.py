from fastapi  import FastAPI
from routes import user

app =FastAPI(title='local delivery app')

app.include_router(user.router)

@app.get("/")
def read_root():
    return{"message":"wellcom my heartiya"}
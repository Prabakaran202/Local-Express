from fastapi  import FastAPI

app =FastAPI(title='local delivery app')


@app.get("/")
def read_root():
    return{"message":"wellcom my heartiya"}
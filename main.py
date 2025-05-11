from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_method():
  return {"message": "Talha Rana AI Engineer"}
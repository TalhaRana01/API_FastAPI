from fastapi import FastAPI

app = FastAPI()

# Get Method
@app.get("/")
def get_method():
  return {"message": "Talha Rana AI Engineer"}
# Put Method
@app.put("/")
def put_method():
  return {"message": "Talha Rana AI Engineer"}

# Post Method
@app.post("/")
def post_method():
  return {"message": "Talha Rana AI Engineer"}

# Delete Method
@app.delete("/")
def delete_method():
  return {"message": "Talha Rana AI Engineer"}
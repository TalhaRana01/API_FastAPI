from fastapi import FastAPI

app = FastAPI()

# # Get Method
# @app.get("/")
# def get_method():
#   return {"message": "Talha Rana AI Engineer"}
# # Put Method
# @app.put("/")
# def put_method():
#   return {"message": "Talha Rana AI Engineer"}

# # Post Method
# @app.post("/")
# def post_method():
#   return {"message": "Talha Rana AI Engineer"}

# # Delete Method
# @app.delete("/")
# def delete_method():
#   return {"message": "Talha Rana AI Engineer"}


@app.get("/")
def get_method():
  return {"message": "Talha Rana AI Engineer"}



data = [
{
  "id": 1,
  "name": "Shahjahan",
  "age": 4,
  "email": "talharana@gmail.com",
  "phone": "03001234567"
  
},
{
  "id": 2,
  "name": "Talha Rana",
  "age": 33,
  "email": "talharana@gmail.com",
  "phone": "03001234567"
  
},
{
  "id": 3,
  "name": "Ali Rana",
  "age": 25,
  "email": "talharana@gmail.com",
  "phone": "03001234567"
  
},
{
  "id": 4,
  "name": "Danyal Rana",
  "age": 27,
  "email": "talharana@gmail.com",
  "phone": "03001234567"
  
},
]

# @app.get("/login")
# def login():
#   return {
#     "data": data,
#     "message": "Talha Rana AI Engineer",
#     "status": "success",
    
#   }

# @app.get("/login/{id}")
# def login(id):
#   try:
#     return {
#       "id": id,
#       "data": [],
#       "message": "Login Successful",
#       "status": "success",
#     }
#     print("Login Successful", data)
#   except Exception as e:
#     return {
#       # "data": [],
#       "message": "Login Failed",
#       "status": 500,
#       "error": str(e)
#     }
    
    # dynamic parameters in route 
# @app.get("/login/{id}/{name}/{age}")
# def login(id, name, age):
#   try:
#     return {
#     "id" : id,
#     "name" : name,
#     "age" :age
#   }    
    
#   except Exception as e:
#    return {
#    "message": "Login Failed",
#    "status": 500,
#    "error": str(e)
    
#   }
     
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  id: int
  name: str
  age: int
  email: str
  profession: str
  phone: str
  
  
@app.post("/user")
def create_user(user: User):
  print(user)
  try:
    
    return {
      "message": "User Created Successfully",
      "status": "success",
      "data": user
    }
    
  except Exception as e:
    return {
      "message": str(e),
      "status": "error",
      "data": None
    }
    
    
# @app.get("/user/{id}")
# def get_id(id: str):
#   return {
#     "id": id,
#   }   


 
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


# @app.get("/login/{id}/{name}/{age}")
# def login(id, name, age):

#  print(id, name, age)
#  return {
#    "id": id,
#    "name": name,
#    "age": age
#  }
     
     
# @app.get("/user")
# def users(q):
#      return {
#        "query": q
#        "name": 
#      }  



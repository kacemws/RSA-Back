from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Enc_Message(BaseModel):
    p: int
    q : int
    message : str

class Dec_Message(BaseModel) : 
    p : int
    q : int
    cry : List[int]

app = FastAPI()

# origins = [
#     "https://my-awesome-website.netlify.app",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/encrypt')
async def encryptMessage(msg : Enc_Message) :
    pass 
    # d = 256
    # q = 3
    # x = rabin_karp_matcher(msg.message, msg.pattern, d, q)
    # return {'message' : x}

@app.post('/decrypt')
async def decryptMessage(msg : Dec_Message) :
    pass 
    # d = 256
    # q = 3
    # x = rabin_karp_matcher(msg.message, msg.pattern, d, q)
    # return {'message' : x}
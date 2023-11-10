from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index(): 
    return {
        "data" : "Testando FastAPI!"
          }

@app.get("/hello")
def hello():
    return {
        "data" : "Hello!"
    }

@app.get("/hello/{name}")
def helloName(name):
    return {
        "data" : f'Hello {name}!'
    }

@app.get("/quadrado/{num}")
def quadrado(num: int):
   return {
       "data" : {
           "num" : num,
           "quadrado" : num ** 2
       }
   }

@app.get("/pares")
def listaPares(limit : Optional[int] = 100, minimo: Optional[int] = 4):
   pares = []
   for i in range(minimo, limit+1, 2):
       pares.append(i)
  
   return {
       "limit" : limit,
       "pares" : pares,
       "minimo" : minimo
   }

class PessoaModel(BaseModel):
   primeiro_nome : str
   ultimo_nome : str
   idade : Optional[int] = 999

@app.post("/hello")
def helloPost(pessoa : PessoaModel):
    if pessoa.idade == 999:
        return {
            "data" : f'Hello {pessoa.primeiro_nome} {pessoa.ultimo_nome}!' 
        }
    return {
       "data" : f'Hello {pessoa.primeiro_nome} {pessoa.ultimo_nome}, you are {pessoa.idade}!'
   }

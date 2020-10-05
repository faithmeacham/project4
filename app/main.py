from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

@app.get("/fibonacci/{length}")
async def fib(length: int):
    fib-string = "1"
    prev = 1
    current = 1
    for x in range(length):
        fib-string += str(current)
        holder = current
        current += prev
        prev = holder
    return fib-string

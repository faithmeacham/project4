from fastapi import FastAPI

app = FastAPI()

@app.get("/fibonacci/{length}")
async def fib(length: int):
    fibstring = "1"
    prev = 1
    current = 1
    for x in range(length-1):
        fibstring += ","
        fibstring += str(current)
        holder = current
        current += prev
        prev = holder
    label = "First " + str(length) + " Fibonacci Numbers"
    return {label: fibstring}

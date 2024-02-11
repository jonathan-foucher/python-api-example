from fastapi import FastAPI

app = FastAPI()

@app.get("/my-app/hello-world-path")
def hello_world():
    return 'Hello World!'

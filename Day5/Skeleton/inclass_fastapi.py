from fastapi import FastAPI

app = FastAPI()

# if you close terminal before quitting, run the below to kill
# ps aux | grep fastapi
# kill -9 {process id}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def custom_intro(name: str | None = None):
    if name:
        return {"message": f"Hello, {name}"}
    return {"message": "Hello, nobody."}


# requests.get("url/hello?name=Diane")
# requests.get("url/hello", params={"name":"Diane"})


@app.get("/hello/{name}")
def custom_intro_w(name: str):
    return {"message": f"Hello, {name}"}

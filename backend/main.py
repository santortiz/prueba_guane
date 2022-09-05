from fastapi import FastAPI
import uvicorn

app = FastAPI()


if __name__ == '__main__':
    print("api running")
    uvicorn.run(app, host='localhost', port=3000)
    
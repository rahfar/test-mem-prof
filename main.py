from fastapi import FastAPI
from memory_profiler import profile

app = FastAPI()


@profile
@app.post("/predict")
async def predict_handler():
    return {"prediction": []}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

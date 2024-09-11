from fastapi import FastAPI
import tensorflow as tf
import numpy as np
from memory_profiler import profile

app = FastAPI()

# Load the TensorFlow model
model = tf.keras.models.load_model("simple_model.keras")


def predict(input_data):
    # Perform prediction using the loaded model
    prediction = model.predict(input_data)
    return prediction

@profile
@app.post("/predict")
async def predict_handler():
    # Generate random input data (784 features)
    input_data = np.random.rand(1, 784)
    # Call the memory-intensive prediction function
    prediction = predict(input_data)
    b = [2] * (2 * 10 ** 7)
    del b
    return {"prediction": prediction.tolist()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow import keras
import tensorflow as tf
import os
import numpy as np
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Make sure it allows all the requests for the CORSMiddleware.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ANIMALS = ["Cat", "Dog", "Panda"]

# It would've been better to use an environment variable to fix this line actually...
model_path = os.getenv("MODEL_PATH")
print(model_path)
model = tf.keras.models.load_model(model_path)


@app.post('/upload/image')
async def uploadImage(img: UploadFile = File(...)):
    original_image = Image.open(img.file)
    resized_image = original_image.resize((64,64))
    images_to_predict = np.expand_dims(np.array(resized_image), axis=0)
    predictions = model.predict(images_to_predict)
    prediction_probabilities = predictions
    classifications = prediction_probabilities.argmax(axis=1)

    print(predictions)
    print(classifications)
    print(classifications.tolist()[0])

    return ANIMALS[classifications.tolist()[0]]




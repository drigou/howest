from tensorflow import keras
import os

model_path = os.path.join(os.getcwd(), "inference", "animal-classification", "INPUT_model_path", "animal-cnn", "model.keras")
model = keras.models.load_model(model_path)

target_dir = os.path.join(os.getcwd(), "inference", "huggingface", "unpacked_keras")
model.save(target_dir, zipped=False)


# …or push directly to your Hub repo (auto-creates it for you):
# model.save("hf://drgou/howest-deployathome")
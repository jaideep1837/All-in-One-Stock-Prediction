import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import pickle

def get_predictions(sym, days):
    if sym =="RELIANCE.NS":
        model = load_model("reliance.keras")
        with open("RELIANCE.pkl", "rb") as f:
            scaler = pickle.load(f)
    elif sym=="TCS.NS":
        model = load_model("tcs.keras")
        with open("TCS.pkl", "rb") as f:
            scaler = pickle.load(f)
    elif sym=="HDFCBANK.NS":
        model = load_model("hdfcbank.keras")
        with open("HDFCBANK.pkl", "rb") as f:
            scaler = pickle.load(f)
    elif sym=="INFY.NS":
        model = load_model("INFY.keras")
        with open("INFY.pkl", "rb") as f:
            scaler = pickle.load(f)
        inputs = pd.read_csv("INFY.csv")
        inputs = np.array(inputs['0'])

    future = []

    for _ in range(days):
        inputs = inputs.reshape(-1,1)
        inputs = inputs.reshape((1, 100, 1))
        output = model.predict(inputs, verbose=0)
        
        future.append(scaler.inverse_transform(output)[0][0])
        
        inputs = list(inputs.ravel())
        inputs.append(output[0][0])
        inputs = inputs[1:]
        inputs = np.array(inputs)
    
    return future
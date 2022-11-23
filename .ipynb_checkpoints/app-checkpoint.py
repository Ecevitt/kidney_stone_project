import os
import pandas as pd
from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("aboutdata.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        if prediction ==1:
                 return render_template("stonespos.html",
                                        prediction_text1 = 
                                        "Your test results indicate the presence of kidney stones.We recommend that you consult your doctor with your urine test values") 
        elif prediction==0:
                return render_template("stonesneg.html",prediction_text2 = "Your test results indicate the absence of kidney stones.We wish you healthy days" )
    except ValueError:
        return  render_template("stoneswrong.html",prediction_text3 = "Please fill the form with numeric values otherwise calculation cannot be done" )
            
if __name__ == "__main__":
    app.run(debug=True)
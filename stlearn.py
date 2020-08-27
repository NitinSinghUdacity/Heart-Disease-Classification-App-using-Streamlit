# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:06:17 2020

@author: Nitin Singh
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle

from PIL import Image
pickle_in=open("rf.pkl","rb")
rf=pickle.load(pickle_in)

def heart_disease_predictor(thalach,ca ,slope,thal,sex,age ,trestbps,restecg ,chol ,fbs ,cp,exang,oldpeak  ):
    prediction=rf.predict([[thalach,ca ,slope,thal,sex,age ,trestbps,restecg ,chol ,fbs,cp,exang,oldpeak ]])
    print(prediction)
    return prediction
def main():
    st.title("Heart Disease Classification")
    thalach=st.text_input("maximum heart rate achieved(Thalach)","Type Here")
    ca=st.text_input("No. of Major Vessels(ca)","Type Here")
    slope=st.text_input("Slope","Type Here")
    thal=st.text_input("Thal","Type Here")
    sex=st.text_input("Sex","Type Here")
    age=st.text_input("Age","Type Here")
    trestbps=st.text_input("resting blood pressure(Trestbps)","Type Here")
    restecg=st.text_input("Resting ECG(restecg)","Type Here")
    chol=st.text_input("Cholestrol(chol)","Type Here")
    fbs=st.text_input("fasting blood sugar(fbs)","Type Here")
    cp=st.text_input("chest pain type(cp)","Type Here")
    exang=st.text_input("exercise induced angina(exang)","Type Here")
    oldpeak=st.text_input("oldpeak","Type Here") 
    result=""
    if st.button("Predict"):
        result=heart_disease_predictor(thalach, ca, slope, thal, sex, age, trestbps, restecg, chol, fbs, cp, exang, oldpeak)
    st.success("The Output {}".format(result))
    if st.button("About"):
        st.text("Build with StreamLit")
if __name__=="__main__":
    main()
    
    
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:58:13 2023

@author: Pooja Sahu
"""

import numpy as np
import pickle 
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/Sujal Sahu/anaconda3/envs/MachineLearning/trained_model.sav', 'rb'))


def Motor_speed_prediction(input_data):
    input_data_asarray=np.asarray(input_data)
    input_data_reshaped=input_data_asarray.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    return prediction


def main():
    
    
#giving a title
    st.title("Motor Speed Prediction Web app")
    
    #getting input data from the user

    ambient= st.text_input("Ambient temperature")
    coolant= st.text_input("Coolant temperature")
    u_d= st.text_input("Direct axis voltage")
    u_q= st.text_input("Quadrature axis voltage")
    i_d= st.text_input("Direct axis current")
    pm= st.text_input("PM")
    stator_winding= st.text_input("Stator temperature")
    
    
    #code for prediction
    empty_string = ''
    
    #Creating a button for prediction
    if st.button('Motor speed prediction'):
        empty_string = Motor_speed_prediction([ambient,coolant,u_d,u_q,i_d,pm,stator_winding])
    st.success(empty_string)



if __name__ == '__main__':
    main()
    



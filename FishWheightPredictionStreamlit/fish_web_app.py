import streamlit as st
import pandas as pd
import pickle

st.write("""
# Fish Wheight Prediction

### Let's predict Fishes Weight by only using some biological features!!!
         """)
         
         

st.write("")
#read the data from the user
st.sidebar.header("User Input Features")
def user_input():
    Length1 = st.sidebar.slider("Length1", 0.0, 59.000000)
    Height = st.sidebar.slider("Height", 0.0, 18.957000)
    Width = st.sidebar.slider("Width", 0.0, 8.142000)
    
    features = {"Length1": Length1, "Height":Height, "Width":Width}
    data = pd.DataFrame(features, index=[0])
    return data

input_in = user_input() 

st.write("Lenghth")
st.line_chart([0.0, 7.500000, 26.247170, 59.000000])

st.write("Height")
st.line_chart([0.0, 1.728400, 8.970994, 18.957000])

st.write("Width")
st.line_chart([0.0, 1.047600,4.417486, 8.142000])



st.subheader("User Input")
st.write(input_in)

#read the model 
load_model = pickle.load(open('myModel2.pkl', 'rb'))
pred = load_model.predict(input_in)

st.subheader("The Wheight prediction is")
st.write(pred)


    

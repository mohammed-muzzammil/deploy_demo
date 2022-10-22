import streamlit as st
import pickle

# Title
st.title("Salary Predictor")
# file path for streamlit share

# Loading the ml model
file = open("/Users/macbook/Downloads/Model.pkl", "rb")
regressor = pickle.load(file)

# Input to take Years of Experience
yoe = st.sidebar.slider("Years of Experience", min_value=0, max_value=50, step=1)

if st.sidebar.button("Predict"):
    # Predict the salary
    salary = regressor.predict([[yoe]])
    st.write("Predicted Salary is: {}".format(salary[0]))

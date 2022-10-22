import streamlit as st
import pickle

#"/app/{repository name}/ {file.extension}"
Pkl_Filename = "/app/deploy_demo/Model.pkl"

#with open('model_pkl', 'wb') as files:
 #   pickle.dump(model, files)

# Load the Model back from file
file = open(Pkl_Filename, 'rb')
Regressor_model = pickle.load(file)
file.close()


st.title('Salary Prediction Model')

yoe = st.sidebar.slider('Years of Expirience', 18, 60)

if st.sidebar.button('Predict'):
    output = Regressor_model.predict([[yoe]])
    st.write('The Predicted Salary is {}'.format(output))
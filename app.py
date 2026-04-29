import streamlit as st
import joblib
import numpy as np

#Chargement du modèle
model = joblib.load("model_random_forest.pkl")

st.title("Prédiction du risque d'abandon scolaire")

#Inputs utilisateur

age = st.slider("Age",15,30)
grade = st.slider("Moyenne",0.0, 20.20)
absent = st.slider("Absentéisme", 0.0, 0.5)
study = st.slider("Temps d'étude", 0.0, 5.0)
gender = st.selectbox("Le sexe de l'étudiant", [0,1])
internet_access = st.selectbox("Internet", [0,1])
extra_activities = st.selectbox("Activités extrascol",[0,1] )
vulnerability_score = st.selectbox("Score de vulnérabilité", [0,1,2,])
 



if st.button("Prédire"):
    data = np.array([[age,grade,absent,study,gender,internet_access,extra_activities,vulnerability_score]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Risque d'abandon")
    else:
        st.success("Pas de risque")
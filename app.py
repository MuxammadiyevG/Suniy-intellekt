import streamlit as st
import pickle

st.header("Doctor")
page_description = """Bu model sizda diabet kasalligi bor yo'qligini tekshira oladi"""
st.markdown(page_description)

model_file_path = "diabetes_model.pkl" 
model = None
pregnancies = st.number_input("Homiladorlik", min_value=0, max_value=20, step=1, value=0)
glucose = st.number_input("Qondagi glyukoza darajasi", min_value=0, max_value=200, step=1, value=0)
blood_pressure = st.number_input("Qon bosimi", min_value=0, max_value=150, step=1, value=0)
skin_thickness = st.number_input("Terining qalinligi", min_value=0, max_value=100, step=1, value=0)
insulin = st.number_input("Insulin darajasi", min_value=0, max_value=900, step=1, value=0)
bmi = st.number_input("Tana massasi indeksi(BMI)", min_value=0.0, max_value=100.0, step=0.001, value=0.0)
diabetes_pedigree_function = st.number_input("Diabetning nasliy ehtimoli", min_value=0.0, max_value=2.5, step=0.001, value=0.0)
age = st.number_input("Yosh", min_value=0, max_value=120, step=1, value=0)

with open("diabetes_model.pkl","rb") as fl:
    pr=pickle.load(fl)
    
if st.button("Tekshirish "):
    diabet_natija=pr.predict([[pregnancies	,glucose,	blood_pressure	,skin_thickness	,insulin,	bmi	,diabetes_pedigree_function	,age]])
    if(diabet_natija==1):
        st.write("Sizda diabet kasalligi mavjud")
    else:
        st.write("Sizda diabet kasalligi yo'q")
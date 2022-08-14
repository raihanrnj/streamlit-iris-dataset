# CALCULATOR SEDERHANA
import streamlit as st

st.title("Contoh Program Kalkulator penjumlahan")

st.write("""

  # Contoh Program Kalkulator penjumlahan

  Yuk tengok

  """)

bil1 = st.number_input("Masukkan angka pertama", 0)
bil2 = st.number_input("Masukkan angka kedua", 0)
hitung = st.button("Hitung Penjumlahan")

if hitung:
  total = bil1 + bil2
  st.success(f"Hasil Penjumlahan adalah : {total}")
  st.balloons()


# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# PAKAI INPUTAN
import streamlit as st
import pandas as pd
import joblib

#Loading Our final trained Knn model 
model= open("Knn_Classifier.pkl", "rb")
knn_clf=joblib.load(model)


st.title("Iris flower species Classification App")

st.sidebar.title("Features")

#Intializing
parameter_list=['Sepal length (cm)','Sepal Width (cm)','Petal length (cm)','Petal Width (cm)']
parameter_input_values=[]
parameter_default_values=['5.2','3.2','4.2','1.2']

sep_len = st.sidebar.number_input('Sepal length (cm)')
sep_wid = st.sidebar.number_input('Sepal Width (cm)')
pet_len = st.sidebar.number_input('Petal length (cm)')
pet_wid = st.sidebar.number_input('Petal Width (cm)')

parameter_input_values=[sep_len,sep_wid,pet_len,pet_wid]


input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
st.write('\n\n')

if st.button("Click Here to Classify"):
  prediction = knn_clf.predict(input_variables)
  st.write(str(prediction[0]))




# PAKAI SLIDER


import streamlit as st
import pandas as pd
import joblib
from PIL import Image

#Loading Our final trained Knn model 
model= open("Knn_Classifier.pkl", "rb")
knn_clf=joblib.load(model)


st.title("Iris flower species Classification App")

#Loading images

setosa= Image.open('setosa.png')
versicolor= Image.open('versicolor.png')
virginica = Image.open('virginica.png')

st.sidebar.title("Features")

#Intializing
parameter_list=['Sepal length (cm)','Sepal Width (cm)','Petal length (cm)','Petal Width (cm)']
parameter_input_values=[]
parameter_default_values=['5.2','3.2','4.2','1.2']

values=[]

#Display
for parameter, parameter_df in zip(parameter_list, parameter_default_values):
  
  values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=8.0, step=0.1)
  parameter_input_values.append(values)
  
input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
st.write('\n\n')

if st.button("Click Here to Classify"):
  prediction = knn_clf.predict(input_variables)
  st.write(str(prediction[0]))
  if prediction == 'versicolor':
    st.image(versicolor)
  elif prediction == 'setosa':
    st.image(setosa)
  elif prediction == 'virginica':
    st.image(virginica)

  # st.image(setosa) if prediction == 0 else st.image(versicolor)  if prediction == 1 else st.image(virginica) 
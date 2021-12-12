import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression


model = pickle.load(open('logistic_regression_model.pkl', 'rb'))

#model = pickle.load(open(r'c:\Users\richa\OneDrive\Documents\Analytics\Proyectos\VS\hello_ds\Nala\logistic_regression_model.pkl','rb'))


st.title('Detector de Fraudes')
st.write('En el banco XYZ somos conscientes de la importancia de la seguridad en las transacciones de nuestros clientes y locales asociados.\
         Para garantizar la máxima seguridad, hemos creado esta aplicación para detectar fraudes en transacciones.\
         Simplemente arrastre las barras laterales hasta el valor deseado y podrá ver la probabilidad de que la transacción sea fraudulenta."')

vars = ['monto', 'hora', 'percent_disc', 'percent_cashback', 'device_score', 'linea_tc', 'mes']

list_linea_tc = [71000, 94000, 55000, 62000, 83000, 33000, 39000, 72000, 76000,
       44000, 81000, 64000, 34000, 67000, 87000, 65000, 28000, 27000,
       99000, 73000, 63000, 50000, 46000, 85000, 52000, 38000, 84000,
       37000, 30000, 61000, 89000, 86000, 35000, 66000, 25000, 58000,
       41000, 59000, 60000, 57000, 97000, 80000, 69000, 40000, 49000,
       96000, 91000, 74000, 43000, 26000, 93000, 51000, 98000, 53000,
       88000, 82000, 42000, 29000, 32000, 70000, 31000, 56000, 45000,
       92000, 54000, 36000, 77000, 47000, 90000, 75000, 68000, 48000,
       78000, 95000, 79000]

meses = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]

list_linea_tc.sort()


st.sidebar.title('Parámetros')

monto = st.sidebar.slider(label = 'Monto', min_value = 0.01,
                          max_value = 1000.0 ,
                          value = 500.0,
                          step = 10.0)

hora = st.sidebar.slider(label = 'Hora', min_value = 1.0,
                          max_value = 24.0 ,
                          value = 1.0,
                          step = 1.0)
                          
percent_disc = st.sidebar.slider(label = 'Porcentaje de Descuento', min_value = 0.0,
                          max_value = 20.0 ,
                          value = 0.0,
                          step = 1.0)                          

percent_cashback = st.sidebar.slider(label = 'Porcentaje de Cashback', min_value = 0.0,
                          max_value = 2.0 ,
                          value = 0.0,
                          step = 0.1)

device_score = st.sidebar.slider(label = 'Puntuación del Dispositivo', min_value= 1.0,
                                 max_value= 5.0,
                                 value = 1.0,
                                 step = 1.0)

linea_tc = st.sidebar.selectbox('Seleccione la Línea de Tarjeta de Crédito', list_linea_tc)


mes = st.sidebar.selectbox('Seleccione el Mes', meses)

features = {'monto': monto, 'hora': hora, 'percent_disc': percent_disc, 'percent_cashback': percent_cashback, 'device_score': device_score, 'linea_tc': linea_tc, 'mes':mes}

features_df = pd.DataFrame([features])

st.table(features_df)

prediction = model.predict(features_df)

prediction_prob = model.predict_proba(features_df)

#Mostrar la prediccion
st.subheader('La transacción tiene un {}% de probabilidad de ser fraude'.format(round(prediction_prob[0][1]*100 , 3)))


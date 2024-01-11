import streamlit as st 

st.title('Suma tres números')

st.write('## Usando `st.number_input`')

num1 = st.number_input('Dime el 1º num: ',step=1)
num2 = st.number_input('Dime el 2º num: ',step=1)
num3 = st.number_input('Dime el 3º num: ',step=1)

st.write('La suma de los tres números es ',num1+num2+num3)


st.write('## Usando `st.slider`')

n1 = st.slider('Dime el 1º num: ')
n2 = st.slider('Dime el 2º num: ')
n3 = st.slider('Dime el 3º num: ')

st.write('La suma de los tres números es ',n1+n2+n3)

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import Panel
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler, scale
from keras import initializers






def app():

  # Define a custom initializer
  orthogonal_initializer = initializers.Orthogonal(gain=1.0, seed=None)

  model = load_model('Stock Market Price Predicter.keras', custom_objects={'Orthogonal': orthogonal_initializer})	
  
  #model= load_model('Stock Market Price Predicter.keras')

  st.title('Welcome To:green[ Stock Market Price Predicter! ]')

  stock = st.text_input('Enter Stock Symbol', 'GOOG')

  start = '2012-01-01'
  end = '2024-04-01'

  data = yf.download(stock,start,end)

  st.subheader(f' {stock} Stock Data')
  st.write(data)

  data_train = pd.DataFrame(data.Close[0:int(len(data)*0.80)])
  data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])

  

   
  scaler = MinMaxScaler(feature_range=(0,1))
  pass_100_days = data_train.tail(100)
  data_test = pd.concat([pass_100_days,data_test], ignore_index=True)
  
  data_test_scaled = scaler.fit_transform(data_test)

  st.subheader('Original Stock Price vs Moving Average 100')
  ma_100_days = data.Close.rolling(100).mean()
  fig1 = plt.figure(figsize=(10,8))
  plt.plot(ma_100_days, 'b',label = 'Moving average 100 days')
  plt.plot(data.Close, 'r',label = 'Original Stock price' )
  plt.xlabel('Year')
  plt.ylabel('Stock Price')
  plt.legend()
  plt.show()
  st.pyplot(fig1)

  st.subheader('Original Stock Price vs Moving Average 200')
  ma_200_days = data.Close.rolling(200).mean()
  fig2 = plt.figure(figsize=(10,8))
  plt.plot(ma_200_days, 'b',label = 'Moving average 200 days')
  plt.plot(data.Close, 'y',label = 'Original Stock price')
  plt.xlabel('Year')
  plt.ylabel('Stock Price')
  plt.legend()
  plt.show()
  st.pyplot(fig2)
  
  

  x = []
  y = []

  for i in range(100,data_test_scaled.shape[0]):
		 x.append(data_test_scaled[i-100:i])
		 y.append(data_test_scaled[i,0])


  x,y = np.array(x), np.array(y)

  predict = model.predict(x)

  scale = 1/scaler.scale_

  predict = predict * scale
  y = y * scale

  st.subheader('Original Stock Price vs Predicted Stock Price')
  fig3 = plt.figure(figsize=(10,8))
  plt.plot(predict, 'b', label='Predicted Stock Price')
  plt.plot(y, 'g', label='Original Stock Price')
  plt.xlabel('Time')
  plt.ylabel('Stock Price')
  plt.legend()
  plt.show()
  st.pyplot(fig3)





   





	
    

     
     




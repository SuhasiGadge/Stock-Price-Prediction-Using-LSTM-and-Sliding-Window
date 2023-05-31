import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from datetime import datetime, date
from keras.models import load_model
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import wikipedia



page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1640340434855-6084b1f4901c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8dHJhZGluZ3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60");
background-size: cover;
}

[data-testid = "stSidebar"] {
background-image: url("https://images.unsplash.com/photo-1651347589091-8f9f43a1e42c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80");
background-position : bottom;

}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.success("Select a page above.")
# Set the page title
st.title("Company Overview")



stock_tickers = ["ADANIENT.NS", "ADANIPORTS.NS", "APOLLOHOSP.NS", "ASIANPAINT.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS",
                 "BPCL.NS", "BHARTIARTL.NS", "BRITANNIA.NS", "CIPLA.NS", "COALINDIA.NS", "DIVISLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS",
                 "HCLTECH.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HINDUNILVR.NS", "HDFC.NS", "ICICIBANK.NS",
                 "ITC.NS", "INDUSINDBK.NS", "INFY.NS", "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS", "M&M.NS", "MARUTI.NS", "NTPC.NS","NESTLEIND.NS",
                 "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS", "SBILIFE.NS", "SBIN.NS", "SUNPHARMA.NS", "TCS.NS", "TATACONSUM.NS", "TATAMOTORS.NS",
                 "TATASTEEL.NS", "TECHM.NS", "TITAN.NS", "UPL.NS", "ULTRACEMCO.NS", "WIPRO.NS"]

st.subheader ('Summary')
st.text_area (wikipedia.summary("National Stock Exchange India"))
user_input = st.selectbox ("Select Stock Ticker", options= stock_tickers)
#user_input = st.text_input('Enter Stock Ticker', 'RELIANCE.NS')

start_date = '2013-1-29'
end_date = datetime.today().date()

# Download the data
data = yf.download(tickers=user_input, start= start_date, end= end_date, interval='1d')

# Display the data
st.subheader("Stock Data For "+ user_input)
st.write(data.tail())

# Plot the opening prices
st.subheader("Opening Prices For "+ user_input)
st.line_chart(data['Open'])

# Preprocess the data
opn = data[['Open']]
ds = opn.values

normalizer = MinMaxScaler(feature_range=(0, 1))
ds_scaled = normalizer.fit_transform(np.array(ds).reshape(-1, 1))

# Split the data into training and testing sets
train_size = int(len(ds_scaled) * 0.70)
test_size = len(ds_scaled) - train_size
ds_train, ds_test = ds_scaled[0:train_size, :], ds_scaled[train_size:len(ds_scaled), :1]

# Create the training and testing datasets
def create_ds(dataset, step):
    Xtrain, Ytrain = [], []
    for i in range(len(dataset) - step - 1):
        a = dataset[i:(i + step), 0]
        Xtrain.append(a)
        Ytrain.append(dataset[i + step, 0])
    return np.array(Xtrain), np.array(Ytrain)

time_stamp = 100
X_train, y_train = create_ds(ds_train, time_stamp)
X_test, y_test = create_ds(ds_test, time_stamp)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

from keras.models import load_model
model = tf.keras.models.load_model('stocks.h5', compile=False)
model.compile( 
   loss = None, 
   metrics = None, 
   loss_weights = None, 
   sample_weight_mode = None, 
   weighted_metrics = None, 
   target_tensors = None)


plot_new=np.arange(1,101)
plot_pred=np.arange(101,106)

# Make future predictions
fut_inp = ds_test[664:]
fut_inp = fut_inp.reshape(1, -1)
tmp_inp = list(fut_inp)
tmp_inp = tmp_inp[0].tolist()
lst_output = []
n_steps = 100
i = 0

while i < 5:
    if len(tmp_inp) > 100:
        fut_inp = np.array(tmp_inp[1:])
        fut_inp = fut_inp.reshape(1, -1)
        fut_inp = fut_inp.reshape((1, n_steps, 1))
        yhat = model.predict(fut_inp, verbose=0)
        tmp_inp.extend(yhat[0].tolist())
        tmp_inp = tmp_inp[1:]
        lst_output.extend(yhat.tolist())
        i += 1
    else:
        fut_inp = fut_inp.reshape((1, n_steps, 1))
        yhat = model.predict(fut_inp, verbose=0)
        tmp_inp.extend(yhat[0].tolist())
        lst_output.extend(yhat.tolist())
        i += 1


# Combine the original data with the predicted prices
ds_new = ds_scaled.tolist()
ds_new.extend(lst_output)


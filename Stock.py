import streamlit as st
from datetime import date
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from alpha_vantage.timeseries import TimeSeries

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"  # Replace with your Alpha Vantage API key

st.title("Stock Prediction App")
stocks = ("AAPL", "GOOG", "MSFT", "GME", "TSLA")
selected_stock = st.selectbox("Select dataset for the prediction", stocks)

n_yrs = st.slider("Years of prediction:", 1, 5)
period = n_yrs * 365

@st.cache_data
def load_data(ticker):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=ticker, outputsize='full')
    data = data.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })
    data = data.sort_index()
    data.reset_index(inplace=True)
    data = data[data['date'] >= START]
    data = data.rename(columns={"date": "Date"})
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...done!")

st.subheader('Raw Data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text='Time Series Data', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Forecasting
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader("Forecast Data")
st.write(forecast.tail())

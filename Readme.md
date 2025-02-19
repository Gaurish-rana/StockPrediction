# Stock Price Prediction App

## Overview
This **Stock Price Prediction App** is a Streamlit-based web application that forecasts stock prices using **Facebook's Prophet** model. It fetches historical stock data from the **Alpha Vantage API** and predicts future stock prices based on user-selected stocks and forecasting periods.

## Features
- **Select Stock:** Choose from predefined stocks (AAPL, GOOG, MSFT, GME, TSLA).
- **Historical Data Visualization:** Displays raw stock data and interactive time-series plots.
- **Forecasting:** Uses **Prophet** to predict future stock prices.
- **Interactive Plots:** Provides dynamic visualization using **Plotly**.
- **User Control:** Users can select a forecasting period (1-5 years).

## Dependencies
To run this app, install the following Python packages:
```bash
pip install streamlit pandas prophet plotly alpha_vantage
```

## Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Gaurish-rana/StockPrediction.git
   cd stock-prediction-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up **Alpha Vantage API Key** in `secrets.toml` or as an environment variable.
4. Run the app:
   ```bash
   streamlit run stock.py
   ```

## Project Structure
```
stock-prediction-app/
│── stock.py             # Main script
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## How It Works
1. The app retrieves stock data from **Alpha Vantage**.
2. Data is processed and visualized using **Pandas** and **Plotly**.
3. **Prophet** is used to model stock prices and generate future predictions.
4. The app displays the forecast along with interactive charts.

## Future Enhancements
- Allow users to enter custom stock symbols.
- Integrate more data sources (Yahoo Finance, Google Finance).
- Improve UI with enhanced visualizations.
- Deploy to a cloud service (e.g., AWS, Heroku, Streamlit Cloud).

## License
This project is open-source and available under the **MIT License**.

---

Developed by Gaurish Rana 🚀


import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from helper import get_predictions

# Streamlit App Title
st.title("Stock Price Analysis")

# Predefined list of stock symbols
stock_options = {
    "Reliance Industries": "RELIANCE.NS",
    'Tata Consultancy Services (TCS)': 'TCS.NS',
    'HDFC Bank': 'HDFCBANK.NS',
    'Infosys': 'INFY.NS',
}

# Dropdown menu for stock selection
stock_name = st.selectbox("Choose a Stock", list(stock_options.keys()))
stock_symbol = stock_options[stock_name]  # Get the corresponding symbol

num_days = st.number_input("Enter Number of Days of Prediction", min_value=1, max_value=365, value=30)

# Fetch Stock Data
if st.button("Get Stock Data"):
    try:
        future = get_predictions(stock_symbol, num_days)

        st.success(f"Showing data for {stock_symbol} for next {num_days} days")
        
        # Matplotlib Plot
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(future, label="Close Price", color="blue")

        ax.set_title(f"Stock Price of {stock_symbol}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Stock Price (RS)")
        ax.legend()
        ax.grid(True)

        # Show the plot in Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error fetching data: {e}")

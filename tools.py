from langchain.tools import Tool
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import ta

def fetch_crypto_data(symbol, period="1mo"):
    crypto = yf.Ticker(symbol)
    history = crypto.history(period=period)
    return history.to_dict()  # Convert to dict for easier serialization

def analyze_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Implement news analysis logic here
    return "News analysis result"

def perform_technical_analysis(data):
    df = pd.DataFrame(data)
    df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
    df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
    # Implement more technical analysis logic here
    return df.to_dict()  # Convert to dict for easier serialization

# Create Tool objects
crypto_data_tool = Tool(
    name="Fetch Crypto Data",
    func=fetch_crypto_data,
    description="Fetches market data for cryptocurrencies"
)

news_analysis_tool = Tool(
    name="Analyze Crypto News",
    func=analyze_news,
    description="Analyzes recent crypto news articles"
)

technical_analysis_tool = Tool(
    name="Perform Technical Analysis",
    func=perform_technical_analysis,
    description="Performs technical analysis on crypto price charts"
)

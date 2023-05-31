import streamlit as st
import wikipedia

page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1640340434855-6084b1f4901c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8dHJhZGluZ3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60");
background-size: cover;
}
[data-testid = "stSidebar"] {
background-image: url("https://images.unsplash.com/photo-1651347589091-8f9f43a1e42c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80");
background-position : center;

}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.success("Select a page above.")

st.title("Resource Hub!")

import streamlit as st

#col1, col2, col3 = st.columns(3)

#with col1:
st.header("NSE Blogs")
st.text_area(wikipedia.summary('National Stock Exchange'))
st.write("Know More About It Here [NSE](https://www.nseindia.com/)")
st.write("Know More About It Here [NIFTY 50 LIVE](https://www.nseindia.com/products-services/indices-nifty50-index)")
st.write("Know More About It Here [INDICES](https://www.nseindia.com/market-data/live-market-indices)")



#with col2:
st.header("Market Overview")
st.text_area(wikipedia.summary('Stock Trading'))
st.write("Know More About It Here [Groww](https://groww.in/)")
st.write("Know More About It Here [Zerodha](https://zerodha.com/)")
st.write("Know More About It Here [Moneycontrol](https://www.moneycontrol.com/)")



#with col3:
st.header("Financial News")
st.text_area(wikipedia.summary('India Finance News'))
st.write("Know More About It Here [YahooFinance](https://finance.yahoo.com/)")
st.write("Know More About It Here [EconomicTimes](https://m.economictimes.com/)")
st.write("Know More About It Here [FinancialExpress](https://www.financialexpress.com/)")
st.write("Know More About It Here [Live Mint](https://www.livemint.com/)")

  
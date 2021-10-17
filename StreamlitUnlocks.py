# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go
#
# df1 = pd.read_csv(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Not Ordered.csv')
# df2 = pd.read_excel(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Grouped by Date.xlsx')
#
# st.title('VSO Unlocks Dashboard')
#
# st.subheader('VSO unlocks by date')
# st.write(df2)
#
# st.subheader('VSO unlock amount by days until unlock')
# st.bar_chart(df2['VSO Amount'])
#
# st.subheader('Cummulative VSO unlocks')
# st.bar_chart(df2['Cummulative VSO Unlocks'])

#######################################################################################################################################

import requests
import json
import streamlit as st
import pandas as pd
import numpy as np
# from pycoingecko import CoinGeckoAPI


url = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=verso&order=market_cap_desc&per_page=100&page=1&sparkline=false', headers={'accept':'application/json'})
current_price = url.json()[0]['current_price']
price_change_percentage_24h = url.json()[0]['price_change_percentage_24h']
market_cap = url.json()[0]['market_cap']
circulating_supply = url.json()[0]['circulating_supply']
fdv = url.json()[0]['fully_diluted_valuation']
total_volume = url.json()[0]['total_volume']


# calling the API directly instead of using requests and url
# cg = CoinGeckoAPI()
# print(cg.get_coins_markets(ids='verso', vs_currency='usd'))


# page layout
st.set_page_config(page_title = 'Streamlit Dashboard',
    layout='wide',
    page_icon='💹')


### market data

st.title("Verso Unlocks Dashboard")

st.markdown("## Market Data")

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi = st.columns(5)

with first_kpi:
    st.markdown("**VSO Current Price**")
    number1 = current_price
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Price Change Percentage 24h**")
    number2 = str(price_change_percentage_24h) + '%'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Market Capitalization**")
    number3 = market_cap
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Circulating Supply**")
    number4 = circulating_supply
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number4}</h1>", unsafe_allow_html=True)

with fifth_kpi:
    st.markdown("**Fully Diluted Valuation**")
    number5 = current_price * 100000000
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number5}</h1>", unsafe_allow_html=True)


### top row

st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Locked Tokens for Vesting")

first_kpi, second_kpi, third_kpi = st.columns(3)


with first_kpi:
    st.markdown("**Internal Addresses**")
    number1 = 111
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**External Addresses**")
    number2 = 222
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)


### second row

st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Circulating Supply")

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)


with first_kpi:
    st.markdown("**Internal Addresses**")
    number1 = 111
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**External Addresses**")
    number2 = 222
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Farms**")
    number3 = 333
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Pools**")
    number1 = 111
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)


st.markdown("## Chart Section: 1")

first_chart, second_chart = st.columns(2)


with first_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


st.markdown("## Chart Section: 2")

first_chart, second_chart = st.columns(2)


with first_chart:
    chart_data = pd.DataFrame(np.random.randn(100, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
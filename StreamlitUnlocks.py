# import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go
import numpy as np
import pandas as pd
import requests
import streamlit as st


# df1 = pd.read_csv(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Not Ordered.csv')
df2 = pd.read_csv(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Grouped by Days Until Unlock 20211017.csv')

print(df2.to_dict())

df = pd.DataFrame.from_dict({'VSO Amount': {0: 16866662, 1: 1791664, 2: 1004165, 3: 1791664, 4: 983332, 5: 1791664, 6: 983332, 7: 1791664, 8: 983332, 9: 1791664, 10: 983332, 11: 1791664, 12: 983332, 13: 1791664, 14: 983332, 15: 1791664, 16: 4150006, 17: 416665, 18: 416665, 19: 416665, 20: 416665},
                             'Days Until Unlock': {0: 0, 1: 14, 2: 15, 3: 44, 4: 45, 5: 75, 6: 76, 7: 106, 8: 107, 9: 134, 10: 135, 11: 165, 12: 166, 13: 195, 14: 196, 15: 226, 16: 227, 17: 256, 18: 287, 19: 318, 20: 348},
                             'Date of Unlock': {0: '10/17/2021', 1: '10/31/2021', 2: '11/1/2021', 3: '11/30/2021', 4: '12/1/2021', 5: '12/31/2021', 6: '1/1/2022', 7: '1/31/2022', 8: '2/1/2022', 9: '2/28/2022', 10: '3/1/2022', 11: '3/31/2022', 12: '4/1/2022', 13: '4/30/2022', 14: '5/1/2022', 15: '5/31/2022', 16: '6/1/2022', 17: '6/30/2022', 18: '7/31/2022', 19: '8/31/2022', 20: '9/30/2022'},
                             'Cummulative VSO Unlocks': {0: 16866662, 1: 18658326, 2: 19662491, 3: 21454155, 4: 22437487, 5: 24229151, 6: 25212483, 7: 27004147, 8: 27987479, 9: 29779143, 10: 30762475, 11: 32554139, 12: 33537471, 13: 35329135, 14: 36312467, 15: 38104131, 16: 42254137, 17: 42670802, 18: 43087467, 19: 43504132, 20: 43920797}}
)

print(df.head)

#######################################################################################################################################



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

st.title("Verso Unlocks Dashboard")



# market data

st.markdown("## Market Data")

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi = st.columns(5)

with first_kpi:
    st.markdown("**VSO Current Price**")
    number1 = str(current_price) + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Price Change Percentage 24h**")
    number2 = str(price_change_percentage_24h) + '%'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Market Capitalization**")
    number3 = str(market_cap) + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Circulating Supply**")
    number4 = str(int(circulating_supply)) + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number4}</h1>", unsafe_allow_html=True)

with fifth_kpi:
    st.markdown("**Fully Diluted Valuation**")
    number5 = str(current_price * 100000000) + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number5}</h1>", unsafe_allow_html=True)


# top row

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


# second row

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


st.markdown("## VSO Unlock Schedule")

st.subheader('Dataset')
st.write(df)

st.subheader('VSO Unlocks per Date')
st.bar_chart(df.rename(columns={'Date of Unlock':'index'}).set_index('index')['VSO Amount'])

st.subheader('Cummulative VSO Unlocks per Date')
st.bar_chart(df.rename(columns={'Date of Unlock':'index'}).set_index('index')['Cummulative VSO Unlocks'])
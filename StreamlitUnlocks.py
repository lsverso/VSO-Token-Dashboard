import pandas as pd
# import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go


df1 = pd.read_csv(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Not Ordered.csv')
df2 = pd.read_excel(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Grouped by Date.xlsx')

print(df2.to_dict())

df = pd.DataFrame.from_dict({'VSO Amount': {0: 16866662, 1: 1791664, 2: 1004165, 3: 1791664, 4: 983332, 5: 1791664, 6: 983332, 7: 1791664, 8: 983332, 9: 1791664, 10: 983332, 11: 1791664, 12: 983332, 13: 1791664, 14: 983332, 15: 1791664, 16: 4150006, 17: 416665, 18: 416665, 19: 416665, 20: 416665}, 'Days Until Unlock': {0: 0, 1: 18, 2: 19, 3: 48, 4: 49, 5: 79, 6: 80, 7: 110, 8: 111, 9: 138, 10: 139, 11: 169, 12: 170, 13: 199, 14: 200, 15: 230, 16: 231, 17: 260, 18: 291, 19: 322, 20: 352},
                   'Unlock Date': {0: "Timestamp('2021-10-14 00:00:00')", 1: "Timestamp('2021-11-01 00:00:00')", 2: "Timestamp('2021-11-02 00:00:00')", 3: "Timestamp('2021-12-01 00:00:00')", 4: "Timestamp('2021-12-02 00:00:00')", 5: "Timestamp('2022-01-01 00:00:00')", 6: "Timestamp('2022-01-02 00:00:00')", 7: "Timestamp('2022-02-01 00:00:00')", 8: "Timestamp('2022-02-02 00:00:00')", 9: "Timestamp('2022-03-01 00:00:00')", 10: "Timestamp('2022-03-02 00:00:00')", 11: "Timestamp('2022-04-01 00:00:00')", 12: "Timestamp('2022-04-02 00:00:00')", 13: "Timestamp('2022-05-01 00:00:00')", 14: "Timestamp('2022-05-02 00:00:00')", 15: "Timestamp('2022-06-01 00:00:00')", 16: "Timestamp('2022-06-02 00:00:00')", 17: "Timestamp('2022-07-01 00:00:00')", 18: "Timestamp('2022-08-01 00:00:00')", 19: "Timestamp('2022-09-01 00:00:00')", 20: "Timestamp('2022-10-01 00:00:00')"},
                   'Cummulative VSO Unlocks': {0: 16866662, 1: 18658326, 2: 19662491, 3: 21454155, 4: 22437487, 5: 24229151, 6: 25212483, 7: 27004147, 8: 27987479, 9: 29779143, 10: 30762475, 11: 32554139, 12: 7471, 13: 35329135, 14: 36312467, 15: 38104131, 16: 42254137, 17: 42670802, 18: 43087467, 19: 43504132, 20: 43920797}})

print(df.head)

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

import numpy as np
import pandas as pd
import requests
import streamlit as st

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
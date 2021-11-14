import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import requests
import streamlit as st
import numpy as np
from pycoingecko import CoinGeckoAPI


# import and print latest VSO Unlock file to copy output and paste into the df variable that follows as a manually created dataframe
# df1 = pd.read_csv(r'F:\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Data - VSO Unlocks Ordered 20211102.csv')
# print(df1.to_dict())

df = pd.DataFrame.from_dict({'VSO Amount': {0: 170833, 1: 16666, 2: 12500, 3: 8333, 4: 208333, 5: 250000, 6: 250000, 7: 250000, 8: 250000, 9: 250000, 10: 916666, 11: 916666, 12: 916666, 13: 916666, 14: 916666, 15: 208333, 16: 208333, 17: 208333, 18: 208333, 19: 208333, 20: 1, 21: 1, 22: 158333, 23: 208333, 24: 208333, 25: 208333, 26: 208333, 27: 791666, 28: 10400000, 29: 33333, 30: 33333, 31: 33333, 32: 33333, 33: 33333, 34: 20833, 35: 170833, 36: 16666, 37: 12500, 38: 8333, 39: 208333, 40: 250000, 41: 916666, 42: 208333, 43: 791666, 44: 33333, 45: 158333, 46: 170833, 47: 16666, 48: 12500, 49: 8333, 50: 208333, 51: 250000, 52: 916666, 53: 208333, 54: 791666, 55: 33333, 56: 158333, 57: 170833, 58: 16666, 59: 12500, 60: 8333, 61: 208333, 62: 250000, 63: 916666, 64: 208333, 65: 791666, 66: 33333, 67: 158333, 68: 170833, 69: 16666, 70: 12500, 71: 8333, 72: 208333, 73: 250000, 74: 916666, 75: 208333, 76: 791666, 77: 33333, 78: 158333, 79: 170833, 80: 16666, 81: 12500, 82: 8333, 83: 208333, 84: 250000, 85: 916666, 86: 208333, 87: 791666, 88: 33333, 89: 158333, 90: 170833, 91: 16666, 92: 12500, 93: 8333, 94: 208333, 95: 250000, 96: 916666, 97: 208333, 98: 791666, 99: 33333, 100: 158333, 101: 170833, 102: 16666, 103: 12500, 104: 8333, 105: 208333, 106: 250000, 107: 916666, 108: 208333, 109: 3958338, 110: 33335, 111: 158333, 112: 170833, 113: 16666, 114: 12500, 115: 8333, 116: 208333, 117: 170833, 118: 16666, 119: 12500, 120: 8333, 121: 208333, 122: 170833, 123: 16666, 124: 12500, 125: 8333, 126: 208333, 127: 170833, 128: 16666, 129: 12500, 130: 8333, 131: 208333},
                             'Days Until Unlock': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 28, 36: 28, 37: 28, 38: 28, 39: 28, 40: 28, 41: 28, 42: 28, 43: 29, 44: 29, 45: 30, 46: 59, 47: 59, 48: 59, 49: 59, 50: 59, 51: 59, 52: 59, 53: 59, 54: 60, 55: 60, 56: 61, 57: 90, 58: 90, 59: 90, 60: 90, 61: 90, 62: 90, 63: 90, 64: 90, 65: 91, 66: 91, 67: 92, 68: 118, 69: 118, 70: 118, 71: 118, 72: 118, 73: 118, 74: 118, 75: 118, 76: 119, 77: 119, 78: 120, 79: 149, 80: 149, 81: 149, 82: 149, 83: 149, 84: 149, 85: 149, 86: 149, 87: 150, 88: 150, 89: 151, 90: 179, 91: 179, 92: 179, 93: 179, 94: 179, 95: 179, 96: 179, 97: 179, 98: 180, 99: 180, 100: 181, 101: 210, 102: 210, 103: 210, 104: 210, 105: 210, 106: 210, 107: 210, 108: 210, 109: 211, 110: 211, 111: 212, 112: 240, 113: 240, 114: 240, 115: 240, 116: 240, 117: 271, 118: 271, 119: 271, 120: 271, 121: 271, 122: 302, 123: 302, 124: 302, 125: 302, 126: 302, 127: 332, 128: 332, 129: 332, 130: 332, 131: 332},
                             'Date of Unlock': {0: '11/02/2021', 1: '11/02/2021', 2: '11/02/2021', 3: '11/02/2021', 4: '11/02/2021', 5: '11/02/2021', 6: '11/02/2021', 7: '11/02/2021', 8: '11/02/2021', 9: '11/02/2021', 10: '11/02/2021', 11: '11/02/2021', 12: '11/02/2021', 13: '11/02/2021', 14: '11/02/2021', 15: '11/02/2021', 16: '11/02/2021', 17: '11/02/2021', 18: '11/02/2021', 19: '11/02/2021', 20: '11/02/2021', 21: '11/02/2021', 22: '11/02/2021', 23: '11/02/2021', 24: '11/02/2021', 25: '11/02/2021', 26: '11/02/2021', 27: '11/02/2021', 28: '11/02/2021', 29: '11/02/2021', 30: '11/02/2021', 31: '11/02/2021', 32: '11/02/2021', 33: '11/02/2021', 34: '11/02/2021', 35: '11/30/2021', 36: '11/30/2021', 37: '11/30/2021', 38: '11/30/2021', 39: '11/30/2021', 40: '11/30/2021', 41: '11/30/2021', 42: '11/30/2021', 43: '12/01/2021', 44: '12/01/2021', 45: '12/02/2021', 46: '12/31/2021', 47: '12/31/2021', 48: '12/31/2021', 49: '12/31/2021', 50: '12/31/2021', 51: '12/31/2021', 52: '12/31/2021', 53: '12/31/2021', 54: '01/01/2022', 55: '01/01/2022', 56: '01/02/2022', 57: '01/31/2022', 58: '01/31/2022', 59: '01/31/2022', 60: '01/31/2022', 61: '01/31/2022', 62: '01/31/2022', 63: '01/31/2022', 64: '01/31/2022', 65: '02/01/2022', 66: '02/01/2022', 67: '02/02/2022', 68: '02/28/2022', 69: '02/28/2022', 70: '02/28/2022', 71: '02/28/2022', 72: '02/28/2022', 73: '02/28/2022', 74: '02/28/2022', 75: '02/28/2022', 76: '03/01/2022', 77: '03/01/2022', 78: '03/02/2022', 79: '03/31/2022', 80: '03/31/2022', 81: '03/31/2022', 82: '03/31/2022', 83: '03/31/2022', 84: '03/31/2022', 85: '03/31/2022', 86: '03/31/2022', 87: '04/01/2022', 88: '04/01/2022', 89: '04/02/2022', 90: '04/30/2022', 91: '04/30/2022', 92: '04/30/2022', 93: '04/30/2022', 94: '04/30/2022', 95: '04/30/2022', 96: '04/30/2022', 97: '04/30/2022', 98: '05/01/2022', 99: '05/01/2022', 100: '05/02/2022', 101: '05/31/2022', 102: '05/31/2022', 103: '05/31/2022', 104: '05/31/2022', 105: '05/31/2022', 106: '05/31/2022', 107: '05/31/2022', 108: '05/31/2022', 109: '06/01/2022', 110: '06/01/2022', 111: '06/02/2022', 112: '06/30/2022', 113: '06/30/2022', 114: '06/30/2022', 115: '06/30/2022', 116: '06/30/2022', 117: '07/31/2022', 118: '07/31/2022', 119: '07/31/2022', 120: '07/31/2022', 121: '07/31/2022', 122: '08/31/2022', 123: '08/31/2022', 124: '08/31/2022', 125: '08/31/2022', 126: '08/31/2022', 127: '09/30/2022', 128: '09/30/2022', 129: '09/30/2022', 130: '09/30/2022', 131: '09/30/2022'},
                             'Withdrawal Address': {0: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 1: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 2: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 3: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 4: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 5: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 6: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 7: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 8: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 9: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 10: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 11: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 12: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 13: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 14: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 15: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 16: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 17: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 18: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 19: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 20: '0xaE778784228B799fa9560ea24fDcda6795205F27', 21: '0x906935f4b42e632137504C0ea00D43C6442272bf', 22: '0xaE778784228B799fa9560ea24fDcda6795205F27', 23: '0xaE778784228B799fa9560ea24fDcda6795205F27', 24: '0xaE778784228B799fa9560ea24fDcda6795205F27', 25: '0xaE778784228B799fa9560ea24fDcda6795205F27', 26: '0xaE778784228B799fa9560ea24fDcda6795205F27', 27: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 28: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 29: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 30: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 31: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 32: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 33: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 34: '0xaE778784228B799fa9560ea24fDcda6795205F27', 35: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 36: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 37: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 38: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 39: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 40: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 41: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 42: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 43: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 44: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 45: '0xaE778784228B799fa9560ea24fDcda6795205F27', 46: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 47: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 48: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 49: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 50: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 51: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 52: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 53: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 54: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 55: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 56: '0xaE778784228B799fa9560ea24fDcda6795205F27', 57: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 58: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 59: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 60: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 61: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 62: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 63: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 64: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 65: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 66: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 67: '0xaE778784228B799fa9560ea24fDcda6795205F27', 68: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 69: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 70: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 71: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 72: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 73: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 74: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 75: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 76: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 77: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 78: '0xaE778784228B799fa9560ea24fDcda6795205F27', 79: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 80: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 81: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 82: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 83: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 84: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 85: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 86: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 87: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 88: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 89: '0xaE778784228B799fa9560ea24fDcda6795205F27', 90: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 91: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 92: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 93: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 94: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 95: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 96: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 97: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 98: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 99: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 100: '0xaE778784228B799fa9560ea24fDcda6795205F27', 101: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 102: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 103: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 104: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 105: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 106: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 107: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 108: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 109: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 110: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 111: '0xaE778784228B799fa9560ea24fDcda6795205F27', 112: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 113: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 114: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 115: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 116: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 117: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 118: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 119: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 120: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 121: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 122: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 123: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 124: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 125: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 126: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 127: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 128: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 129: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 130: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 131: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F'},
                             'Internal or External': {0: 'Internal', 1: 'External', 2: 'External', 3: 'External', 4: 'External', 5: 'Internal', 6: 'Internal', 7: 'Internal', 8: 'Internal', 9: 'Internal', 10: 'Internal', 11: 'Internal', 12: 'Internal', 13: 'Internal', 14: 'Internal', 15: 'External', 16: 'External', 17: 'External', 18: 'External', 19: 'External', 20: 'External', 21: 'Unknown', 22: 'External', 23: 'External', 24: 'External', 25: 'External', 26: 'External', 27: 'Internal', 28: 'Internal', 29: 'Unknown', 30: 'Unknown', 31: 'Unknown', 32: 'Unknown', 33: 'Unknown', 34: 'External', 35: 'Internal', 36: 'External', 37: 'External', 38: 'External', 39: 'External', 40: 'Internal', 41: 'Internal', 42: 'External', 43: 'Internal', 44: 'Unknown', 45: 'External', 46: 'Internal', 47: 'External', 48: 'External', 49: 'External', 50: 'External', 51: 'Internal', 52: 'Internal', 53: 'External', 54: 'Internal', 55: 'Unknown', 56: 'External', 57: 'Internal', 58: 'External', 59: 'External', 60: 'External', 61: 'External', 62: 'Internal', 63: 'Internal', 64: 'External', 65: 'Internal', 66: 'Unknown', 67: 'External', 68: 'Internal', 69: 'External', 70: 'External', 71: 'External', 72: 'External', 73: 'Internal', 74: 'Internal', 75: 'External', 76: 'Internal', 77: 'Unknown', 78: 'External', 79: 'Internal', 80: 'External', 81: 'External', 82: 'External', 83: 'External', 84: 'Internal', 85: 'Internal', 86: 'External', 87: 'Internal', 88: 'Unknown', 89: 'External', 90: 'Internal', 91: 'External', 92: 'External', 93: 'External', 94: 'External', 95: 'Internal', 96: 'Internal', 97: 'External', 98: 'Internal', 99: 'Unknown', 100: 'External', 101: 'Internal', 102: 'External', 103: 'External', 104: 'External', 105: 'External', 106: 'Internal', 107: 'Internal', 108: 'External', 109: 'Internal', 110: 'Unknown', 111: 'External', 112: 'Internal', 113: 'External', 114: 'External', 115: 'External', 116: 'External', 117: 'Internal', 118: 'External', 119: 'External', 120: 'External', 121: 'External', 122: 'Internal', 123: 'External', 124: 'External', 125: 'External', 126: 'External', 127: 'Internal', 128: 'External', 129: 'External', 130: 'External', 131: 'External'}})

# save dataframe to file
df.to_csv(r'F:\PycharmProjects\VSO-Token-Unlocks\Manually Built Pandas DataFrame.csv', index=False)


df['Date of Unlock'] = pd.to_datetime(df['Date of Unlock'])
pivot_table = df.pivot_table(index=['Date of Unlock', 'Internal or External'], values=['VSO Amount'], fill_value=0, aggfunc=np.sum)

pivot_table = df.pivot_table(index='Date of Unlock', columns='Internal or External', values='VSO Amount', aggfunc='sum', fill_value=0)


# get market data from coingecko's API and assign values to variables
url = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=verso&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=7d', headers={'accept':'application/json'})
current_price = url.json()[0]['current_price']
price_change_percentage_24h = url.json()[0]['price_change_percentage_24h']
price_changepercentage_7d = url.json()[0]['price_change_percentage_7d_in_currency']
market_cap = url.json()[0]['market_cap']
circulating_supply = url.json()[0]['circulating_supply']
fdv = url.json()[0]['fully_diluted_valuation']
total_volume = url.json()[0]['total_volume']


# calling VSO and AVAX pricing data from coingecko's API directly instead of using requests and url
cg = CoinGeckoAPI()
vso_prices = cg.get_coin_market_chart_by_id(id='verso', vs_currency='usd', days=30)
avax_prices = cg.get_coin_market_chart_by_id(id='avalanche-2', vs_currency='usd', days=30)


# create date and price dataframes for each token pair
df_vso = pd.DataFrame(vso_prices['prices'], columns=['Date', 'Price'])

# try to read all AVAX prices, and if code doesn't run it's because AVAX prices haven't updated as fast as VSO's, so in that case, run avax_prices['prices'][:-1]
try:
    df_avax = pd.DataFrame(avax_prices['prices'][:-1], columns=['Date', 'Price'])
    df_vso_avax = pd.DataFrame(np.array(df_vso['Price']) / np.array(df_avax['Price']),
                               columns=['Price'])  # VSO/AVAX pair

except:
    df_avax = pd.DataFrame(avax_prices['prices'], columns=['Date', 'Price'])
    df_vso_avax = pd.DataFrame(np.array(df_vso['Price'])/np.array(df_avax['Price']), columns=['Price']) # VSO/AVAX pair


# create date-indexed df for all tokens (one token per column)
df_token_prices = pd.DataFrame({'Date': df_vso['Date'], 'VSO/USD': df_vso['Price'], 'AVAX/USD': df_avax['Price'], 'VSO/AVAX': df_vso_avax['Price']})
df_token_prices = df_token_prices.set_index('Date')
df_token_prices.index = pd.to_datetime(df_token_prices.index, unit='ms')
# print(df_token_prices)


# calculate 7-day price percentage change
pd.set_option("display.max_rows", None, "display.max_columns", None)
vso_price_change_percentage_7_days = df_token_prices['VSO/USD'].pct_change()


# prepare variables for plotting later
colors = px.colors.qualitative.T10


# page layout
st.set_page_config(page_title = 'Streamlit Dashboard',
    layout='wide',
    page_icon='💹')

st.title("VSO Token Dashboard")


# market data
st.markdown("## Market Data")

first_kpi, second_kpi, third_kpi, fourth_kpi, = st.columns(4)

with first_kpi:
    st.markdown("**VSO Current Price**")
    number1 = str(current_price) + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)


with second_kpi:
    st.markdown("**Price Change 24h**")
    number2 = str(round(price_change_percentage_24h, 2)) + '%'
    if price_change_percentage_24h >= 0:
        st.markdown(f"<h1 style='text-align: left; color: darkgreen;'>{number2}</h1>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)


with third_kpi:
    st.markdown("**Price Change 7d**")
    number2 = str(round(price_changepercentage_7d, 2)) + '%'
    if price_changepercentage_7d >= 0:
        st.markdown(f"<h1 style='text-align: left; color: green;'>{number2}</h1>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)


with fourth_kpi:
    st.markdown("**Volume 24h**")
    number3 = str(f'{total_volume:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number3}</h1>", unsafe_allow_html=True)


fifth_kpi, sixth_kpi, seventh_kpi = st.columns(3)

st.text("")
st.text("")
st.text("")
st.text("")

with fifth_kpi:
    st.markdown("**Market Capitalization**")
    number3 = str(f'{market_cap:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number3}</h1>", unsafe_allow_html=True)

with sixth_kpi:
    st.markdown("**Circulating Supply**")
    number4 = str(f'{int(circulating_supply):,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number4}</h1>", unsafe_allow_html=True)

with seventh_kpi:
    st.markdown("**Fully Diluted Valuation**")
    number5 = str(f'{int(current_price * 100000000):,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number5}</h1>", unsafe_allow_html=True)


# TODO AVAX data

# plot token returns (percentage change)
st.markdown("<hr/>", unsafe_allow_html=True)


# Price Charts
st.markdown("## VSO Charts")

newnames = {'wide_variable_0': 'VSO/USD', 'wide_variable_1': 'AVAX/USD'} # prepare newnames variable for line chart labels renaming later

st.markdown("### Price Chart")

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]], print_grid=False)

# Add traces
fig.add_trace(
    go.Scatter(x=df_token_prices.index, y=df_token_prices['VSO/USD'], name="VSO/USD"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df_token_prices.index, y=df_token_prices['VSO/AVAX'], name="VSO/AVAX"),
    secondary_y=True
)

# Add figure title
fig.update_layout(
    height=400,
    width=750
)

# Set x-axis title
fig.update_xaxes(title_text="Date", showgrid=False)

# Set y-axes titles
fig.update_yaxes(title_text="VSO/USD Price", secondary_y=False)
fig.update_yaxes(title_text="VSO/AVAX Price", secondary_y=True, showgrid=False)

st.plotly_chart(fig)







# plot token cumulative returns (cumulative percentage change)
st.markdown("### Token Returns (cumulative percentage change)")

fig2 = px.line(df_token_prices,
             x = df_token_prices.index,
             y = [(df_token_prices['VSO/USD'].pct_change()+1).cumprod(), (df_token_prices['AVAX/USD'].pct_change()+1).cumprod()],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             height=400,
             width=750
             )

fig2.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     ))
st.plotly_chart(fig2)

# plot token returns (percentage change)
st.markdown("### Token Returns (percentage change)")

fig3 = px.line(df_token_prices,
             x = df_token_prices.index,
             y = [df_token_prices['VSO/USD'].pct_change(), df_token_prices['AVAX/USD'].pct_change()],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=400,
             width=750
             )

fig3.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     ))
st.plotly_chart(fig3)





st.markdown("## VSO Token Distribution")

# define variables for internal an external vested tokens
# TODO adjust static "today" date to dynamic "today"
internal_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'Internal') &(df['Date of Unlock'] >= '2021-11-02T00:00:00')].sum()
external_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'External') &(df['Date of Unlock'] >= '2021-11-02T00:00:00')].sum()
unknown_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'Unknown') & (df['Date of Unlock'] >= '2021-11-02T00:00:00')].sum()

external_locked_total = external_locked + unknown_locked




max_supply = 100000000

# circulating supply
# liquid_supply_internal =
# liquid_supply_external =
# liquid_supply = liquid_supply_internal + liquid_supply_external
#
# total_pools =
# total_farms =
# illiquid_supply =

# circ_supply = liquid_supply + illiquid_supply

# vested tokens
vested_tokens = internal_locked + external_locked_total

st.markdown("### Max Supply = Circulating Supply + Vested Tokens")
formula_value = str(f'{max_supply:,}') + ' = ' + str(f'{max_supply - vested_tokens:,}') + ' + ' + str(f'{vested_tokens:,}')
st.markdown("### " + formula_value)

st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("### Vested Tokens")

first_kpi, second_kpi = st.columns(2)

with first_kpi:
    st.markdown("**Total Locked VSO - Internal Addresses**")
    number1 = str(f'{internal_locked:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Total Locked VSO - External Addresses**")
    number2 = str(f'{external_locked_total:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number2}</h1>", unsafe_allow_html=True)


st.text("")
st.text("")
st.text("")
st.text("")

# Circulating Supply
st.markdown("### Circulating Supply")

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)


with first_kpi:
    st.markdown("**Internal Addresses**")
    number1 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**External Addresses**")
    number2 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Farms**")
    number3 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number3}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Pools**")
    number4 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number4}</h1>", unsafe_allow_html=True)


# VSO Unlock Schedule
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## VSO Unlock Schedule")

st.subheader('Dataset')
st.write(df)


# TODO add cumulative back to DataFrame
# st.subheader('Cumulative VSO Unlocks per Date')
# st.bar_chart(df.rename(columns={'Date of Unlock':'index'}).set_index('index')['Cumulative VSO Amount'])

# old way of plotting unlocks
pivot_chart = pivot_table.unstack().plot(kind='bar', stacked=True)
# print(pivot_chart)

# add bars
st.subheader('VSO Unlocks per Date')

pivot_table_subset = pivot_table[pivot_table.index > '2021-11-02T00:00:00']


fig = px.bar(pivot_table_subset,
             x = pivot_table_subset.index,
             y = [c for c in pivot_table_subset.columns],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=400,
             width=750
             )

fig.update_traces(marker_line_width=1.5)
# fig.update_layout(barmode='stack')
st.plotly_chart(fig)








# VSO Pool2s Numbers
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## VSO Pool2s Liquidity")
# load parameters for the covalenthq API url
API_KEY = 'ckey_e1328ce2b7104ccaa03d0955258'
chain_id = 43114
contract_address = '0x84cf8ef74974399b4473bcf474507fe9557250ab'
page_size = 200_000
payload = {
                "key": API_KEY,
                "page-size": page_size,
                "block-signed-at-asc": True
            }


# load VSO-ELK Pool on ELk Finance from covalenthq API
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_elk_finance['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_elk_finance['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'ELK':
        balance_elk = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_elk_finance['elk_balance'].append(balance_elk)

        quote_rate_elk = item['quote_rate']
        # df_elk_finance['elk_quote_rate'].append(quote_rate_elk)
        continue


st.markdown("### VSO-ELK Elk Finance")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{balance_vso:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**ELK Amount**")
    number1 = str(f'{balance_elk:,}') + ' ELK'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Total Liquidity in USD**")
    total_liq = float("{:.2f}".format((balance_vso * quote_rate_vso) + (balance_elk * quote_rate_elk)))
    number1 = str(f'{total_liq:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)


# load VSO-WAVAX Pool on Pangolin from covalenthq API
contract_address = '0x2b532bC0aFAe65dA57eccFB14ff46d16a12de5E6'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'WAVAX':
        balance_wavax = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_wavax = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue


st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("### VSO-WAVAX Pangolin")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{balance_vso:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**WAVAX Amount**")
    number1 = str(f'{balance_wavax:,}') + ' WAVAX'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Total Liquidity in USD**")
    total_liq = float("{:.2f}".format((balance_vso * quote_rate_vso) + (balance_wavax * quote_rate_wavax)))
    number1 = str(f'{total_liq:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)


# load PNG-VSO Pool on Pangolin from covalenthq API
contract_address = '0x9D472e21f6589380B21C42674B3585C47b74c891'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue


    if item['contract_ticker_symbol'] == 'PNG':
        balance_png = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_png = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue


st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("### PNG-VSO Pangolin")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{balance_vso:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**PNG Amount**")
    number1 = str(f'{balance_png:,}') + ' PNG'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Total Liquidity in USD**")
    total_liq = float("{:.2f}".format((balance_vso * quote_rate_vso) + (balance_png * quote_rate_png)))
    number1 = str(f'{total_liq:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)


# load VSO-WAVAX Pool on Lydia Finance from covalenthq API
contract_address = '0x4C9b23dFFF6a15cad84008ecf5B424B715D8E82C'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'WAVAX':
        balance_wavax = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_wavax = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue


st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("### VSO-WAVAX Lydia Finance")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{balance_vso:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**WAVAX Amount**")
    number1 = str(f'{balance_wavax:,}') + ' WAVAX'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Total Liquidity in USD**")
    total_liq = float("{:.2f}".format((balance_vso * quote_rate_vso) + (balance_wavax * quote_rate_wavax)))
    number1 = str(f'{total_liq:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)


# load VSO-WAVAX Pool on Trader Joe from covalenthq API
contract_address = '0x00979bd14bd5eb5c456c5478d3bf4b6e9212ba7d'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'WAVAX':
        balance_wavax = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_wavax = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue


# VSO Pool2s Numbers
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## VSO Farms and Staking Pools")
# load parameters for the covalenthq API url
API_KEY = 'ckey_e1328ce2b7104ccaa03d0955258'
chain_id = 43114
contract_address = '0xda420bd5f676da1c8cb620313b0ba6d93e963e5f'
page_size = 200_000
payload = {
                "key": API_KEY,
                "page-size": page_size,
                "block-signed-at-asc": True
            }



covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/transactions_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

transaction_list = []
# load data for pool contract address
items = url.json()['data']['items']
for item in items:
    log_events = item['log_events']

    # if the transaction is not a VSO transaction, skip to next log_event
    for log_event in log_events:
        if log_event['sender_contract_ticker_symbol'] != 'VSO':
            continue

        # create one dictionary per details/parameters of each transaction
        tx_params = {}

        block_height = log_event['block_height']
        tx_params['block_height'] = block_height

        tx_hash = log_event['tx_hash']
        tx_params['tx_hash'] = tx_hash
        # print(block_height, tx_hash)

        decoded = log_event['decoded']
        params = decoded['params']

        # some params objects are TypeNone, so skip those
        if params is None:
            continue

        # create for loop for each parameter (from (address), to (address), amount (value of VSO transaction))
        for param_dict in params:
            name = param_dict['name']

            if name == 'from':
                tx_params['from'] = param_dict['value']
                continue
            elif name == 'to':
                tx_params['to'] = param_dict['value']
                continue
            elif name == 'value':
                tx_params['amount'] = param_dict['value']

            # for each created dictionary of transaction parameters, add it to the empty list created in the beginning
            transaction_list.append(tx_params)

df = pd.DataFrame(transaction_list)

# reformat 'amount' column into floats
df['amount'] = [float("{:.2f}".format(float(item) / 10 ** 18)) for item in df['amount']]

# print(df.dropna().head())

grouped_txs = df['amount'].groupby(df['to']).sum()
total_outflows = []
for row in grouped_txs:
    if row > 1000000:
        total_inflows = row
    else:
        total_outflows.append(row)

total_outflows = sum(total_outflows)
balance = total_inflows - total_outflows

st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("### VSO 90-Day Lockup Staking Pool Trustswap")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{round(balance, 2):,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)







# load parameters for the covalenthq API url
API_KEY = 'ckey_e1328ce2b7104ccaa03d0955258'
chain_id = 43114
contract_address = '0xDa719fE5443a2EFD5a61Ceb11fcb2a02FCeb8923'
page_size = 200_000
payload = {
                "key": API_KEY,
                "page-size": page_size,
                "block-signed-at-asc": True
            }



covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/transactions_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

transaction_list = []
# load data for pool contract address
items = url.json()['data']['items']
for item in items:
    log_events = item['log_events']

    # if the transaction is not a VSO transaction, skip to next log_event
    for log_event in log_events:
        if log_event['sender_contract_ticker_symbol'] != 'VSO':
            continue

        # create one dictionary per details/parameters of each transaction
        tx_params = {}

        block_height = log_event['block_height']
        tx_params['block_height'] = block_height

        tx_hash = log_event['tx_hash']
        tx_params['tx_hash'] = tx_hash
        # print(block_height, tx_hash)

        decoded = log_event['decoded']
        params = decoded['params']

        # some params objects are TypeNone, so skip those
        if params is None:
            continue

        # create for loop for each parameter (from (address), to (address), amount (value of VSO transaction))
        for param_dict in params:
            name = param_dict['name']

            if name == 'from':
                tx_params['from'] = param_dict['value']
                continue
            elif name == 'to':
                tx_params['to'] = param_dict['value']
                continue
            elif name == 'value':
                tx_params['amount'] = param_dict['value']

            # for each created dictionary of transaction parameters, add it to the empty list created in the beginning
            transaction_list.append(tx_params)

df = pd.DataFrame(transaction_list)

# reformat 'amount' column into floats
df['amount'] = [float("{:.2f}".format(float(item) / 10 ** 18)) for item in df['amount']]

# print(df.dropna().head())

grouped_txs = df['amount'].groupby(df['to']).sum()
total_outflows = []
for row in grouped_txs:
    if row > 1000000:
        total_inflows = row
    else:
        total_outflows.append(row)

total_outflows = sum(total_outflows)
balance = total_inflows - total_outflows


st.markdown("### VSO Staking Pool Trustswap")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{round(balance, 2):,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)
print('hi')




# load SWAP-VSO Staking Pool on Trustswap
contract_address = '0x454d379Ba89EB7BdA6AAA0420B056bD03fcF012B'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'SWAP.e':
        balance_swap = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_swap = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue

st.markdown("### SWAP-VSO Staking Pool on Trustswap")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{round(balance_vso, 2):,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)
print('hi')


# load Verso Staking Pool on Trustswap
contract_address = '0xDa719fE5443a2EFD5a61Ceb11fcb2a02FCeb8923'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'SWAP.e':
        balance_swap = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_swap = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue

st.markdown("### SWAP-VSO Staking Pool on Trustswap")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{round(balance_vso, 2):,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: deepskyblue;'>{number1}</h1>", unsafe_allow_html=True)
print('hi')

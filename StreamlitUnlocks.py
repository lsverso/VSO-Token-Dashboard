import plotly.express as px
import pandas as pd
import requests
import streamlit as st
import numpy as np
from pycoingecko import CoinGeckoAPI



# import and print latest VSO Unlock file to copy output and paste into the df variable that follows as a manually created dataframe
# df1 = pd.read_csv(r'C:\Users\L.SCHEUER\OneDrive - Zurich Insurance\Escritorio\VSO Unlocks Not Ordered New Table.csv')
# print(df1.to_dict())

df = pd.DataFrame.from_dict({'VSO Amount': {0: 250000, 1: 250000, 2: 250000, 3: 250000, 4: 916666, 5: 916666, 6: 916666, 7: 916666, 8: 208333, 9: 208333, 10: 208333, 11: 208333, 12: 1, 13: 1, 14: 208333, 15: 208333, 16: 208333, 17: 208333, 18: 10400000, 19: 33333, 20: 33333, 21: 33333, 22: 33333, 23: 170833, 24: 16666, 25: 12500, 26: 8333, 27: 208333, 28: 250000, 29: 916666, 30: 208333, 31: 158333, 32: 791666, 33: 33333, 34: 20833, 35: 170833, 36: 16666, 37: 12500, 38: 8333, 39: 208333, 40: 250000, 41: 916666,42: 208333, 43: 158333, 44: 791666, 45: 33333, 46: 170833, 47: 16666, 48: 12500, 49: 8333, 50: 208333, 51: 250000, 52: 916666, 53: 208333, 54: 158333, 55: 791666, 56: 33333, 57: 170833, 58: 16666, 59: 12500, 60: 8333, 61: 208333, 62: 250000, 63: 916666, 64: 208333, 65: 158333, 66: 791666, 67: 33333, 68: 170833, 69: 16666, 70: 12500, 71: 8333, 72: 208333, 73: 250000, 74: 916666, 75: 208333, 76: 158333, 77: 791666, 78: 33333, 79: 170833, 80: 16666, 81: 12500, 82: 8333, 83: 208333, 84:250000, 85: 916666, 86: 208333, 87: 158333, 88: 791666, 89: 33333, 90: 170833, 91: 16666, 92: 12500, 93: 8333, 94: 208333, 95: 250000, 96: 916666, 97: 208333, 98: 158333, 99: 791666, 100: 33333, 101: 170833, 102: 16666, 103: 12500, 104: 8333, 105: 208333, 106: 250000, 107: 916666, 108: 208333, 109: 158333, 110: 3958338, 111: 33335, 112: 170833, 113: 16666, 114: 12500, 115: 8333, 116: 208333, 117: 170833, 118: 16666, 119: 12500, 120: 8333, 121: 208333, 122: 170833, 123: 16666, 124: 12500, 125: 8333, 126: 208333, 127: 170833, 128: 16666, 129: 12500, 130: 8333, 131: 208333},
                             'Days Until Unlock': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 14, 24: 14, 25: 14, 26: 14, 27: 14, 28: 14, 29: 14, 30: 14, 31: 15, 32: 15, 33: 15, 34: 15, 35: 44, 36: 44, 37: 44, 38: 44, 39: 44, 40: 44, 41: 44, 42: 44, 43: 45, 44: 45, 45: 45, 46: 75, 47: 75, 48: 75, 49: 75, 50: 75, 79: 165, 80: 165, 81: 165, 82: 165, 83: 165, 84: 165, 85: 165, 86: 165, 87: 166, 88: 166, 89: 166, 90: 195, 91: 195, 92: 195, 93: 195, 94: 195, 95: 195, 96: 195, 97: 195, 98: 196, 99: 196, 100: 196, 101: 226, 102: 226, 103: 226, 104: 226, 105: 226, 106: 226, 107: 226, 108: 226, 109: 227, 110: 227, 111: 227, 112: 256, 113: 256, 114: 256, 115: 256, 116: 256, 117: 287, 118: 287, 119: 287, 120: 287, 121: 287, 122: 318, 123: 318, 124: 318, 125: 318, 126: 318, 127: 348, 128: 348, 129: 348, 130: 348, 131: 348},
                             'Date of Unlock': {0: '10/17/2021', 1: '10/17/2021', 2: '10/17/2021', 3: '10/17/2021', 4: '10/17/2021', 5: '10/17/2021', 6: '10/17/2021', 7: '10/17/2021', 8: '10/17/2021', 9: '10/17/2021', 10: '10/17/2021', 11: '10/17/2021', 12: '10/17/2021', 13: '10/17/2021', 14: '10/17/2021', 15: '10/17/2021', 16: '10/17/2021', 17: '10/17/2021', 18: '10/17/2021', 19: '10/17/2021', 20: '10/17/2021', 21: '10/17/2021', 22: '10/17/2021', 23: '10/31/2021', 24: '10/31/2021', 25: '10/31/2021', 26: '10/31/2021', 27: '10/31/2021', 28: '10/31/2021', 29: '10/31/2021', 30: '10/31/2021', 31: '11/1/2021', 32: '11/1/2021', 33: '11/1/2021', 34: '11/1/2021', 35: '11/30/2021', 36: '11/30/2021', 37: '11/30/2021', 38: '11/30/2021', 39: '11/30/2021', 40: '11/30/2021', 41: '11/30/2021', 42: '11/30/2021', 43: '12/1/2021', 44: '12/1/2021', 45: '12/1/2021', 46: '12/31/2021', 47: '12/31/2021', 48: '12/31/2021', 49: '12/31/2021', 50: '12/31/2021', 51: '12/31/2021', 52: '12/31/2021', 53: '12/31/2021', 54: '1/1/2022', 55: '1/1/2022', 56: '1/1/2022', 57: '1/31/2022', 58: '1/31/2022', 59: '1/31/2022', 60: '1/31/2022', 61: '1/31/2022', 62: '1/31/2022', 63: '1/31/2022', 64: '1/31/2022', 65: '2/1/2022', 66: '2/1/2022', 67: '2/1/2022', 68: '2/28/2022', 69: '2/28/2022', 70: '2/28/2022', 71: '2/28/2022', 72: '2/28/2022', 73: '2/28/2022', 74: '2/28/2022', 75: '2/28/2022', 76: '3/1/2022', 77: '3/1/2022', 78: '3/1/2022', 79: '3/31/2022', 80: '3/31/2022', 81: '3/31/2022', 82: '3/31/2022', 83: '3/31/2022', 84: '3/31/2022', 85: '3/31/2022', 86: '3/31/2022', 87: '4/1/2022', 88: '4/1/2022', 89: '4/1/2022', 90: '4/30/2022', 91: '4/30/2022', 92: '4/30/2022', 93: '4/30/2022', 94: '4/30/2022', 95: '4/30/2022', 96: '4/30/2022', 97: '4/30/2022', 98: '5/1/2022', 99: '5/1/2022', 100: '5/1/2022', 101: '5/31/2022', 102: '5/31/2022', 103: '5/31/2022', 104: '5/31/2022', 105: '5/31/2022', 106: '5/31/2022', 107: '5/31/2022', 108: '5/31/2022', 109: '6/1/2022', 110: '6/1/2022', 111: '6/1/2022', 112: '6/30/2022', 113: '6/30/2022', 114: '6/30/2022', 115: '6/30/2022', 116: '6/30/2022', 117: '7/31/2022', 118: '7/31/2022', 119: '7/31/2022', 120: '7/31/2022', 121: '7/31/2022', 122: '8/31/2022', 123: '8/31/2022', 124: '8/31/2022', 125: '8/31/2022', 126: '8/31/2022', 127: '9/30/2022', 128: '9/30/2022', 129: '9/30/2022', 130: '9/30/2022', 131: '9/30/2022'},
                             'Withdrawal Address': {0: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 1: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 2: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 3: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 4: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 5: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 6: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 7: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 8: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 9: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 10: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 11: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 12: '0xaE778784228B799fa9560ea24fDcda6795205F27', 13: '0x906935f4b42e632137504C0ea00D43C6442272bf', 14: '0xaE778784228B799fa9560ea24fDcda6795205F27', 15: '0xaE778784228B799fa9560ea24fDcda6795205F27', 16: '0xaE778784228B799fa9560ea24fDcda6795205F27', 17: '0xaE778784228B799fa9560ea24fDcda6795205F27', 18: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 19: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 20: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 21: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 22: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 23: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 24: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 25: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 26: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 27: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 28: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 29: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 30: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 31: '0xaE778784228B799fa9560ea24fDcda6795205F27', 32: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 33: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 34: '0xaE778784228B799fa9560ea24fDcda6795205F27', 35: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 36: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 37: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 38: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 39: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 40: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 41: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 42: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 43: '0xaE778784228B799fa9560ea24fDcda6795205F27', 44: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 45: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 46: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 47: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 48: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 49: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 50: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 51: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 52: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 53: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 54: '0xaE778784228B799fa9560ea24fDcda6795205F27', 55: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 56: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 57: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 58: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 59: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 60: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 61: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 62: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 63: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 64: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 65: '0xaE778784228B799fa9560ea24fDcda6795205F27', 66: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 67: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 68: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 69: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 70:'0xD55A5d574842E4aFff7470A60AF8343672cE6687', 71: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 72: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 73: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 74: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 75: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 76: '0xaE778784228B799fa9560ea24fDcda6795205F27', 77: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 78: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 79: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 80: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 81: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 82: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 83: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 84: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 85: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 86: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 87: '0xaE778784228B799fa9560ea24fDcda6795205F27', 88: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 89: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 90: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 91: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 92: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 93: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 94: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 95: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 96: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 97: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 98: '0xaE778784228B799fa9560ea24fDcda6795205F27', 99: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 100: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 101: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 102: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 103: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 104: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 105: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 106: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 107: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 108: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 109: '0xaE778784228B799fa9560ea24fDcda6795205F27', 110: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 111: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 112: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 113: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 114: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 115: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 116: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 117: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 118: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 119: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 120: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 121: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 122: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 123: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 124: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 125: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 126: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 127: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 128: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 129: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 130: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 131: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F'},
                             'Internal or External': {0: 'External', 1:'External', 2: 'External', 3: 'External', 4: 'Internal', 5: 'Internal', 6: 'Internal', 7: 'Internal', 8: 'Internal', 9: 'Internal', 10: 'Internal', 11: 'Internal', 12: 'External', 13: 'Unknown', 14: 'External', 15: 'External', 16: 'External', 17: 'External', 18: 'Internal', 19: 'Unknown', 20: 'Unknown', 21: 'Unknown', 22: 'Unknown', 23: 'Internal', 24: 'External', 25: 'External', 26: 'External', 27: 'External', 28: 'External', 29: 'Internal', 30: 'Internal', 31: 'External', 32: 'Internal', 33: 'Unknown', 34: 'External', 35: 'Internal', 36: 'External', 37: 'External', 38: 'External', 39: 'External', 40: 'External', 41: 'Internal', 42: 'Internal', 43: 'External', 44: 'Internal', 45: 'Unknown', 46: 'Internal', 47: 'External', 48: 'External', 49: 'External', 50: 'External', 51: 'External', 52: 'Internal', 53: 'Internal', 54: 'External', 55: 'Internal', 56: 'Unknown', 57: 'Internal', 58: 'External', 59: 'External', 60: 'External', 61: 'External', 62: 'External', 63: 'Internal', 64: 'Internal', 65: 'External', 66: 'Internal', 67: 'Unknown', 68: 'Internal', 69: 'External', 70: 'External', 71: 'External', 72: 'External', 73: 'External', 74: 'Internal', 75: 'Internal', 76: 'External', 77: 'Internal', 78: 'Unknown', 79: 'Internal', 80: 'External', 81: 'External', 82: 'External', 83: 'External', 84: 'External', 85: 'Internal', 86: 'Internal', 87: 'External', 88: 'Internal', 89: 'Unknown', 90: 'Internal', 91: 'External', 92: 'External', 93: 'External', 94: 'External', 95: 'External', 96: 'Internal', 97: 'Internal', 98: 'External', 99: 'Internal', 100: 'Unknown', 101: 'Internal', 102: 'External', 103: 'External', 104: 'External', 105: 'External', 106: 'External', 107: 'Internal', 108: 'Internal', 109: 'External', 110: 'Internal', 111: 'Unknown', 112: 'Internal', 113: 'External', 114: 'External', 115: 'External', 116: 'External', 117: 'Internal', 118: 'External', 119: 'External', 120: 'External', 121: 'External', 122: 'Internal', 123: 'External', 124: 'External', 125: 'External', 126: 'External', 127: 'Internal', 128: 'External', 129: 'External', 130: 'External', 131: 'External'}})

# save dataframe to file
df.to_csv(r'F:\PycharmProjects\VSO-Token-Unlocks\Manually Built Pandas DataFrame.csv', index=False)


df['Date of Unlock'] = pd.to_datetime(df['Date of Unlock'])
pivot_table = df.pivot_table(index=['Date of Unlock', 'Internal or External'], values=['VSO Amount'], fill_value=0, aggfunc=np.sum)

pivot_table = df.pivot_table(index='Date of Unlock', columns='Internal or External', values='VSO Amount', aggfunc='sum', fill_value=0)

# pivot_chart = pivot_table.unstack().plot(kind='bar', stacked=True)
# st.pyplot(pivot_chart)


# explicitly create DataFrame with Unlock Schedule as of October 17th 2021 (static dataset/dataframe)
# df = pd.DataFrame.from_dict({'VSO Amount': {0: 16866662, 1: 1791664, 2: 1004165, 3: 1791664, 4: 983332, 5: 1791664, 6: 983332, 7: 1791664, 8: 983332, 9: 1791664, 10: 983332, 11: 1791664, 12: 983332, 13: 1791664, 14: 983332, 15: 1791664, 16: 4150006, 17: 416665, 18: 416665, 19: 416665, 20: 416665},
#                              'Days Until Unlock': {0: 0, 1: 14, 2: 15, 3: 44, 4: 45, 5: 75, 6: 76, 7: 106, 8: 107, 9: 134, 10: 135, 11: 165, 12: 166, 13: 195, 14: 196, 15: 226, 16: 227, 17: 256, 18: 287, 19: 318, 20: 348},
#                              'Date of Unlock': {0: '10/17/2021', 1: '10/31/2021', 2: '11/1/2021', 3: '11/30/2021', 4: '12/1/2021', 5: '12/31/2021', 6: '1/1/2022', 7: '1/31/2022', 8: '2/1/2022', 9: '2/28/2022', 10: '3/1/2022', 11: '3/31/2022', 12: '4/1/2022', 13: '4/30/2022', 14: '5/1/2022', 15: '5/31/2022', 16: '6/1/2022', 17: '6/30/2022', 18: '7/31/2022', 19: '8/31/2022', 20: '9/30/2022'},
#                              'Cumulative VSO Amount': {0: 16866662, 1: 18658326, 2: 19662491, 3: 21454155, 4: 22437487, 5: 24229151, 6: 25212483, 7: 27004147, 8: 27987479, 9: 29779143, 10: 30762475, 11: 32554139, 12: 33537471, 13: 35329135, 14: 36312467, 15: 38104131, 16: 42254137, 17: 42670802, 18: 43087467, 19: 43504132, 20: 43920797}})


# change data type of Date of Unlock Column to datetime
# df['Date of Unlock'] = pd.to_datetime(df['Date of Unlock'])


# get market data from coingecko's API and assign values to variables
url = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=verso&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=7d', headers={'accept':'application/json'})
# url = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=verso&order=market_cap_desc&per_page=100&page=1&sparkline=false', headers={'accept':'application/json'})
current_price = url.json()[0]['current_price']
price_change_percentage_24h = url.json()[0]['price_change_percentage_24h']
price_changepercentage_7d = url.json()[0]['price_change_percentage_7d_in_currency']
market_cap = url.json()[0]['market_cap']
circulating_supply = url.json()[0]['circulating_supply']
fdv = url.json()[0]['fully_diluted_valuation']
total_volume = url.json()[0]['total_volume']


# calling VSO and AVAX pricing data from coingecko's API directly instead of using requests and url
cg = CoinGeckoAPI()
vso_prices = cg.get_coin_market_chart_by_id(id='verso', vs_currency='usd', days=15)
avax_prices = cg.get_coin_market_chart_by_id(id='avalanche-2', vs_currency='usd', days=15)


# create date and price dataframes for each token pair
df_vso = pd.DataFrame(vso_prices['prices'], columns=['Date', 'Price'])
df_avax = pd.DataFrame(avax_prices['prices'][:-1], columns=['Date', 'Price'])
df_vso_avax = pd.DataFrame(np.array(df_vso['Price'])/np.array(df_avax['Price']), columns=['Price']) # VSO/AVAX pair


# create date-indexed df for all tokens (one token per column)
df_token_prices = pd.DataFrame({'Date': df_vso['Date'], 'VSO/USD': df_vso['Price'], 'AVAX/USD': df_avax['Price'], 'VSO/AVAX': df_vso_avax['Price']})
df_token_prices = df_token_prices.set_index('Date')
df_token_prices.index = pd.to_datetime(df_token_prices.index, unit='ms')
print(df_token_prices)


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
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Price Change 24h**")
    number2 = str(round(price_change_percentage_24h, 2)) + '%'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Price Change 7d**")
    number2 = str(round(price_changepercentage_7d, 2)) + '%'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Volume 24h**")
    number3 = str(f'{total_volume:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

fifth_kpi, sixth_kpi, seventh_kpi = st.columns(3)

with fifth_kpi:
    st.markdown("**Market Capitalization**")
    number3 = str(f'{market_cap:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with sixth_kpi:
    st.markdown("**Circulating Supply**")
    number4 = str(f'{int(circulating_supply):,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number4}</h1>", unsafe_allow_html=True)

with seventh_kpi:
    st.markdown("**Fully Diluted Valuation**")
    number5 = str(f'{int(current_price * 100000000):,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number5}</h1>", unsafe_allow_html=True)


# TODO AVAX data
# first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi = st.columns(5)
#
# with first_kpi:
#     st.markdown("**AVAX Current Price**")
#     number1 = str(avax_current_price) + ' USD'
#     st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)


# convert 'Date' column from unix (in milliseconds) format to datetime format
# df_vso['Date'] = pd.to_datetime(df_vso['Date'], unit='ms')
# df_avax['Date'] = pd.to_datetime(df_avax['Date'], unit='ms')


# plot token returns (percentage change)
st.markdown("<hr/>", unsafe_allow_html=True)


# Price Charts
st.markdown("## Price Charts")

st.markdown("### VSO/AVAX Price Chart")

newnames = {'wide_variable_0': 'VSO/USD', 'wide_variable_1': 'AVAX/USD'} # prepare newnames variable for line chart labels renaming later
fig = px.line(df_token_prices,
             x = df_token_prices.index,
             y = df_token_prices['VSO/AVAX'],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=800,
             width=2000
             )

# fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
#                                       legendgroup = newnames[t.name],
#                                       hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
#                                      ))
st.plotly_chart(fig)



# plot token cumulative returns (cumulative percentage change)
st.markdown("### VSO and AVAX Token Returns (cumulative percentage change)")

fig2 = px.line(df_token_prices,
             x = df_token_prices.index,
             y = [(df_token_prices['VSO/USD'].pct_change()+1).cumprod(), (df_token_prices['AVAX/USD'].pct_change()+1).cumprod()],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=800,
             width=2000
             )

fig2.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     ))
st.plotly_chart(fig2)

# plot token returns (percentage change)
st.markdown("### VSO and AVAX Token Returns (percentage change)")

fig3 = px.line(df_token_prices,
             x = df_token_prices.index,
             y = [df_token_prices['VSO/USD'].pct_change(), df_token_prices['AVAX/USD'].pct_change()],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=800,
             width=2000
             )

fig3.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     ))
st.plotly_chart(fig3)


# Locked Tokens for Vesting
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Locked Tokens for Vesting")

first_kpi, second_kpi = st.columns(2)

# define variables for internal an external locked tokens
# TODO adjust static "today" date to dynamic "today"
internal_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'Internal') &(df['Date of Unlock'] > '2021-10-17T00:00:00')].sum()
external_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'External') &(df['Date of Unlock'] > '2021-10-17T00:00:00')].sum()
unknown_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'Unknown') &(df['Date of Unlock'] > '2021-10-17T00:00:00')].sum()

external_locked_total = external_locked + unknown_locked


with first_kpi:
    st.markdown("**Total Locked VSO - Internal Addresses**")
    number1 = str(f'{internal_locked:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Total Locked VSO - External Addresses**")
    number2 = str(f'{external_locked_total:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)


# Circulating Supply
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Circulating Supply")

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)


with first_kpi:
    st.markdown("**Internal Addresses**")
    number1 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**External Addresses**")
    number2 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Farms**")
    number3 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Pools**")
    number4 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number4}</h1>", unsafe_allow_html=True)


# VSO Unlcock Schedule
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## VSO Unlock Schedule")

st.subheader('Dataset')
st.write(df)


# TODO add cumulative back to DataFrame
# st.subheader('Cumulative VSO Unlocks per Date')
# st.bar_chart(df.rename(columns={'Date of Unlock':'index'}).set_index('index')['Cumulative VSO Amount'])

# old way of plotting unlocks
pivot_chart = pivot_table.unstack().plot(kind='bar', stacked=True)

# add bars
st.subheader('VSO Unlocks per Date')


fig = px.bar(pivot_table,
             x = pivot_table.index,
             y = [c for c in pivot_table.columns],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=800,
             width=2000
             )

fig.update_traces(marker_line_width=1.5)
# fig.update_layout(barmode='stack')
st.plotly_chart(fig)

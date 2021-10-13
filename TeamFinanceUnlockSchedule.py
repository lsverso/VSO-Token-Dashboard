# import packages
import sys
import pandas
sys.path.append('C:\Python39\Lib\site-packages')
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
import tempfile
import os
import pandas as pd

# open the url ina  web browser (Chrome)
browser = webdriver.Chrome()
browser.get("https://team.finance/view-coin/0x846D50248BAf8b7ceAA9d9B53BFd12d7D7FBB25a?name=VersoToken&symbol=VSO")


# parse web page data
c = browser.page_source
soup = BeautifulSoup(c, 'html.parser')
time.sleep(2)


# read entire block of unlocks (calling the block "division")
division = browser.find_element_by_id('root')
division_text = division.text


# create string locators for entire lines in the scrape output (first batch of locators) and compile
keywords = ['Locked VersoToken Tokens', 'D –', 'Unlocks ']
pattern = re.compile('|'.join(keywords))


# create string locators for desired data within lines (second batch of locators) and compile
keywords1 = ['Locked VersoToken Tokens']
keywords2 = ['D –']
keywords3 = ['Unlocks ']

pattern1 = re.compile('|'.join(keywords1))
pattern2 = re.compile('|'.join(keywords2))
pattern3 = re.compile('|'.join(keywords3))


# create empty lists to store compiled strings afterwards
token_amount = []
unlock_countdown_days = []
unlock_date = []


# create temporary .txt file to store output from scrape, and don't delete it when done
with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    print(tmp.name)
    tmp.write(division_text)
    # reopen the file for reading
with open(tmp.name) as tmp:
    new_division_text = tmp.readlines()

    for line in new_division_text:
        print(line)

        if re.search(pattern1, line):
            token_amount.append(line)
        if re.search(pattern2, line):
            unlock_countdown_days.append(line)
        if re.search(pattern3, line):
            unlock_date.append(line)

# remove the file manually
os.remove(tmp.name)

# # write .txt file with the text output of the unlocks
# file1 = open("TrustswapTokenUnlocks.txt","w")
# file1.write(division_text)
# file1.close()

# old way of writing on txt files (now we use tmp files)
# keywords = ['Locked VersoToken Tokens', 'D –', 'Unlocks ']  # etc - you probably get those from some source
# pattern = re.compile('|'.join(keywords))
#
# token_amount = []
#
# with open('TrustswapTokenUnlocks.txt', "r") as TrustswapTokenUnlocks:
#     for line in TrustswapTokenUnlocks:
#         print(line)
#         if re.search(pattern, line):
#             token_amount.append(line)
# print(token_amount)


# # create "string locators" (keywords) to select only lines with the specified keyword below and compile lines
# keywords1 = ['Locked VersoToken Tokens']
# keywords2 = ['D –']
# keywords3 = ['Unlocks ']
#
# pattern1 = re.compile('|'.join(keywords1))
# pattern2 = re.compile('|'.join(keywords2))
# pattern3 = re.compile('|'.join(keywords3))
#
#
# # create empty lists to append string data later
# token_amount = []
# unlock_countdown_days = []
# unlock_date = []
#
# # read read .txt file with located data
# with open('TrustswapTokenUnlocks.txt', "r") as TrustswapTokenUnlocks:
#     for line in TrustswapTokenUnlocks:
#         print(line)
#         if re.search(pattern1, line):
#             token_amount.append(line)
#         if re.search(pattern2, line):
#             unlock_countdown_days.append(line)
#         if re.search(pattern3, line):
#             unlock_date.append(line)

print(len(token_amount))
print(len(unlock_countdown_days))
print(len(unlock_date))


# create dataframe with 3 columns; each populated by the lists created before
d = {'col1': token_amount, 'col2': unlock_countdown_days[1:], 'col3': unlock_date[1:]}
df = pd.DataFrame(d)


# split strings and transform into appropriate type
token_amount = [re.sub("[^0-9]", "", i) for i in token_amount]
token_amount = [float("{:.2f}".format(int(number) / 100.0)) for number in token_amount]

unlock_countdown_days = [j.split('D', 1)[0] for j in unlock_countdown_days]
unlock_countdown_days = [int(days) for days in unlock_countdown_days]

# apply changes
for number in token_amount:
    number = float("{:.2f}".format(number / 100.0))
    print(number, type(number))


# create dataframe with formatted columns
# df_formatted contains all unlocks and days until unlock in the order displayed on Team Finance
d_formatted = {'VSO Amount': token_amount, 'Days Until Unlock': unlock_countdown_days[1:]}  # , 'col3': unlock_date[1:]}
df_formatted = pd.DataFrame(d_formatted)
df_formatted['VSO Amount'] = df_formatted['VSO Amount'].astype(float)


# replace 2 VSO amounts where number formatting was messed up with number 1
df_formatted['VSO Amount'][96] = 1
df_formatted['VSO Amount'][97] = 1


# make dataframe row amount print unlimited
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df_formatted)


# create new dataframe with VSO amount ordered by Days Until Unlock
df_sorted_days_until_unlock = df_formatted.sort_values(by=['Days Until Unlock'])


# plot unlocks by days until unlock
fig, ax = plt.subplots()
ax.bar(df_sorted_days_until_unlock['Days Until Unlock'], df_sorted_days_until_unlock['VSO Amount'])

ax.set(xlabel='Days Until Unlock', ylabel='VSO Unlocked', title='VSO Token Unlocks')
ax.grid()
plt.rcParams["figure.figsize"] = (50, 20)
plt.show()


# create dataframe where unlocks for same unlock dates are summed (there won't be repeated values in the Days Until
# Unlock column)
df_grouped_days_until_unlock = df_sorted_days_until_unlock.groupby(df_sorted_days_until_unlock['Days Until Unlock']).sum()
df_grouped_days_until_unlock['Days Until Unlock'] = df_grouped.index

# add cumulative VSO unlocks column (dataframe remains ordered by Days Until Unlock)
df_grouped['Cummulative VSO Unlocks'] = df_grouped['VSO Amount'].cumsum()

# save df_formatted into a .csv file within a .zip file
compression_opts = dict(method='zip',
                        archive_name='VSO Unlocks Not Ordered.csv')
df_formatted.to_csv('VSO Unlocks Not Ordered.zip', index=False,
                    compression=compression_opts)


# save the df_grouped_days_until_unlock into a .csv file within a .zip file
compression_opts = dict(method='zip',
                        archive_name='VSO Unlocks Grouped by Days Until Unlock.csv')
df_grouped_days_until_unlock.to_csv('VSO Unlocks Grouped by Days Until Unlock.zip', index=False,
                  compression=compression_opts)

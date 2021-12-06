import pandas as pd
pd.set_option('display.max_rows', None)
import pymongo

# connect to MongoDB client
MONGO_URI = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(MONGO_URI)

###################################################################
# compute token holder difference 1d, 7d
###################################################################

# connect to VSO-Holders collection in Token-Holders-db database
db = client['Token_Holders_db']
collection = db['VSO_Holders']
print(client.list_database_names())

# crete empty list to store each object (dictionary)
collection_list = []

# append each object to list
for obj in collection.find():
    collection_list.append(obj)

# create dataframe from objects
df = pd.DataFrame(collection_list)

# replace all NaT values with the datetime object created above and change type of 'timestamp' column to datetime
df['timestamp'] = pd.to_datetime(df["timestamp"].dt.strftime('%Y-%m-%d'))
print(df.head())

# compute difference of amount of token holders between most recent timestamp and every other timestamp
df2 = df.groupby("timestamp")[["timestamp"]].count().rename(columns={"timestamp": "holder count change"})
diff = df2.at[max(df2.index), "holder count change"] - df2
print(diff['holder count change'][0])

##################################################################
# compute VSO token trading volume difference 1d, 7d
###################################################################



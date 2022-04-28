import pandas as pd
from CloudSQLConnection import CloudSQLConnection

"""
Initiate Connection to GCP Cloud DB
    Make sure to whitelist your IP on GCP
        GOTO database instance(ordodb),
        Click "Edit" -> "Connections" -> "ADD NETWORK",
        Add Name and Network
"""
cnx = CloudSQLConnection()
cursor = cnx.cursor()

#### Execute query ####
query1 = ("SELECT * FROM TWEETS;")
cursor.execute(query1)

#### Query result to pandas table ####
df = pd.DataFrame(cursor.fetchall())
df.columns = [['MOVIEID','TWEETID','CONTENT']]
print(df)
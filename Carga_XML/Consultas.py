import pymongo
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

client = pymongo.MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)

try:   
    print(client.start_session)
    
except Exception:
    print("Unable to connect to the server.")

dbSiedco = client.siedco
dfDelitos = pd.DataFrame(list(dbSiedco.delitos.find()))
dfDelitos.tail()
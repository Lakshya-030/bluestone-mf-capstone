import pandas as pd
import requests 
url="https://api.mfapi.in/mf/125497"
response = requests.get(url)
response.status_code
data = response.json()
type(data)
data.keys()
data['meta']
Nav_df = pd.DataFrame(data['data'])
Nav_df.head()
Nav_df.to_csv("Data/Raw/live_nav_125497.csv",index=False)

def Fetch_Nav(amfi_code):
    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)
    data=response.json()
    Nav_Df = pd.DataFrame(data['data'])
    Nav_Df.to_csv(f"Data/Raw/Nav_{amfi_code}.csv",index=False)

    print(f"Saved NAV data for {amfi_code}")

    return Nav_Df.head()
Fetch_Nav(119551)
Fetch_Nav(120503)
Fetch_Nav(118632)
Fetch_Nav(119092)
Fetch_Nav(120841)

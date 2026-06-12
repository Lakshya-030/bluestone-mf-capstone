"""
Fetch live NAV data from MFAPI.
"""

import pandas as pd
import requests


def fetch_nav(amfi_code):

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"Data/Raw/Nav_{amfi_code}.csv",
        index=False
    )

    print(f"Saved NAV data for {amfi_code}")

    return nav_df


if __name__ == "__main__":

    fetch_nav(119551)
    fetch_nav(120503)
    fetch_nav(118632)
    fetch_nav(119092)
    fetch_nav(120841)
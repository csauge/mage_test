import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data_from_api(*args, **kwargs):
    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
    data = requests.get(url).json()
    return pd.json_normalize(data["data"]["stations"])

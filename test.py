import pandas as pd
import requests
import datetime

if __name__ == "__main__":
    datetime_startDate = datetime.datetime(2020,1,1).date()
    datetime_endDate = datetime.datetime(2021,1,1).date()

    data_dict = {'country': "US",
            'ticker' : "AAPL",
            'startDate': datetime_startDate,
            'endDate': datetime_endDate}

    data_dict["username"] = "IG_rasp"
    data_dict["password"] = "devbysb"

    r = requests.post('http://119.194.201.232:9001/market_database',data = data_dict)


    # print(type(r.json()))

    dataframe_Data_from_json = pd.read_json(r.json())
    # print(dataframe_Data_from_json)
    # print(dataframe_Data_from_json.columns)
    # print(type(dataframe_Data_from_json))
    # print(type(dataframe_Data_from_json["Date"]))
    # print(type(dataframe_Data_from_json["Date"][0]))
    # print(dataframe_Data_from_json["Date"])
    dataframe_Data_from_json["Date"] = pd.to_datetime(dataframe_Data_from_json["Date"]).dt.date
    # print(type(dataframe_Data_from_json["Date"][0]))
    print(dataframe_Data_from_json)


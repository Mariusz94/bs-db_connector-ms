import pprint
import pandas as pd
from service.database import psql_database_repository
from service.database.psql_database import BS_DB


def getBalance(user_id: str) -> dict:
    df: pd.DataFrame = psql_database_repository.getBalance(user_id)
    data = df.to_dict()
    pprint(data)
    return data


def GetUserInfo(user_id: str) -> dict:
    df: pd.DataFrame = psql_database_repository.getUserInfo(user_id)
    data = df.to_dict()
    pprint(data)
    return data

import logging

import pandas as pd
from service.database import psql_database_repository
from service.database.psql_database import BS_DB


def get_balance(user_id: str) -> dict:
    df: pd.DataFrame = psql_database_repository.get_balance(BS_DB, user_id)
    data = df.to_dict(orient="index")
    return data[0]


def get_user_info(user_id: str) -> dict:
    df: pd.DataFrame = psql_database_repository.get_user_info(BS_DB, user_id)
    data = df.to_dict(orient="index")
    return data[0]

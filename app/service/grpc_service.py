import logging

import pandas as pd
from service.database import psql_database_repository
from service.database.psql_database import BS_DB


def get_balance(user_id: str) -> dict:
    """
    Method allow obtain balance for user by user id.

    Args:
        user_id (str): User id.

    Returns:
        dict: Balance info.
    """
    df: pd.DataFrame = psql_database_repository.get_balance(BS_DB, user_id)
    data = df.to_dict(orient="index")
    return data[0]


def get_user_info(user_id: str) -> dict:
    """
    Method allow obtain user info by user id.

    Args:
        user_id (str): User id.

    Returns:
        dict: User info.
    """
    df: pd.DataFrame = psql_database_repository.get_user_info(BS_DB, user_id)
    data = df.to_dict(orient="index")
    return data[0]

def login(login:str, password:str) -> dict:
    """
    Method to login user.

    Args:
        login (str): User login.
        password (str): User password.

    Returns:
        dict: User info.
    """
    df: pd.DataFrame = psql_database_repository.login(BS_DB, login, password)
    data = df.to_dict(orient="index")
    return data[0]
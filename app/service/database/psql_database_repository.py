import logging
from service.database.psql_database import PSQLDatabase
import pandas as pd
from sqlalchemy import and_


def get_balance(db: PSQLDatabase, user_id: str) -> pd.DataFrame:
    """
    Method allow obtain balance for user by user id.

    Args:
        db (PSQLDatabase): Instance of database.
        user_id (str): User id.

    Returns:
        pd.DataFrame: Balance info.
    """
    logging.info(f"Getting balance for user {user_id}")
    try:
        table_name: str = "balance"
        table = db.get_table(table_name)
        query = table.select().where(table.c.id == user_id).limit(1)
        df = db.get_df_from_sql(query=query)
        logging.info(f"Obtain balance for user {user_id}")
        logging.debug(df)
        return df
    except Exception as error:
        logging.error(f"Can not get balance for user {user_id} " + str(error))
        raise error


def get_user_info(db: PSQLDatabase, user_id: str) -> pd.DataFrame:
    """
    Method allow obtain user info by user id.

    Args:
        db (PSQLDatabase): Instance of database.
        user_id (str): User id.

    Returns:
        pd.DataFrame: User info.
    """
    logging.info(f"Getting user info for user {user_id}")
    try:
        table_name: str = "user"
        table = db.get_table(table_name)
        query = table.select().where(table.c.id == user_id).limit(1)
        df = db.get_df_from_sql(query=query)
        logging.info(f"Obtain balance for user {user_id}")
        logging.debug(df)
        return df
    except Exception as error:
        logging.error(f"Can not get user info for user {user_id} " + str(error))
        raise error


def login(db: PSQLDatabase, login: str, password: str) -> pd.DataFrame:
    """
    Method allow obtain user info by user login and password.

    Args:
        db (PSQLDatabase): Instance of database.
        login (str): User login.
        password (str): User password.

    Returns:
        pd.DataFrame: User info.
    """
    logging.info(f"Getting user info for user {login}")
    try:
        table_name: str = "user"
        table = db.get_table(table_name)
        query = (
            table.select()
            .where(and_(table.c.login == login, table.c.password == password))
            .limit(1)
        )
        df = db.get_df_from_sql(query=query)
        logging.info(f"Obtain balance for user {login}")
        logging.debug(df)
        return df
    except Exception as error:
        logging.error(f"Can not get user info for user {login} " + str(error))
        raise error

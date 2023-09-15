import logging
from service.database.psql_database import PSQLDatabase
import pandas as pd


def getBalance(db: PSQLDatabase, user_id: str) -> pd.DataFrame:
    """
    Method allow obtain balance for user by user id.

    Args:
        db (PSQLDatabase): Instance of database.
        user_id (str): User id.

    Returns:
        pd.DataFrame: Balance info.
    """
    logging.info("Getting balance for user {user_id}")
    try:
        table_name: str = "user"
        table = db.get_table(table_name)
        query = table.select().where(table.c.id == user_id)
        df = db.get_df_from_sql(query=query)
        logging.info("Obtain balance for user {user_id}")
        logging.debug(df)
        return df
    except Exception as error:
        logging.error("Can not get balance for user {user_id} " + str(error))
        raise error


def getUserInfo(db: PSQLDatabase, user_id: str) -> pd.DataFrame:
    """
    Method allow obtain balance for user by user id.

    Args:
        db (PSQLDatabase): Instance of database.
        user_id (str): User id.

    Returns:
        pd.DataFrame: Balance info.
    """
    logging.info("Getting balance for user {user_id}")
    try:
        table_name: str = "user"
        table = db.get_table(table_name)
        query = table.select().where(table.c.id == user_id)
        df = db.get_df_from_sql(query=query)
        logging.info("Obtain balance for user {user_id}")
        logging.debug(df)
        return df
    except Exception as error:
        logging.error("Can not get balance for user {user_id} " + str(error))
        raise error
import logging

import pandas as pd
from sqlalchemy import Table
from sqlalchemy.orm import registry


class RelationalDatabase:
    """
    Class contain methods for relational databases.
    """

    def __init__(self, engine, db_schema: str):
        self.engine = engine
        self.db_schema = db_schema
        self.mapper_registry = registry()

    def get_table(self, table_name: str) -> Table:
        """
        Returns the Table class object, if table 'table_name' exists in database.

        Args:
            table_name (str): Table name.

        Returns:
            Table: Object of class Table.
        """
        logging.info(f"Getting table {table_name}.")
        try:
            return Table(
                table_name,
                self.mapper_registry.metadata,
                autoload=True,
                autoload_with=self.engine,
            )
        except Exception as error:
            logging.error("Couldn't get table : " + str(error))
            raise error

    def send_df_to_db(self, table_name: str, df: pd.DataFrame) -> bool:
        """
        Inserts DataFrame into the table in database.

        Note:
            If provided table (parameter: table_name) exist in database, data will be insert in that table. Otherwise, new table will be created

        Args:
            table_name (str): Table name.
            data (pd.DataFrame): Data to insert.

        Returns:
            bool: Result of action.
        """
        logging.info(f"Sending df to table {table_name}.")
        logging.debug(df)
        try:
            df.to_sql(name=table_name, con=self.engine, if_exists="append", index=False)

            logging.info("Wrote data to database.")
            return True
        except Exception as error:
            logging.error("Can not write data to database " + str(error))
            raise error

    def get_df_from_sql(self, query: str) -> pd.DataFrame:
        """
        Read SQL query to obtain data from database.

        Args:
            query (str): SQL query to be execute.

        Returns:
            pd.DataFrame: Data.
        """
        logging.info(f"Getting data by query.")
        logging.debug(query)
        try:
            conn = self.engine.connect()
            df = pd.read_sql(query, conn)
            logging.info(f"Obtain data.")
            logging.debug(f"{df=}")
            return df
        except Exception as error:
            logging.error("Can not read data from database " + str(error))
            raise error

    def update(self, table_name: str, id: str, data: dict) -> bool:
        """
        Updates existing data in database.

        Args:
            table_name (str): Table name.
            id (str): ID of the row to update.
            data (dict): Data to update database.

        Returns:
            bool: Result of action.
        """
        logging.info(f"Updating data in {table_name} table by {id=}")
        logging.debug(f"{data=}")
        try:
            table = self.get_table(table_name=table_name)

            query = table.update().where(table.c.id == id).values(data)

            with self.engine.connect() as conn:
                conn.execute(query)
            logging.info(f"Data was updated.")
            return True
        except Exception as error:
            logging.error("Can not update data in database " + str(error))
            raise error

    def delete(self, table_name: str, id: str, id_column) -> bool:
        """
        Delete indicated row from database.

        Args:
            table_name (str): Table name.
            id (str): PK of the row to delete.
            id_column (str): PK table name.

        Returns:
            bool: Result of action.
        """

        logging.info(f"Deleting data in {table_name} table by {id_column}={id}")
        try:
            table = self.get_table(table_name=table_name)

            query = table.delete().where(id_column == id)

            with self.engine.connect() as conn:
                conn.execute(query)
            logging.info(f"Data was removed.")
            return True
        except Exception as error:
            logging.error("Can not remove data in database " + str(error))
            raise error

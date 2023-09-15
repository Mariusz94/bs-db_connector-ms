import config
from service.database.relational_database import RelationalDatabase
from sqlalchemy import create_engine


class PSQLDatabase(RelationalDatabase):
    """
    Class contain methods for PostgreSQL database.
    """

    def __init__(
        self,
        db_address: str,
        db_port: int,
        db_user: str,
        db_password: str,
        db_name: str,
        db_schema: str = "public",
    ):
        self.db_address = db_address
        self.db_port = db_port
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
        self.db_schema = db_schema
        self.engine = create_engine(
            f"postgresql://{db_user}:{db_password}@{db_address}:{db_port}/{db_name}"
        )
        super().__init__(self.engine, db_schema)


BS_DB = PSQLDatabase(
    config.BS_DATABASE_IP,
    config.BS_DATABASE_PORT,
    config.BS_DATABASE_USERNAME,
    config.BS_DATABASE_PASSWORD,
    config.BS_DATABASE_NAME,
    config.BS_DATABASE_SCHEMA,
)
"""Instance of bank system database"""

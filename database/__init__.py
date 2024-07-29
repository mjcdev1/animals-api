"""TEMPORARY PLACEHOLDER DOCSTRING!"""

import os

from dotenv import load_dotenv
from psycopg2 import pool
from psycopg2.extensions import connection

load_dotenv('.env')


class Database:
    """TEMPORARY PLACEHOLDER DOCSTRING!"""

    def __init__(self) -> None:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        self.database_name = os.getenv('DATABASE_NAME')
        self.database_host = os.getenv('DATABASE_HOST')
        self.database_user = os.getenv('DATABASE_USER')
        self.database_pw = os.getenv('DATABASE_PW')
        self.database_port = os.getenv('DATABASE_PORT')
        self.db_pool = pool.SimpleConnectionPool(
            1,  # Min connections
            10,  # Max connections
            dbname=self.database_name,
            user=self.database_user,
            password=self.database_pw,
            host=self.database_host,
            port=self.database_port
        )

    def db_connect(self) -> connection:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        conn = self.db_pool.getconn()
        assert isinstance(conn, connection), (
            "db_pool.getconn() did not return a psycopg2 connection"
        )
        return conn

    def db_close(self, conn: connection) -> None:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        self.db_pool.putconn(conn)

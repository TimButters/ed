import pandas as pd
import pandasql as ps
import re
import os

from pathlib import Path

from .exceptions import EdDbAlreadyExists, EdDbNotConnected, EdTableNotFound, EdTableAlreadyExists


class Ed:
    """Excel database instance.

    Interact with an existing database, or
    create a new one.
    """

    def __init__(self, *, root: str | Path | None = None):
        if root is None:
            env_root = os.environ.get("ED_ROOT_DIR")
            self._root = Path(".") if env_root is None else Path(env_root)
        else:
            self._root = Path(root)

        self._db_path = None
        self._tables = {}

    def connect(self, dbname):
        """Connect to an existing Excel database.

        If the instance is already connected to an
        Excel database this connection will be dropped
        and any unsaved transactions lost.

        Parameters
        ----------
        dbname: str
            The name of the database to connect to. This will
            use the `ED_ROOT_DIR` environment variable as the
            path prefix.
        """
        self._tables = {}
        self._db_path = self._root / Path(dbname)
        for f in self._db_path.iterdir():
            if f.match("*.xlsx"):
                table_name = str(f).split("/")[-1].split(".")[0]
                self._tables[table_name] = pd.read_excel(f)
        return self

    def create(self, dbname):
        """Create a new Excel database.

        Parameters
        ----------
        dbname: str
            The name of the database to create. This will
            use the `ED_ROOT_DIR` environment variable as the
            path prefix.

        Raises
        ------
        EdDbExists:
            Raised if there is an existing database at the
            same location.
        """
        path = self._root / Path(dbname)
        if path.exists():
            raise EdDbAlreadyExists(f"Excel database `{dbname}` already exists.")
        path.mkdir(parents=True, exist_ok=False)
        return self

    def write_table(self, table: str, df: pd.DataFrame):
        """Write a new table to the Excel database.

        Parameters
        ----------
        table: str
            The name of the table to create.
        df: pandas.DataFrame
            The dataframe to write to the table.

        Raises
        ------
        EdDbNotConnected:
            If not currently connected to an Excel database.
        EdTableAlreadyExists:
            Raised if a table with the same name already exists
            in the Excel database.
        """
        if self._db_path is None:
            raise EdDbNotConnected()

        if table in self._tables:
            raise EdTableAlreadyExists(f"Table `{table}` already exists in the database.")

        self._tables[table] = df
        filename = self._db_path / (table + ".xlsx")
        df.to_excel(filename)

    def sql(self, query: str):
        if self._db_path is None:
            raise EdDbNotConnected()

        tables = re.findall(r"FROM\s+(\w+)", query, re.IGNORECASE)
        for table in tables:
            if table not in self._tables:
                raise EdTableNotFound(f"Table `{table}` not found in current database.")
            locals()[table] = self._tables[table]

        return ps.sqldf(query, locals())

import pandas as pd
import pandasql as ps
import re

from pathlib import Path


class Ed:
    def __init__(self, dbname):
        self._tables = {}
        for f in Path(dbname).iterdir():
            if f.match("*.xlsx"):
                table_name = str(f).split("/")[-1].split(".")[0]
                self._tables[table_name] = pd.read_excel(f)

    def sql(self, query: str, table: str):
        df = self._tables[table]
        q = re.sub(r"FROM\s+\w+", r"FROM df", query, re.IGNORECASE)
        return ps.sqldf(q, locals())

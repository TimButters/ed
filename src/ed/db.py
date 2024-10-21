import pandas as pd
import pandasql as ps
import re

from pathlib import Path


class Ed:
    def __init__(self, dbname):
        dfs = []
        for f in Path(dbname).iterdir():
            if f.match("*.xlsx"):
                dfs.append(pd.read_excel(f))
        self._df = pd.concat(dfs)

    def sql(self, query: str):
        df = self._df
        q = re.sub(r"FROM\s+\w+", r"FROM df", query, re.IGNORECASE)
        return ps.sqldf(q, locals())

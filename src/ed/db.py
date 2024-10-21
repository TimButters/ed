import pandas as pd
import pandasql as ps
import re


class Ed:
    def __init__(self, filename):
        self._df = pd.read_excel(filename)

    def sql(self, query: str):
        df = self._df
        q = re.sub(r"FROM\s+\w+", r"FROM df", query, re.IGNORECASE)
        return ps.sqldf(q, globals())

import pandas as pd

from ed import Ed


def test_db_create():
    db = Ed("tests/testdb")
    res = db.sql("SELECT * FROM table", "test")
    assert isinstance(res, pd.DataFrame)
    assert len(res) == 2

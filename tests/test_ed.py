import pandas as pd
import pytest

from pathlib import Path

from ed import Ed
from ed.exceptions import EdDbAlreadyExists, EdDbNotConnected, EdTableNotFound, EdTableAlreadyExists


def test_db_query():
    db = Ed(root=Path(__file__).parent)
    db.connect("testdb")
    res = db.sql("SELECT * FROM test")
    assert isinstance(res, pd.DataFrame)
    assert len(res) == 2


def test_db_query_with_missing_table():
    db = Ed(root=Path(__file__).parent)
    db.connect("testdb")
    with pytest.raises(EdTableNotFound, match="Table `wrong_table` not found"):
        db.sql("SELECT * FROM wrong_table")


def test_sql_without_connection():
    db = Ed()
    with pytest.raises(EdDbNotConnected, match="Not currently connected to an"):
        db.sql("SELECT * FROM table")


def test_create_new():
    db = Ed(root=Path(__file__).parent)
    db.create("testdb2")
    assert (Path(__file__).parent / "testdb2").is_dir()
    (Path(__file__).parent / "testdb2").rmdir()


def test_db_create_over_existing():
    db = Ed(root=Path(__file__).parent)
    with pytest.raises(EdDbAlreadyExists, match="Excel database `testdb` already exists."):
        db.create("testdb")


def test_write_table():
    db = Ed(root=Path(__file__).parent)
    db.create("testdb3")
    db.connect("testdb3")
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
    db.write_table("test", df)
    assert (Path(__file__).parent / "testdb3/test.xlsx").exists()
    (Path(__file__).parent / "testdb3/test.xlsx").unlink()
    (Path(__file__).parent / "testdb3").rmdir()


def test_write_table_without_connection():
    db = Ed(root=Path(__file__).parent)
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
    with pytest.raises(EdDbNotConnected, match="Not currently connected to an"):
        db.write_table("test", df)


def test_write_table_over_existing():
    db = Ed(root=Path(__file__).parent)
    db.create("testdb4")
    db.connect("testdb4")
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
    db.write_table("test", df)
    with pytest.raises(EdTableAlreadyExists, match="Table `test` already exists"):
        db.write_table("test", df)
    (Path(__file__).parent / "testdb4/test.xlsx").unlink()
    (Path(__file__).parent / "testdb4").rmdir()

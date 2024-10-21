from ed import Ed


def test_db_create():
    db = Ed("testdb")
    db.sql("SELECT * FROM df")

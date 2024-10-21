from ed import Ed, sql


def test_db_create():
    db = EdDb("./test.xlsx")
    sql("SELECT * FROM df")

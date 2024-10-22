# Ed: Excel database

People are always trying to use Excel as a database. Well, with this handy package, they can!

Why not use the world's foremost data product as the backend to your entire data estate. None of that expensive or confusing server setup, and if anything goes wrong, just open it in the handy GUI editor _you already have_ and you're back up and running in no time!

## Advantages

A lot of software consists of a complex backend with a simplified, easy to use, GUI front end. Ed, however, utilises an easy to use GUI-based backend and adds a more technical API on top.

Due to the complexities of sharding a proprietary file format, Ed is entirely in-memory, just like Spark!

## Examples

### Querying an Excel database

Select all values from the table `users` in the `testdb` database.

```python
>>> from ed import Ed

>>> db = Ed()
>>> db.connect("testdb")
>>> db.sql("SELECT * FROM users")
  Name         Team
0  Tim      science
1   Ed  engineering
```

### Creating a new database

Create a new database `myed` and create two tables, `users` and `products`

```python
>>> from ed import Ed

>>> db = Ed()
>>> db.create("myed")
>>> db.write_table("users", df_user)
>>> db.write_table("products", df_product)
```

## Future Work

* Remove `pandasql` dependency and build queries by parsing a feature grammar translation between SQL and the Pandas API.
* Re-write in Rust and/or Haskell.

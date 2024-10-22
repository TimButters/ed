# Ed: Excel database

People are always trying to use Excel as a database. Well, with this handy package, they can!

Why not use the world's foremost data product as the backend to your entire data estate. None of that expensive or confusing server setup, and if anything goes wrong, just open it in the handy GUI editor _you already have_ and you're back up and running in no time!

## Advantages

A lot of software consists of a complex backend with a simplified, easy to use, GUI front end. Ed, however, utilises a an easy to use GUI-based backend and adds a more technical API.

Due to the complexities of sharding a proprietary file format, Ed is entirely in-memory, just like Spark!

## Examples

```python
>>> from ed import Ed

>>> db = Ed("testdb")
>>> db.sql("SELECT * FROM table")
  Name         Team
0  Tim      science
1   Ed  engineering
```

## Future Work

* Databases can hold multiple tables delineated by different sets of Excel files.
* Remove `pandasql` dependency and build queries by parsing a feature grammar translation between SQL and the Pandas API.

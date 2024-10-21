# Ed: Excel database

People are always trying to use Excel as a database. Well, with this handy package, they can!

Why not use the world's foremost data product as the backend to your entire data estate. None of that expensive or confusing server setup, and if anything goes wrong, just open it in the handy GUI editor _you already have_ and you're back up and running in no time!

## Examples

```python
>>> from ed import Ed

>>> db = Ed("testdb")
>>> db.sql("SELECT * FROM db")
  Name         Team
0  Tim      science
1   Ed  engineering
```

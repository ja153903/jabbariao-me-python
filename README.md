# jabbariao.com Python API

## About

This is yet another rewrite of my API for my personal website. However, this time I wanted to write it in Python.

This project uses FastAPI and Poetry with a PostgreSQL database.

Like Django, I'm structuring each endpoint to be its own app.

This means that each app will have the following core files:

1. `api.py` which defines the router and routes
2. `crud.py` which defines the ORM operations to make queries
3. `models.py` which defines the database tables
4. `schemas.py` which defines app-level types

## Commands

**Start Project**: `poetry run start`

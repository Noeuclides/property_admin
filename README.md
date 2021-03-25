# Property App

Django application to register properties.

## Requirements
Python3.7 or greater.

You have to set psql on your local machine.

To run the django app use the python package manager [pipenv](https://pipenv-es.readthedocs.io/es/latest/).


## Installation

Install the dependencies:

```bash
pipenv install
```

Configure psql database:

```bash
psql postgres -f create_db.sql
```

## Usage

Run the migrate command to have the db structure on your local db:

```bash
pipenv run migrate
```

And then you can run the server and go to the home page
```bash
pipenv run server
```

To register a superuser run:
```bash
pipenv run createsuperuser
```

Note: The migrate, server, createsuperuser commands are configured in the Pipfile.



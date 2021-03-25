# Property App

Django application to register properties.

## Requirements
To run on docker make sure to configurate Docker and docker compose on your local machine.

Otherwise you have to set:
- Python3.7 or greater.

- psql on your local machine.

- The python package manager [pipenv](https://pipenv-es.readthedocs.io/es/latest/).


## Installation
If docker:
only run and go to http://127.0.0.1:8000 on the browser.
```bash
docker-compose up --build
```
Else:
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



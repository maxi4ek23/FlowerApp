# Family Budget backend

## Creating venv

Run this command in terminal

```bash
python -m venv venv
```

And then to activate venv run this

```bash
.\venv\Scripts\activate
```

## Installing modules

Install all modules from requirements.txt

```bash
python -m pip install -r requirements.txt
```

## Configere database

.\venv\Scripts\activate
Open `app.yml` file and change there database name here

```yml
SQLALCHEMY_DATABASE_URI: "mysql://{0}:{1}@localhost/YOUR_DB_NAME"
```

and in this file also change mysql username and password

```yml
MYSQL_ROOT_USER: username
MYSQL_ROOT_PASSWORD: password
```

## Running server

And now you have all what you need to run your server

To do this you need just to run app.py

If you are using vscode you can just press `F5` to run with debuger or `CTRL+F5` to run without debuger anywhere in this poject.

CRUD requests
\*User:

-----POST:http://127.0.0.1:5000/user

```json
{
  "name": "user",
  "email": "user@gmail.com",
  "password": "1234",
  "is_admin": false
}
```

-----POST: http://127.0.0.1:5000/user/login

```json
{
  "email": "admin@gmail.com",
  "password": "1234"
}
```

-----GET(all):http://127.0.0.1:5000/user

-----PUT:http://127.0.0.1:5000/user/1

```json
{
  "name": "user1111",
  "email": "user@gmail.com",
  "password": "1234",
  "is_admin": false
}
```

\*Category:
------POST:http://127.0.0.1:5000/category

```json
{
  "name": "test"
}
```

-----GET(all):http://127.0.0.1:5000/category

\*Goods:

```
-----POST:http://127.0.0.1:5000/goods
```

```json
{
  "name": "rose",
  "price": 20,
  "description": "hfhf",
  "category_id": 1
}
```

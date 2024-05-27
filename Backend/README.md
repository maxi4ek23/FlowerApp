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
  "is_admin": false,
  "card_type": "bonus" (or empty if user dont
   have a card)
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
  "is_admin": false,
  "card_type": "bonus" (or empty if user dont
   have a card)
}
```

\*Catalogue:
------POST:http://127.0.0.1:5000/catalogue
`

```json
{
  "name": "test"
}
```

-----GET(all):http://127.0.0.1:5000/catalogue

\*Order:

```
-----POST:http://127.0.0.1:5000/order
```

```json
{
  "price": 700,
  "deliveryType": "Nova Poshta",
  "clientId": 1,
  "bouquets": [
    {
      "name": "Rose Bouquet",
      "eventType": "Birthday",
      "price": 600,
      "packing": {
        "name": "Craft",
        "price": 55
      },
      "catalogue": "Bouquets",

      "flowers": [
        {
          "name": "White Rose",
          "color": "white",
          "price": 30
        },
        {
          "name": "Red Rose",
          "color": "red",
          "price": 40
        },
        {
          "name": "Pink Rose",
          "color": "pink",
          "price": 40
        }
      ]
    }
  ]
}
```

\*Packing(update):

```
-----PUT:http://127.0.0.1:5000/packing
```

```json
{
  "name": "Craft",
  "price": 100
}
```

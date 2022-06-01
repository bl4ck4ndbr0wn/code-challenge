# Assignment: Coding Challenge

Given a web endpoint "\GET", create an API and prepare an application that will receive as an
input an integer number
● if the integer is

■ a multiple of 5, it should return "L"
■ a multiple of 7, it should return "R"
■ a multiple of both 5 and 7, then both "LR" should be displayed

● otherwise the provided integer should be returned
● the output should be a properly formatted JSON file

[![CircleCI](https://circleci.com/gh/bl4ck4ndbr0wn/code-challenge/tree/main.svg?style=svg)](https://circleci.com/gh/bl4ck4ndbr0wn/code-challenge/tree/main)

[![Coverage Status](https://coveralls.io/repos/github/bl4ck4ndbr0wn/code-challenge/badge.svg?branch=main)](https://coveralls.io/github/bl4ck4ndbr0wn/code-challenge?branch=main)

## Setup

In a python virtual environment, run:

- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser` (to create user that you'll use to log in)

### Run the application

```bash
python manage.py runserver
```

Now, you are good to go. Your app is ready.

### Test

```bash
python manage.py test
```

## API Spec

The preferred JSON object to be returned by the API should be structured as follows:

### Errors and Status Codes

If a request fails any validations, expect errors in the following format:

```source-json
{
  "errors":{
    "body": [
      "can't be empty"
    ]
  }
}
```

### Other status codes:

404 for Not found requests, when a resource can't be found to fulfill the request

## Endpoints:

### Get challenge

`GET /api/challenge/`

Returns input parameter is required, provide `number`, query parameter to find if the integer is a multiple of 5 or 7.

Query Parameters:

Filter by number:

`?number=0`

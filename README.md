![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Build Status](https://travis-ci.com/BrianSerem/Send-It-API.svg?branch=develop)](https://travis-ci.com/BrianSerem/Send-It-API)
[![Coverage Status](https://coveralls.io/repos/github/BrianSerem/Send-It-API/badge.svg?branch=develop)](https://coveralls.io/github/BrianSerem/Send-It-API?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/609b635d8231deaa3689/maintainability)](https://codeclimate.com/github/BrianSerem/Send-It-API/maintainability)

[![Maintainability](https://api.codeclimate.com/v1/badges/609b635d8231deaa3689/maintainability)](https://codeclimate.com/github/andela/ah-legion-backend/maintainability)

# Send-It-API
api for sendit application, an pp used for sending and tracking parcels across the country

This project shows one of the possible ways to implement RESTful API server.

There are two implemented models: User and Todo, one user has many todos.

## _Main libraries used_:

1. Flask-RESTful - restful API library.
2. Flask-Script - provides support for writing external scripts.



## Running 

1. Clone repository.

https://github.com/BrianSerem/Send-It-API.git

### Create and activate a virtual environment

    virtualenv env --python=python3.6

    source env/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

## Running the application

```
$ export FLASK_APP="run.py"
$ export FLASK_DEBUG=1
$ export APP_SETTINGS="development"
```
### Open Terminal and type
$ flask run

### Open postman and use the below endpoints.


## Endpoints currently available
| Method | Endpoint                        | Description                           | User-type         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
|1.POST   | /api/v2/parcels                | Creates a new parcel order.|customers        |
|2.GET   | /api/v2/parcels                 | Get all parcel orders                    | admin         |
|3.GET    |/api/v2/parcels/int      | Get a specific parcel order          | customers/admin   |
|4.PUT| /api/v2/parcels/int/destination|Change a parcel's destination| customers       |
|5.PUT| /api/v2/users/int/status| gets all parcels orders for a user| Admin         |
|6.PUT| /api/v2/parcels/int/presentloaction|changes parcel current location|admin  
|7.GET| /api/v2/parcels/int/|Get a specific parcel|customers/admin   |
|8.GET| /api/v2/users| gets all registered users for a user| Admin         |
|9.GET| /api/v2/parcels/int/presentloaction|changes parcel current location|admin 
|10.POST| /api/v2/auth/signup|Registers a user to the app| customers       |
|11.POST| /api/v2/auth/login|Logs in a user to the app| Admin         |
|12.POST| /api/v2/auth|authenticates user for fresh access token|admin   



	`
## How to test the hosted version:
Heroku app hosted on: 
https://sendit123.herokuapp.com/
place the different endpoints at the end of the above url to test

i.e To test user signup; place /api/v2/signup at the end of the url:
https://sendit123.herokuapp.com/api/v2/signup

NB: Test on POSTMAN to allow testing all GET,PUT, DELETE and POST methods.
Documentation can be found here:
https://documenter.getpostman.com/view/5800340/RzfdpAdu

The UI for this API is here, to be connected later.

https://brianserem.github.io/SendIT/


KEEP CHECKING AND BE COOL!!

# API-Endpoints

This API lets the user create an account,login make and modify a maintenance or repair request to the operations department. 

The user can be in position to monitor the status of their request whether it is approved, disapproved or resolved by the admin.

The API also allows the admin to get all the requests for a logged in user, get a single request for a logged in user, approve, disapprove or resolve the requests.

## Features of the API (Endpoints)
Endpoint | Functionality
-------- | -------------
POST/auth/register | Register a user
POST/auth/login | login a user
GET /api/v1/users/requests | Fetch all the requests of a logged in user
GET /api/v1/users/requests/`<requestId>` | Fetch a request that belongs to a logged in user
POST /api/v1/users/requests/ | Create a request
PUT /api/v1/users/requests/`<requestId>`/ | Modify a request.

##  Stack
- Python
- Flask 

##  Technologies suitable
- Python 3.6

## Create and activate virtualenv
```
python -m venv venv
venv\Scripts\activate => for windows
```
## Requirements

```
pip install -r requirements
```
##  Run the app
Run python run.py in the terminal
- After the app is run copy this link http://127.0.0.1:5000/
- Paste is in postman and it will return the index page

## Import unittest library in the test file
- import Unittest
- import BaseTestCase
- write tests
- Run nosetests --with-coverage on the terminal to see passing and failing tests.
- In case there are tests failing, then fix them and re-run the tests to make sure they all pass.




# codepuzzle
## Best Available Seat
This REST API returns the best available seat (closest to the front & middle of the row).

To add a Venue, enter a list of open seats, with row and column numbers.
Rows follow alphabetical order with « A » being the first row. 
Columns follow numerical order from left to right (starting with 1).
For example:
```
{
    "venue": {
        "layout": {
            "rows": 10,
            "columns": 50
        }
    },
    "seats": {
        "a1": {
            "id": "a1",
            "row": "a",
            "column": 1,
            "status": "AVAILABLE"
        },
        "b5": {
            "id": "b5",
            "row": "b",
            "column": 5,
            "status": "AVAILABLE"
        },
        "h7": {
            "id": "h7",
            "row": "h",
            "column": 7,
            "status": "AVAILABLE"
        }
    }
}
```
The list of open seats, row and column numbers (seats) are configurable and are based on a JSON input.

The solution finds the best open seat (closest to the front & middle of the row) given the input JSON and number of requested seats. 
To keep things simple, in this solution, any seat in a closer row will always be preferred to a seat in a further row.

## Requirements
To install and run this application, you need:
- Python 3.3+
- virtualenv 

## Installation
The commands below set everything up to run the application:
```
$ git clone https://github.com/miguelgrinberg/flask-examples.git
$ cd flask-examples
$ virtualenv venv
$ . venv/bin/activate
(venv)$ pip install -r requirements.txt
```
## Run application
To run the application, type the commands below:
```
$ python test.py
$ python api.py
```
For more information, please refer to the [documentation](docs/documentation.md).


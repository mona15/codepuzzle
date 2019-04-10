## Possible scenario
First launch your app:
```
$python api.py
```

Then try one of the next steps in a different terminal:


## Get all seats

```
$curl http://localhost:5000/venues
```

if you did not post anything the result should be:

```
{}
```

## Post a new venue

```
$curl -H "Content-Type: application/json" -X POST -d '{ "venue": { "layout": { "rows": 10, "columns": 50 } }, "seats": { "a1": { "id": "a1", "row": "a", "column": 1, "status": "AVAILABLE" }, "b5": { "id": "b5", "row": "b", "column": 5, "status": "AVAILABLE" }, "h7": { "id": "h7", "row": "h", "column": 7, "status": "AVAILABLE" } } }'  http://localhost:5000/venues
```

if this is your first post you should get this value:

```
$curl http://localhost:5000/venues/venue1
```

## Update venue

to update venue1 rows, columns or to add seats:

```
$curl http://localhost:5000/venues/venue1 -d "rows=1" -d "columns=5" -d 'open-seats={"a2": { "id": "a2", "row": "a", "column": 2, "status": "AVAILABLE" }}' -X PUT -v
```

## Get the first best available seat

to get the first best available seat, type the URL like this:
http://localhost:5000/<your_venue>/<number_of_requested_seats> :

```
$curl http://localhost:5000/venue1/1
```

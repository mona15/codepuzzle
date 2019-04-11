from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import ast


VENUES = {
}

def abort_if_venue_doesnt_exist(venue_id):
    if venue_id not in VENUES:
        abort(404, message="Venue {} doesn't exist".format(venue_id))

parser = reqparse.RequestParser()
parser.add_argument('venue')
parser.add_argument('rows')
parser.add_argument('columns')
parser.add_argument('open-seats')

# Venue
# shows a single venue item and lets you delete a venue item
class Venue(Resource):
    def get(self, venue_id):
        abort_if_venue_doesnt_exist(venue_id)
        return VENUES[venue_id]

    def delete(self, venue_id):
        abort_if_venue_doesnt_exist(venue_id)
        del VENUES[venue_id]
        return '', 204

    def put(self, venue_id):
        """this function updates number of rows, columns and add open seats
           and returns the updated venue
           parameters that can be passed are rows, columns, open-seats
        """
        args = parser.parse_args()
        selected_venue = VENUES[venue_id]
        open_seats = selected_venue['seats']
        dict_seat_value = ast.literal_eval(args['open-seats'])

        for x in  dict_seat_value:
            open_seats.update({x: dict_seat_value[x]})

        update_venue = {
                    "venue": {
                        "layout": {
                            "rows": int(args['rows']),
                            "columns": int(args['columns'])
                        }
                    }
                }
        update_venue.update({"seats": open_seats})

        VENUES[venue_id] = update_venue
        return update_venue, 201

# VenueList
# shows a list of all VENUES, and lets you POST to add new venue
class VenueList(Resource):
    def get(self):
        return VENUES

    def post(self):
        """ to post a venue add the venue in json format as in the exemple of the documentation
        """
        some_json = request.get_json()
        if VENUES:
            venue_id = int(max(VENUES.keys()).lstrip('venue')) + 1
            venue_id =  'venue%i' % venue_id
        else:
            venue_id = 'venue1'
        VENUES[venue_id] = some_json

        return VENUES[venue_id], 201

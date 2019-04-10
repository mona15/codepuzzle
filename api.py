from flask import Flask, request
from flask_restful import abort, Api, Resource
from seats import the_best_seat, list_best_seats, list_multiple_seat
from crud import VenueList, Venue, abort_if_venue_doesnt_exist, VENUES
import ast
app = Flask(__name__)
api = Api(app)

# get the first best seat available
class FirstBestSeat(Resource):
    def get(self, venue_id, num, venues=VENUES):
        """this fuction check the seat which is in the closest row 
           and closest to the center. And if 2 seats was found with the same distance to the center 
           the on left side will be prefered 
           BONUS: for multiple requests a row has to full available
        """
        abort_if_venue_doesnt_exist(venue_id)
        venue = venues[venue_id]
        seats = venue['seats']
        seats_json = {}

        columns = venue['venue']['layout']['columns']
        seats_num_requested = 1
        columns = columns/2
        if int(num) == 1:
            x = the_best_seat(columns, seats)
            seats_json[x] = seats[x]
            return seats_json

        best_seat_odered = list_best_seats(columns, seats)
        multiple_best_seats = list_multiple_seat(best_seat_odered, int(num))
        
        for x in multiple_best_seats:
            seat_index = 'best_seat'+str(multiple_best_seats.index(x) + 1)
            seats_json[seat_index] = x

        return seats_json, 200


##
## Actually setup the Api resource routing here
##
api.add_resource(VenueList, '/venues')
api.add_resource(Venue, '/venues/<venue_id>')
api.add_resource(FirstBestSeat, '/<venue_id>/<num>')


if __name__ == '__main__':
    app.run(debug=True)
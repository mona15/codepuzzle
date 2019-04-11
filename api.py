from flask import Flask, request
from flask_restful import abort, Api, Resource
from seats import the_best_seat, list_best_seats, requested_seats
from crud import VenueList, Venue, abort_if_venue_doesnt_exist, VENUES
import collections
import ast
app = Flask(__name__)
api = Api(app)

# get the first best seat available
class FirstBestSeat(Resource):
    def get(self, venue_id, num, venues=VENUES):
        """this fuction get the seat(s) which is in the closest row 
           and closest to the center. And if 2 seats are found with the same distance to the center 
           the on the left side will be prefered 
           BONUS: for multiple seats requested get the seats available in the closest row
        """
        abort_if_venue_doesnt_exist(venue_id)
        venue = venues[venue_id]
        seats = venue['seats']
        seats_json = {}

        seats_test = {}
        for x in seats:
            seats_test[x] = x

        columns = venue['venue']['layout']['columns']
        seats_num_requested = 1

        if int(num) == 1:
            x = the_best_seat(columns, seats_test)
            seats_json[x] = seats[x]
            return seats_json, 200

        arroud_available = 'OK'
        best_seat_odered = list_best_seats(columns, seats_test)
        
        if columns < int(num):
            return {}, 200

        multiple_best_seats = requested_seats(best_seat_odered, int(num), best_seat_odered, arroud_available)
        
        for x in multiple_best_seats:
            seats_json[x] = seats[x]
            
        order_seats_json = collections.OrderedDict(sorted(seats_json.items()))

        return order_seats_json, 200


##
## Setup the Api resource routing here
##
api.add_resource(VenueList, '/venues')
api.add_resource(Venue, '/venues/<venue_id>')
api.add_resource(FirstBestSeat, '/<venue_id>/<num>')


if __name__ == '__main__':
    app.run(debug=True)
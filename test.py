import unittest
from flask import current_app
from api import app 
import json

data_json = '{ "venue": { "layout": { "rows": 3, "columns": 6 } }, "seats": { "a3": { "id": "a3", "row": "a", "column": 3, "status": "AVAILABLE" }, "b3": { "id": "b3", "row": "b", "column": 3, "status": "AVAILABLE" }, "b4": { "id": "b4", "row": "b", "column": 4, "status": "AVAILABLE" }, "c3": { "id": "c3", "row": "c", "column": 3, "status": "AVAILABLE" }, "c4": { "id": "c4", "row": "c", "column": 4, "status": "AVAILABLE" }, "c5": { "id": "c5", "row": "c", "column": 5, "status": "AVAILABLE" },  "c6": { "id": "c6", "row": "c", "column": 6, "status": "AVAILABLE" } } }'

"""
seat_1 = { "a3": { "id": "a3", "row": "a", "column": 3, "status": "AVAILABLE" }}
seat_2 = { "b3": { "id": "b3", "row": "b", "column": 3, "status": "AVAILABLE" }}
seat_3 = { "b4": { "id": "b4", "row": "b", "column": 4, "status": "AVAILABLE" }}
seat_4 = { "c3": { "id": "c3", "row": "c", "column": 3, "status": "AVAILABLE" }}
seat_5 = { "c4": { "id": "c4", "row": "c", "column": 4, "status": "AVAILABLE" }}
seat_6 = { "c5": { "id": "c5", "row": "c", "column": 5, "status": "AVAILABLE" }}
seat_7 = { "c6": { "id": "c6", "row": "c", "column": 6, "status": "AVAILABLE" }}
"""

class BasicsTestCase(unittest.TestCase):
	# Ensure that flask was setup correctly
	def test_get_all(self):
		tester = app.test_client(self)
		response = tester.get('/venues', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure that data is posted correctly
	def test_venue_post(self):
		tester = app.test_client(self)
		response = tester.post('/venues', data=data_json ,content_type='application/json')
		self.assertEqual(response.status_code, 201)

	# Ensure a venue can be retrieved correctly
	def test_get_one_venue(self):
		tester = app.test_client(self)
		tester.post('/venues', data=data_json ,content_type='application/json')
		response = tester.get('/venues/venue1', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	# Ensure we get the best seat available 
	def test_first_best_seat(self):
		tester = app.test_client(self)
		tester.post('/venues', data=data_json ,content_type='application/json')
		response = tester.get('/venue1/1', content_type='application/json')
		self.assertIn(b'a3', response.data)

	# Ensure we can not get a venue that does not exist
	def test_get_venue_does_not_exist(self):
		tester = app.test_client(self)
		response = tester.get('/venues/venue9', content_type='application/json')
		self.assertEqual(response.status_code, 404)

	# Ensure to return nothing if there is not enought seats available
	def test_multiple_best_seat_not_allow(self):
		tester = app.test_client(self)
		tester.post('/venues', data=data_json ,content_type='application/json')
		response = tester.get('/venue1/7', content_type='application/json')
		self.assertIn(b'{}', response.data)

	# Ensure multiple seat can be requested
	def test_multiple_best_seat(self):
		tester = app.test_client(self)
		tester.post('/venues', data=data_json ,content_type='application/json')
		response = tester.get('/venue1/2', content_type='application/json')
		self.assertIn(b'{"b3": {"id": "b3", "row": "b", "column": 3, "status": "AVAILABLE"}, "b4": {"id": "b4", "row": "b", "column": 4, "status": "AVAILABLE"}}', response.data)

	# Ensure multiple seats can be requested with one element missing from the left:
	def test_multiple_right(self):
		tester = app.test_client(self)
		tester.post('/venues', data=data_json ,content_type='application/json')
		response = tester.get('/venue1/3', content_type='application/json')
		self.assertIn(b'{"c3": {"id": "c3", "row": "c", "column": 3, "status": "AVAILABLE"}, "c4": {"id": "c4", "row": "c", "column": 4, "status": "AVAILABLE"}, "c5": {"id": "c5", "row": "c", "column": 5, "status": "AVAILABLE"}}', response.data)


if __name__ == '__main__':
    unittest.main()
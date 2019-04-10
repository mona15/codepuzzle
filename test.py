import unittest
from flask import current_app
from api import app 
import json

data_json = '{ "venue": { "layout": { "rows": 10, "columns": 50 } }, "seats": { "a1": { "id": "a1", "row": "a", "column": 1, "status": "AVAILABLE" }, "a2": { "id": "a1", "row": "a", "column": 1, "status": "AVAILABLE" }, "b5": { "id": "b5", "row": "b", "column": 5, "status": "AVAILABLE" }, "h7": { "id": "h7", "row": "h", "column": 7, "status": "AVAILABLE" } } }'

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

	# Ensure a venue can be retrieve correctly
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
		self.assertIn(b'a1', response.data)

	# Ensure we can not get a venue that does not exist
	def test_get_venue_does_not_exist(self):
		tester = app.test_client(self)
		response = tester.get('/venues/venue9', content_type='application/json')
		self.assertEqual(response.status_code, 404)

	# Ensure multiple seat can be requested
	def test_multiple_best_seat(self):
		tester = app.test_client(self)
		tester.post('/venues', data=data_json ,content_type='application/json')
		response = tester.get('/venue1/2', content_type='application/json')
		self.assertIn(b'{"best_seat1": "a2", "best_seat2": "a1"}', response.data)

	def test_multiple_best_seat_not_allow(self):
		tester = app.test_client(self)
		tester.post('/venues', data=data_json ,content_type='application/json')
		response = tester.get('/venue1/3', content_type='application/json')
		self.assertIn(b'{}', response.data)


if __name__ == '__main__':
    unittest.main()
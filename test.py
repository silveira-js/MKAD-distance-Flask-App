from app import my_app
import unittest
from app.src.helpers import get_coordinates,get_distance_to_mkad
import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app = my_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)


class HelpersTestCase(unittest.TestCase):

    def test_get_coordinates(self):
        address = 'Avenida Jaime Estefano Becker, São José, Santa Catarina, Brasil'
        test_coordinates = ['-48.65139 -27.610293']
        coordinates, number = get_coordinates(address)
        self.assertEqual(coordinates, test_coordinates)
    
    def test_get_distance_of_location_inside_mkad(self):
        coordinates = ['37.609182 55.719419']
        result = "The specified address is located inside the MKAD"
        self.assertEqual(get_distance_to_mkad(coordinates), result)

    def test_get_coordinates_and_distance_together(self):
        address = 'Shabolovka St, Moskva, Rússia, 119049'
        result = "The specified address is located inside the MKAD"
        coordinates, number = get_coordinates(address)
        self.assertEqual(get_distance_to_mkad(coordinates), result)

    def test_get_distance_of_location_outside_mkad(self):
        coordinates = ['21.0122287 52.2296756']
        result = '1138.82 km'
        self.assertEqual(get_distance_to_mkad(coordinates), result)



if __name__ == '__main__':
    unittest.main()
from urllib.parse import urlencode
import requests
import geopy.distance
from .mkad_coordinates import mkad_km_coordinates

api_key = '32de70c6-6e45-43af-bd60-f66b407e0a73'

def get_coordinates(address):
    '''
    Function to consume the geocode yandex API;

    Input: Address;
    Output: Coordinates of the given address.

    '''

    endpoint = 'https://geocode-maps.yandex.ru/1.x'
    params = {"apikey": api_key, "format": 'json',
              "geocode": address, "lang": 'en-US'}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        r = {}
    r_json = r.json()
    print(r_json)
    number_of_results_found = int(
        r_json['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'])

    number_of_results = len(
        r_json['response']['GeoObjectCollection']['featureMember'])

    coordinates = [r_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']]

    return coordinates, number_of_results_found


def get_distance_to_mkad(coordinates):

    '''
    Function to calculate the distance between the coordinates 
    of the given address and the coordinates of the MKAD

    Input: Coordinates;
    Output: Distance.
    '''

    # Prepare the geocoded coordinates to calculate
    coords_1 = coordinates[0].split()
    coords_1 = list(map(float, coords_1))
    coords_1.reverse()

    # Prepare values ​​to verify that coordinates are within MKAD 
    latitude = coords_1[0]
    longitude = coords_1[1]
    max_latitude = max(map(lambda x: x[0], mkad_km_coordinates))
    min_latitude = min(map(lambda x: x[0], mkad_km_coordinates))
    max_longitude = max(map(lambda x: x[1], mkad_km_coordinates))
    min_longitude = min(map(lambda x: x[1], mkad_km_coordinates))

    # Conditional to check the location and calculate the minimum distance from the address to the MKAD
    if min_latitude < latitude < max_latitude and min_longitude < longitude < max_longitude:
        return "The specified address is located inside the MKAD"
    else:
        distances = [geopy.distance.geodesic(
            coords_1, coords_2).km for coords_2 in mkad_km_coordinates]
        return f'{round(min(distances), 2)} km'
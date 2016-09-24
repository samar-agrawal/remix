'''Fetch the customer based on geographical
   co-ordinates mentioned in the file, calculating the distance
   using great-circle distance formula
'''

import json
from math import radians, acos, sin, cos

EARTH_RADIUS = 6371

class DistanceCalculator(object):
    '''Initializes class with given params, reads the file,
       and prints user_id and name of eligible customers
       :param file_name: name of the file to be parsed, along with path
       :param_origin_latitude: Latitude from where the distance needs to be calculated
       :param origin_longitude: Longitude from where the distance needs to be calculated
       :param required_distance: Distance Criteria for Invite
     '''

    def __init__(self, file_name, origin_latitude, origin_longitude, required_distance):
        self.file_name = file_name
        self.earth_radius = EARTH_RADIUS
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.required_distance = required_distance

    def calculate_distance(self, latitude, longitude):
        '''Calculate Distance between 2 geographical co-ordinates
           formula ref: https://en.wikipedia.org/wiki/Great-circle_distance
        '''

        latitude_1, longitude_1, latitude_2, longitude_2 = map(radians,\
               [self.origin_latitude, self.origin_longitude, latitude, longitude])
        distance_angle = acos(sin(latitude_1)*sin(latitude_2)+\
            cos(latitude_1)*cos(latitude_2)*cos(longitude_2-longitude_1))
        distance = distance_angle * EARTH_RADIUS
        return distance

    def fetch_file(self):
        '''Read a file and return list of dict element for each record'''

        with open(self.file_name, "r") as customer_file:
            content = customer_file.readlines()

        data = [json.loads(val) for val in content]
        return data

    def get_eligible_customers(self):
        '''Print the list of customers sorted by user_id, that matches the criteria'''

        data = self.fetch_file()

        eligible_invites = {}
        for record in data:

            try:
                distance = self.calculate_distance(\
                     float(record['latitude']), float(record['longitude']))
            except (ValueError, KeyError) as e:
                print("Incorrect data - {0}".format(e))
                return False

            if distance <= self.required_distance:
                eligible_invites[record['user_id']] = record['name']

        return sorted(eligible_invites.items())

if __name__ == "__main__":

    customer_object = DistanceCalculator('gistfile1.txt', 53.3381985, -6.2592576, 100.0)
    list_of_customers = customer_object.get_eligible_customers()

    if list_of_customers:
        for user_id, name in list_of_customers:
            print(user_id, name)

import requests

drivers = [{'ID': 'Driver A', 'location': 'Atlanta, GA'},
    {'ID': 'Driver B', 'location': 'Kennesaw, GA'},
    {'ID': 'Driver C', 'location': 'Monroe, GA'}]

def get_drivers():
    return drivers

def assign_driver(vehicle_location, drivers, api_key):
    closest_driver = 0
    shortest_distance = 9999999999

    for person in drivers:
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"
        parameter = {
            "origins": person['location'],
            "destinations": vehicle_location,
            "key": api_key
        }
        response = requests.get(url, parameter)
        data = response.json()

        if data['rows'] and data['rows'][0]['elements']:
            distance_value = data['rows'][0]['elements'][0]['distance']['value']

            if distance_value < shortest_distance:
                shortest_distance = distance_value
                closest_driver = person

    return closest_driver
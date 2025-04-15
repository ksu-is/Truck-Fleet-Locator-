import requests
def get_distance(api_key, origin, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    parameters = {
        "origins": origin,
        "destinations": destination,
        "key": api_key
    }
    response = requests.get(url, parameters)
    data = response.json()
    
    if data['rows'] and data['rows'][0]['elements']:
        distance_value = data['rows'][0]['elements'][0]['distance']['value']
        return distance_value
    else:
        return None
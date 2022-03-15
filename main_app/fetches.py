import requests

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Manhattan&type=tourist_attraction&key=AIzaSyBd3BeYOCFPOuYIBOD9HlPYYL__hbOm8mU"

payload={}
headers = {}

response = requests.get(url, headers=headers, data=payload)
manhattan_tourist_attraction = response.json()['results']
place_list = []
for result in manhattan_tourist_attraction:
    places = {
        "name": result['name'],
        "address": result['formatted_address'],
        "interest_category": result['types'],
        "rating": result['rating'],
        "image": result['photos'][0]['html_attributions'][0].split('"')[1]
    }
    place_list.append(places)


    
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Manhattan&type=restaurant&key=AIzaSyBd3BeYOCFPOuYIBOD9HlPYYL__hbOm8mU"

payload={}
headers = {}

response = requests.get(url, headers=headers, data=payload)
manhattan_restaurant = response.json()['results']
for result in manhattan_restaurant:
    places = {
        "name": result['name'],
        "address": result['formatted_address'],
        "interest_category": result['types'],
        "rating": result['rating']
    }
    place_list.append(places)


url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Manhattan&type=park&key=AIzaSyBd3BeYOCFPOuYIBOD9HlPYYL__hbOm8mU"

payload={}
headers = {}

response = requests.get(url, headers=headers, data=payload)
manhattan_parks = response.json()['results']
for result in manhattan_parks:
    places = {
        "name": result['name'],
        "address": result['formatted_address'],
        "interest_category": result['types'],
        "rating": result['rating']
    }
    place_list.append(places)


print(place_list)
import requests
import webbrowser

# https://developers.google.com/maps/documentation/urls/guide#forming-the-map-url
# Google map direction calling address.
GOOGLE_MAPS_API_URL = 'https://www.google.com/maps/dir/?api=1'


origin_A = input("Enter the origin location:  ")
destination_B = input("Enter the destination location  ")

param = {'origin': origin_A,
         'destination': destination_B}

# Module calling
req = requests.get(GOOGLE_MAPS_API_URL, params=param)
print(req.url)
webbrowser.open(req.url)

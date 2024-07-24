import requests

# coordinates
lat = 30.0074
lon = -90.115

# nominatim API
url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&addressdetails=1"

# headers
headers = {
    'User-Agent': 'Target Mapping (noha@theundivideproject.org)'
}

# make request
response = requests.get(url, headers=headers)

# check status code
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)

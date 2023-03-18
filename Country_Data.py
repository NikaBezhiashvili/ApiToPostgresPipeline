import requests

# --------------------------------------------------------- Api Connection  --------------------------------------------------------- #

endpoint = 'https://api.yelp.com/v3/businesses/search?location=NYC&term=food&categories=&open_now=true&sort_by=best_match&limit=20'


headers = {
    "accept": "application/json",
    "Authorization": "Bearer VWWat1HmqRhrpBLx5aUvD8hQMQ8Zu75P8JD4F3CGHYtZlqngPp41WAf4PlDTPrmusQ5MaS8uLl7GEnPK08R6soF2cUNICEk2teA4m2HRzGSHEO0gvQvHYRivu-EVZHYx"
}

response = requests.get(endpoint, headers=headers)

if response.status_code == 200:
    pass
else:
    print(f'Request failed with status code {response.status_code}')

# --------------------------------------------------------- Api Data --------------------------------------------------------- #


mainData = response.json()['businesses']


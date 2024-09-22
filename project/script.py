import requests
import json

response = requests.get('https://api.github.com/events')
event = response.json()[0]

print(f'Last event: {event['type']} | {event['repo']['name']}')


import requests
import json
import logging

response = requests.get('https://api.github.com/events')
event = response.json()[0]

logging.info(f'Last event: {event['type']} | {event['repo']['name']}')


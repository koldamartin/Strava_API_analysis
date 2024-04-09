# based on: https://www.grace-dev.com/python-apis/strava-api/

import json
import os
import requests
import time
import dotenv
import pandas as pd

dotenv.load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = 'http://localhost/'

def request_token(client_id, client_secret, code):
    response = requests.post(url='https://www.strava.com/oauth/token',
                             data={'client_id': client_id,
                                   'client_secret': client_secret,
                                   'code': code,
                                   'grant_type': 'authorization_code'})
    return response

def refresh_token(client_id, client_secret, refresh_token):

    response = requests.post(url='https://www.strava.com/api/v3/oauth/token',
                             data={'client_id': client_id,
                                   'client_secret': client_secret,
                                   'grant_type': 'refresh_token',
                                   'refresh_token': refresh_token})
    return response

def write_token(token):

    with open('strava_token.json', 'w') as outfile:
        json.dump(token, outfile)

def get_token():

    with open('strava_token.json', 'r') as token:
        data = json.load(token)

    return data

if not os.path.exists('./strava_token.json'):
    request_url = f'http://www.strava.com/oauth/authorize?client_id={client_id}' \
                  f'&response_type=code&redirect_uri={redirect_uri}' \
                  f'&approval_prompt=force' \
                  f'&scope=profile:read_all,activity:read_all'


    print('Click here:', request_url)
    print('Please authorize the app and copy&paste below the generated code!')
    print('P.S: you can find the code in the URL')
    code = input('Insert the code from the url: ')

    token = request_token(client_id, client_secret, code)

    #Save json response as a variable
    strava_token = token.json()
    # Save tokens to file
    write_token(strava_token)


data = get_token()

if data['expires_at'] < time.time():
    print('Refreshing token!')
    new_token = refresh_token(client_id, client_secret, data['refresh_token'])
    strava_token = new_token.json()
    # Update the file
    write_token(strava_token)

data = get_token()

access_token = data['access_token']

athlete_url = f"https://www.strava.com/api/v3/athlete?" \
              f"access_token={access_token}"
response = requests.get(athlete_url)
athlete = response.json()

print('RESTful API:', athlete_url)
print('='* 5, 'ATHLETE INFO', '=' * 5)
print('Name:', athlete['firstname'], athlete['lastname'])
print('Gender:', athlete['sex'])
print('City:', athlete['city'], athlete['country'])
print('Strava athlete from:', athlete['created_at'])

df = pd.DataFrame(columns=['start_date', 'distance [km]', 'average_speed [km/h]', 'max_speed [km/h]',
                           'moving_time [min]', 'total_elevation_gain [m]', 'type',
                           'gear_id', 'kilojoules'])

for page in range(1,10):

    activities_url = f"https://www.strava.com/api/v3/athlete/activities?per_page=200&page={page}&" \
              f"access_token={access_token}"
    print('RESTful API:', activities_url)
    response = requests.get(activities_url)

    for i in range(len(response.json())):
        activity = response.json()[i]
        df.loc[len(df)] = [
            activity.get('start_date', None),
            activity.get('distance', None) / 1000,
            activity.get('average_speed', None) * 3.6,
            activity.get('max_speed', None) * 3.6,
            round(activity.get('moving_time', None) / 60, 2),
            activity.get('total_elevation_gain', None),
            activity.get('type', None),
            activity.get('gear_id', None),
            activity.get('kilojoules', None)
        ]

df.to_csv('activities.csv', index=False)

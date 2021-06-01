import requests
from datetime import datetime

callsign = 'YC0DMS'
loc = 'OI33'
apikey = 'yourAPIkey'

url = f'https://api.aprs.fi/api/get?name={callsign}&what=loc&apikey={apikey}&format=json'

res = requests.get(url=url)
data = res.json()['entries'][0]
name = data['name']
lat = data['lat']
long = data['lng']
comment = data ['comment']
path = data['path']
timefirst = datetime.fromtimestamp(int(data['time'])).strftime('%Y-%m-%d %H:%M:%S')
timelast = datetime.fromtimestamp(int(data['lasttime'])).strftime('%Y-%m-%d %H:%M:%S')

res = f"""Name : {name}
Lat/Long : {lat},{long}
Comment : {comment}
Path : {path}
Start Time :{timefirst} 
End Time : {timelast}
"""

print(res)

import requests
import json
from bs4 import BeautifulSoup

appID = '63'
reportID = '22370'
withData = 'true'

newStatusID = '984'
newStatusName = 'Cancelled'

auth = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImVtYWlscm9ib3RAYnl1aS5lZHUiLCJ0ZHhfZW50aXR5IjoiMSIsInRkeF9wYXJ0aXRpb24iOiI3MyIsIm5iZiI6MTY4Mjk1NzMzMSwiZXhwIjoxNjgzMDQzNzMxLCJpYXQiOjE2ODI5NTczMzEsImlzcyI6IlREIiwiYXVkIjoiaHR0cHM6Ly93d3cudGVhbWR5bmFtaXguY29tLyJ9.MEz9dud1f_ksHOmEsNh-ULgrHDc94gVI-ultytRvBDs'

url = 'https://td.byui.edu/TDWebApi'
url += f'/api/reports/{reportID}?withData={withData}'
print(url)

headers = { 'content-type': 'application/json', 'authorization': auth}

r = requests.get(url, headers=headers)
#payload = {'some': 'data'}
#data=json.dumps(payload)
print(r)
json_data = r.json()
#print(data)
rows = json_data['DataRows']
#print(rows)


payload_no_json = [
  {"op": "add", "path": "/StatusID", "value": newStatusID},
  {"op": "add", "path": "/StatusName", "value": newStatusName}]
payload = json.dumps(payload_no_json)
for ticket in rows:
    ticketID = ticket['TicketID']
    url = 'https://td.byui.edu/TDWebApi'
    url += f'/api/{appID}/tickets/{ticketID}'
    r = requests.patch(url, data=payload, headers=headers)
    



# 
# 
# print(r)
# print(r.json())





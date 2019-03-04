import http.client
import json
import config
connection = http.client.HTTPConnection("api.football-data.org")
headers = { "X-Auth-Token": config.API_CONFIG["key"] }
connection.request("GET", "/v2/teams/{}".format(config.API_CONFIG["teamid"]), None, headers )
response = json.loads(connection.getresponse().read().decode())["email"]
print (response);

import http.client
import json
import config
import notify2
connection = http.client.HTTPConnection("api.football-data.org")
headers = { "X-Auth-Token": config.API_CONFIG["key"] }
connection.request("GET", "/v2/teams/{}".format(config.API_CONFIG["teamid"]), None, headers )
response = json.loads(connection.getresponse().read().decode())
notify2.init("Socccer")
name = response["name"]
id = str(response["id"])
n = notify2.Notification(name, id, "notification-message-im")
n.show()

import http.client
import json
import config
import notify2

next = ""
def nextmatch():
    global next
    connection = http.client.HTTPConnection("api.football-data.org")
    headers = { "X-Auth-Token": config.API_CONFIG["key"] }
    connection.request("GET", "/v2/teams/{}/matches?status=SCHEDULED".format(config.API_CONFIG["teamid"]), None, headers )
    response = json.loads(connection.getresponse().read().decode())
    notify2.init("Socccer")
    match = ("\n" + response["matches"][0]["homeTeam"]["name"] + " vs " + response["matches"][0]["awayTeam"]["name"]
             + "\n" + response["matches"][0]["utcDate"]
             )
    if(next != match):
        next = match
        n = notify2.Notification("Next scheduled match:", match, "notification-message-im")
        n.show()

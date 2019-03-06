import http.client
import json
import config
import notify2

def livematch():
    global homescore
    global awayscore
    connection = http.client.HTTPConnection("api.football-data.org")
    headers = { "X-Auth-Token": config.API_CONFIG["key"] }
    connection.request("GET", "/v2/matches", None, headers )
    response = json.loads(connection.getresponse().read().decode())
    matches = response["matches"]
    print(matches)
    if(matches == []):
        print("No live matches")

import threading
from soccer.modules import next, live

def checknextmatch():
    threading.Timer(43200.0, checknextmatch).start()
    next.nextmatch()

checknextmatch()
live.livematch()

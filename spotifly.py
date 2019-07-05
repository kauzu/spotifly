import dbus
from dbus.mainloop.glib import DBusGMainLoop
import pympris
import time

dbLoop = DBusGMainLoop()
bus = dbus.SessionBus(mainloop=dbLoop)

players = list(pympris.available_players())

spotify = pympris.MediaPlayer(players[0], bus)

while True:
    time.sleep(25)
    spotify.player.Next()
    

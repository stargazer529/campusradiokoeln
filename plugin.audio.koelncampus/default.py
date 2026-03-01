 
import xbmc
import xbmcgui

# Stream URL und Infos
STREAM_URL = "https://live.koelncampus.com/live"
TITLE = "Kölncampus Live"
THUMB = "koelncampus.png" # Beispiel-Icon

def play_stream():
    # Erstellt ein Playback-Objekt
    list_item = xbmcgui.ListItem(path=STREAM_URL)
    list_item.setInfo('music', {'title': TITLE})
    list_item.setArt({'thumb': THUMB})

    # Startet die Wiedergabe
    xbmc.Player().play(STREAM_URL, list_item)

    # Hinweis: Webseiten-Anzeige ist in LibreELEC ohne Browser-Addon nicht möglich.
    # Alternativ kann eine Benachrichtigung eingeblendet werden:
    xbmcgui.Dialog().notification('Kölncampus', 'Stream gestartet', xbmcgui.NOTIFICATION_INFO, 5000)

if __name__ == '__main__':
    play_stream()

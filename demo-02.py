from picamera2 import Picamera2, Preview
from time import sleep

# Kamera initialisieren
picam2 = Picamera2()

# Vorschau Konfiguration erstellen
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

# Vorschau auf dem Bildschirm anzeigen
# Preview.QTGL steht für Qt OpenGL, eine Kombination aus der 
# Qt-Bibliothek (für GUI-Elemente) und OpenGL (für Hardwarebeschleunigtes Rendering). 
# Das bedeutet, dass diese Option verwendet wird, um die Kamera-Vorschau 
# in einem Fenster darzustellen, das mit Hilfe von OpenGL auf der GPU gerendert 
# wird. Dies ermöglicht eine reibungslose und flüssige Vorschau, 
# besonders bei hohen Auflösungen oder Bildraten.
picam2.start_preview(Preview.QT)

# Kamera starten
picam2.start()

# Dank des Sleeps wird die Vorschau für fünf Sekunden angezeigt
sleep(5)

# Kamera stoppen
picam2.stop()

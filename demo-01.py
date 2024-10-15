from picamera2 import Picamera2
from time import sleep

# Kamera initialisieren
picam2 = Picamera2()

# Konfiguration für die Vorschau abrufen
preview_config = picam2.create_preview_configuration()

# Konfiguration anwenden
picam2.configure(preview_config)

# Kamera starten
picam2.start()
sleep(2)  # Warte ein paar Sekunden, damit die Belichtung stabilisiert ist

# Bild aufnehmen und speichern
picam2.capture_file("bild.jpg")

# Kamera stoppen
picam2.stop()

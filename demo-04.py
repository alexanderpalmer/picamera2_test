from picamera2 import Picamera2
import cv2
from time import sleep

# Kamera initialisieren
picam2 = Picamera2()

# Vorschau-Konfiguration erstellen
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

# Kamera starten
picam2.start()
sleep(2)  # Stabilisierung

try:
    while True:
        # Frame von der Kamera erfassen
        frame = picam2.capture_array()
        
        # Zeigt das Frame mit OpenCV an
        cv2.imshow("Camera View", frame)
        
        # Beende mit 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Kamera stoppen und OpenCV-Fenster schließen
    picam2.stop()
    cv2.destroyAllWindows()